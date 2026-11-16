"""Ponto de entrada principal do projeto IdeiaFlui.

Este script inicializa o ambiente, constrói o grafo de orquestração do LangGraph
e executa o ciclo completo da solução multiagente:
1. Recebe o assunto desejado (via argumento de linha de comando ou prompt interativo);
2. Roteia a demanda para a empresa especialista correspondente;
3. Executa a equipe CrewAI para simular as atividades operacionais e identificar gargalos;
4. Aciona o agente comercial da IdeiaFlui para redigir uma proposta comercial customizada.
"""

import argparse
import sys
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

# Carrega as variáveis de ambiente a partir do arquivo .env
load_dotenv()

from src.fluxo.grafo import construir_grafo

# Compilação lazy do grafo sob demanda para não compilar ao importar o módulo
_grafo = None


def obter_grafo():
    """Retorna a instância compilada do grafo, compilando-a se necessário."""
    global _grafo
    if _grafo is None:
        _grafo = construir_grafo()
    return _grafo


def __getattr__(name: str) -> Any:
    """Permite acesso compatível a 'grafo' e 'graph' sem compilar durante a importação."""
    if name in ("grafo", "graph"):
        return obter_grafo()
    raise AttributeError(f"módulo '{__name__}' não possui o atributo '{name}'")


def executar(assunto: str) -> dict[str, Any]:
    """Executa o fluxo completo do LangGraph para o assunto informado.

    Args:
        assunto (str): Tema, produto, campanha ou situação a ser analisada.

    Returns:
        dict[str, Any]: Estado final consolidado após a execução dos nós.
    """
    print(f"\n[+] Iniciando orquestração para o assunto: '{assunto}'...")
    try:
        resultado_fluxo = obter_grafo().invoke({"assunto": assunto})
    except Exception as erro:
        msg_erro = str(erro)
        if any(
            termo in msg_erro
            for termo in [
                "429",
                "RESOURCE_EXHAUSTED",
                "ResourceExhausted",
                "Quota exceeded",
                "rate limit",
                "Rate limit",
            ]
        ):
            print("\n[!] Erro: Limite de cota da API atingido (código 429 / Resource Exhausted).")
            print("    O limite diário ou por minuto do modelo foi ultrapassado. Aguarde a renovação da cota ou utilize outro plano/chave de API.")
            sys.exit(1)
        raise

    empresa = resultado_fluxo.get("empresa", "nenhuma")
    briefing = resultado_fluxo.get("briefing", "")
    justificativa = resultado_fluxo.get("justificativa", "")

    print("\n" + "=" * 60)
    print("RESULTADO DO ROTEAMENTO:")
    print(f"- Empresa Selecionada: {empresa}")
    print(f"- Justificativa: {justificativa}")
    if briefing:
        print(f"- Briefing Operacional: {briefing}")
    print("=" * 60)

    if empresa != "nenhuma":
        arquivo = resultado_fluxo.get("arquivo")
        arquivo_proposta = resultado_fluxo.get("arquivo_proposta")
        sucesso_arquivos = (
            arquivo is not None
            and Path(arquivo).is_file()
            and arquivo_proposta is not None
            and Path(arquivo_proposta).is_file()
        )
        diretorio_relatorios = Path("relatorios") / empresa

        if sucesso_arquivos:
            print(f"\n[✓] Relatórios e proposta gerados com sucesso!")
            print(f"[✓] Arquivos salvos no diretório: '{diretorio_relatorios}'")
        else:
            print(f"\n[!] Execução concluída para '{empresa}', mas os arquivos de relatório ou proposta não foram confirmados no disco.")
    else:
        print("\n[!] O assunto informado não teve correspondência com as empresas cadastradas.")

    return resultado_fluxo


def main() -> None:
    """Função principal com suporte a argumentos CLI e modo interativo."""
    parser = argparse.ArgumentParser(
        description="IdeiaFlui - Orquestrador Multiagente (LangGraph + CrewAI)"
    )
    parser.add_argument(
        "-a",
        "--assunto",
        type=str,
        help="Assunto ou tema a ser analisado pelo fluxo multiagente.",
    )

    args = parser.parse_args()

    if args.assunto is not None:
        assunto_usuario = args.assunto.strip()
    else:
        try:
            assunto_usuario = input("Qual o assunto para simulação? ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nOperação cancelada pelo usuário.")
            sys.exit(0)

    if not assunto_usuario:
        print("Erro: O assunto não pode ser vazio.")
        sys.exit(1)

    executar(assunto_usuario)


if __name__ == "__main__":
    main()

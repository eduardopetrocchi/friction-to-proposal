"""Módulo do agente Vendedor da IdeiaFlui no LangGraph.

Este módulo analisa os relatórios gerenciais produzidos pelas empresas clientes,
identifica gargalos operacionais e tarefas manuais, cruza com o catálogo
oficial de serviços da IdeiaFlui e redige uma proposta comercial consultiva.
"""

from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from .estado import EstadoFluxo
from .roteador import EMPRESAS

# Carrega variáveis de ambiente
load_dotenv()

# Caminho base do catálogo de serviços da IdeiaFlui
RAIZ_PROJETO = Path(__file__).resolve().parents[2]
CAMINHO_SERVICOS = RAIZ_PROJETO / "config" / "ideiaflui" / "servicos.yaml"

PROMPT_SISTEMA_VENDEDOR = """
Você é o diretor comercial da IDEIAFLUI, uma empresa especializada
em soluções de Inteligência Artificial, automação de processos
e integração de sistemas para pequenas e médias empresas.

SUA MISSÃO:

Analisar relatórios gerenciais produzidos sobre empresas
potenciais clientes (leads), identificar dificuldades operacionais
e elaborar propostas comerciais para vender os serviços da IDEIAFLUI.

IDENTIDADE COMERCIAL:

- Prestadora dos serviços: IdeiaFlui.
- Cliente potencial: empresa descrita no contexto recebido.
- A IdeiaFlui é quem apresenta e assina a proposta.
- A empresa analisada é a destinatária da proposta.
- Nunca confunda a empresa cliente com a prestadora dos serviços.

CATÁLOGO DE SERVIÇOS:

Você receberá no contexto um catálogo atualizado dos serviços
oferecidos pela IdeiaFlui.

Utilize esse catálogo como fonte oficial para identificar
quais soluções podem ser comercializadas.

REGRAS DE UTILIZAÇÃO DO CATÁLOGO:

- Ofereça somente serviços presentes no catálogo.
- Não invente serviços ou funcionalidades.
- Relacione cada dificuldade identificada a um ou mais
  serviços compatíveis.
- Não ofereça todo o catálogo indiscriminadamente.
- Priorize soluções com maior potencial de impacto operacional.
- Explique como cada serviço poderá resolver o problema.
- Quando uma dificuldade não tiver solução compatível
  no catálogo, não invente uma alternativa.
- Não confunda os serviços da empresa cliente com os
  serviços da IdeiaFlui.

OBJETIVO DA ANÁLISE:

Leia integralmente o relatório gerencial e identifique:

- Processos manuais e repetitivos.
- Gargalos operacionais.
- Atividades que consomem horas de trabalho.
- Processos sujeitos a erros humanos.
- Falhas de comunicação entre sistemas.
- Problemas de organização e disponibilidade de informações.
- Oportunidades de automação e aplicação de IA.

RELACIONAMENTO ENTRE PROBLEMAS E SOLUÇÕES:

Para cada dificuldade identificada, avalie se existe uma solução
dentro do portfólio da IdeiaFlui.

Priorize soluções que:
- Eliminem ou reduzam tarefas repetitivas.
- Reduzam retrabalho e erros operacionais.
- Melhorem a integração entre ferramentas.
- Agilizem o processamento de informações.
- Aumentem a produtividade da equipe.
- Permitam que colaboradores se concentrem em atividades
  estratégicas.

IMPORTANTE:

A IdeiaFlui VENDE soluções tecnológicas e de automação.

A IdeiaFlui NÃO vende serviços de:
- BPO Financeiro.
- Terceirização de departamento financeiro.
- Controladoria.
- Consultoria contábil.
- Execução de serviços fiscais.
- Gestão financeira terceirizada.

Se o relatório identificar problemas nessas áreas,
identifique oportunidades de automatizar os processos envolvidos,
sem oferecer a execução das atividades especializadas.

REGRAS COMERCIAIS:

- A proposta deve ser escrita em nome da IdeiaFlui.
- A empresa analisada deve ser tratada como cliente potencial.
- Não apresente os serviços da empresa analisada como se fossem
  serviços da IdeiaFlui.
- Não copie simplesmente as soluções recomendadas no relatório.
- Desenvolva soluções tecnológicas próprias a partir dos problemas
  identificados.
- Não invente integrações já existentes ou funcionalidades
  garantidas.
- Não prometa eliminação total de erros ou resultados financeiros.
- Não invente preços, prazos, métricas ou garantias.
- Quando não houver valores definidos, utilize:
  "Investimento a definir mediante diagnóstico técnico e aprovação
  do escopo."
- Diferencie claramente os problemas identificados das soluções
  propostas.
- Utilize linguagem comercial, profissional e persuasiva.

ESTRUTURA DA PROPOSTA:

# Proposta Comercial
## Soluções de Automação e Inteligência Artificial

**Apresentada por:** IdeiaFlui
**Destinatário:** [Nome da empresa cliente]

## 1. Apresentação
Apresente a IdeiaFlui e contextualize o objetivo da proposta.

## 2. Diagnóstico e oportunidades identificadas
Apresente os principais problemas encontrados no relatório,
priorizando impacto operacional, tempo perdido e riscos.

## 3. Soluções propostas pela IdeiaFlui
Associe cada problema a uma solução tecnológica específica.
Explique como a automação ou IA poderá ajudar.

## 4. Escopo e entregáveis
Descreva os fluxos, integrações, agentes e funcionalidades
propostos.

## 5. Metodologia de implementação
Apresente as etapas de diagnóstico técnico, desenvolvimento,
integração, testes e implantação.

## 6. Benefícios esperados
Destaque ganhos potenciais de produtividade, redução de tarefas
manuais, organização e eficiência operacional.
Não apresente estimativas sem sustentação.

## 7. Investimento e condições comerciais
Informe que os valores serão definidos após validação técnica
do escopo, caso não existam informações comerciais disponíveis.

## 8. Próximos passos
Convide o cliente para uma reunião de diagnóstico e alinhamento
técnico e comercial.

## 9. Considerações finais
Finalize reforçando o posicionamento da IdeiaFlui como parceira
tecnológica para evolução operacional da empresa.

FORMATO:

- Gere um documento Markdown.
- Utilize tabelas quando facilitarem a comparação entre problemas
  e soluções.
- Seja específico em relação às dificuldades encontradas.
- Evite textos genéricos e promessas exageradas.
- A proposta deve parecer um documento comercial real,
  pronto para ser apresentado ao cliente.

- O relatório pode listar mais processos do que a oferta cobre. Escolha UM fluxo prioritário
  (o de maior impacto), declare-o na seção 3 e liste os demais em "Etapas futuras (fora deste
  escopo)", sob nova proposta.
- Não some nem calcule totais: use apenas totais que constem no relatório.
- Se um serviço avulso e um pacote cobrem a mesma entrega, recomende somente o pacote.
- Na seção 4, para cada oferta, escreva "Escopo incluso" e "Fora do escopo" conforme o catálogo.
- Na seção 5, use exatamente os nomes das etapas da METODOLOGIA do catálogo.
- Na seção 7, inclua o pagamento e as garantias do catálogo.
- Na seção 8, inclua o contato.
- Use exatamente as seções do formato, com esses títulos e nessa ordem.
"""


def carregar_catalogo_servicos() -> dict[str, Any]:
    """Lê e valida o catálogo de serviços oficiais da IdeiaFlui.

    Returns:
        dict[str, Any]: Estrutura com serviços, pacotes e contatos.

    Raises:
        FileNotFoundError: Se o arquivo servicos.yaml não for localizado.
        ValueError: Se o arquivo estiver vazio ou corrompido.
    """
    if not CAMINHO_SERVICOS.exists():
        raise FileNotFoundError(f"Catálogo de serviços não encontrado em: {CAMINHO_SERVICOS}")

    with CAMINHO_SERVICOS.open(encoding="utf-8") as f:
        catalogo = yaml.safe_load(f)

    if not catalogo or not catalogo.get("servicos"):
        raise ValueError("Catálogo de serviços está vazio ou em formato inválido.")

    return catalogo


SERVICOS = carregar_catalogo_servicos()


def _obter_llm_vendedor() -> ChatGoogleGenerativeAI:
    """Instancia o modelo LLM do agente vendedor."""
    return ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0.3,
    )


def vendedor(estado: EstadoFluxo) -> dict[str, str]:
    """Nó do LangGraph responsável por redigir a proposta comercial personalizada.

    Args:
        estado (EstadoFluxo): Estado do fluxo contendo as informações da empresa
            analisada e o caminho do relatório gerencial.

    Returns:
        dict[str, str]: Dicionário com 'proposta' e 'arquivo_proposta'.

    Raises:
        FileNotFoundError: Se o relatório gerencial indicado não existir.
        ValueError: Se a resposta da LLM for vazia.
    """
    caminho_relatorio = Path(estado["arquivo"])
    if not caminho_relatorio.exists():
        raise FileNotFoundError(
            f"Relatório gerencial não localizado no caminho: {caminho_relatorio}"
        )

    conteudo_relatorio = caminho_relatorio.read_text(encoding="utf-8")
    info_empresa = EMPRESAS[estado["empresa"]]

    contexto_venda = f"""
PRESTADORA DOS SERVIÇOS:
IdeiaFlui

CATÁLOGO OFICIAL DE SERVIÇOS:
{yaml.safe_dump(SERVICOS, allow_unicode=True, sort_keys=False)}

CLIENTE POTENCIAL:
{info_empresa['nome_completo']}

SEGMENTO:
{info_empresa['segmento']}

PÚBLICO-ALVO:
{info_empresa['publico_alvo']}

ASSUNTO ORIGINAL:
{estado['assunto']}

BRIEFING:
{estado['briefing']}

RELATÓRIO GERENCIAL:
{conteudo_relatorio}

INSTRUÇÃO:
Analise o relatório, identifique as dificuldades da empresa
e elabore uma proposta comercial da IdeiaFlui.

Selecione somente os serviços do catálogo que sejam
compatíveis com os problemas identificados.
"""

    llm = _obter_llm_vendedor()
    resposta = llm.invoke(
        [
            SystemMessage(PROMPT_SISTEMA_VENDEDOR),
            HumanMessage(contexto_venda),
        ]
    )

    texto_proposta = resposta.text
    if not texto_proposta or not texto_proposta.strip():
        raise ValueError("O agente vendedor retornou uma proposta vazia.")

    caminho_arquivo_proposta = caminho_relatorio.parent / "proposta_venda.md"
    caminho_arquivo_proposta.write_text(texto_proposta, encoding="utf-8")

    return {
        "proposta": texto_proposta,
        "arquivo_proposta": str(caminho_arquivo_proposta),
    }


# Aliases para compatibilidade
SISTEMA = PROMPT_SISTEMA_VENDEDOR
SERVICOS_PATH = CAMINHO_SERVICOS
carregar_servicos = carregar_catalogo_servicos

"""Módulo de definição da equipe da Aurora Skin com CrewAI.

Este módulo implementa a equipe multiagente da marca de cosméticos Aurora Skin,
composta por especialistas em marketing e conteúdo, e-commerce e conversão,
ciência cosmética e gerência geral.
"""

from pathlib import Path
from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task

# Caminhos base para as configurações de agentes e tarefas
DIRETORIO_ATUAL = Path(__file__).resolve().parent
RAIZ_PROJETO = DIRETORIO_ATUAL.parents[1]
CONFIG_DIR = RAIZ_PROJETO / "config" / "empresas" / "aurora_skin"


@CrewBase
class EquipeAuroraSkin:
    """Equipe multiagente da Aurora Skin (Cosméticos & E-commerce).

    Responsável por planejar ações de marketing, otimização de conversão em
    e-commerce e validação técnica de formulações cosméticas, gerando um
    relatório semanal consolidado com seus gargalos operacionais.
    """

    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config = str(CONFIG_DIR / "agents.yaml")
    tasks_config = str(CONFIG_DIR / "tasks.yaml")

    def _obter_llm(self) -> LLM:
        """Cria e configura o modelo de linguagem (LLM) para os agentes.

        Returns:
            LLM: Instância configurada do CrewAI LLM com modelo Gemini.
        """
        return LLM(
            model="gemini/gemini-3.6-flash",
            max_tokens=600,
            temperature=0.3,
        )

    @agent
    def agente_marketing_aurora(self) -> Agent:
        """Agente responsável pela criação de conteúdo educativo e criativos.

        Returns:
            Agent: Especialista em marketing da Aurora Skin.
        """
        return Agent(
            config=self.agents_config["agente_marketing_aurora"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def agente_ecommerce_aurora(self) -> Agent:
        """Agente responsável pela gestão de loja online e quebra de objeções.

        Returns:
            Agent: Gestor de e-commerce e conversão da Aurora Skin.
        """
        return Agent(
            config=self.agents_config["agente_ecommerce_aurora"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def agente_produto_aurora(self) -> Agent:
        """Agente responsável pela revisão técnica e segurança regulatória cosmética.

        Returns:
            Agent: Especialista em produto e ciência cosmética.
        """
        return Agent(
            config=self.agents_config["agente_produto_aurora"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def gerente_geral_aurora(self) -> Agent:
        """Agente de gestão geral e consolidação do relatório semanal.

        Returns:
            Agent: Gerente geral da Aurora Skin.
        """
        return Agent(
            config=self.agents_config["gerente_geral_aurora"],
            llm=self._obter_llm(),
            verbose=True,
        )

    # Tarefas
    @task
    def plano_marketing(self) -> Task:
        """Tarefa de planejamento de conteúdo, anúncios e tendências de mercado.

        Returns:
            Task: Tarefa configurada para o especialista de marketing.
        """
        return Task(config=self.tasks_config["plano_marketing"])

    @task
    def plano_ecommerce(self) -> Task:
        """Tarefa de ajustes da oferta, quebra de objeções e pós-venda.

        Returns:
            Task: Tarefa configurada para o gestor de e-commerce.
        """
        return Task(config=self.tasks_config["plano_ecommerce"])

    @task
    def validacao_produto(self) -> Task:
        """Tarefa de revisão técnica de alegações e elaboração de glossário.

        Returns:
            Task: Tarefa configurada para a especialista de produto.
        """
        return Task(config=self.tasks_config["validacao_produto"])

    @task
    def relatorio_gerencial_aurora(self) -> Task:
        """Tarefa de consolidação executiva e mapeamento de gargalos.

        Returns:
            Task: Tarefa configurada para consolidação do relatório gerencial.
        """
        return Task(config=self.tasks_config["relatorio_gerencial_aurora"])

    @crew
    def equipe(self) -> Crew:
        """Monta a equipe sequencial da Aurora Skin com seus agentes e tarefas.

        Returns:
            Crew: Instância da equipe configurada com processo sequencial.
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

    def crew(self) -> Crew:
        """Alias para o método equipe() visando compatibilidade com CrewAI padrão.

        Returns:
            Crew: Instância da equipe configurada.
        """
        return self.equipe()


# Aliases para compatibilidade
Aurora_Skin = EquipeAuroraSkin
AuroraSkin = EquipeAuroraSkin


if __name__ == "__main__":
    from dotenv import load_dotenv
    from src.fluxo.equipes import carregar_restricoes_empresa

    load_dotenv()
    briefing_exemplo = (
        "Planejar a semana de lançamento do Kit Ritual Serenidade, com ações de "
        "conteúdo, vendas e explicação dos produtos."
    )
    restricoes_exemplo = carregar_restricoes_empresa("aurora_skin")
    resultado = EquipeAuroraSkin().equipe().kickoff(
        inputs={"briefing": briefing_exemplo, "restricoes": restricoes_exemplo}
    )
    print("Execução da equipe Aurora Skin concluída:")
    print(resultado)

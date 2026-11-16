"""Módulo de definição da equipe da Atlas Gestão Financeira com CrewAI.

Este módulo implementa a equipe multiagente da empresa fictícia Atlas Gestão,
composta por especialistas em controle financeiro, rotinas fiscais,
liderança comercial B2B e gerência executiva.
"""

from pathlib import Path
from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task

# Caminhos base para as configurações de agentes e tarefas
DIRETORIO_ATUAL = Path(__file__).resolve().parent
RAIZ_PROJETO = DIRETORIO_ATUAL.parents[1]
CONFIG_DIR = RAIZ_PROJETO / "config" / "empresas" / "atlas_gestao"


@CrewBase
class EquipeAtlasGestao:
    """Equipe multiagente da Atlas Gestão Financeira.

    Responsável por analisar dados simulados de finanças, conciliação fiscal e
    prospecção comercial, consolidando tudo em um relatório gerencial com
    foco em identificação de gargalos operacionais.
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
    def agente_financeiro_atlas(self) -> Agent:
        """Agente responsável pela gestão financeira e fluxo de caixa.

        Returns:
            Agent: Especialista de controle financeiro da Atlas Gestão.
        """
        return Agent(
            config=self.agents_config["agente_financeiro_atlas"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def agente_fiscal_atlas(self) -> Agent:
        """Agente responsável pela esteira e validação de NF-e.

        Returns:
            Agent: Analista fiscal e de processos da Atlas Gestão.
        """
        return Agent(
            config=self.agents_config["agente_fiscal_atlas"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def agente_comercial_atlas(self) -> Agent:
        """Agente responsável pelo posicionamento comercial e qualificação de leads.

        Returns:
            Agent: Líder comercial e de conteúdo B2B da Atlas Gestão.
        """
        return Agent(
            config=self.agents_config["agente_comercial_atlas"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def gerente_geral_atlas(self) -> Agent:
        """Agente gestor geral responsável pela consolidação e identificação de gargalos.

        Returns:
            Agent: Sócio-gerente da Atlas Gestão.
        """
        return Agent(
            config=self.agents_config["gerente_geral_atlas"],
            llm=self._obter_llm(),
            verbose=True,
        )

    # Tarefas
    @task
    def painel_financeiro(self) -> Task:
        """Tarefa de elaboração do painel de fluxo de caixa e DRE gerencial.

        Returns:
            Task: Tarefa configurada para o agente financeiro.
        """
        return Task(config=self.tasks_config["painel_financeiro"])

    @task
    def rotina_fiscal(self) -> Task:
        """Tarefa de desenho e quantificação da rotina manual de NF-e.

        Returns:
            Task: Tarefa configurada para o analista fiscal.
        """
        return Task(config=self.tasks_config["rotina_fiscal"])

    @task
    def plano_comercial(self) -> Task:
        """Tarefa de planejamento semanal de marketing e qualificação comercial.

        Returns:
            Task: Tarefa configurada para o líder comercial.
        """
        return Task(config=self.tasks_config["plano_comercial"])

    @task
    def relatorio_gerencial_atlas(self) -> Task:
        """Tarefa de consolidação de relatórios e levantamento de gargalos.

        Returns:
            Task: Tarefa de consolidação para o gerente geral.
        """
        return Task(config=self.tasks_config["relatorio_gerencial_atlas"])

    @crew
    def equipe(self) -> Crew:
        """Monta a equipe sequencial da Atlas Gestão com seus agentes e tarefas.

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


# Alias para compatibilidade com nomenclaturas anteriores
Atlas_Gestao = EquipeAtlasGestao
AtlasGestao = EquipeAtlasGestao


if __name__ == "__main__":
    from dotenv import load_dotenv
    from src.fluxo.equipes import carregar_restricoes_empresa

    load_dotenv()
    briefing_exemplo = (
        "Planejar e acompanhar a operação da próxima semana, identificando "
        "prioridades e gargalos de cada setor."
    )
    restricoes_exemplo = carregar_restricoes_empresa("atlas_gestao_financeira")
    resultado = EquipeAtlasGestao().equipe().kickoff(
        inputs={"briefing": briefing_exemplo, "restricoes": restricoes_exemplo}
    )
    print("Execução da equipe Atlas Gestão concluída:")
    print(resultado)

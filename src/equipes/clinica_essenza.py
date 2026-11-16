"""Módulo de definição da equipe da Clínica Essenza com CrewAI.

Este módulo implementa a equipe multiagente da clínica estética e médica boutique
Clínica Essenza, composta por especialistas em marketing em saúde, atendimento
e agendamento, gestão operacional/financeira e conformidade ética (CFM).
"""

from pathlib import Path
from crewai import LLM, Agent, Crew, Process, Task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai.project import CrewBase, agent, crew, task

# Caminhos base para as configurações de agentes e tarefas
DIRETORIO_ATUAL = Path(__file__).resolve().parent
RAIZ_PROJETO = DIRETORIO_ATUAL.parents[1]
CONFIG_DIR = RAIZ_PROJETO / "config" / "empresas" / "clinica_essenza"


@CrewBase
class EquipeClinicaEssenza:
    """Equipe multiagente da Clínica Essenza (Saúde & Estética Avançada).

    Responsável pela produção de conteúdo educativo em conformidade com as
    regras do CFM, elaboração do fluxo de acolhimento e agendamento de pacientes,
    acompanhamento de indicadores de ocupação/retornos e consolidação de gargalos
    operacionais.
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
    def agente_marketing_essenza(self) -> Agent:
        """Agente responsável pela comunicação educativa e posicionamento ético.

        Returns:
            Agent: Especialista de marketing da Clínica Essenza.
        """
        return Agent(
            config=self.agents_config["agente_marketing_essenza"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def agente_agendamento_essenza(self) -> Agent:
        """Agente responsável pelo primeiro contato, acolhimento e agendamentos.

        Returns:
            Agent: Atendente de agendamento e jornada do paciente.
        """
        return Agent(
            config=self.agents_config["agente_agendamento_essenza"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def gestor_operacional_essenza(self) -> Agent:
        """Agente responsável pela ocupação de salas, retornos e finanças.

        Returns:
            Agent: Gestor operacional da clínica.
        """
        return Agent(
            config=self.agents_config["gestor_operacional_essenza"],
            llm=self._obter_llm(),
            verbose=True,
        )

    @agent
    def gerente_geral_essenza(self) -> Agent:
        """Agente responsável pela conformidade ética e relatório executivo.

        Returns:
            Agent: Gerente geral e compliance da Clínica Essenza.
        """
        return Agent(
            config=self.agents_config["gerente_geral_essenza"],
            llm=self._obter_llm(),
            verbose=True,
        )

    # Tarefas
    @task
    def plano_conteudo(self) -> Task:
        """Tarefa de planejamento de conteúdo ético sem termos vetados pelo CFM.

        Returns:
            Task: Tarefa configurada para o especialista de marketing.
        """
        return Task(config=self.tasks_config["plano_conteudo"])

    @task
    def plano_atendimento(self) -> Task:
        """Tarefa de definição do fluxo de acolhimento e modelo de respostas.

        Returns:
            Task: Tarefa configurada para a atendente de agendamento.
        """
        return Task(config=self.tasks_config["plano_atendimento"])

    @task
    def painel_operacional(self) -> Task:
        """Tarefa de levantamento de KPIs operacionais e tarefas manuais da recepção.

        Returns:
            Task: Tarefa configurada para o gestor operacional.
        """
        return Task(config=self.tasks_config["painel_operacional"])

    @task
    def relatorio_gerencial_essenza(self) -> Task:
        """Tarefa de consolidação com auditoria ética e destaque de gargalos manuais.

        Returns:
            Task: Tarefa configurada para a gerência geral.
        """
        return Task(config=self.tasks_config["relatorio_gerencial_essenza"])

    @crew
    def equipe(self) -> Crew:
        """Monta a equipe sequencial da Clínica Essenza com seus agentes e tarefas.

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
Clinica_Essenza = EquipeClinicaEssenza
ClinicaEssenza = EquipeClinicaEssenza


if __name__ == "__main__":
    from dotenv import load_dotenv
    from src.fluxo.equipes import carregar_restricoes_empresa

    load_dotenv()
    briefing_exemplo = (
        "Planejar a próxima semana de operação, com foco em atrair novos pacientes "
        "para a consulta de 60 minutos e organizar a agenda e os retornos."
    )
    restricoes_exemplo = carregar_restricoes_empresa("clinica_essenza")
    resultado = EquipeClinicaEssenza().equipe().kickoff(
        inputs={"briefing": briefing_exemplo, "restricoes": restricoes_exemplo}
    )
    print("Execução da equipe Clínica Essenza concluída:")
    print(resultado)

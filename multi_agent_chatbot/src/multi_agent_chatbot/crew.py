from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import PDFSearchTool
from pathlib import Path
import yaml
from dotenv import load_dotenv

load_dotenv()

# Get the directory where the script is located
SCRIPT_DIR = Path(__file__).parent
pdf_path = str(SCRIPT_DIR / "agentops.pdf")

# Use the resolved path for the PDFSearchTool
pdf_search_tool = PDFSearchTool(pdf=pdf_path)

@CrewBase
class MultiAgentChatbot():
    """MultiAgentChatbot crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    ollama_llm = LLM(
        model="ollama/mistral:7b",
        base_url="http://localhost:11434"
    )

    @agent
    def pdf_rag_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_rag_agent'],
            tools=[pdf_search_tool],
            verbose=True,
            llm=self.ollama_llm
        )


    @agent
    def pdf_summary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_summary_agent'],
            verbose=True,
            llm=self.ollama_llm
        )

    @agent
    def pdf_mcq_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['pdf_mcq_agent'],
            verbose=True,
            llm=self.ollama_llm
        )

    @agent
    def ask_question_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ask_question_agent'],  # if you created a new agent config
            verbose=True,
            llm=self.ollama_llm
        )





    @task
    def pdf_rag_task(self) -> Task:
        return Task(
            config=self.tasks_config['pdf_rag_task'],
        )

    @task
    def pdf_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config['pdf_summary_task'],
        )

    @task
    def pdf_mcq_task(self) -> Task:
        return Task(
            config=self.tasks_config['pdf_mcq_task'],
        )

    @task
    def ask_question_task(self) -> Task:
        return Task(
            config=self.tasks_config['ask_question_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the PdfRag crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

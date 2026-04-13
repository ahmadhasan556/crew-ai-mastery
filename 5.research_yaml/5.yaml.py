from crewai import Agent, Crew,Task
from crewai.project import CrewBase ,agent , crew, task
from serpapi import GoogleSearch
from crewai.tools import BaseTool

from dotenv import load_dotenv
load_dotenv()
import os
SERP_API_KEY= os.getenv("SERPER_API_KEY")

#custiom tool
class SerpApiSearchTool(BaseTool):
  name:str = "google_search"
  description:str = "Search google using SerpApi and return the results"
  
  def _run(self,query:str):
    params = {
        "q": query,
        "hl": "en",
        "gl": "us",
        "api_key": SERP_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    # Extract top results (titles + links)
    if "organic_results" in results:
        return [
            {"title": r["title"], "link": r["link"], "snippet": r.get("snippet", "")}
            for r in results["organic_results"][:5]
        ]
    return {"error": "No results found"}
    

@CrewBase
class BlogCrew():
  """Blog writing crew"""
  
  agents_config = 'config/agent.yaml'
  tasks_config = 'config/tasks.yaml'
  
  @agent
  def researcher(self) -> Agent:
    return Agent(
      config = self.agents_config['research_agent'],
      tools=[SerpApiSearchTool()],
      verbose =True
    )
    
  @agent
  def writer(self) -> Agent:
    return Agent(
      config = self.agents_config['writer_agent'],
      verbose =True
    )
    
  @task
  def researcher_task(self) -> Task:
    return Task(
      config = self.tasks_config['research_task'],
      agent= self.researcher()
    )
    
  @task
  def writer_task(self) -> Task:
    return Task(
      config= self.tasks_config['writing_task'],
      agent= self.writer()
    )
    
  @crew
  def crew(self) -> Crew:
    return Crew(
      agents= [self.researcher(), self.writer()],
      tasks=  [self.researcher_task(), self.writer_task()]
    )
    
if __name__ == "__main__":
  blog_crew = BlogCrew()
  crew_instance = blog_crew.crew()
  crew_instance.kickoff(inputs={"topic": "P2P Clouds"})
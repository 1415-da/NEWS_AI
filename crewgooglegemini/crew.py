from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer
from dotenv import load_dotenv
import os
import sys
sys.path.append('..')
from config import GOOGLE_API_KEY, SERPER_API_KEY

# Load environment variables
load_dotenv()

# Set up API keys for LiteLLM
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["SERPER_API_KEY"] = SERPER_API_KEY

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process with enhanced feedback

try:
    result=crew.kickoff(inputs={'topic':'AI in healthcare'})
    print(result)
except Exception as e:
    print(f"Error occurred: {e}")
    print("Please make sure your GOOGLE_API_KEY is set in the config.py file")
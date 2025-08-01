## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os
import sys
sys.path.append('..')
from config import SERPER_API_KEY

os.environ['SERPER_API_KEY'] = SERPER_API_KEY

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()
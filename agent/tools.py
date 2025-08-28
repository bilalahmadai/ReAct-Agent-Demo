from crewai_tools import ScrapeWebsiteTool, SerperDevTool
import streamlit as st
import json
from agent.components import show_observation
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

search = SerperDevTool(n_results=5)

def calculate(what):
    with st.spinner("👩🏻‍💻 Calculating..."):
        result = eval(what)
        st.expander("Tool: Calculation", icon="👩🏻‍💻").info(show_observation(what, f"```bash\n{result}\n```"))
        return result
    
def google_search(what):
    with st.spinner("🔍 Searching..."):
        result = search.run(search_query=what)
        result = json.dumps(result, indent=2)
        result = f"```json\n{result}\n```"
        st.expander("Tool: Google Search", icon="🔍").info(show_observation(what, result))
        return result
    
def scrape_website(url):
    with st.spinner("🔍📄 Scraping..."):
        result = ScrapeWebsiteTool(url).run()
        show = result[:1500] + "\n\n..."
        st.expander("Tool: Scrape Website", icon="🔍").info(show_observation(url, show))
        return result
  
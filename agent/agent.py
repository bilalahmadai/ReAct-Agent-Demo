import streamlit as st
import re
import openai
from dotenv import load_dotenv
import os
from agent.components import show_thought
from agent.tools import calculate, google_search, scrape_website
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


class ChatBot:
    def __init__(self, system_prompt):
        self.messages = []
        if system_prompt:
            self.messages.append({"role": "system", "content": system_prompt})
        
    def __call__(self, message):
        self.messages.append({"role": "user", "content": message})
        result = self.execute()
        self.messages.append({"role": "assistant", "content": result})
        return result

    def execute(self):
        with st.spinner("🤖"):
            completion = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=self.messages
            )
            return completion.choices[0].message.content

known_actions = {
    "calculate": calculate,
    "google_search": google_search,
    "scrape_website": scrape_website,
}



action_re = re.compile('^Action: (\w+): (.*)')

def run_agent(question, max_turns=5):
    i = 0
    system_prompt = """
    You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop you output an Answer.
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.

Your available actions are:
calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point
syntax if necessary

google_search:
e.g. google_search: What is the capital of France?
Searches the web for the answer and returns the first result urls, titles and snippets

scrape_website:
e.g. scrape_website: https://en.wikipedia.org/wiki/France
Scrapes the website and returns the text

Example session:
Question: What is the capital of France?
Thought: I should look up France on Wikipedia
Action: wikipedia: France
PAUSE

You will be called again with this:
Observation: France is a country. The capital is Paris.

You then output:
Answer: The capital of France is Paris
    """
    bot = ChatBot(system_prompt)
    next_prompt = question
    
    while i < max_turns:
        i += 1
        st.write(f"✨ Thinking...")
        
        result = bot(next_prompt)
        
        # Extract thought if present
        for line in result.split('\n'):
            if line.startswith('Thought:'):
                thought = line.replace('Thought:', '').strip()
                show_thought(thought)
        
        # Look for actions
        actions = [action_re.match(a) for a in result.split('\n') if action_re.match(a)]
        if actions:
            st.write("💡 Performing Action...")
            with st.spinner("💡..."):
                action, action_input = actions[0].groups()
                if action not in known_actions:
                    raise Exception(f"Unknown action: {action}: {action_input}")
                tool_call = f"{action}: {action_input}"
                print("Tool Call: ",tool_call)
                st.write(f"🛠️ **{tool_call}**...")
                with st.spinner(f"🛠️..."):
                        
                    observation = known_actions[action](action_input)
                # print("Observation: ",observation)
                # show_observation(str(observation))
                
                
                
                next_prompt = f"Observation: {observation}"
        else:
            # If no actions, treat as final answer
            final_answer = result
            if result.startswith('Answer:'):
                final_answer = result.replace('Answer:', '').strip()
            st.markdown("---")
            st.header("🤖 Final Answer")
            st.markdown(final_answer)
            st.markdown("---")
            st.header("📜 History")
            st.json(bot.messages)
            break

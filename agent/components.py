import streamlit as st

def show_thought(thought: str):
    st.expander("Thought", icon="🤖").info(thought)

def show_observation(tool_input: str, observation: str):
    return f"{tool_input}\n## 🕵🏻‍♂️ Observation: \n{observation}"

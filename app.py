import streamlit as st
from agent.agent import run_agent

st.title("ReAct Agent")

prompt = st.text_input("Enter your prompt")
if st.button("Generate"):
    if prompt:
        run_agent(prompt, max_turns=10)
    else:
        st.warning("Please enter a prompt first!")


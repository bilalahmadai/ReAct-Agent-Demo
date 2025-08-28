# ReAct Agent Demo

<div align="center">
  <img src="scr/agent_demo.gif" width="400" alt="Agent Demo" style="display:inline-block;"/>
</div>

<p align="center">  
  <b>A demonstration of the ReAct (Reason + Act) paradigm for AI agents.</b>  
</p>

<p align="center">  
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-App-red?logo=streamlit" alt="Streamlit"></a>  
  <a href="./src/certificate.webp">
    <img src="https://img.shields.io/badge/Certificate-Hugging%20Face-yellow?logo=huggingface" alt="Certificate"></a>
</p>

---
> ⚠️ **Warning**  
> This project is for **learning purposes only** and is **not production-ready**.  

## 📌 Overview

The **ReAct Agent Demo** provides a hands-on example of how AI agents operate in a cycle of **reasoning, acting, and observing**.

This project is inspired by the Hugging Face **Agent Fundamentals** course and is intended for those interested in understanding **how agents internally work**.

---

## 🧠 The ReAct Paradigm

The agent operates in a continuous loop of:

1. **Think (LLM):** Reason about the current situation and decide the next step.
2. **Act (Tool):** Execute an action, such as calling a tool or function.
3. **Observe (Feedback):** Analyze the result and update reasoning.

This process continues until the agent completes its task.

---

## 🚀 Demo Features

- Step-by-step visualization of the agent’s **thoughts, actions, and observations**.
- Interactive prompt input to experiment with different queries.
- A simple and transparent way to understand AI agent workflows.

---

## ⚡ Getting Started

### 1. Install requirements

```bash
pip install streamlit crewai['tool']
```

### 2. Setup .env File

```bash
OPENAI_API_KEY = "*******"
SERPER_API_KEY = "*******"
```

### 3. Run the app

```bash
streamlit run app.py
```

### 4. Open in browser

Navigate to the URL provided by Streamlit to interact with the demo.

---

## 🙌 Acknowledgements

- Inspired by **AI Agents By Hugging Face🤗**.
- Developed by **Bilal Ahmad**.

---

<p align="center"><i>Explore how agents <b>Think → Act → Observe</b> in real time.</i></p>
<p align="center">
    <a href="https://huggingface.co/learn/agents-course/unit0/introduction">
        <img src="https://img.shields.io/badge/Start Learning-Hugging%20Face-yellow?logo=huggingface" alt="Start Learning">
    </a>
</p>


## 📫 Let's Connect  
[![LinkedIn](https://custom-icon-badges.demolab.com/badge/LinkedIn-0A66C2?logo=linkedin-white&logoColor=fff)](https://linkedin.com/in/bilalahmadai)  [![GitHub](https://img.shields.io/badge/-GitHub-000?style=flat&logo=github)](https://github.com/bilalahmadai)  [![Mail](https://img.shields.io/badge/Mail-D14836?logo=gmail&logoColor=white)](mailto:bilalahmadai.me@gmail.com)

📌 **Let's build AI solutions that drive real impact!**
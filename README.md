# 🚀 Code Review AI Environment

This project simulates a real-world **AI-powered code review system** where an intelligent agent analyzes code snippets and performs actions such as bug detection, performance optimization, and security analysis.

---

## 🧠 Overview

We built a **hybrid AI system** that combines:

- 🤖 **LLM-based reasoning (AI)**
- 🧠 **Rule-based fallback system**

This ensures:
- Intelligent decision-making
- High reliability even when APIs fail

---

## ✨ Features

- 🔍 Multi-type issue detection  
  - Syntax errors  
  - Performance issues  
  - Security vulnerabilities  

- ⚖️ Difficulty-based evaluation  
  - Easy / Medium / Hard levels  

- 🎯 Reward shaping system  
  - Full reward for correct actions  
  - Partial reward for near-correct decisions  

- 🔁 Hybrid AI architecture  
  - Uses AI when available  
  - Falls back to rule-based logic if needed  

- ⚡ Async environment design  

- 🐳 Dockerized & OpenEnv compatible  

---

## 🤖 Actions

The agent can perform:

- `report_bug` → Detect bugs or security issues  
- `improve_code` → Suggest optimizations  
- `approve` → Mark code as correct  

---

## 🧪 Example

### Input Code:
```python
eval(input())
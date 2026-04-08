# Code Review AI Environment

🔗 **Live Demo:** https://prateekpro-code-review-env.hf.space  

---

## Overview

This project simulates a real-world **AI-powered code review system** where an intelligent agent analyzes code snippets and performs:

- 🐞 Bug detection  
- ⚡ Performance optimization  
- 🔐 Security analysis  

We built a **hybrid AI system** that combines:

- 🤖 LLM-based reasoning  
- 🧠 Rule-based fallback system  

This ensures reliable performance even when AI is unavailable.

---

## Features

- 🔍 Multi-type issue detection  
  - Syntax errors  
  - Performance issues  
  - Security vulnerabilities  

- ⚖️ Difficulty-based evaluation  
  - Easy / Medium / Hard levels  

- 🎯 Reward shaping system  
  - Full reward for correct actions  
  - Partial reward for near-correct actions  

- 🔁 Hybrid AI architecture  
  - Uses AI when available  
  - Falls back to rule-based logic  

- ⚡ Async environment design  

- 🐳 Dockerized & OpenEnv compatible  

---

## Actions

- `report_bug` → Detect bugs or security issues  
- `improve_code` → Suggest improvements  
- `approve` → Mark code as correct  

---

## Example

### Input:
```python
eval(input())
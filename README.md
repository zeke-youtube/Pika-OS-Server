# 🚀 PikaOS Server

> Experimental, self-hosted server dashboard focused on **visibility**, not magic.

**PikaOS Server** is an experimental server runtime and web dashboard built by **Zeke**.  
Run one Python file, open a browser, and observe what your server is doing in real time.

This project is designed for **learning, experimentation, and transparency** — not production or enterprise use.

📘 **Documentation (Wiki):**  
https://github.com/zeke-youtube/Pika-OS-Server/wiki

---

## ⚠️ Disclaimer

> **This project is experimental.**  
> **Security is the responsibility of the operator.**

PikaOS Server:
- has not been security audited
- is not production-hardened
- makes no security guarantees

If you expose it to the internet, you do so at your own risk.

---

## ✨ Features

- 🖥️ **Modern Web Dashboard**  
  Clean, browser-based interface.

- 🌐 **Network Visibility**  
  View traffic, connections, and activity patterns.

- 📜 **System & Access Logs**  
  Real-time logs for transparency and debugging.

- 🚨 **Traffic Anomaly Detection**  
  Detect unusual traffic behavior.  
  *Mitigation: coming soon™*

- 🤖 **Optional AI Features**  
  Experimental AI assistance using `gpt-oss` via Groq (server-side only).

---

## 🧠 Project Philosophy

PikaOS Server is built around these ideas:

- **Safe defaults** (local-only by default)
- **Explicit warnings** for risky actions
- **Visibility over enforcement**
- **No hidden behavior**
- **No overpromising**

This project does **not** try to:
- replace firewalls
- provide enterprise security
- silently block attacks
- act like a full operating system

---

## ▶️ Getting Started

### Requirements
- Python 3.9+
- A modern web browser

### Run the server
```bash
python server.py
```
Open the dashboard

http://localhost:8000

Default mode is local-only and recommended.

⸻

🌐 Local vs Public Access
	•	Local (recommended):

127.0.0.1


	•	Public / Network (optional):

0.0.0.0



When public access is enabled, a warning is shown:

“Chill bro 😅 — this is not 100% secure.”

Public exposure is always opt-in.

⸻

🔐 Authentication

PikaOS Server uses PikaLogin, a self-hosted authentication system.
	•	Authentication is enabled by default
	•	Designed for trusted environments
	•	Prevents accidental access
	•	Not enterprise-grade security

Authentication exists to reduce exposure, not to guarantee safety.

⸻

🤖 AI Features (Optional)
	•	Disabled by default
	•	Runs server-side only
	•	Uses gpt-oss via Groq
	•	Requires a user-provided API key
	•	Rate-limited

AI is intended to assist, not automate decisions.

Create a .env file if you want AI:

GROQ_API_KEY=your_api_key_here


⸻

📁 Configuration

Main configuration is handled in:

configfile.py

Configuration controls:
	•	host & port
	•	authentication
	•	AI features
	•	logging
	•	experimental flags

Restart the server after changes.

⸻

🔍 Observability, Not Protection

PikaOS Server focuses on:
	•	logs
	•	network visibility
	•	transparency

It does not:
	•	block traffic
	•	prevent DDoS attacks
	•	enforce security policies

Use proper firewalls and infrastructure if exposing publicly.

⸻

🧪 Project Status

🚧 Early development
	•	APIs may change
	•	Features may be incomplete
	•	Breaking changes may occur
	•	“Coming soon™” means no promises

Stability and clarity matter more than feature count.

⸻

🛠️ Tech Stack
	•	Python
	•	Flask
	•	Web dashboard (HTML / JS)
	•	Optional AI via Groq (gpt-oss)
	•	GitHub CodeQL & Dependabot enabled

⸻

🤝 Contributing

Contributions are welcome, but expectations are realistic.
	•	Read CONTRIBUTING.md
	•	Open issues for bugs or ideas
	•	Small, focused PRs preferred

Not everything will be merged.

⸻

🔐 Security

See SECURITY.md for full details.

Summary:
	•	No audit
	•	No guarantees
	•	Operator is responsible
⸻
# Commercial Use

PikaOS Server may be used commercially.

For companies that require:
- custom features
- support
- internal deployment assistance

Please contact the maintainer.
⸻

📄 License

MIT License © 2026 Zeke Cheng

⸻

🧠 Final Note

PikaOS Server is honest about what it is — and what it is not.

If you want a polished, enterprise-ready solution, this project is probably not for you.
If you want to learn, experiment, and observe, welcome 😄

---

# 🚀 PikaOS Server

**PikaOS Server** is an experimental, self-hosted server dashboard and runtime built by **Zeke**.  
Run one Python file, open a browser, and manage everything through a modern web dashboard.

> ⚠️ **Disclaimer**  
> This project is experimental.  
> **Security is the responsibility of the operator.**

---

## ✨ Features

- 🖥️ **Modern Web Dashboard**  
  Clean, fast UI accessible from your browser.

- 🌐 **Network Activity Dashboard**  
  View traffic, connections, and request activity.

- 📜 **System & Access Logs**  
  Real-time logs for debugging and monitoring.

- 🚨 **Traffic Anomaly / DDoS Detection**  
  Detect abnormal traffic spikes.  
  *Mitigation: coming soon™*

- 🤖 **Optional AI Features**  
  Server-side AI calls using `gpt-oss` via Groq (rate-limited).

---

## 🧠 How It Works

1. Start the server:
   ```bash
   python server.py

	2.	Open the dashboard:

http://localhost:8000



Local vs Public Access
	•	Default: 127.0.0.1 (local only, recommended)
	•	Optional: 0.0.0.0 (public / network access)

When public access is enabled, a warning is shown:

“Chill bro 😅 — this is not 100% secure.”

⸻

🔐 Authentication

PikaOS Server uses PikaLogin, a self-hosted authentication service.
	•	Login required to access the dashboard
	•	Public exposure requires explicit opt-in
	•	Designed for trusted environments

This is not enterprise-grade authentication.

⸻

🤖 AI Features (Optional)
	•	Disabled by default
	•	Uses Groq (gpt-oss) via a server-side API key
	•	Rate-limited
	•	Depends on third-party availability

AI features may be limited or unavailable at any time.

⸻

💸 Pricing Model
	•	🆓 Free
	•	All core features
	•	Dashboard, logs, network view
	•	❌ No AI
	•	⭐ Premium
	•	AI features enabled
	•	Usage billed per minute
	•	🏢 Company
	•	No AI limits
	•	Custom usage
	•	🏛️ Government / Education
	•	Full access
	•	Free

Pricing and AI availability may change.

⸻

⚠️ Security Notice
	•	Experimental software
	•	No security audit
	•	No guarantee of safety
	•	Not production-hardened

Do not expose to the public internet unless you understand the risks.

⸻

🛠️ Tech Stack
	•	Python (backend)
	•	Web dashboard (HTML / JS)
	•	Optional AI via Groq (gpt-oss)
	•	Self-hosted authentication
	•	Cloudflare-hosted auth service

⸻

📌 Roadmap
	•	Improved traffic anomaly detection
	•	Optional DDoS mitigation
	•	More dashboard modules
	•	Plugin / runtime expansion

(“Coming soon” means whenever it actually comes.)

⸻

📄 License

MIT License © 2026 Zeke Cheng

---

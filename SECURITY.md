# 🔐 Security Policy

## ⚠️ Important Notice

**PikaOS Server is experimental software.**

This project has **not** been security audited and is **not** intended to be production-hardened.

> **Security is the responsibility of the operator.**

If you expose this software to a public network or the internet, you do so at your own risk.

---

## 🧠 Security Model (What This Project Does)

PikaOS Server focuses on:
- Visibility (logs, network activity)
- Access control (basic authentication)
- Warnings for unsafe configurations

It does **not** claim to provide:
- Enterprise-grade security
- Full DDoS protection
- Attack mitigation at scale
- Compliance guarantees

---

## 🌐 Public Exposure Warning

By default, PikaOS Server is intended to run on:

127.0.0.1

If configured to bind to:

0.0.0.0

A warning is shown:
> *“Chill bro 😅 — this is not 100% secure.”*

This warning exists to reduce **accidental exposure**, not to prevent all attacks.

---

## 🔐 Authentication

- Authentication is required to access the dashboard
- Uses a self-hosted authentication system (PikaLogin)
- Designed for trusted environments
- Not a replacement for enterprise identity systems

---

## 🤖 AI Features

- AI features are optional and disabled by default
- Use third-party APIs (Groq / gpt-oss)
- Rate-limited
- Availability depends on external services

No AI calls are made without user configuration.

---

## 🐛 Reporting Security Issues

If you discover a **security vulnerability**:

- Please **do not** publish exploits
- Open a GitHub issue with a clear description
- Provide steps to reproduce if possible

This is a small indie project, so response times may vary.

---

## 🚫 Out of Scope

The following are **out of scope** for security guarantees:

- Misconfigured deployments
- Exposing the dashboard publicly without protection
- Third-party service failures
- User-provided plugins or modifications

---

## 📄 Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

By using this software, you acknowledge that:
- It may contain bugs
- It may be insecure
- It may change or break at any time

---

## 👤 Maintainer

Maintained by **Zeke**  
Solo developer. Experimental systems.

---

Thanks for understanding and using PikaOS Server responsibly 😄


⸻

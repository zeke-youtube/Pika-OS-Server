"""
PikaOS Server Configuration File

This project is experimental.
Security is the responsibility of the operator.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env (optional)
load_dotenv()

# -------------------------
# Server Settings
# -------------------------

# Host binding
# Use "127.0.0.1" for local-only (recommended)
# Use "0.0.0.0" to expose to network / internet
HOST = "127.0.0.1"

# Server port
PORT = 8000

# Debug mode (DO NOT use in public mode)
DEBUG = False


# -------------------------
# Authentication
# -------------------------

# Enable authentication
AUTH_ENABLED = True

# Authentication provider
# Options: "pikalogin", "local", "none"
AUTH_PROVIDER = "pikalogin"

# PikaLogin service URL
PIKA_LOGIN_URL = "https://zekecologin.dpdns.org"


# -------------------------
# AI Features
# -------------------------

# Enable AI features
AI_ENABLED = False

# Groq API key (stored in .env)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model name
AI_MODEL = "gpt-oss"

# Simple rate limit (seconds between requests)
AI_COOLDOWN_SECONDS = 15


# -------------------------
# Logging
# -------------------------

# Enable logging
LOGGING_ENABLED = True

# Log level: DEBUG, INFO, WARNING, ERROR
LOG_LEVEL = "INFO"

# Log file path (None = console only)
LOG_FILE = None


# -------------------------
# Network / Security Warnings
# -------------------------

# Show warning when HOST is 0.0.0.0
SHOW_PUBLIC_WARNING = True

PUBLIC_WARNING_TEXT = (
    "Chill bro 😅\n"
    "You are about to expose this dashboard to the public internet.\n"
    "This project is not 100% secure."
)


# -------------------------
# Experimental Flags
# -------------------------

# Traffic anomaly detection (experimental)
ENABLE_TRAFFIC_DETECTION = False

# DDoS mitigation (coming soon™)
ENABLE_DDOS_MITIGATION = False

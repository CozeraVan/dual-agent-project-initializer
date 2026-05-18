$ErrorActionPreference = "Stop"
try { py -3 scripts/agent_status.py } catch { python scripts/agent_status.py }

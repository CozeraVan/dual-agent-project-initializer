$ErrorActionPreference = "Stop"
try { py -3 scripts/check_progress_docs.py } catch { python scripts/check_progress_docs.py }

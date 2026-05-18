$ErrorActionPreference = "Stop"
try { py -3 scripts/git_finalize_check.py } catch { python scripts/git_finalize_check.py }

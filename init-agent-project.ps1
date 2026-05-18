$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
try {
    py -3 "$ScriptDir\init-agent-project.py" @args
} catch {
    python "$ScriptDir\init-agent-project.py" @args
}

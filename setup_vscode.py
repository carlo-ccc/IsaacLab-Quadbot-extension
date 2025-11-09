import json
from pathlib import Path

def main():
    root = Path(__file__).parent
    vscode_dir = root / ".vscode"
    vscode_dir.mkdir(exist_ok=True)
    settings_path = vscode_dir / "settings.json"

    settings = {
        "python.defaultInterpreterPath": str((root / ".venv" / "Scripts" / "python.exe")),
        "python.testing.pytestEnabled": True,
        "python.testing.unittestEnabled": False,
        "editor.formatOnSave": True,
        "python.formatting.provider": "black",
        "files.eol": "\n",
        "terminal.integrated.defaultProfile.windows": "PowerShell",
    }

    if settings_path.exists():
        try:
            existing = json.loads(settings_path.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
        existing.update(settings)
        settings = existing

    settings_path.write_text(json.dumps(settings, indent=2), encoding="utf-8")
    print(f"Wrote {settings_path}")

if __name__ == "__main__":
    main()
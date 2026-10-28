"""Execute this original stdlib-only notebook unchanged, with network disabled.

Default: compare actual outputs with the saved notebook; no source-file writes.
Optional: --write-output PATH saves a newly executed copy for review.
This is sequential Python execution, not a Jupyter-kernel execution claim.
MIT License. Copyright (c) 2026 szj2ys.
"""
import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import socket
import sys


def no_network(*args, **kwargs):
    raise RuntimeError("Network is disabled for offline notebook reproduction")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-output", type=Path, help="Save a reviewed execution copy; default only compares outputs")
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    os.chdir(base)
    notebook = json.loads((base / "audit.ipynb").read_text(encoding="utf-8"))
    socket.socket = no_network
    socket.create_connection = no_network
    namespace = {"__name__": "__main__"}
    different = []
    execution = 0
    for cell in notebook["cells"]:
        if cell["cell_type"] != "code":
            continue
        execution += 1
        source = "".join(cell["source"])
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
            exec(compile(source, "notebook-cell-" + str(execution), "exec"), namespace)
        text = stream.getvalue()
        actual = [{"output_type":"stream", "name":"stdout", "text":text}] if text else []
        # Normalize notebook list-of-lines text representation before comparing.
        saved = cell.get("outputs", [])
        for output in saved:
            if isinstance(output.get("text"), list):
                output["text"] = "".join(output["text"])
        if actual != saved:
            different.append(cell.get("id", str(execution)))
        cell["outputs"] = actual
        cell["execution_count"] = execution
        print("--- Code cell", execution, "---")
        print(text, end="")
    notebook["metadata"]["audit_execution"] = {
        "executed_at":datetime.now(timezone.utc).isoformat(),
        "method":"Fresh sequential Python execution; exact code cells; network sockets blocked; not a Jupyter kernel",
        "python_version":sys.version.split()[0], "code_cells":execution,
    }
    if args.write_output:
        target = args.write_output.resolve()
        if target == base / "audit.ipynb":
            raise ValueError("Use a separate execution-copy path; do not overwrite the source notebook")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(notebook,indent=1,ensure_ascii=False)+'\n',encoding='utf-8')
        print("Executed", execution, "code cells; saved separate execution copy.")
    elif different:
        raise SystemExit("Saved outputs differ in cells: " + ", ".join(different))
    else:
        print("PASS:", execution, "code cells executed; all saved outputs match; no network.")


if __name__ == "__main__":
    main()

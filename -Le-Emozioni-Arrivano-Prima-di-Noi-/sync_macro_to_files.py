#!/usr/bin/env python3
"""
Sincronizza i 3 file macro con i file Markdown separati del progetto.

Uso:
    python3 sync_macro_to_files.py --project-dir .

Opzioni:
    --dry-run   mostra cosa verrebbe modificato senza scrivere
    --no-backup non crea copie .bak
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


START_RE = re.compile(
    r"^# --- INIZIO FILE: (?P<name>[^/\r\n]+\.md) ---\s*$",
    re.MULTILINE,
)

DEFAULT_MACROS = (
    "00-04_LINEE_GUIDA_E_PROGETTO.md",
    "05-09_OPERATIVO_E_RICERCA.md",
    "10-14_CAPITOLO_1_E_MANOSCRITTO.md",
)


@dataclass(frozen=True)
class Section:
    filename: str
    content: str
    macro: Path


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").strip()


def extract_sections(macro_path: Path) -> list[Section]:
    text = macro_path.read_text(encoding="utf-8")
    matches = list(START_RE.finditer(text))

    if not matches:
        raise ValueError(
            f"Nessun marcatore trovato in {macro_path.name}. "
            "Formato richiesto: # --- INIZIO FILE: nome.md ---"
        )

    sections: list[Section] = []

    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)

        filename = match.group("name")
        content = text[start:end].lstrip("\r\n").rstrip() + "\n"

        sections.append(
            Section(
                filename=filename,
                content=content,
                macro=macro_path,
            )
        )

    return sections


def resolve_macro(project_dir: Path, requested_name: str) -> Path:
    exact = project_dir / requested_name
    if exact.exists():
        return exact

    stem = Path(requested_name).stem
    candidates = sorted(project_dir.glob(f"{stem}*.md"))

    if len(candidates) == 1:
        return candidates[0]

    if not candidates:
        raise FileNotFoundError(f"File macro non trovato: {requested_name}")

    names = ", ".join(path.name for path in candidates)
    raise RuntimeError(
        f"Più varianti trovate per {requested_name}: {names}. "
        "Rinomina quella corretta con il nome canonico."
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Sincronizza i file macro con i file Markdown separati."
    )
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=Path.cwd(),
        help="Cartella principale del progetto",
    )
    parser.add_argument(
        "--macro",
        action="append",
        dest="macros",
        help="File macro da elaborare; opzione ripetibile",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Mostra le modifiche senza scrivere",
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Non creare file .bak",
    )
    args = parser.parse_args()

    project_dir = args.project_dir.expanduser().resolve()

    if not project_dir.is_dir():
        print(f"ERRORE: cartella non valida: {project_dir}", file=sys.stderr)
        return 2

    macro_names = tuple(args.macros) if args.macros else DEFAULT_MACROS

    try:
        macro_paths = [
            resolve_macro(project_dir, macro_name)
            for macro_name in macro_names
        ]
    except (FileNotFoundError, RuntimeError) as error:
        print(f"ERRORE: {error}", file=sys.stderr)
        return 2

    collected: dict[str, Section] = {}
    duplicate_sources: dict[str, list[Path]] = {}

    try:
        for macro_path in macro_paths:
            for section in extract_sections(macro_path):
                previous = collected.get(section.filename)

                if previous is None:
                    collected[section.filename] = section
                    continue

                duplicate_sources.setdefault(
                    section.filename,
                    [previous.macro],
                ).append(section.macro)

                if normalize(previous.content) != normalize(section.content):
                    print(
                        f"ERRORE: {section.filename} compare in più macro "
                        "con contenuti differenti.",
                        file=sys.stderr,
                    )
                    print(f"  - {previous.macro.name}", file=sys.stderr)
                    print(f"  - {section.macro.name}", file=sys.stderr)
                    return 3

    except (OSError, UnicodeError, ValueError) as error:
        print(f"ERRORE: {error}", file=sys.stderr)
        return 2

    if duplicate_sources:
        print("AVVISO: sezioni duplicate ma identiche:")
        for filename, sources in sorted(duplicate_sources.items()):
            source_names = ", ".join(path.name for path in sources)
            print(f"  {filename}: {source_names}")
        print()

    changed = 0
    unchanged = 0

    for filename, section in sorted(collected.items()):
        destination = project_dir / filename

        try:
            current = (
                destination.read_text(encoding="utf-8")
                if destination.exists()
                else None
            )
        except (OSError, UnicodeError) as error:
            print(f"ERRORE leggendo {destination}: {error}", file=sys.stderr)
            return 2

        if current is not None and normalize(current) == normalize(section.content):
            print(f"INVARIATO   {filename}")
            unchanged += 1
            continue

        if args.dry_run:
            action = "CREEREBBE" if current is None else "AGGIORNEREBBE"
            print(f"{action:<12} {filename} <- {section.macro.name}")
            changed += 1
            continue

        try:
            if destination.exists() and not args.no_backup:
                backup = destination.with_suffix(destination.suffix + ".bak")
                shutil.copy2(destination, backup)

            destination.write_text(section.content, encoding="utf-8")

        except OSError as error:
            print(f"ERRORE scrivendo {destination}: {error}", file=sys.stderr)
            return 2

        action = "CREATO" if current is None else "AGGIORNATO"
        print(f"{action:<12} {filename} <- {section.macro.name}")
        changed += 1

    if args.dry_run:
        print(
            f"\nSimulazione completata: {changed} file cambierebbero, "
            f"{unchanged} già allineati."
        )
    else:
        print(
            f"\nSincronizzazione completata: {changed} file modificati, "
            f"{unchanged} già allineati."
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
# Estrae dal glossario approvato solo le righe dei termini tecnici che riguardano un file, piu eccezioni e parole vaghe.
# Uso: python3 strumenti/scheda_glossario.py CAP06 [reports/struttura/GLOSSARIO_LIBRO.md]
import re, sys

sigla = sys.argv[1].upper()
g = open(sys.argv[2] if len(sys.argv) > 2 else 'reports/struttura/GLOSSARIO_LIBRO.md', encoding='utf-8').read()
def sezione(titolo):
    m = re.search(r'^## ' + titolo + r'.*?$(.*?)(?=^## |\Z)', g, flags=re.M | re.S)
    return m.group(1).strip() if m else ''
righe = [r for r in sezione('Termini tecnici').splitlines() if r.startswith('|')]
intest, corpo = righe[:2], righe[2:]
mie = [r for r in corpo if re.search(r'\b' + sigla + r'\b', r.split('|')[-2] if r.count('|') > 2 else r)]
print(f"# Scheda glossario per {sigla} ({len(mie)} termini su {len(corpo)})\n")
print('\n'.join(intest + mie))
vaghe = [r for r in sezione('Parole vaghe').splitlines() if r.startswith('|')]
print("\n## Parole vaghe che compaiono in " + sigla + "\n")
print('\n'.join(vaghe[:2] + [r for r in vaghe[2:] if re.search(r'\b' + sigla + r'\b', r)]))
print("\n## Eccezioni ammesse\n")
print(sezione('Eccezioni ammesse'))

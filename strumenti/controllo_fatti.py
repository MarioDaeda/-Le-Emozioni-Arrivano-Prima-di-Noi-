#!/usr/bin/env python3
# Confronta un capitolo con una versione precedente (default: main) e segnala i "fatti" che sono diminuiti:
# numeri (cifre, ore, percentuali, importi) e parole con l'iniziale maiuscola (nomi propri, aziende, sigle).
# Uso: python3 strumenti/controllo_fatti.py capitoli/CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md [riferimento_git]
# Non giudica: elenca solo ciò che compare meno volte di prima. Va letto da una persona o da un modello.
import re, subprocess, sys
from collections import Counter

percorso = sys.argv[1]
rif = sys.argv[2] if len(sys.argv) > 2 else 'main'
prima = subprocess.run(['git', 'show', f'{rif}:{percorso}'], capture_output=True, text=True, encoding='utf-8').stdout
dopo = open(percorso, encoding='utf-8').read()
if not prima:
    sys.exit(f"Nessuna versione di {percorso} in {rif}")

def fatti(t):
    t = '\n'.join(r for r in t.splitlines() if not r.lstrip().startswith('#'))  # niente titoli
    num = re.findall(r'\d+(?:[.,:]\d+)*\s?%?', t)
    # Solo maiuscole dentro la frase (dopo una minuscola, una cifra o una virgola): esclude gli inizi di frase.
    nomi = re.findall(r"(?<=[a-zà-ÿ0-9,;] )[A-ZÀ-Ý][\wÀ-ÿ'’.-]*[A-Za-zÀ-ÿ0-9]", t)
    return Counter(x.strip() for x in num), Counter(nomi)

(np, mp), (nd, md) = fatti(prima), fatti(dopo)
def diff(a, b):
    return sorted(((k, a[k], b.get(k, 0)) for k in a if b.get(k, 0) < a[k]), key=lambda x: (x[2] > 0, x[0]))
dn, dm = diff(np, nd), diff(mp, md)
print(f"numeri diminuiti={len(dn)} (spariti={sum(1 for x in dn if x[2] == 0)})")
for k, a, b in dn:
    print(f"  NUM {'SPARITO ' if b == 0 else ''}{k!r}: prima {a}, dopo {b}")
print(f"parole maiuscole diminuite={len(dm)} (sparite={sum(1 for x in dm if x[2] == 0)}). Solo le sparite:")
for k, a, b in dm:
    if b == 0:
        print(f"  NOME SPARITO {k!r}: prima {a}")

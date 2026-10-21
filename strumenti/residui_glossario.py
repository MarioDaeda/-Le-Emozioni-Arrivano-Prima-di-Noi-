#!/usr/bin/env python3
# Cerca in capitoli/ le "forme da sostituire" del glossario approvato e ne elenca le occorrenze rimaste.
# Sono candidati: eccezioni ammesse (citazioni, mail, battute, titoli) vanno escluse da chi legge l'elenco.
# Uso: python3 strumenti/residui_glossario.py [glossario] [cartella_o_file]   (default: GLOSSARIO_LIBRO.md e capitoli/)
import glob, os, re, sys

g = open(sys.argv[1] if len(sys.argv) > 1 else 'reports/struttura/GLOSSARIO_LIBRO.md', encoding='utf-8').read()
cartella = sys.argv[2] if len(sys.argv) > 2 else 'capitoli'
m = re.search(r'^## Termini tecnici.*?$(.*?)(?=^## |\Z)', g, flags=re.M | re.S)
forme = []
for r in (m.group(1) if m else '').splitlines():
    c = [x.strip() for x in r.split('|')]
    if len(c) < 5 or not c[1].isdigit():
        continue
    scelta, da_sost = c[2], re.sub(r'\([^)]*\)', '', c[3])
    for f in re.split(r'[,;]', da_sost):
        f = f.strip(' "“”«».').strip()
        if len(f) >= 4 and '"' not in f and ' solo ' not in f and f.lower() not in scelta.lower():
            forme.append((f, scelta))
file = [cartella] if os.path.isfile(cartella) else sorted(p for p in glob.glob(os.path.join(cartella, '*.md')) if not os.path.basename(p).startswith('._'))
per_file = {}
tot = 0
for forma, scelta in forme:
    pat = re.compile(r'(?<![\wÀ-ÿ])' + re.escape(forma) + r'(?![\wÀ-ÿ])', re.I)
    for p in file:
        for n, riga in enumerate(open(p, encoding='utf-8'), 1):
            for mm in pat.finditer(riga):
                tot += 1
                per_file[os.path.basename(p)] = per_file.get(os.path.basename(p), 0) + 1
                print(f"{os.path.basename(p)[:12]}:{n}  «{forma}» → «{scelta}»  …{riga[max(0, mm.start() - 50):mm.end() + 30].strip()}…")
print(f"\nforme cercate={len(forme)} occorrenze trovate={tot}")
for k, v in sorted(per_file.items()):
    print(f"  {k}: {v}")

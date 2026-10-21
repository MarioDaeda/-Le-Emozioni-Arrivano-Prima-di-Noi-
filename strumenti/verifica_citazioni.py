#!/usr/bin/env python3
# Controlla che le citazioni di un report esistano parola per parola nel capitolo.
# Citazioni lette: blocchi che iniziano con ">", esclusi quelli preceduti da una riga "Proposta".
# Uso: python3 strumenti/verifica_citazioni.py reports/struttura/CAP06_struttura.md capitoli/CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md
# Confronto tollerante: ignora maiuscole, spazi, asterischi, trattini bassi e tipo di virgolette o apostrofi.
import re, sys

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('–', '-').replace('—', '-').replace('…', '...')
    s = re.sub(r'[*_`«»"“”]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()

rep = open(sys.argv[1], encoding='utf-8').read()
cap = norm(re.sub(r'^>\s?', '', open(sys.argv[2], encoding='utf-8').read(), flags=re.M))
# Salta i blocchi che sono proposte di riscrittura (preceduti da una riga con "Proposta").
blocchi = []
for mb in re.finditer(r'(?:^>.*(?:\n|$))+', rep, flags=re.M):
    prima = [r for r in rep[:mb.start()].splitlines() if r.strip()][-1:]
    if prima and 'proposta' in prima[0].lower():
        continue
    blocchi.append(re.sub(r'^>\s?', '', mb.group(0), flags=re.M))
trovate, mancanti = 0, []
for b in blocchi:
    q = norm(b).strip(' .')
    if len(q.split()) < 4:
        continue
    if q in cap:
        trovate += 1
    else:
        mancanti.append(b.strip().replace('\n', ' ')[:140])
print(f"citazioni={trovate + len(mancanti)} trovate={trovate} mancanti={len(mancanti)}")
for m in mancanti:
    print("NON TROVATA:", m)

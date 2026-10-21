#!/usr/bin/env python3
# Dalla scheda di lavoro estrae gli interventi di frase "da tenere" e "da correggere"
# la cui citazione originale esiste ancora (una sola volta) nel capitolo, e scrive l'elenco per l'esecutore Haiku.
# Uso: python3 strumenti/prepara_da_applicare.py reports/struttura/lavoro/CAP06_scheda.md capitoli/CAPITOLO_06_....md > reports/struttura/lavoro/CAP06_da_applicare.md
# Formato atteso nella scheda (sezione 3):
#   ### [NN] da tenere            (oppure: da correggere / da sospendere)
#   > citazione originale
#   Proposta:
#   > proposta
import re, sys

def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('–', '-').replace('—', '-').replace('…', '...')
    s = re.sub(r'[*_`«»"“”]', '', s)
    return re.sub(r'\s+', ' ', s).strip().lower()

scheda = open(sys.argv[1], encoding='utf-8').read()
cap = norm(re.sub(r'^>\s?', '', open(sys.argv[2], encoding='utf-8').read(), flags=re.M))
voci = re.split(r'^###\s+', scheda, flags=re.M)[1:]
ok, superate, sospese, malformate = [], [], [], []
for v in voci:
    m = re.match(r'\[(\d+)\]\s*(da tenere|da correggere|da sospendere)', v, flags=re.I)
    if not m:
        continue
    num, stato = m.group(1), m.group(2).lower()
    blocchi = [re.sub(r'^>\s?', '', b, flags=re.M).strip() for b in re.findall(r'(?:^>.*(?:\n|$))+', v, flags=re.M)]
    if stato == 'da sospendere':
        orig = blocchi[0] if blocchi else ''
        if orig and cap.count(norm(orig).strip(' .')) == 1:
            sospese.append(num)
        continue
    if len(blocchi) < 2 or 'proposta' not in v.lower():
        malformate.append(num)
        continue
    orig, prop = blocchi[0], blocchi[1]
    if cap.count(norm(orig).strip(' .')) == 1:
        ok.append((num, stato, orig, prop))
    else:
        superate.append(num)
print("# Interventi di frase da applicare alla lettera\n")
for num, stato, orig, prop in ok:
    print(f"### [{num}] {stato}\n")
    print('\n'.join('> ' + r for r in orig.splitlines()))
    print("\nProposta:\n")
    print('\n'.join('> ' + r for r in prop.splitlines()))
    print()
print("<!-- RIEPILOGO", f"da_applicare={len(ok)}", f"superate={superate}", f"sospese_ancora_presenti={sospese}", f"malformate={malformate}", "-->")
sys.stderr.write(f"da_applicare={len(ok)} superate(citazione assente o ripetuta)={superate} sospese_con_citazione_ancora_presente={sospese} malformate={malformate}\n")

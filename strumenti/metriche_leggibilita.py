#!/usr/bin/env python3
# Metriche di leggibilita di un capitolo: parole, frasi, media, % frasi oltre 35 parole, frasi oltre 50, Gulpease.
# Uso: python3 strumenti/metriche_leggibilita.py capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md
# Esclude titoli (#), formula ($$) e separatori (---). E una stima, serve solo come controllo.
import re,sys
t=open(sys.argv[1],encoding='utf-8').read()
righe=[r for r in t.split('\n') if r.strip() and not r.startswith('#') and not r.strip().startswith('$$') and r.strip()!='---']
testo=' '.join(righe)
testo=re.sub(r'[*`>]|^\s*[-\d]+[.)]\s+','',testo)
frasi=[f.strip() for f in re.split(r'(?<=[.!?…»])\s+(?=[«"A-ZÀ-Ý*_(\d])|(?<=[.!?])\s*[»]\s+',testo) if f.strip()]
par=re.findall(r"[\wÀ-ÿ'’]+",testo)
parole=[p for p in par if re.search(r'\w',p)]
lettere=sum(len(re.findall(r'[A-Za-zÀ-ÿ]',p)) for p in parole)
lens=[len(re.findall(r"[\wÀ-ÿ'’]+",f)) for f in frasi]
n=len(frasi);P=len(parole)
print(f"parole={P} frasi={n} media={P/n:.1f} oltre35={sum(l>35 for l in lens)/n*100:.1f}% ({sum(l>35 for l in lens)}) oltre50={sum(l>50 for l in lens)} gulpease={89+(300*n-10*lettere)/P:.1f}")

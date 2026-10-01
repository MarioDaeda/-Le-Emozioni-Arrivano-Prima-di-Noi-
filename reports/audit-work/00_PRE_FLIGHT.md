# 00 PRE-FLIGHT
Data: 2026-10-01 · Branch di lavoro: claude/busy-mccarthy-j9u2h1 (HEAD 971e0a0 = origin/main)
## Git iniziale
- `git status --short`: vuoto (working tree pulito). Nessuna modifica utente preesistente.
## Localizzazione file
- Nel branch di lavoro MANCANO: CONTEXT.md, docs/adr/0001..0003. Il LIBRO_COMPLETO locale è versione vecchia (3259 linee, blob 63cdbf6).
- Unica fonte completa: branch remoto `origin/revisioni-deep-pov` (c2915ae, 2026-09-30). Contiene tutti i file target e governance.
- Decisione: audit sui blob di `origin/revisioni-deep-pov`, estratti read-only in scratchpad (/tmp/...). Nessun checkout/merge. Numeri di riga ancorati al blob sotto.
## File target
| File | blob (origin/revisioni-deep-pov) | linee | parole |
|---|---|---:|---:|
| LIBRO_COMPLETO_LE_EMOZIONI_ARRIVANO_PRIMA_DI_NOI.md | 100c6bdf84a0366fafc91b2d3915c6b261f4698e | 3791 | 73611 (regex \w+) / 71357 (wc) |
| sha256 manoscritto | a7fc2dccadc7c99d0330ac15ba506bb32f36232bf6498dd195f8a5db90e5bbd3 | | |
| CONTEXT.md | d7f1de8 | 99 | |
| ADR 0001 | 5507b67 | 18 | |
| ADR 0002 | 0766e86 | 17 | |
| ADR 0003 | a0cdbf7 | 18 | |
| .agents/skills/editing-creativo/SKILL.md | bcce4eb | 174 | |
Prompt dichiarava ~73.611 parole / ~3.792 linee → coincide (3791 linee effettive).
## Mappa sezione-linea (macro)
| Sezione | Inizio | Fine | Note |
|---|---:|---:|---|
| Frontespizio + Indice | 1 | 53 | |
| Prefazione | 54 | 211 | |
| Cap.1 | 212 | 511 | titoli scena senza etichette Atto |
| Cap.2 | 512 | 839 | ATTO I-V espliciti + Note di lavorazione |
| Cap.3 | 840 | 1134 | idem |
| Cap.4 | 1135 | 1498 | idem |
| Header lavoro Cap.5 | 1499 | 1518 | "# 2026-09-30 — Capitolo 5 — Riscrittura..." |
| Cap.5 | 1519 | 1848 | |
| Cap.6 | 1849 | 2202 | struttura tipo Cap.1 |
| Header lavoro Cap.7 | 2203 | 2218 | |
| Cap.7 | 2219 | 2582 | |
| Header lavoro Cap.8 | 2583 | 2600 | |
| Cap.8 | 2601 | 2950 | |
| Header lavoro Cap.9 | 2951 | 2971 | |
| Cap.9 | 2972 | 3325 | |
| Epilogo+Toolkit | 3326 | 3791 | 9 schede 3402-3644; 10 frasi; tabella; manifesto |
(POV/personaggi/atti per capitolo: vedi 04_ARCHITETTURA_TOOLKIT.md)
## Vincoli governance (estratto)
- ADR0001: 5 entità. Omnia (Quinzano/ZAI VR, fond. Andrea+Luca); O.M.P. Precision (Quinzano d'Oglio/Verona, 120 dip., 44 macchine 5 assi Mori Seiki, Ti gr5, ergal 7075-T6, Ra 0.8, "tolleranze al centesimo di mm", clienti Kuka/Hydac); NexSys (S.Martino B.A./ZAI VR Sud, Marco Vantini, MES in Rust, burn rate, Mediocredito/FCG); LogiDistretto S.c.a.r.l. (Interporto Q.E., Claudio Marcolini, soste passive); Studio Colombo & Associati (Quinzano) "guidato da Elena".
- ADR0002: Modello B; coralità; primato somatico; Deep POV Grado 4 = eliminazione totale filter words e saggistica in scena; verità industriale (2 micron, ore mandrino, spread...); apparati teorici SOLO in Atti III e V, purezza Atti I, II, IV.
- ADR0003: Toolkit IO•ALTRI•ALTRO governa Protocollo 180 s + 9 Schede tarate sui 9 capitoli.
- CONTEXT: glossario; IO=4-7-8; DSO 115-120 gg; Tolleranza 2 micron (0,002 mm) su "medicali (Kuka)" e idraulici (Hydac); Avoid "tolleranza centesimale generica".
- SKILL: max 3 battute consecutive senza beat; filter words (sentì/provò/sapeva/si rese conto/realizzò/capì/notò/vide/udì/scorse); no thought-tags; Atti I-II vietati esiti YES; Cap2 blocco mandrino 19:42; tabella voci: Marta "Tecnica Senior", Fabio Dir. Commerciale, Enrico "Ingegnere Gestionale".
## Conflitti di governance candidati
- G1 ADR0001:12 "tolleranze al centesimo di millimetro" (=10 µm) vs CONTEXT:93-95 "2 micron (0,002 mm)" + Avoid "tolleranza centesimale" + ADR0002:14 "2 micron". Da verificare impatto nel testo.
- G2 CONTEXT:94 "componenti medicali (Kuka)": Kuka è robotica industriale; contraddice ADR0001 (Kuka committente meccatronico) e prompt ("boccole robot Kuka").
- G3 ADR0001:12 O.M.P. "Quinzano d'Oglio / Verona": Quinzano d'Oglio è comune in provincia di Brescia; Quinzano è quartiere di Verona. Ambiguità geografica (verificare uso nel testo).
- G4 ADR0001:15 Studio Colombo "guidato da Elena" vs nome Colombo (prompt: Elena consulente presso lo Studio). Verificare testo.
- G5 CONTEXT:18,34 attribuzione a Damasio di "carico allostatico" (concetto McEwen) e "Sopravvivenza nel ruolo"; verificare se replicato nel testo.
- G6 Prompt vs governance: prompt descrive Enrico "giovane controller", SKILL:107 "Ingegnere Gestionale"; prompt Marta "da capotecnica ad Accademia", SKILL:104 "Tecnica Senior". Verificare testo.

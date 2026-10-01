# 00 MAPPA FONTI CANONICHE (v2 — 2026-10-01, dopo istruzione utente)
Fonte dichiarata dall'utente: `capitoli/` su `origin/main` @ 1f51621 ("versioni definitive divise"); master unificato `LIBRO_COMPLETO…md` @ origin/main (b767fd1, blob 56315a7, sha256 16520c5a…, 3714 linee, 70.821 parole regex / 68.775 wc).
Copie read-only in scratchpad/main/. Working tree locale = vecchio main 971e0a0 (non aggiornato: merge/reset vietati dal mandato).
Verifica: capitoli/* == bozze_capitoli/* (main) byte per byte; corpo capitoli == sezioni LIBRO main (righe non vuote, esclusi separatori) per tutte le sezioni; Cap.8: unica differenza BOM U+FEFF a inizio file.
| Sezione | File canonico | File precedente | Motivo della precedenza | Stato |
|---|---|---|---|---|
| Frontespizio+Indice | LIBRO main L1-53 | — | nessun file in capitoli/ | NON REVISIONATA — fonte: manoscritto unificato |
| Prefazione | capitoli/PREFAZIONE_METODOLOGICA.md (154) | LIBRO L54-211 | dichiarazione utente; identico | REVISIONE CANONICA |
| Cap.1 | capitoli/CAPITOLO_01_…md (296) | LIBRO L212-511; revisioni/2026-09-28_CAP01 | idem; rev sim 0,97 | REVISIONE CANONICA |
| Cap.2 | capitoli/CAPITOLO_02_…md (320) | LIBRO L512-835; revisioni/2026-09-28_CAP02 (testo diverso, sim 0,0) | dichiarazione utente + commit 1f51621 posteriore | REVISIONE CANONICA |
| Cap.3 | capitoli/CAPITOLO_03_…md (293) | LIBRO L836-1132; revisioni/…CAP03 (sim 0,06) | idem | REVISIONE CANONICA |
| Cap.4 | capitoli/CAPITOLO_04_…md (360) | LIBRO L1133-1496; revisioni/…CAP04 (sim 0,07) | idem | REVISIONE CANONICA |
| Cap.5 | capitoli/CAPITOLO_05_…md (326) | LIBRO L1497-1826 | idem | REVISIONE CANONICA |
| Cap.6 | capitoli/CAPITOLO_06_…md (350) | LIBRO L1827-2180 | idem | REVISIONE CANONICA |
| Cap.7 | capitoli/CAPITOLO_07_…md (360) | LIBRO L2181-2544 | idem | REVISIONE CANONICA |
| Cap.8 | capitoli/CAPITOLO_08_…md (346, BOM) | LIBRO L2545-2894 | idem | REVISIONE CANONICA |
| Cap.9 | capitoli/CAPITOLO_09_…md (350) | LIBRO L2895-3248 | idem | REVISIONE CANONICA |
| Epilogo | capitoli/EPILOGO_E_TOOLKIT_OPERATIVO.md §1 | LIBRO L3249+ | idem | REVISIONE CANONICA |
| Toolkit | capitoli/EPILOGO_E_TOOLKIT_OPERATIVO.md §2-6 | LIBRO | idem | REVISIONE CANONICA |
Note:
- `revisioni/` contiene ancora testi dichiarati "definitivi" per Cap.2/3/4 divergenti dal canone (Cap.2 rev: Davide impiegato HR). Non adottati; rischio di confusione d'archivio (nota metodologica, non anomalia del testo).
- Su origin/main esiste già `reports/2026-09-30_REFERTO_AUDIT_FINALE_OPERA_COMPLETA.md` (b767fd1, altro agente): stesso percorso dell'output richiesto. Il working tree locale non lo contiene → nessuna sovrascrittura locale; da segnalare all'utente.
- Righe del referto: file in capitoli/.

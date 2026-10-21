# Revisione del libro a basso consumo — indice per l'autore

> Questo file è per te. **Le sessioni non lo leggono:** leggono solo `prompt/revisione/risparmio/REGOLE.md` e il file del proprio lotto. Il metodo è quello provato su CAP03 e PREF: due fermate per l'autore, prima la struttura e poi le frasi, un ramo per file.

## Dove si risparmia

| Accorgimento | Che cosa evita |
|---|---|
| **File piccoli, uno per lotto.** `risparmio/REGOLE.md` è di circa 2 KB, `APPLICA.md` di circa 5 KB | Che ogni sessione legga e si porti dietro, a ogni turno, un prompt di 28 KB |
| **Prompt dei subagenti in file separati** (`risparmio/agenti/`). La sessione scrive una riga sola: "Esegui agenti/LENTE.md con SIGLA=…" | Che la sessione, e Sonnet in APPLICA, ricopi a ogni lancio istruzioni di 2–3 KB: i token in uscita sono quelli più cari |
| **I subagenti scrivono da soli i file di lavoro.** Se il sistema glielo impedisce, restituiscono il testo | Che report e schede di 5 KB passino dal contesto della sessione e vengano riscritti da lei |
| **`prepara_da_applicare.py`** costruisce l'elenco per l'esecutore Haiku | Che Sonnet ricopi 20–30 citazioni e proposte |
| **Script per tutti i controlli:** metriche, citazioni, fatti, glossario | Conteggi e controlli fatti da un modello, a pagamento e meno affidabili |
| **Haiku esegue, Sonnet giudica** | Sonnet usato per lavoro meccanico |
| **Niente rilettura del capitolo intero dopo le modifiche,** e il diff si legge in modalità `--word-diff`, più compatta | Il capitolo, circa 9 mila token, caricato due volte nel contesto |
| **Sessione 0 con Haiku, senza subagenti** | Un subagente in più solo per scrivere la sintesi della guida |

**Dove non si risparmia, per non perdere qualità:**
- il verificatore della struttura resta Sonnet;
- gli interventi di struttura e le fermate restano a Sonnet;
- le 3 lenti restano indipendenti.

**Dove la qualità può calare un po':**
- **frasi applicate da Haiku:** le rivede Sonnet sul diff, ma senza rileggere tutto il capitolo;
- **coordinamento di STRUTTURA:** lo fa Haiku. I suoi compiti sono meccanici, e le citazioni le controlla uno script.

## Le sessioni

Ogni riga è una **sessione nuova** nella cartella `Libro Emozioni`, **senza** "ultracode".

| # | Sessione | Modello della sessione | Subagenti |
|---|---|---|---|
| 0 | PREPARAZIONE | Haiku 5.5, medio | nessuno |
| 1 | APPLICA EPIL | Sonnet 5.5, medio | 3 Haiku |
| 2 | STRUTTURA CAP06 CAP07 CAP09 | Haiku 5.5, medio | 9 Haiku, 3 Sonnet, 3 Haiku |
| 3–5 | APPLICA CAP06, CAP07, CAP09 (una sessione ciascuno) | Sonnet 5.5, medio | 3 Haiku |
| 6 | STRUTTURA CAP05 CAP08 CAP04 | Haiku 5.5, medio | 9, 3, 3 |
| 7–9 | APPLICA CAP05, CAP08, CAP04 | Sonnet 5.5, medio | 3 Haiku |
| 10 | STRUTTURA CAP02 CAP01 | Haiku 5.5, medio | 6, 2, 2 |
| 11–12 | APPLICA CAP02, CAP01 | Sonnet 5.5, medio | 3 Haiku |
| 13 | FINALE | Sonnet 5.5, medio | 3 Haiku |

**Se la voce ti sembra appiattita dopo un APPLICA,** rifai solo il passo 3.5 (la revisione del diff) di quel file con Opus 5.5.

**Prova sulla sessione 1.** Confronta il consumo con quello di PREF e leggi il diff con attenzione. Se le frasi applicate da Haiku sono da rifare in buona parte, scrivi alla sessione: "salta 3.4, applica tu le frasi da `<SIGLA>_da_applicare.md`".

**Dopo ogni APPLICA:** scrivi "unisci" nella stessa sessione prima di aprire la successiva.

## Messaggi da incollare

**Sessione 0 — Haiku 5.5, medio.** Completa le decisioni sui fatti; le righe lasciate con "..." non vengono registrate.
```
Leggi prompt/revisione/risparmio/REGOLE.md e prompt/revisione/risparmio/PREPARAZIONE.md ed eseguilo. Autorizzo l'unione di revisione-pref in main.
Decisioni sui fatti:
- Settori di OMP: ...
- Tolleranze dei pezzi in titanio: 2 micron (D1 del glossario)
- Sara e Dario in PREF: ...
- Anni dei soci (25 o 20): ...
- Fondatori di Omnia: ...
```

**APPLICA — Sonnet 5.5, medio.** Cambia solo la sigla: EPIL, CAP06, CAP07, CAP09, CAP05, CAP08, CAP04, CAP02, CAP01.
```
Leggi prompt/revisione/risparmio/REGOLE.md e prompt/revisione/risparmio/APPLICA.md ed eseguilo con SIGLA=EPIL
```

**STRUTTURA — Haiku 5.5, medio.** Cambia solo le sigle: `CAP06 CAP07 CAP09`, poi `CAP05 CAP08 CAP04`, poi `CAP02 CAP01`.
```
Leggi prompt/revisione/risparmio/REGOLE.md e prompt/revisione/risparmio/STRUTTURA.md ed eseguilo con SIGLE=CAP06 CAP07 CAP09
```

**FINALE — Sonnet 5.5, medio.**
```
Leggi prompt/revisione/risparmio/REGOLE.md e prompt/revisione/risparmio/FINALE.md ed eseguilo.
```

## File

- `risparmio/REGOLE.md`: regole comuni e tabella dei file.
- `risparmio/PREPARAZIONE.md`, `STRUTTURA.md`, `APPLICA.md`, `FINALE.md`: un file per lotto.
- `risparmio/agenti/`: i prompt dei subagenti. `LENTE` e `REPORT` per la struttura; `VERIFICA` con Sonnet; `SCHEDA`, `ESECUTORE` e `LETTORE` per l'applicazione.
- `strumenti/`: `metriche_leggibilita.py`, `verifica_citazioni.py`, `controllo_fatti.py`, `scheda_glossario.py`, `residui_glossario.py`, `prepara_da_applicare.py`.

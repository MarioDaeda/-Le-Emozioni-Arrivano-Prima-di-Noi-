# Lotto STRUTTURA (sessione Haiku 5.5: coordini e basta)

Input: le sigle del messaggio, al massimo 3. Output: `reports/struttura/<SIGLA>_struttura.md` per ogni file.
Il capitolo non lo leggi tu: lo leggono i subagenti.

1. **Controlli.** Fermati e dimmelo se uno fallisce:
   - sei su `main` (altrimenti `git switch main`);
   - `grep -c APPROVATO reports/struttura/GLOSSARIO_LIBRO.md` è maggiore di 0;
   - `git status --short capitoli/` è vuoto, ignorando i file `._`.
2. **Script.** `mkdir -p reports/struttura/lavoro`. Poi, per ogni sigla:
   `python3 strumenti/scheda_glossario.py <SIGLA> > reports/struttura/lavoro/<SIGLA>_glossario.md`
3. **Lenti.** In un solo messaggio lancia 3 subagenti per file, `model: "haiku"`. Ognuno ha il prompt di una riga `Esegui prompt/revisione/risparmio/agenti/LENTE.md con SIGLA=..., FILE=..., LENTE=...`, con LENTE uguale a `curiosita`, `ponte` o `architettura`. Se un subagente restituisce il JSON invece di scriverlo, salvalo tu in `reports/struttura/lavoro/<SIGLA>_<LENTE>.json`.
4. **Verifica.** In un solo messaggio lancia un subagente per file, `model: "sonnet"`, con il prompt `Esegui prompt/revisione/risparmio/agenti/VERIFICA.md con SIGLA=..., FILE=...`.
5. **Report.** In un solo messaggio lancia un subagente per file, `model: "haiku"`, con il prompt `Esegui prompt/revisione/risparmio/agenti/REPORT.md con SIGLA=..., FILE=...`. Se uno restituisce il testo invece di scriverlo, salvalo tu nel percorso del report.
6. **Citazioni.** Per ogni file esegui `python3 strumenti/verifica_citazioni.py reports/struttura/<SIGLA>_struttura.md capitoli/<FILE>`. Se ci sono citazioni non trovate:
   - cerca con grep la frase giusta nel capitolo e correggi la citazione con Edit;
   - se non la trovi, aggiungi "(citazione da verificare)" all'intervento.
7. **Commit** con i soli report: `docs(struttura): report di struttura <SIGLE>`.
8. Rispondi con al massimo 6 righe:
   - per file: confermate ALTA, MEDIA e BASSA, e scartate;
   - per file: la riga `CONTEGGI:` del report;
   - il messaggio della prossima sessione, preso da `prompt/revisione/PROMPT_REVISIONE_LIBRO_RISPARMIO.md`.

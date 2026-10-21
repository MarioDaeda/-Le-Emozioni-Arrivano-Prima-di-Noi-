# Sessione PREPARAZIONE (Haiku 5.5, una volta sola)

Niente subagenti: fai tutto tu.

1. **Unione di PREF**, autorizzata dall'autore nel messaggio:
   - `git switch main`;
   - `git merge --no-ff revisione-pref -m "revisione(pref): unisci la revisione della prefazione"`. L'unione porta in `main` anche il glossario approvato e i report PREF ed EPIL, che stavano su `riordino-cartella`;
   - con `git branch --no-merged main` controlla che restino non uniti solo rami vecchi, non `riordino-cartella` né `revisione-pref`.
2. **Strumenti e prompt.** Aggiungi `reports/struttura/lavoro/` in fondo a `.gitignore`. Poi fai un commit, messaggio `chore(strumenti): script di controllo e prompt a basso consumo`, con soltanto:
   - `.gitignore`;
   - `strumenti/verifica_citazioni.py`, `strumenti/controllo_fatti.py`, `strumenti/scheda_glossario.py`, `strumenti/residui_glossario.py`, `strumenti/prepara_da_applicare.py`;
   - `prompt/revisione/PROMPT_REVISIONE_LIBRO_RISPARMIO.md`, `prompt/revisione/PROMPT_REVISIONE_LIBRO_COMPLETO.md`;
   - tutta la cartella `prompt/revisione/risparmio/`.
3. **Sintesi della guida stilistica.** Leggi `progetto/03_GUIDA_STILISTICA.md` e scrivi `progetto/03_GUIDA_STILISTICA_SINTESI.md`: al massimo 900 parole, in italiano semplice, per un editor che riscrive frasi mantenendo la voce del libro. Contenuto:
   1. la voce in 5 righe: persona, tono, registro, rapporto con il lettore;
   2. le regole di scrittura, una per riga, con un esempio breve copiato dalla guida quando c'è;
   3. che cosa è vietato;
   4. come si scrivono le scene e le spiegazioni, e come si passa dalle une alle altre;
   5. convenzioni: dialoghi, numeri, sigle, corsivi, grassetti, titoli.

   Usa le parole della guida, senza aggiungere regole tue. Segnala in fondo le contraddizioni della guida, se ce ne sono. Fai un commit con il solo file.
4. **Fatti decisi dall'autore**, se il messaggio ne contiene. Aggiungili in fondo a `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md`, il file già tracciato da git, in una sezione `## Decisioni dell'autore durante la revisione (<data>)`, una riga per fatto. Fai un commit con il solo file. Le righe lasciate con "..." non vanno registrate.
5. Rispondi con 4 righe: commit fatti, rami non uniti, sintesi scritta (numero di parole), messaggio per la sessione 1 preso da `prompt/revisione/PROMPT_REVISIONE_LIBRO_RISPARMIO.md`.

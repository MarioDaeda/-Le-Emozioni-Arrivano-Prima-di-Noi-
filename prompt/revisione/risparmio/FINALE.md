# Lotto FINALE (sessione Sonnet 5.5, medio)

1. **Stato.**
   - `git switch main`.
   - `git branch --no-merged main` non deve mostrare rami `revisione-*`.
   - Devono esserci 11 file `reports/struttura/*_REGISTRO_MODIFICHE.md`.

   Se manca qualcosa, elencalo e chiedimi se proseguire.
2. **Metriche (script).** Per ogni file di `capitoli/`:
   - misura la versione di oggi con `metriche_leggibilita.py`;
   - misura la versione di partenza: `git show 8816686:capitoli/<FILE>`, in un file temporaneo.

   Prepara una tabella prima/dopo.
3. **Residui (script).** `python3 strumenti/residui_glossario.py > reports/struttura/lavoro/residui.txt`.
4. **Tre subagenti `model: "haiku"`** nello stesso messaggio, ognuno con un prompt di 3–4 righe:
   - **RESIDUI.** Legge `reports/struttura/lavoro/residui.txt` e la sezione "Eccezioni ammesse" di `reports/struttura/GLOSSARIO_LIBRO.md`. Restituisce solo i residui veri, per file e riga, escludendo citazioni, mail, battute e titoli. Comprende CAP03: domanda cardine, Mappa Minima, fido.
   - **PROMESSE.** Legge, trovandole con grep, solo le sezioni "Registro delle promesse" degli 11 report `reports/struttura/*_struttura.md`. Per ogni promessa verso un altro capitolo, o segnata MAI, controlla con grep se il capitolo di arrivo la mantiene. Restituisce quelle aperte.
   - **DECISIONI.** Legge solo le sezioni "Non toccato, da decidere" degli 11 registri. Restituisce un elenco unico, senza doppioni.
5. **Fermata.** Mostrami metriche, residui veri, promesse aperte e decisioni aperte. Poi **aspetta**.
6. **Correzioni.** Sul ramo `revisione-finale`, partito da `main`, applica solo ciò che approvo: un commit per file, rileggendo solo i paragrafi toccati. Unisci a `main` solo se scrivo "unisci".
7. **Libro assemblato.** Con uno script Python unisci i file di `capitoli/` nell'ordine PREF, CAP01…CAP09, EPIL, separati da `---`, in `reports/finale/LIBRO_REVISIONATO_<data>.md`. Non toccare `archivio/` né `assemble_book.ps1`.
8. **Rapporto.** Scrivi `reports/finale/RAPPORTO_FINALE.md` con i risultati dei punti 2–4 e le prossime azioni. Tra queste c'è la prova con 3–5 lettori reali.
9. Fai un commit con i soli file di `reports/finale/`. Rispondi con al massimo 8 righe.

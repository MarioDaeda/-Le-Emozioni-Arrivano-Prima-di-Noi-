# Regole comuni (leggere in ogni sessione)

1. Non inventare: nessun fatto, cifra, nome, battuta, scena o riferimento scientifico nuovo. Si sposta, taglia, unisce, divide, riformula.
2. Le decisioni sono dell'autore: domande e casi che richiedono materiale nuovo si chiedono, e si aspetta.
3. Prima la struttura, poi le frasi. Gli interventi "da sospendere" non si applicano.
4. La voce resta quella del libro.
5. Git:
   - si parte da `main`;
   - si aggiungono i file per nome, mai `git add .` o `-A`;
   - non si aggiungono i file modificati solo per i fine riga (CRLF), né `.agents/`, né la copia di `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md` con l'accento scomposto;
   - prima di ogni commit si controlla con `git diff --cached --stat`;
   - mai push.
6. Risparmio di token:
   - leggi ogni file una volta sola;
   - dei file lunghi leggi solo le righe trovate con grep, oppure con offset e limit;
   - non rileggere il capitolo intero dopo averlo modificato: rileggi solo i tratti toccati;
   - non leggere `archivio/`, `capitoli_revisionati/`, `reports/struttura/primo_test/`, né i file di `reports/struttura/lavoro/` di altri capitoli.
7. Subagenti:
   - strumento Agent, `subagent_type: "general-purpose"`, con il `model` indicato;
   - il loro prompt è **una riga sola**, per esempio: `Esegui prompt/revisione/risparmio/agenti/LENTE.md con SIGLA=CAP06, FILE=CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md, LENTE=ponte`. Non copiare le istruzioni nel prompt: il subagente le legge dal file;
   - lancia nello stesso messaggio i subagenti indipendenti tra loro, e aspetta che finiscano tutti.
8. I subagenti non modificano `capitoli/`, salvo l'ESECUTORE.

| Sigla | File in `capitoli/` |
|---|---|
| PREF | `PREFAZIONE_METODOLOGICA.md` |
| CAP01 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` |
| CAP02 | `CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` |
| CAP03 | `CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` |
| CAP04 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` |
| CAP05 | `CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md` |
| CAP06 | `CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` |
| CAP07 | `CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md` |
| CAP08 | `CAPITOLO_08_IL_GELO_TRA_PARI.md` |
| CAP09 | `CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` |
| EPIL | `EPILOGO_E_TOOLKIT_OPERATIVO.md` |

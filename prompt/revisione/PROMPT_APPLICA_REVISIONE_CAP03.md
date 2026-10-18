# PROMPT — Applicare la revisione a CAP03 (Sonnet 5.5, effort alto, senza ultracode)

> **Come lanciarlo.** Apri una sessione **nuova** di Claude Code nella cartella `Libro Emozioni`, con modello **Sonnet 5.5** ed effort **alto**. **Non** scrivere "ultracode": qui un solo agente modifica un solo file, e più agenti in parallelo sullo stesso file si sovrascriverebbero a vicenda. Incolla tutto ciò che sta sotto la linea.
>
> **Cosa fa.** Applica a `capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` prima gli interventi di struttura, poi quelli di frase. Lavora su un ramo git separato, con un commit per fase, così puoi vedere ogni modifica e annullarla. Si ferma due volte per chiederti di decidere.

---

## Ruolo

Sei l'editor del libro *Le Emozioni Arrivano Prima di Noi*: saggistica narrativa italiana sulle emozioni nel business, scritta per manager e imprenditori di PMI. Applichi a un solo capitolo una revisione già fatta e verificata. **Non** fai una nuova revisione: le decisioni su cosa cambiare sono già nei report. Tu le metti in pratica bene e rispetti la voce del libro.

## File

- **Da modificare:** `capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md`
- **Interventi di struttura:** `reports/struttura/CAP03_struttura.md`. Contiene gli interventi [S01]–[S07], la sezione "Interventi di frase di Haiku" divisa in "da tenere", "da sospendere" e "da correggere", e l'"Ordine di lavoro consigliato".
- **Interventi di frase:** `reports/leggibilita/CAP03_leggibilita.md`, interventi [01]–[24].
- **Glossario:** `reports/struttura/GLOSSARIO_PROPOSTO_CAP01-03.md`. È una bozza.
- **Voce e coerenza, solo da leggere:**
  - `progetto/03_GUIDA_STILISTICA.md`
  - `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md` (nomi, cifre, date, fatti dei personaggi)

## Regole assolute

1. **Non inventare.** Nessun fatto, nessuna cifra, nessun nome, nessuna battuta, nessuna scena e nessun riferimento scientifico nuovi. Puoi spostare, tagliare, unire, dividere e riformulare quello che c'è.
2. **Non toccare altri file del libro.** Modifichi solo il capitolo 3. Ai report e al registro accedi solo in lettura. L'unico file nuovo è il registro delle modifiche (passo 6).
3. **Nessuna decisione al posto dell'autore.** Quando un intervento è una domanda per l'autore, oppure richiede materiale nuovo, chiedi e aspetta.
4. **La voce resta quella del libro.** Una frase più semplice deve sembrare scritta dallo stesso autore. Le scene restano scene e non diventano spiegazioni.
5. **Ordine fisso:** prima la struttura, poi le frasi. Gli interventi di frase "da sospendere" non si applicano.

## Procedura

### Passo 0 — Preparazione
1. Controlla che `git status --short capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` non mostri modifiche. Se il file è già modificato, fermati e chiedimi cosa fare. I file `._` sono metadati di macOS e vanno ignorati.
2. Crea e attiva il ramo `revisione-cap03` con `git switch -c revisione-cap03`. Le altre modifiche già presenti nella cartella restano dove sono. **Non** aggiungerle mai ai commit.
3. Leggi per intero: il capitolo, i due report, il glossario, la guida stilistica. Nel registro della continuità leggi le voci dei personaggi e delle cifre che compaiono nel capitolo 3.
4. Calcola e annota le metriche di partenza del capitolo con un piccolo script Python nella tua cartella temporanea, senza installare nulla:
   - parole e frasi;
   - lunghezza media delle frasi;
   - percentuale di frasi oltre 35 parole;
   - numero di frasi oltre 50 parole;
   - indice Gulpease = 89 + (300 × frasi − 10 × lettere) / parole.

### Passo 1 — Prima fermata: decisioni dell'autore
Prima di modificare qualsiasi cosa, mostrami **in una volta sola**:
- **a. Glossario.** Solo i termini tecnici che compaiono nel capitolo 3. Per ognuno: il termine proposto e le varianti che verrebbero sostituite. Chiedimi di confermare o di cambiare.
- **b. Domande per l'autore.** Gli interventi di struttura e le voci dell'"Ordine di lavoro" che sono domande o richiedono materiale nuovo, per esempio [S07]. Per ognuno: che cosa chiede e le opzioni possibili.
- **c. Eventuali conflitti.** Interventi di struttura e di frase che toccano lo stesso paragrafo in modi incompatibili.

Poi **aspetta la mia risposta**. Le voci a cui non rispondo restano come sono nel testo.

### Passo 2 — Struttura
1. Applica gli interventi [S01]–[S07] confermati, nell'ordine dell'"Ordine di lavoro consigliato". Per ognuno:
   - cerca la citazione con grep -F;
   - modifica solo ciò che l'intervento richiede;
   - rileggi il paragrafo prima e quello dopo, per controllare che i passaggi reggano.
2. Se un intervento non si può applicare senza inventare, saltalo e annotalo.
3. Rileggi il capitolo intero una volta, dall'inizio alla fine, per controllare il filo: domande aperte e chiuse, ritorni alla scena.
4. Fai un commit con il solo capitolo: `git add capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` e poi `git commit -m "revisione(cap-03): interventi di struttura"`.

### Passo 3 — Frasi
1. Applica gli interventi [01]–[24] di `CAP03_leggibilita.md`:
   - **"da tenere":** usa la proposta di Haiku come base. Puoi migliorarla se suona meno naturale dell'originale, ma senza cambiare il significato.
   - **"da correggere":** usa la proposta corretta scritta in `CAP03_struttura.md`.
   - **"da sospendere":** non applicarli. Se però il paragrafo è rimasto uguale dopo il passo 2, ricontrollali uno per uno: applicali solo se la citazione esiste ancora identica e la proposta ha ancora senso.
2. Applica il glossario confermato al passo 1: un solo termine per ogni concetto tecnico in tutto il capitolo.
3. Se una citazione non esiste più perché il passo 2 ha cambiato il paragrafo, non forzarla. Annotala come "superata dalla struttura".
4. Fai un commit con il solo capitolo: `git commit -m "revisione(cap-03): interventi di frase e glossario"`.

### Passo 4 — Verifica (senza modificare)
1. **Fatti invariati.** Confronta con `git diff main -- capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` ed elenca ogni cifra, data, nome proprio e riferimento scientifico che compare in una riga tolta o aggiunta. Tutti devono esistere ancora nel capitolo, identici. Se qualcosa è sparito o cambiato, correggilo e fai un commit di correzione.
2. **Metriche.** Ricalcola le metriche del passo 0 e mettile a confronto. Le metriche servono solo come controllo. **Non** spezzare frasi solo per far salire il Gulpease.
3. **Rilettura da lettore.** Leggi il capitolo come lo leggerebbe un imprenditore stanco la sera. Segnala, senza correggere, i 3 punti in cui potrebbe ancora fermarsi.

### Passo 5 — Seconda fermata: revisione dell'autore
Mostrami:
- le metriche prima e dopo;
- l'elenco di ciò che è stato applicato, saltato o superato;
- i 3 punti a rischio del passo 4.3;
- il comando per vedere tutte le modifiche: `git diff main -- capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md`.

Poi **aspetta**. Non unire il ramo a `main` e non fare push. Lo decido io.

### Passo 6 — Registro delle modifiche (dopo la mia risposta al passo 5)
Se ti chiedo altre correzioni, applicale prima, con un commit. Poi scrivi `reports/struttura/CAP03_REGISTRO_MODIFICHE.md`:
- **intestazione:** data, ramo, i due commit;
- **una tabella** con: intervento | stato (applicato / saltato / superato / sospeso / domanda per l'autore) | nota di una riga;
- **le metriche** prima e dopo;
- **le decisioni del glossario** confermate.

Fai un commit che contenga solo questo file.

# Passaggio di consegne: revisione del libro

Aggiornato al 18 ottobre 2026. Questo file serve a un altro modello (o a una persona) per riprendere la revisione senza rifare il lavoro già fatto. Leggi prima questo file, poi `README.md` per la mappa delle cartelle.

## Il libro in breve

*Le Emozioni Arrivano Prima di Noi*: saggistica narrativa italiana sulle emozioni nel business, per manager e imprenditori di PMI. Il lettore è colto, non specialista, legge la sera ed è stanco. Il testo definitivo è in `capitoli/`: prefazione, capitoli 1-9, epilogo e toolkit. Ogni capitolo alterna scena e spiegazione scientifica.

Voce, stile e fatti dei personaggi stanno in `progetto/`:
- `03_GUIDA_STILISTICA.md`: voce del libro e regole di scrittura
- `08_REGISTRO_DELLA_CONTINUITÀ.md`: personaggi, cifre, date
- `riferimenti/CONTEXT.md`: glossario canonico di filiera e metodo

## Regole che valgono sempre

1. **Non inventare.** Nessun fatto, cifra, nome, battuta, scena o riferimento scientifico nuovi. Si può spostare, tagliare, unire, dividere, riformulare.
2. **Le decisioni sono dell'autore.** Se un intervento richiede materiale nuovo o è una domanda per l'autore, si chiede e si aspetta.
3. **Prima la struttura, poi le frasi.** Gli interventi di frase che toccano un paragrafo riscritto dalla struttura non si applicano ("da sospendere").
4. **La voce resta quella del libro.** Una frase più semplice deve sembrare scritta dallo stesso autore.
5. **Un ramo per capitolo** (`revisione-capNN`), commit solo del capitolo: uno per la struttura, uno per frasi e glossario. Nessun merge su `main` senza il via dell'autore.
6. **Gli agenti non scrivono file.** Restituiscono il testo e lo salva la sessione principale. Il modello Haiku si è rifiutato più volte di creare file `.md`.
7. **Mai rigenerare un singolo report con `resumeFromRunId`**: la ripresa rifà tutte le fasi e cambia i numeri.

## Stato per capitolo

| File | Leggibilità (frasi) | Struttura | Interventi applicati al testo |
|---|---|---|---|
| Prefazione | report fatto | no | no |
| Cap. 1 | report fatto | report fatto, **da rigenerare** (versione vecchia del prompt) | no |
| Cap. 2 | report fatto | report fatto, **da rigenerare** (versione vecchia del prompt) | no |
| **Cap. 3** | report fatto | report fatto (versione definitiva) | **sì, completo** |
| Cap. 4-9 | report fatto | no | no |
| Epilogo | report fatto | no | no |

- Report di leggibilità: `reports/leggibilita/` (indice e classifica di priorità in `00_INDICE_LEGGIBILITA.md`).
- Report di struttura: `reports/struttura/`. In `primo_test/` ci sono le versioni precedenti dei report, tenute solo per confronto.
- Capitolo 4: ha anche una correzione precedente del calcolo Hydac (`441613c`), fuori da questa pipeline.
- I capitoli 2, 5, 7, 8, 9 hanno già avuto tolta la sezione "Note di lavorazione" (`a69b8ef`).

## Come è stato revisionato il capitolo 3 (modello da ripetere)

Il registro completo è in `reports/struttura/CAP03_REGISTRO_MODIFICHE.md`. I passaggi:

1. **Report di leggibilità** (Haiku): 24 interventi di frase, numerati [01]-[24].
2. **Report di struttura** (Sonnet, tre lenti, verificatori scettici, Haiku per i passaggi meccanici): interventi [S01]-[S07], con domande per l'autore.
3. **Applicazione**: il prompt `prompt/revisione/PROMPT_APPLICA_REVISIONE_CAP03.md` è il modello. Procedura: ramo, metriche di partenza, **prima fermata** (glossario, domande per l'autore, conflitti), struttura, commit, frasi e glossario, commit, verifica dei fatti, **seconda fermata**, registro delle modifiche.
4. **Verifica dei fatti**: confronto con `main`; ogni cifra, data, nome e riferimento tolto deve esistere ancora, a meno che sia stato tolto di proposito.
5. **Metriche**: `strumenti/metriche_leggibilita.py`. Capitolo 3, prima e dopo: Gulpease 50,8 → 53,3, frasi oltre 35 parole 12,4% → 8,0%. Le metriche sono solo un controllo: non si spezzano frasi per far salire il Gulpease.

## Prompt disponibili (`prompt/revisione/`)

- `PROMPT_REVISIONE_LEGGIBILITA_HAIKU.md`: report di leggibilità, un subagente per file.
- `PROMPT_REVISIONE_STRUTTURA_SONNET_ULTRACODE.md`: revisione di struttura completa (circa 110 agenti).
- `PROMPT_STRUTTURA_TEST_RISPARMIO_CAP01-03.md`: versione a basso consumo (circa 25 agenti), con le correzioni dopo il primo test. **È quella da usare per rigenerare CAP01 e CAP02** e per i capitoli successivi. Va lanciata un capitolo alla volta (basta lasciare una sola riga nell'array `FILES`) e i report si salvano dalla sessione principale.
- `PROMPT_APPLICA_REVISIONE_CAP03.md`: applicazione al testo. Per un altro capitolo basta cambiare nome del file e dei report.
- `PROMPT_REVISIONE_FINALE_CAPITOLI_1_2_3_SONNET.md`: revisione finale precedente, per consultazione.

Altre cartelle di prompt (`audit/`, `riscrittura/`, `stesura/`) sono lavori già eseguiti.

## Cosa lasciare all'autore (capitolo 3)

Nel capitolo 3 non sono stati toccati, perché sono fatti e non frasi:
- la perizia è "del software" nella mail e nelle battute della banca, ma "dei brevetti" nella scena di Giulia, nel resoconto della mail e nel protocollo;
- l'erogazione è fissata a "venerdì 28", mentre l'accredito arriva giovedì 27 alle 16:30; il saldo degli stipendi "il lunedì successivo" non viene mai mostrato;
- la formula in LaTeX della mappa minima può comparire come codice grezzo in impaginazione;
- "fuori sacco" nella battuta di Marangoni non è stato verificato;
- il titolo del capitolo ("panico da anticipazione") è citato anche negli altri capitoli.

## Glossario: decisioni già prese e limiti

Per il solo capitolo 3 l'autore ha confermato 14 scelte (G1-G14), elencate nel registro delle modifiche. Per esempio: "circuito difensivo di sopravvivenza", "cervello predittivo", "panico da anticipazione", "fidi", "Comitato Rischi" unico, "contratto di rete".

Il file `reports/struttura/GLOSSARIO_PROPOSTO_CAP01-03.md` è **una bozza parziale** (solo capitoli 1-3, generata da un agente Haiku): va rifatta sul libro intero e approvata dall'autore prima di applicarla agli altri capitoli. Le scelte del capitolo 3 vanno controllate per coerenza con i capitoli 1 e 2.

## Cose da sapere per non sbagliare

- **Il libro assemblato è vecchio.** `archivio/LIBRO_COMPLETO_…md` e `strumenti/assemble_book.ps1` partono da `archivio/bozze_capitoli/`, che contiene ancora le note di lavorazione e non ha le correzioni dei capitoli 3 e 4. Per riassemblare, lo script va puntato su `capitoli/`. Ha anche un percorso base di Windows.
- **I numeri dei report variano.** Gli interventi di Haiku e il numero di segnalazioni confermate cambiano da una esecuzione all'altra: sono indicativi, non misure.
- **Le citazioni vanno verificate.** Ogni citazione di un report va cercata nel capitolo con `grep -F` prima di applicare l'intervento. Dopo la revisione di struttura alcune citazioni non esistono più ("superata dalla struttura").
- **Sul disco** i file hanno spesso i fine riga CRLF mentre il repository ha LF: `git status` mostra decine di file "modificati" che non hanno modifiche di contenuto. Non committarli. Il file `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md` ha anche una versione con l'accento scomposto, che git vede come file nuovo: non aggiungerla.
- **I report storici** in `reports/` e le note in `.agents/` citano ancora i vecchi percorsi (per esempio `bozze_capitoli/`): sono registri di lavori già fatti.
- **Il push su GitHub** richiede un Personal Access Token (permesso `repo`).

## Prossimi passi consigliati

1. Rigenerare i report di struttura di CAP01 e CAP02 con `PROMPT_STRUTTURA_TEST_RISPARMIO_CAP01-03.md` (un capitolo alla volta).
2. Applicare la revisione a CAP01 e CAP02 con la procedura del capitolo 3, con le due fermate per l'autore.
3. Fare il report di struttura dei capitoli 4-9, prefazione ed epilogo, e applicarlo seguendo la classifica di priorità di `reports/leggibilita/00_INDICE_LEGGIBILITA.md` (in cima CAP02 e CAP05, con 14 ALTA ciascuno).
4. Rifare il glossario sul libro intero e farlo approvare dall'autore.
5. Riassemblare il libro da `capitoli/`, a fine revisione.

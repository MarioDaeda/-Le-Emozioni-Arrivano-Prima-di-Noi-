# PROMPT — Revisione completa del libro, a basso consumo di token

> Questo file contiene **quattro lotti**. Ogni lotto si esegue in una sessione nuova di Claude Code, aperta nella cartella `Libro Emozioni`. In ogni sessione incolli solo il **messaggio breve** del lotto, indicato nella tabella qui sotto. È la sessione a leggere questo file. Il metodo è quello già provato sul capitolo 3: `reports/struttura/CAP03_REGISTRO_MODIFICHE.md` e `PASSAGGIO_DI_CONSEGNE.md`.

## Piano delle sessioni

| # | Lotto | Modello ed effort | Ultracode | Agenti circa |
|---|---|---|---|---|
| 1 | GLOSSARIO (libro intero) e approvazione | Sonnet 5.5, medio | sì | 12 |
| 2 | STRUTTURA `PREF EPIL` | Sonnet 5.5, medio | sì | 16 |
| 3 | APPLICA `PREF`, poi una sessione per `EPIL` | Sonnet 5.5, **alto** | **no** | 1 |
| 4 | STRUTTURA `CAP06 CAP07 CAP09` | Sonnet 5.5, medio | sì | 24 |
| 5 | APPLICA, una sessione per file: `CAP06`, `CAP07`, `CAP09` | Sonnet 5.5, alto | no | 1 |
| 6 | STRUTTURA `CAP05 CAP08 CAP04` | Sonnet 5.5, medio | sì | 24 |
| 7 | APPLICA, una sessione per file: `CAP05`, `CAP08`, `CAP04` | Sonnet 5.5, alto | no | 1 |
| 8 | STRUTTURA `CAP02 CAP01` | Sonnet 5.5, medio | sì | 16 |
| 9 | APPLICA, una sessione per file: `CAP02`, `CAP01` | Sonnet 5.5, alto | no | 1 |
| 10 | FINALE (coerenza e libro assemblato) | Sonnet 5.5, medio | no | 1 |

**Perché questo ordine.** Si parte dai file più difficili secondo le metriche reali, non secondo le etichette di Haiku. Prefazione ed Epilogo hanno Gulpease 43–44; CAP06, CAP07 e CAP09 50–51; CAP05, CAP08 e CAP04 52–53; CAP02 55; CAP01 63. Il capitolo 3 è già fatto. Ogni lotto STRUTTURA è seguito subito dai lotti APPLICA degli stessi file, così ogni report si usa quando è appena stato scritto.

**Perché questi modelli.**
- **STRUTTURA:** gli agenti leggono e giudicano. Sonnet con effort medio basta, perché i verificatori fanno da filtro.
- **APPLICA:** un solo agente riscrive il testo nella tua voce. È il compito più delicato, e con un agente solo l'effort alto costa poco. Niente ultracode: più agenti sullo stesso file si sovrascriverebbero.
- **Se dopo APPLICA senti la voce appiattita:** rifai solo quel file con Opus 5.5.

**Costo stimato (non misurato).** Per ogni file, STRUTTURA costa circa 250–300 mila token degli agenti: il test su 3 capitoli ne ha usati circa 790 mila. GLOSSARIO costa circa 300 mila. APPLICA dipende da quanto dura il dialogo con te. Se una sessione rischia di superare il tuo limite delle 5 ore, lancia STRUTTURA un file alla volta: la riga `file` accetta qualsiasi elenco di sigle.

### Messaggi brevi da incollare

Lotto GLOSSARIO:
```
ultracode
Leggi prompt/revisione/PROMPT_REVISIONE_LIBRO_COMPLETO.md ed esegui la sezione "LOTTO GLOSSARIO".
```

Lotto STRUTTURA (cambia le sigle):
```
ultracode
Leggi prompt/revisione/PROMPT_REVISIONE_LIBRO_COMPLETO.md ed esegui la sezione "LOTTO STRUTTURA" con file: PREF EPIL
```

Lotto APPLICA (un file per sessione, senza ultracode):
```
Leggi prompt/revisione/PROMPT_REVISIONE_LIBRO_COMPLETO.md ed esegui la sezione "LOTTO APPLICA" con file: PREF
```

Lotto FINALE (senza ultracode):
```
Leggi prompt/revisione/PROMPT_REVISIONE_LIBRO_COMPLETO.md ed esegui la sezione "LOTTO FINALE".
```

---

## Regole comuni a tutti i lotti

1. **Non inventare.** Nessun fatto, cifra, nome, battuta, scena o riferimento scientifico nuovo. Si può spostare, tagliare, unire, dividere, riformulare.
2. **Le decisioni sono dell'autore.** Se un intervento richiede materiale nuovo, o è una domanda per l'autore, chiedi e aspetta.
3. **Prima la struttura, poi le frasi.** Gli interventi di frase "da sospendere" non si applicano.
4. **La voce resta quella del libro.** Una frase più semplice deve sembrare scritta dallo stesso autore.
5. **Gli agenti dei workflow non scrivono file.** Restituiscono il testo, e lo salva la sessione principale con Write. L'utente chiede espressamente questi file.
6. **Mai `resumeFromRunId` per rigenerare un singolo report.** La ripresa si usa solo se il workflow si interrompe prima di finire. Se manca un report, scrivilo dai dati di `journal.jsonl`, senza lanciare altri agenti.
7. **Git.** Fai commit solo dei file del lotto. Sul disco molti file risultano "modificati" solo per i fine riga (CRLF): non aggiungerli mai. Non aggiungere neppure la seconda copia di `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md` con l'accento scomposto. Mai push.
8. **Risparmio di token.** Leggi ogni file una volta sola. Dei file lunghi di riferimento leggi solo le parti che servono, cercandole con grep: registro della continuità, CONTEXT.md, registri delle modifiche. Non leggere `archivio/`, `capitoli_revisionati/` o `reports/struttura/primo_test/`.

**Tabella dei file** (sigla → file in `capitoli/` → tipo):

| Sigla | File | Tipo |
|---|---|---|
| PREF | `PREFAZIONE_METODOLOGICA.md` | prefazione |
| CAP01 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` | narrativo |
| CAP02 | `CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` | narrativo |
| CAP03 | `CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` | narrativo (già revisionato) |
| CAP04 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` | narrativo |
| CAP05 | `CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md` | narrativo |
| CAP06 | `CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` | narrativo |
| CAP07 | `CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md` | narrativo |
| CAP08 | `CAPITOLO_08_IL_GELO_TRA_PARI.md` | narrativo |
| CAP09 | `CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` | narrativo |
| EPIL | `EPILOGO_E_TOOLKIT_OPERATIVO.md` | epilogo e toolkit |

---

## LOTTO GLOSSARIO

**Obiettivo:** un solo glossario approvato per tutto il libro. Va in `reports/struttura/GLOSSARIO_LIBRO.md`, e tutti i lotti successivi lo usano.

1. Esegui con lo strumento **Workflow** lo script "Script GLOSSARIO" qui sotto, così com'è, con `args` = `{"data": "<oggi AAAA-MM-GG>"}`.
2. Salva `glossario_md` del risultato in `reports/struttura/GLOSSARIO_LIBRO.md` con Write.
3. **Fermata per l'autore.** Mostrami in chat, in una volta sola:
   - le decisioni elencate nella sezione "Decisioni per l'autore" del glossario, numerate D1, D2 e così via, ognuna con le opzioni possibili;
   - i conflitti con le scelte G1–G14 già prese nel capitolo 3, se ci sono.

   Poi **aspetta la mia risposta**.
4. Applica le mie risposte al file. In cima scrivi `**APPROVATO dall'autore il <data>**` al posto della dicitura di bozza. Le decisioni a cui non ho risposto restano come "proposta" e vanno annotate in fondo al file.
5. Fai un commit con il solo `reports/struttura/GLOSSARIO_LIBRO.md`, messaggio `docs(glossario): glossario del libro approvato`.
6. Rispondi con al massimo 5 righe: termini confermati, decisioni ancora aperte, percorso del file.

### Script GLOSSARIO

```javascript
export const meta = {
  name: 'glossario-libro',
  description: 'Glossario unico del libro: estrazione dei termini per file con Haiku, fusione con Sonnet a partire dalle scelte gia approvate',
  phases: [
    { title: 'Estrazione', detail: 'un agente Haiku per file', model: 'haiku' },
    { title: 'Fusione', detail: 'un agente Sonnet' },
  ],
}

const FILES = [
  { sigla: 'PREF',  file: 'PREFAZIONE_METODOLOGICA.md' },
  { sigla: 'CAP01', file: 'CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md' },
  { sigla: 'CAP02', file: 'CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md' },
  { sigla: 'CAP03', file: 'CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md' },
  { sigla: 'CAP04', file: 'CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md' },
  { sigla: 'CAP05', file: 'CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md' },
  { sigla: 'CAP06', file: 'CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md' },
  { sigla: 'CAP07', file: 'CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md' },
  { sigla: 'CAP08', file: 'CAPITOLO_08_IL_GELO_TRA_PARI.md' },
  { sigla: 'CAP09', file: 'CAPITOLO_09_IL_CINISMO_DI_REPARTO.md' },
  { sigla: 'EPIL',  file: 'EPILOGO_E_TOOLKIT_OPERATIVO.md' },
]
const DATA = (args && args.data) ? args.data : 'data non indicata'

const TERMS_SCHEMA = {
  type: 'object',
  properties: {
    termini: { type: 'array', items: { type: 'object', properties: {
      concetto: { type: 'string' },
      forme_usate: { type: 'array', items: { type: 'string' } },
      occorrenze: { type: 'number' },
      prima_sezione: { type: 'string' },
      definito_alla_prima_comparsa: { type: 'boolean' },
      tipo: { type: 'string', enum: ['tecnico', 'vago'] },
    }, required: ['concetto', 'forme_usate', 'occorrenze', 'prima_sezione', 'definito_alla_prima_comparsa', 'tipo'] } },
  },
  required: ['termini'],
}
const MD_SCHEMA = { type: 'object', properties: { markdown: { type: 'string' } }, required: ['markdown'] }

phase('Estrazione')
const estrazioni = await parallel(FILES.map(f => () => agent(
  [
    'Leggi una sola volta, per intero, capitoli/' + f.file + '. Non leggere altri file e non scrivere file.',
    'Elenca i concetti tecnici (psicologia, neuroscienze, finanza, gestione d impresa, filiera) e le parole vaghe usate spesso (per esempio "sistemico", "relazionale").',
    'Per ogni concetto indica TUTTE le forme usate nel file per dirlo (sinonimi, varianti, sigle, termini inglesi), le occorrenze totali, la prima sezione in cui compare, se alla prima comparsa viene spiegato in modo concreto, e se è "tecnico" o "vago".',
    'Al massimo 40 concetti, i più frequenti o importanti.',
  ].join('\n\n'),
  { label: 'estrai:' + f.sigla, phase: 'Estrazione', model: 'haiku', effort: 'medium', schema: TERMS_SCHEMA }
).then(r => r ? { sigla: f.sigla, termini: r.termini } : null)))

const valide = estrazioni.filter(Boolean)
const mancanti = FILES.filter(f => !valide.find(v => v.sigla === f.sigla)).map(f => f.sigla)
if (mancanti.length) log('ATTENZIONE: estrazione mancante per ' + mancanti.join(', '))

phase('Fusione')
const fuso = await agent(
  [
    'Prepara il GLOSSARIO UNICO del libro "Le Emozioni Arrivano Prima di Noi" (saggistica narrativa per manager di PMI). NON scrivere file: restituisci il Markdown nel campo "markdown". Data: ' + DATA + '.',
    'Estrazioni dai file (sigla, concetti, forme usate):\n' + JSON.stringify(valide),
    'Leggi anche, cercandole con grep e senza leggere i file interi:',
    '- la sezione "## Glossario confermato" di reports/struttura/CAP03_REGISTRO_MODIFICHE.md (scelte G1-G14 già approvate dall autore: sono vincolanti);',
    '- le voci di riferimenti/CONTEXT.md (glossario canonico di filiera e metodo) che corrispondono ai concetti estratti.',
    'REGOLE: per ogni concetto TECNICO si sceglie una sola forma da usare in tutto il libro, senza alternare sinonimi. Le scelte G1-G14 e le definizioni di CONTEXT.md hanno la precedenza. Le parole VAGHE si riducono, con alternative concrete. Se due fonti sono in conflitto, non decidere: mettilo tra le decisioni per l autore.',
    'STRUTTURA:',
    '# Glossario del libro',
    'In cima, in grassetto: "BOZZA — da approvare dall autore". Poi la data.',
    '## Termini tecnici: tabella con forma scelta | forme da sostituire | definizione di una riga, concreta | dove va spiegato (sigla e sezione della prima comparsa nel libro, nell ordine PREF, CAP01...CAP09, EPIL) | fonte della scelta (G1-G14, CONTEXT.md, proposta) | file in cui compare.',
    '## Eccezioni ammesse: dove una forma diversa deve restare (citazioni testuali, nomi propri, testo di mail o documenti dentro la storia, titoli).',
    '## Parole vaghe: tabella con parola | occorrenze per file | alternative concrete.',
    '## Decisioni per l autore: elenco numerato D1, D2 e così via; per ognuna il problema in una riga e 2-3 opzioni.',
    'Al massimo 60 termini tecnici e 20 parole vaghe.',
  ].join('\n\n'),
  { label: 'fusione', phase: 'Fusione', schema: MD_SCHEMA }
)
return { glossario_md: fuso ? fuso.markdown : '', estrazioni_mancanti: mancanti }
```

---

## LOTTO STRUTTURA

**Obiettivo:** il report di struttura dei file indicati nel messaggio (`file: SIGLA SIGLA ...`). Va in `reports/struttura/SIGLA_struttura.md`. Se esiste già un report per quel file, viene sovrascritto: le versioni precedenti di CAP01 e CAP02 sono già salvate in `primo_test/`.

1. Controlla che `reports/struttura/GLOSSARIO_LIBRO.md` esista e contenga "APPROVATO". Se non è così, fermati e dimmi di eseguire prima il lotto GLOSSARIO.
2. Esegui con lo strumento **Workflow** lo script "Script STRUTTURA" qui sotto, così com'è, con `args` = `{"data": "<oggi AAAA-MM-GG>", "file": ["SIGLA", "SIGLA"]}`. Le sigle sono quelle del messaggio.
3. Per ogni elemento di `completati`, salva `markdown` in `percorso` con Write. Se `markdown` è vuoto, scrivi il report tu, dai dati del journal.
4. Controlla con `git status --short capitoli/` che nessun capitolo sia cambiato, ignorando i file `._`.
5. Fai un commit con i soli report scritti, messaggio `docs(struttura): report di struttura SIGLA, SIGLA`.
6. Rispondi con al massimo 6 righe:
   - per ogni file: ALTA, MEDIA, BASSA e scartate;
   - per ogni file: gli interventi di Haiku da tenere, da sospendere e da correggere;
   - il messaggio breve per il primo lotto APPLICA.

### Script STRUTTURA

```javascript
export const meta = {
  name: 'struttura-libro',
  description: 'Report di struttura a basso consumo sui file scelti: 3 lenti, verifica a gruppi, secondo scettico sulle ALTA, incrocio con i report di frase',
  phases: [
    { title: 'Lenti', detail: '3 lenti di struttura per file' },
    { title: 'Verifica', detail: 'uno scettico per lente, piu uno sulle ALTA' },
    { title: 'Report', detail: 'incrocio e report con Haiku', model: 'haiku' },
  ],
}

const NOTA_PREF = 'TIPO DI FILE: prefazione metodologica, senza scene né personaggi. Adatta i criteri: per "scena" intendi un esempio concreto o un caso; per "strumento azionabile" intendi la promessa chiara di che cosa il lettore saprà fare alla fine del libro; l apertura deve agganciare un problema del lettore; la chiusura deve dare un motivo per iniziare il capitolo 1. Se un criterio non si applica, non segnalare nulla per quel criterio.'
const NOTA_EPIL = 'TIPO DI FILE: epilogo e toolkit operativo. Per "scena" intendi il richiamo ai casi e ai personaggi dei capitoli. Valuta soprattutto: ogni strumento si può applicare lunedì mattina? Richiama il capitolo e il personaggio da cui nasce? I passi sono numerati, brevi, in ordine d uso? Il ripasso e il richiamo dei concetti sono qui centrali. Se un criterio non si applica, non segnalare nulla per quel criterio.'

const TUTTI = [
  { sigla: 'PREF',  file: 'PREFAZIONE_METODOLOGICA.md', nota: NOTA_PREF },
  { sigla: 'CAP01', file: 'CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md', nota: '' },
  { sigla: 'CAP02', file: 'CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md', nota: '' },
  { sigla: 'CAP03', file: 'CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md', nota: '' },
  { sigla: 'CAP04', file: 'CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md', nota: '' },
  { sigla: 'CAP05', file: 'CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md', nota: '' },
  { sigla: 'CAP06', file: 'CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md', nota: '' },
  { sigla: 'CAP07', file: 'CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md', nota: '' },
  { sigla: 'CAP08', file: 'CAPITOLO_08_IL_GELO_TRA_PARI.md', nota: '' },
  { sigla: 'CAP09', file: 'CAPITOLO_09_IL_CINISMO_DI_REPARTO.md', nota: '' },
  { sigla: 'EPIL',  file: 'EPILOGO_E_TOOLKIT_OPERATIVO.md', nota: NOTA_EPIL },
]
const A = args || {}
const DATA = A.data ? A.data : 'data non indicata'
const FILES = TUTTI.filter(f => (A.file || []).indexOf(f.sigla) >= 0)
if (!FILES.length) throw new Error('args.file deve contenere almeno una sigla tra: ' + TUTTI.map(f => f.sigla).join(', '))
if (FILES.length < (A.file || []).length) log('ATTENZIONE: alcune sigle non valide sono state ignorate')
const GLOSSARIO_FILE = 'reports/struttura/GLOSSARIO_LIBRO.md'
const MAX_PER_LENTE = 8

const REGOLE = [
  'REGOLE:',
  '- Non modificare MAI nessun file. Leggi soltanto.',
  '- Il lettore è un manager o imprenditore di PMI: colto, non specialista, legge la sera ed è stanco.',
  '- Le citazioni devono essere copiate ESATTAMENTE dal file, da 8 a 30 parole.',
  '- Leggi il file una volta sola, per intero. Non leggere altri file se non è richiesto.',
].join('\n')

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    segnalazioni: { type: 'array', items: { type: 'object', properties: {
      controllo: { type: 'string' },
      gravita: { type: 'string', enum: ['ALTA', 'MEDIA', 'BASSA'] },
      sezione: { type: 'string' },
      citazione: { type: 'string' },
      problema: { type: 'string' },
      intervento: { type: 'string', enum: ['spostare', 'tagliare', 'aggiungere', 'riscrivere', 'unire', 'dividere', 'domanda per l autore'] },
      proposta: { type: 'string' },
      evidenza: { type: 'string', enum: ['solida', 'moderata', 'mestiere'] },
    }, required: ['controllo', 'gravita', 'sezione', 'citazione', 'problema', 'intervento', 'proposta', 'evidenza'] } },
    curva_tensione: { type: 'array', items: { type: 'string' } },
    promesse: { type: 'array', items: { type: 'object', properties: {
      testo: { type: 'string' }, dove_si_apre: { type: 'string' }, dove_si_chiude: { type: 'string' },
    }, required: ['testo', 'dove_si_apre', 'dove_si_chiude'] } },
    scartate: { type: 'number' },
  },
  required: ['segnalazioni', 'curva_tensione', 'promesse', 'scartate'],
}
const VERDICTS_SCHEMA = {
  type: 'object',
  properties: {
    verdetti: { type: 'array', items: { type: 'object', properties: {
      indice: { type: 'number' },
      citazione_trovata: { type: 'boolean' },
      smontata: { type: 'boolean' },
      gravita_corretta: { type: 'string', enum: ['ALTA', 'MEDIA', 'BASSA'] },
      motivo: { type: 'string' },
    }, required: ['indice', 'citazione_trovata', 'smontata', 'gravita_corretta', 'motivo'] } },
  },
  required: ['verdetti'],
}
const REPORT_SCHEMA = {
  type: 'object',
  properties: {
    markdown: { type: 'string' },
    tenere: { type: 'number' },
    sospendere: { type: 'number' },
    correggere: { type: 'number' },
  },
  required: ['markdown', 'tenere', 'sospendere', 'correggere'],
}

const LENTI = [
  {
    chiave: 'curiosita',
    titolo: 'Curiosità, domande aperte e promesse',
    criteri: [
      '1. DOMANDA PRIMA DELLA SPIEGAZIONE: ogni spiegazione scientifica o concettuale è preceduta da una domanda concreta del lettore o di un personaggio (Loewenstein 1994; evidenza solida)?',
      '2. DOMANDE CHIUSE: ogni domanda aperta riceve risposta entro il file o in un punto dichiarato? Segnala i cicli aperti abbandonati.',
      '3. PROMESSE: ogni "come vedremo", "più avanti", "nel prossimo capitolo" viene mantenuto? Compila il campo "promesse", indicando dove ognuna si chiude oppure "MAI". Per le promesse verso altri capitoli scrivi la sigla del capitolo.',
      '4. RISPOSTE SENZA DOMANDA: parti in cui il testo risponde a una domanda che il lettore non si è ancora posto.',
      '5. AFFERMAZIONI CONTESTATE: se il testo presenta l effetto Zeigarnik come un fatto, o i cliffhanger come sicuramente efficaci, segnalalo (Ghibellini & Meier 2025; Wirz et al. 2023).',
    ].join('\n'),
  },
  {
    chiave: 'ponte',
    titolo: 'Ponte tra scena e scienza, dettagli seducenti, esempi',
    criteri: [
      '1. PONTE DI ANDATA: il passaggio dalla scena alla spiegazione ha un aggancio esplicito (un gesto, una frase, una cifra della scena) o è un salto di registro brusco?',
      '2. PONTE DI RITORNO: dopo la spiegazione il testo torna alla scena e mostra il concetto applicato al personaggio?',
      '3. BLOCCHI DI SOLA ESPOSIZIONE troppo lunghi per questo lettore: indica inizio e fine con citazioni.',
      '4. DETTAGLI SEDUCENTI: aneddoti, dati o descrizioni interessanti che non portano il concetto, il personaggio o la trama (Rey 2012; Sundararajan & Adesope 2020; evidenza solida).',
      '5. DUE CASI PER PRINCIPIO: i principi chiave sono mostrati con almeno due casi da confrontare (Gentner, Loewenstein & Thompson 2003)? Se manca un caso, è una domanda per l autore.',
      '6. ASTRATTO SENZA CONCRETO: concetti chiave che restano astratti per l intera sezione.',
    ].join('\n'),
  },
  {
    chiave: 'architettura',
    titolo: 'Aperture, chiusure, stacchi, tensione, strumenti, ripasso',
    criteri: [
      '1. APERTURA: le prime 5-8 righe mettono un personaggio in azione, o pongono un problema concreto? (regola di mestiere)',
      '2. CHIUSURA: il file chiude con un gancio leggero in avanti e con il punto chiaro? Non serve un cliffhanger forte (Wirz et al. 2023).',
      '3. STACCHI DI SEZIONE: la sezione successiva riparte con un motivo per continuare? Il lettore capisce subito dove e quando si trova e chi parla?',
      '4. CURVA DELLA TENSIONE: compila il campo "curva_tensione" con 4-6 punti. Segnala i tratti lunghi senza tensione né domanda.',
      '5. MOSTRARE PRIMA DI NOMINARE: le emozioni sono mostrate con corpo, gesti e azioni prima di essere nominate o spiegate?',
      '6. STRUMENTO AZIONABILE: lo strumento pratico è mostrato mentre un personaggio lo usa, ed è abbastanza preciso da poterlo applicare lunedì mattina?',
      '7. RIPASSO E RICHIAMI: ci sono domande di richiamo a fine file, o richiami ai capitoli precedenti? Indica dove servirebbero (Dunlosky et al. 2013; evidenza solida).',
    ].join('\n'),
  },
]

const GRAVITA = [
  'GRAVITÀ: ALTA = probabile punto di abbandono, oppure il concetto chiave non arriva. MEDIA = la lettura rallenta o la tensione cala. BASSA = migliorabile.',
  'Massimo ' + MAX_PER_LENTE + ' segnalazioni, le più gravi. Non devi arrivare al massimo: segnala solo problemi reali. Non c è un numero atteso di ALTA, possono essere zero o molte. In "scartate" indica quante altre ne hai lasciato fuori.',
  'PROPOSTE: preferisci spostare, tagliare, unire o riformulare ciò che c è già. Non proporre scene, personaggi, battute, casi o fatti nuovi. Se l unico rimedio è aggiungere materiale nuovo, usa intervento = "domanda per l autore" e scrivi la domanda, non il testo.',
  'Prima di segnalare, controlla che il testo non risolva già il problema poco prima o poco dopo: una domanda già posta, un ritorno alla scena, una promessa mantenuta altrove.',
  'Compila i campi "curva_tensione" e "promesse" solo se i tuoi criteri li chiedono; altrimenti lasciali vuoti.',
].join('\n')

const risultati = await pipeline(
  FILES,

  // Lenti (Sonnet): 3 letture indipendenti
  (f) => parallel(LENTI.map(l => () => agent(
    [
      'Sei un editor di sviluppo per la saggistica narrativa italiana. Analizzi la STRUTTURA di capitoli/' + f.file + '.',
      f.nota,
      'Lente: ' + l.titolo + '. Non segnalare frasi lunghe o parole difficili: le ha già controllate un altra revisione.',
      'CRITERI:\n' + l.criteri,
      GRAVITA,
      'Per ogni segnalazione dai: il controllo (numero e nome del criterio), la sezione (il titolo più vicino), una citazione esatta che indichi il punto, il problema in 1-2 frasi, il tipo di intervento e una proposta concreta. Non inventare fatti, cifre o nomi.',
      REGOLE,
    ].filter(Boolean).join('\n\n'),
    { label: l.chiave + ':' + f.sigla, phase: 'Lenti', schema: FINDINGS_SCHEMA }
  ).then(r => r ? Object.assign({ lente: l.chiave }, r) : null))),

  // Verifica a gruppi (Sonnet): uno scettico per lente
  (lenti, f) => {
    const valide = lenti.filter(Boolean)
    const curva = (valide.find(x => x.lente === 'architettura') || {}).curva_tensione || []
    const promesse = (valide.find(x => x.lente === 'curiosita') || {}).promesse || []
    return parallel(valide.filter(x => x.segnalazioni.length).map(x => () => agent(
      [
        'Sei un verificatore scettico. Prova a SMONTARE ognuna di queste segnalazioni di struttura sul file capitoli/' + f.file + ' (lente: ' + x.lente + ').',
        f.nota,
        'Segnalazioni, numerate da 0:\n' + x.segnalazioni.map((s, i) => i + ') ' + JSON.stringify(s)).join('\n'),
        'Per ciascuna:',
        '1. Cerca la citazione con grep -F nel file. Se non c è parola per parola, citazione_trovata = false.',
        '2. Il problema è reale per un manager di PMI che legge la sera? Oppure il testo lo risolve poco prima o poco dopo?',
        '3. La proposta peggiorerebbe il testo o inventerebbe fatti nuovi? Una "domanda per l autore" non conta come invenzione.',
        'Se hai dubbi, smontata = true. Restituisci un verdetto per ogni indice, con la gravità che ritieni corretta e il motivo in una frase.',
        REGOLE,
      ].filter(Boolean).join('\n\n'),
      { label: 'verifica:' + f.sigla + ':' + x.lente, phase: 'Verifica', schema: VERDICTS_SCHEMA, effort: 'medium' }
    ).then(v => {
      const verd = v ? v.verdetti : []
      return x.segnalazioni.map((s, i) => {
        const d = verd.find(z => z.indice === i)
        const ok = !!d && d.citazione_trovata && !d.smontata
        return { s: Object.assign({ lente: x.lente }, s, { gravita: ok ? d.gravita_corretta : s.gravita }), ok: ok, motivo: d ? d.motivo : 'nessun verdetto' }
      })
    }))).then(gruppi => ({ tutte: gruppi.filter(Boolean).flat(), curva: curva, promesse: promesse }))
  },

  // Secondo scettico solo sulle ALTA sopravvissute
  (ver, f) => {
    const alte = ver.tutte.filter(x => x.ok && x.s.gravita === 'ALTA')
    if (!alte.length) return ver
    return agent(
      [
        'Sei un secondo verificatore scettico, indipendente dal primo. Queste segnalazioni ALTA sul file capitoli/' + f.file + ' sono state confermate una volta. Prova a smontarle.',
        'Segnalazioni, numerate da 0:\n' + alte.map((x, i) => i + ') ' + JSON.stringify(x.s)).join('\n'),
        'Giudica la gravità in modo neutrale: ALTA = probabile punto di abbandono, oppure il concetto chiave non arriva; MEDIA = la lettura rallenta o la tensione cala. Mantieni ALTA se il criterio è soddisfatto, declassa solo se non lo è. Restituisci un verdetto per ogni indice.',
        REGOLE,
      ].join('\n\n'),
      { label: 'verifica-alta:' + f.sigla, phase: 'Verifica', schema: VERDICTS_SCHEMA, effort: 'medium' }
    ).then(v => {
      const verd = v ? v.verdetti : []
      alte.forEach((x, i) => {
        const d = verd.find(z => z.indice === i)
        if (!d || d.smontata || !d.citazione_trovata) { x.ok = false; x.motivo = 'smontata dal secondo verificatore: ' + (d ? d.motivo : 'nessun verdetto') }
        else if (d.gravita_corretta !== 'ALTA') { x.s.gravita = d.gravita_corretta; x.motivo = 'declassata dal secondo verificatore: ' + d.motivo }
      })
      return ver
    })
  },

  // Incrocio + report (Haiku)
  (ver, f) => {
    const conf = ver.tutte.filter(x => x.ok).map(x => x.s)
    const scart = ver.tutte.filter(x => !x.ok).map(x => ({ controllo: x.s.controllo, sezione: x.s.sezione, motivo: x.motivo }))
    return agent(
      [
        'Prepara in Markdown il report reports/struttura/' + f.sigla + '_struttura.md, in italiano semplice, per un autore che non è un programmatore. Data: ' + DATA + '.',
        'NON scrivere file: restituisci il testo completo nel campo "markdown", e lo salverà la sessione principale. Nei campi tenere, sospendere e correggere metti i conteggi degli interventi di Haiku.',
        'Leggi SOLO due file: reports/leggibilita/' + f.sigla + '_leggibilita.md (interventi di frase numerati [01], [02] e così via) e ' + GLOSSARIO_FILE + ' (glossario approvato). Non rileggere il capitolo.',
        'Segnalazioni di struttura confermate: ' + JSON.stringify(conf),
        'Scartate dai verificatori: ' + JSON.stringify(scart),
        'Curva della tensione: ' + JSON.stringify(ver.curva),
        'Promesse e domande aperte: ' + JSON.stringify(ver.promesse),
        'Per OGNI intervento di frase del report di Haiku decidi lo stato:',
        '- "da sospendere": il suo paragrafo verrebbe tagliato, spostato o riscritto da una segnalazione di struttura (confronta sezione e citazione).',
        '- "da correggere": la proposta usa una forma che il glossario sostituisce, o contraddice una segnalazione di struttura. Scrivi la proposta corretta con la forma scelta del glossario.',
        '- "da tenere": tutto il resto.',
        'STRUTTURA DEL FILE:',
        '# Struttura e tenuta del lettore — ' + f.file,
        '## Sintesi: 4-6 righe con il giudizio, i numeri (ALTA, MEDIA, BASSA, scartate) e la cosa più importante da fare.',
        '## Curva della tensione',
        '## Interventi di struttura: da ALTA a BASSA; per ognuno [S01] e così via, gravità, lente, evidenza, sezione, citazione in blocco >, problema, intervento proposto. Le domande per l autore vanno segnate come tali.',
        '## Registro delle promesse e delle domande aperte: tabella con promessa | dove si apre | dove si chiude (oppure MAI, oppure la sigla di un altro capitolo).',
        '## Interventi di frase di Haiku: tre elenchi (da tenere, da sospendere, da correggere) con numero e motivo in una riga; per quelli da correggere, la nuova proposta.',
        '## Ordine di lavoro consigliato',
        '## Scartate dai verificatori: una riga ciascuna.',
      ].join('\n\n'),
      { label: 'report:' + f.sigla, phase: 'Report', model: 'haiku', effort: 'medium', schema: REPORT_SCHEMA }
    ).then(rep => ({
      sigla: f.sigla,
      percorso: 'reports/struttura/' + f.sigla + '_struttura.md',
      alta: conf.filter(s => s.gravita === 'ALTA').length,
      media: conf.filter(s => s.gravita === 'MEDIA').length,
      bassa: conf.filter(s => s.gravita === 'BASSA').length,
      scartate: scart.length,
      markdown: rep ? rep.markdown : '',
      haiku: rep ? { tenere: rep.tenere, sospendere: rep.sospendere, correggere: rep.correggere } : null,
    }))
  }
)

const fatti = risultati.filter(Boolean)
const mancanti = FILES.filter(f => !fatti.find(r => r.sigla === f.sigla)).map(f => f.sigla)
if (mancanti.length) log('ATTENZIONE: file non completati: ' + mancanti.join(', '))
const vuoti = fatti.filter(r => !r.markdown).map(r => r.sigla)
if (vuoti.length) log('ATTENZIONE: report vuoti, da scrivere dal journal: ' + vuoti.join(', '))
return { completati: fatti, mancanti: mancanti, report_vuoti: vuoti }
```

---

## LOTTO APPLICA

**Obiettivo:** applicare a **un solo file** (la sigla del messaggio) gli interventi del suo report di struttura e del suo report di frase. Il lavoro si fa su un ramo git a parte, con due fermate per l'autore. Il modello è la revisione del capitolo 3. Non usare Workflow né subagenti: lavora da solo, in questa sessione.

**File:**
- **da modificare:** `capitoli/<FILE>` (vedi la tabella dei file)
- **struttura:** `reports/struttura/<SIGLA>_struttura.md`
- **frasi:** `reports/leggibilita/<SIGLA>_leggibilita.md`
- **glossario approvato:** `reports/struttura/GLOSSARIO_LIBRO.md`
- **voce:** `progetto/03_GUIDA_STILISTICA.md`, da leggere una volta
- **fatti:** `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md`. Leggi solo le voci dei personaggi, delle aziende e delle cifre che compaiono nel file, cercandole con grep.

### Passo 0 — Preparazione
1. Controlla che `reports/struttura/<SIGLA>_struttura.md` esista e che il glossario contenga "APPROVATO". Se manca qualcosa, fermati e dimmi quale lotto eseguire prima.
2. `git switch main`. Poi controlla che `git status --short capitoli/<FILE>` non mostri modifiche: se ne mostra, fermati e chiedi.
3. `git switch -c revisione-<sigla in minuscolo>` (per esempio `revisione-pref`, `revisione-cap06`).
4. Leggi per intero il file, i due report e il glossario. Leggi la guida stilistica e le voci utili del registro.
5. Misura il file di partenza con `python3 strumenti/metriche_leggibilita.py capitoli/<FILE>`.

### Passo 1 — Prima fermata
Mostrami in una volta sola:
- **a. Domande per l'autore:** gli interventi di struttura segnati come domande, e le voci dell'"Ordine di lavoro" che richiedono materiale nuovo. Per ognuna dai 2–3 opzioni.
- **b. Conflitti:** interventi di struttura e di frase sullo stesso paragrafo che non si possono applicare entrambi.
- **c. Glossario nel file:** solo i casi in cui la forma scelta dal glossario stonerebbe qui, per esempio in una battuta di dialogo o in un documento dentro la storia. Proponi un'eccezione.
- **d. Incongruenze di fatti** che noti leggendo: cifre, date, nomi, sigle. Non correggerle: elencale.

Poi **aspetta la mia risposta**. Le voci senza risposta restano come sono.

### Passo 2 — Struttura
1. Applica gli interventi [S..] confermati, nell'ordine dell'"Ordine di lavoro consigliato".
2. Per ognuno: cerca la citazione con grep -F, modifica solo ciò che serve, rileggi il paragrafo prima e quello dopo.
3. Se un intervento non si può applicare senza inventare, saltalo e annotalo.
4. Rileggi il file una volta, dall'inizio alla fine, per controllare il filo.
5. `git add capitoli/<FILE>` e `git commit -m "revisione(<sigla>): interventi di struttura"`.

### Passo 3 — Frasi e glossario
1. Interventi "da tenere": usa come base la proposta di Haiku. Migliorala solo se suona meno naturale dell'originale.
2. Interventi "da correggere": usa la proposta corretta scritta nel report di struttura.
3. Interventi "da sospendere": non si applicano. Fa eccezione il caso in cui, dopo il passo 2, la citazione esiste ancora identica e la proposta ha ancora senso.
4. Applica il glossario approvato, con le eccezioni decise al passo 1.
5. Le citazioni sparite per effetto del passo 2 vanno annotate come "superate dalla struttura".
6. `git commit -m "revisione(<sigla>): interventi di frase e glossario"`, con il solo file del capitolo.

### Passo 4 — Verifica (senza modificare)
1. **Fatti invariati.** Usa `git diff main -- capitoli/<FILE>`. Ogni cifra, data, nome proprio e riferimento scientifico presente in una riga tolta deve esistere ancora nel file, a meno che sia stato tolto di proposito da un intervento approvato. Se ne manca qualcuno, correggilo con un commit.
2. **Metriche.** Ripeti la misura del passo 0. Non spezzare frasi solo per alzare il Gulpease.
3. **Rilettura da lettore stanco.** Indica i 3 punti in cui il lettore potrebbe ancora fermarsi, senza correggerli.

### Passo 5 — Seconda fermata
Mostrami:
- le metriche prima e dopo;
- che cosa è stato applicato, saltato, superato o sospeso;
- i 3 punti a rischio;
- il comando `git diff main -- capitoli/<FILE>`.

Poi **aspetta**. Applica le altre correzioni che ti chiedo, con un commit.

### Passo 6 — Registro e unione
1. Scrivi `reports/struttura/<SIGLA>_REGISTRO_MODIFICHE.md`, nello stesso formato di quello del capitolo 3:
   - intestazione con data, ramo e commit;
   - tabella degli interventi di struttura e di frase con stato e nota;
   - metriche prima e dopo;
   - eccezioni al glossario;
   - sezione "Non toccato, da decidere" con le incongruenze di fatti.

   Fai un commit con il solo registro.
2. **Solo se ti scrivo "unisci":** `git switch main` e poi `git merge --no-ff revisione-<sigla>`. Mai push.
3. Rispondi con 3 righe: stato, file del registro, messaggio breve per il prossimo lotto secondo il piano delle sessioni.

---

## LOTTO FINALE

**Obiettivo:** controllare la coerenza tra i capitoli e assemblare il libro revisionato. Non usare Workflow né subagenti. Quasi tutto si fa con script Python nella tua cartella temporanea, senza installare nulla.

1. **Stato.** Controlla con `git branch --no-merged main` che non resti nessun ramo `revisione-*` da unire, e che esistano 11 registri `reports/struttura/*_REGISTRO_MODIFICHE.md`. Se manca qualcosa, elencalo e chiedimi se proseguire.
2. **Metriche del libro.** Esegui `python3 strumenti/metriche_leggibilita.py` su ogni file di `capitoli/`, ora e nella versione di partenza: `git show 8816686:capitoli/<FILE>`, salvata in un file temporaneo. Prepara una tabella prima/dopo per file.
3. **Glossario.** Per ogni riga della tabella "Termini tecnici" di `GLOSSARIO_LIBRO.md`, cerca con grep le "forme da sostituire" in tutti i file di `capitoli/`. Elenca le occorrenze rimaste, escluse le eccezioni ammesse e quelle annotate nei registri.
4. **Promesse tra capitoli.** Dagli 11 report di struttura prendi le righe del "Registro delle promesse" che rimandano a un altro capitolo o che sono segnate MAI. Controlla con grep se il capitolo di arrivo le mantiene. Elenca quelle che restano aperte.
5. **Decisioni aperte.** Raccogli in un elenco unico le sezioni "Non toccato, da decidere" di tutti i registri.
6. **Libro assemblato.** Unisci in `reports/finale/LIBRO_REVISIONATO_<data>.md` i file di `capitoli/` in quest'ordine: PREF, CAP01…CAP09, EPIL, separati da una riga `---`. Non toccare `archivio/` e non usare `assemble_book.ps1`.
7. **Rapporto.** Scrivi `reports/finale/RAPPORTO_FINALE.md` con i risultati dei punti 2–5. Aggiungi le prossime azioni per l'autore, tra cui la prova con 3–5 lettori reali, che è l'unico controllo con validità diretta.
8. Fai un commit con i soli file di `reports/finale/`, messaggio `docs(finale): rapporto finale e libro assemblato`. Rispondi con al massimo 8 righe.

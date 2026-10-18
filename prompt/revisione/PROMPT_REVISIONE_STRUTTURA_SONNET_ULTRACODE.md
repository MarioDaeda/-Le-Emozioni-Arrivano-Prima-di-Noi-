# PROMPT — Revisione di struttura e tenuta del lettore (Sonnet 5.5, ultracode)

> **Cosa fa.** È il punto 3 del piano: guarda la struttura dei capitoli intera, prima di correggere le frasi. Usa 3 lenti di lettura e verifica ogni segnalazione con agenti scettici. Poi incrocia i risultati con i 274 interventi di frase già fatti da Haiku e prepara una bozza di glossario dei termini fissi. **Nessun file in `capitoli/` viene modificato.**
>
> **Come lanciarlo: a lotti, una sessione per riga.** Ogni volta apri una sessione **nuova** di Claude Code nella cartella `Libro Emozioni`, con modello **Sonnet 5.5** ed effort **medio**. Incolla tutto ciò che sta sotto la linea, poi cambia solo la riga `LOTTO:` in fondo al messaggio. Lancia il lotto successivo solo quando il precedente è finito, e dopo che il limite delle 5 ore si è azzerato.
>
> | Sessione | Riga LOTTO da usare | Agenti circa |
> |---|---|---|
> | 1 | `LOTTO: glossario` | 12 |
> | 2 | `LOTTO: capitoli PREF EPIL` | 70–80 |
> | 3 | `LOTTO: capitoli CAP01 CAP02 CAP03` | 100–110 |
> | 4 | `LOTTO: capitoli CAP04 CAP05 CAP06` | 100–110 |
> | 5 | `LOTTO: capitoli CAP07 CAP08 CAP09` | 100–110 |
> | 6 | `LOTTO: indice` | 1 |
>
> La sessione 1 deve venire per prima, perché i lotti dei capitoli leggono il glossario. La sessione 6 deve venire per ultima. L'ordine delle sessioni 2–5 è libero, ma conviene partire da Prefazione ed Epilogo, che sono i file più difficili. Se un lotto da 3 file supera il tuo limite, dividilo in lotti da 1–2 file: lo script accetta qualsiasi elenco di sigle.

---

ultracode

## Compito

Leggi la riga `LOTTO:` in fondo a questo messaggio. Poi esegui con lo strumento **Workflow** lo script qui sotto, così com'è, con questi `args`:

- `LOTTO: glossario` → `{"data": "<oggi AAAA-MM-GG>", "fase": "glossario"}`
- `LOTTO: capitoli SIGLA SIGLA ...` → `{"data": "<oggi AAAA-MM-GG>", "fase": "capitoli", "file": ["SIGLA", "SIGLA"]}`
- `LOTTO: indice` → `{"data": "<oggi AAAA-MM-GG>", "fase": "indice"}`

Se la riga contiene più lotti separati da `+` (per esempio `LOTTO: glossario + capitoli CAP01 CAP02 CAP03`), esegui un workflow per ogni lotto, nell'ordine scritto. Parti con il successivo solo quando il precedente è finito.

Non riscrivere lo script e non cambiare l'effort degli agenti. Se il workflow si interrompe, rilancialo **in questa stessa sessione** con `resumeFromRunId`: le parti già fatte non vengono ripetute.

Prima di partire, con un lotto `capitoli`, controlla che esista `reports/struttura/GLOSSARIO_PROPOSTO.md`. Se manca, fermati e dimmi di lanciare prima il lotto `glossario`.

Alla fine:
1. Controlla con `git status --short capitoli/` che nessun capitolo sia stato modificato. I file che iniziano con `._` sono metadati di macOS e vanno ignorati.
2. Controlla che esistano i file previsti dal lotto in `reports/struttura/`.
3. Rispondi in chat con al massimo 10 righe:
   - i file prodotti;
   - le segnalazioni confermate e quelle scartate dai verificatori;
   - quanti interventi di Haiku sono da tenere, da sospendere e da correggere;
   - quale lotto manca ancora. Lo capisci da quali report esistono in `reports/struttura/`.

## Contesto per te (non per lo script)

- Il libro è saggistica narrativa italiana sulle emozioni nel business. I lettori sono manager e imprenditori di PMI.
- Il report di ricerca `reports/Controlli di leggibilità per il libro.md` contiene le regole. Le sezioni che servono qui sono quelle da "Il lettore continua quando ha una domanda aperta" a "Ripasso e richiami".
- I report di frase già fatti sono in `reports/leggibilita/` (`CAP01_leggibilita.md`, ecc.).

## Script

```javascript
export const meta = {
  name: 'revisione-struttura-capitoli',
  description: 'Revisione di struttura e tenuta del lettore a lotti (glossario, capitoli scelti, indice), con verifica avversaria e incrocio con i report di frase',
  phases: [
    { title: 'Glossario', detail: 'estrazione dei termini tecnici per file, poi fusione' },
    { title: 'Lenti', detail: '3 lenti di struttura per file' },
    { title: 'Verifica', detail: 'scettici che provano a smontare ogni segnalazione' },
    { title: 'Incrocio', detail: 'stato dei 274 interventi di frase alla luce della struttura' },
    { title: 'Report', detail: 'un report per file e un indice' },
  ],
}

const FILES = [
  { sigla: 'PREF',  file: 'PREFAZIONE_METODOLOGICA.md', genere: 'prefazione metodologica' },
  { sigla: 'CAP01', file: 'CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP02', file: 'CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP03', file: 'CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP04', file: 'CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP05', file: 'CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP06', file: 'CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP07', file: 'CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP08', file: 'CAPITOLO_08_IL_GELO_TRA_PARI.md', genere: 'capitolo narrativo' },
  { sigla: 'CAP09', file: 'CAPITOLO_09_IL_CINISMO_DI_REPARTO.md', genere: 'capitolo narrativo' },
  { sigla: 'EPIL',  file: 'EPILOGO_E_TOOLKIT_OPERATIVO.md', genere: 'epilogo e toolkit operativo' },
]

const RICERCA = 'reports/Controlli di leggibilità per il libro.md'
const GLOSSARIO_FILE = 'reports/struttura/GLOSSARIO_PROPOSTO.md'
const A = args || {}
const DATA = A.data ? A.data : 'data non indicata'
const FASE = A.fase
if (['glossario', 'capitoli', 'indice'].indexOf(FASE) < 0) {
  throw new Error('args.fase deve essere "glossario", "capitoli" oppure "indice"')
}
const SELEZIONE = FASE === 'capitoli'
  ? FILES.filter(f => (A.file || []).indexOf(f.sigla) >= 0)
  : []
if (FASE === 'capitoli' && SELEZIONE.length === 0) {
  throw new Error('Con fase "capitoli" serve args.file con almeno una sigla valida: ' + FILES.map(f => f.sigla).join(', '))
}
if (FASE === 'capitoli' && SELEZIONE.length < (A.file || []).length) {
  log('ATTENZIONE: alcune sigle non sono valide e sono state ignorate')
}

const REGOLE_COMUNI = [
  'REGOLE VALIDE PER TUTTI:',
  '- Non modificare MAI nessun file in capitoli/. Leggi soltanto.',
  '- Il lettore è un manager o imprenditore di PMI: colto, non specialista, legge la sera ed è stanco.',
  '- Ogni citazione che riporti deve essere copiata ESATTAMENTE dal capitolo, da 8 a 40 parole. Prima di restituirla, verificala con grep -F sul file. Se non la trovi, correggila o scartala.',
  '- Nella prefazione e nell epilogo non ci sono sempre scene: adatta i criteri al genere del file e dichiaralo.',
  '- Distingui le regole con evidenza solida (curiosità, dettagli seducenti, ripasso) dalle regole di mestiere (aperture, ritmo): lo trovi indicato nel report di ricerca.',
].join('\n')

// ---------- Schemi ----------
const TERMS_SCHEMA = {
  type: 'object',
  properties: {
    termini: { type: 'array', items: { type: 'object', properties: {
      termine: { type: 'string' },
      varianti_usate: { type: 'array', items: { type: 'string' } },
      occorrenze: { type: 'number' },
      prima_sezione: { type: 'string' },
      definita_alla_prima_comparsa: { type: 'boolean' },
      tipo: { type: 'string', enum: ['tecnico', 'vago'] },
    }, required: ['termine', 'varianti_usate', 'occorrenze', 'prima_sezione', 'definita_alla_prima_comparsa', 'tipo'] } },
  },
  required: ['termini'],
}

const FINDINGS_SCHEMA = {
  type: 'object',
  properties: {
    segnalazioni: { type: 'array', items: { type: 'object', properties: {
      controllo: { type: 'string' },
      gravita: { type: 'string', enum: ['ALTA', 'MEDIA', 'BASSA'] },
      sezione: { type: 'string' },
      citazione: { type: 'string' },
      problema: { type: 'string' },
      intervento: { type: 'string', enum: ['spostare', 'tagliare', 'aggiungere', 'riscrivere', 'unire', 'dividere'] },
      proposta: { type: 'string' },
      evidenza: { type: 'string', enum: ['solida', 'moderata', 'mestiere'] },
    }, required: ['controllo', 'gravita', 'sezione', 'citazione', 'problema', 'intervento', 'proposta', 'evidenza'] } },
    scartate: { type: 'number' },
    nota_genere: { type: 'string' },
  },
  required: ['segnalazioni', 'scartate', 'nota_genere'],
}

const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    citazione_trovata: { type: 'boolean' },
    smontata: { type: 'boolean' },
    gravita_corretta: { type: 'string', enum: ['ALTA', 'MEDIA', 'BASSA'] },
    motivo: { type: 'string' },
  },
  required: ['citazione_trovata', 'smontata', 'gravita_corretta', 'motivo'],
}

const MAPPING_SCHEMA = {
  type: 'object',
  properties: {
    interventi: { type: 'array', items: { type: 'object', properties: {
      numero: { type: 'string' },
      stato: { type: 'string', enum: ['tenere', 'sospendere', 'correggere'] },
      motivo: { type: 'string' },
      correzione: { type: 'string' },
    }, required: ['numero', 'stato', 'motivo', 'correzione'] } },
  },
  required: ['interventi'],
}

// ---------- Lenti ----------
const LENTI = [
  {
    chiave: 'curiosita',
    titolo: 'Curiosità, domande aperte e promesse',
    criteri: [
      '1. DOMANDA PRIMA DELLA SPIEGAZIONE: ogni spiegazione scientifica o concettuale è preceduta da una domanda concreta che il lettore o un personaggio si pone (un vuoto specifico e colmabile, Loewenstein 1994)? Segnala le spiegazioni che arrivano senza domanda.',
      '2. DOMANDE CHIUSE: ogni domanda aperta riceve risposta entro il capitolo o in un punto dichiarato? Segnala i cicli aperti abbandonati.',
      '3. REGISTRO DELLE PROMESSE: ogni "come vedremo", "più avanti", "nel prossimo capitolo" viene mantenuto? Elenca le promesse e indica dove si chiudono; segnala quelle non mantenute.',
      '4. SPIEGAZIONI SENZA DOMANDA: le parti in cui il testo risponde a una domanda che il lettore non si è ancora posto.',
      '5. AFFERMAZIONI CONTESTATE: se il testo cita l effetto Zeigarnik come fatto, o presenta i cliffhanger come sicuramente efficaci, segnalalo (meta-analisi Ghibellini & Meier 2025; Wirz et al. 2023).',
    ].join('\n'),
  },
  {
    chiave: 'ponte',
    titolo: 'Ponte tra scena e scienza, dettagli seducenti, esempi',
    criteri: [
      '1. PONTE DI ANDATA: il passaggio dalla scena alla spiegazione ha un aggancio esplicito (un gesto, una frase o una cifra della scena) o è un salto di registro brusco?',
      '2. PONTE DI RITORNO: dopo la spiegazione il testo torna alla scena e mostra il concetto applicato al personaggio? Segnala le spiegazioni che non tornano mai alla scena.',
      '3. BLOCCHI DI SPIEGAZIONE TROPPO LUNGHI: tratti di sola esposizione che interrompono la narrazione troppo a lungo per questo lettore. Indica inizio e fine con citazioni.',
      '4. DETTAGLI SEDUCENTI: aneddoti, dati o descrizioni interessanti ma che non portano il concetto, il personaggio o la trama (Rey 2012; Sundararajan & Adesope 2020, g circa -0,33). Proponi di tagliarli o di legarli al concetto.',
      '5. DUE CASI PER PRINCIPIO: i principi chiave del capitolo sono mostrati con almeno due casi da confrontare (Gentner, Loewenstein & Thompson 2003)? Segnala i principi chiave con un solo caso.',
      '6. ASTRATTO SENZA CONCRETO: concetti chiave che restano astratti per l intera sezione, senza un esempio concreto vicino.',
    ].join('\n'),
  },
  {
    chiave: 'architettura',
    titolo: 'Aperture, chiusure, stacchi, tensione, strumenti, ripasso',
    criteri: [
      '1. APERTURA: le prime 5-8 righe mettono un personaggio in azione, oppure pongono una domanda o un problema concreto? Segnala le aperture che partono da astrazioni o da riassunti.',
      '2. CHIUSURA: il capitolo chiude con un gancio leggero in avanti e con il punto chiaro? Non serve un cliffhanger forte (Wirz et al. 2023: alza l eccitazione, non la voglia di continuare). Segnala le chiusure piatte o che riassumono troppo.',
      '3. STACCHI DI SEZIONE: ogni stacco è un punto in cui il lettore può smettere. La sezione successiva riparte con un motivo per continuare? Il lettore capisce subito dove e quando si trova e chi parla?',
      '4. CURVA DELLA TENSIONE: descrivi in 4-6 punti come sale e scende la tensione nel capitolo. Segnala i tratti lunghi senza alcuna tensione né domanda.',
      '5. MOSTRARE PRIMA DI NOMINARE: le emozioni dei personaggi sono mostrate con corpo, gesti e azioni prima di essere nominate o spiegate?',
      '6. STRUMENTO AZIONABILE: lo strumento pratico del capitolo è mostrato mentre un personaggio lo usa nella storia, ed è abbastanza preciso da poterlo applicare lunedì mattina?',
      '7. RIPASSO E RICHIAMI: ci sono una o più domande di richiamo, o un riepilogo attivo, a fine capitolo? Ci sono richiami a concetti dei capitoli precedenti? Indica dove aggiungerli (Dunlosky et al. 2013: richiamo attivo e ripasso distanziato).',
    ].join('\n'),
  },
]

const GRAVITA = [
  'GRAVITÀ:',
  'ALTA = probabile punto di abbandono, oppure il concetto chiave del capitolo non arriva.',
  'MEDIA = la lettura rallenta o la tensione cala, ma il lettore probabilmente continua.',
  'BASSA = migliorabile.',
  'Massimo 12 segnalazioni per lente, le più gravi. Indica in "scartate" quante altre ne hai lasciato fuori.',
].join('\n')

// ---------- LOTTO glossario (la fusione richiede tutti i file) ----------
if (FASE === 'glossario') {
phase('Glossario')
const estrazioni = await parallel(FILES.map(f => () => agent(
  [
    'Leggi per intero capitoli/' + f.file + ' (' + f.genere + ').',
    'Elenca i termini tecnici di psicologia, neuroscienze, finanza o gestione (per esempio "somatico", "allostatico", "frattura", "vincolo", "WYSIATI", "burn rate") e le parole vaghe usate spesso ("sistemico", "relazionale").',
    'Per ogni termine indica: le varianti o i sinonimi usati per lo stesso concetto, il numero di occorrenze, la prima sezione in cui compare, se viene definito in modo concreto alla prima comparsa, e se è "tecnico" o "vago".',
    'Al massimo 40 termini, i più rilevanti.',
    REGOLE_COMUNI,
  ].join('\n\n'),
  { label: 'glossario:' + f.sigla, phase: 'Glossario', schema: TERMS_SCHEMA, effort: 'medium' }
).then(r => r ? { sigla: f.sigla, termini: r.termini } : null)))

const estrazioniValide = estrazioni.filter(Boolean)
log('Glossario: estratti termini da ' + estrazioniValide.length + ' file su ' + FILES.length)

const glossario = await agent(
  [
    'Unisci queste estrazioni di termini da 11 file in un unico GLOSSARIO PROPOSTO per il libro.',
    JSON.stringify(estrazioniValide),
    'Regola del report di ricerca: per i termini TECNICI si usa sempre la stessa parola in tutto il libro (niente sinonimi alternati, che fanno pensare a concetti diversi). Le parole VAGHE si riducono o si sostituiscono con parole concrete.',
    'Scrivi il file reports/struttura/GLOSSARIO_PROPOSTO.md (crea la cartella se non esiste), in italiano semplice. Deve contenere:',
    '1. una tabella dei termini tecnici: termine scelto | varianti da eliminare | definizione proposta di una riga, concreta | capitolo e sezione della prima comparsa | definito bene alla prima comparsa? | occorrenze totali;',
    '2. una tabella delle parole vaghe: parola | occorrenze per file | alternative concrete;',
    '3. le decisioni che spettano all autore, cioè i casi in cui la scelta della parola non è ovvia.',
    'In cima scrivi in grassetto che è una BOZZA che l autore deve approvare.',
    'Restituisci come testo finale l elenco dei termini tecnici scelti, uno per riga, nel formato "termine: varianti da eliminare".',
    REGOLE_COMUNI,
  ].join('\n\n'),
  { label: 'glossario:fusione', phase: 'Glossario' }
)
return { lotto: 'glossario', file_letti: estrazioniValide.length, file_glossario: GLOSSARIO_FILE, termini: glossario }
}

// ---------- LOTTO capitoli: pipeline sui file scelti ----------
if (FASE === 'capitoli') {
log('Lotto capitoli: ' + SELEZIONE.map(f => f.sigla).join(', '))
const risultati = await pipeline(
  SELEZIONE,

  // Lenti: 3 letture indipendenti dello stesso file
  (f) => parallel(LENTI.map(l => () => agent(
    [
      'Sei un editor di sviluppo per la saggistica narrativa. Analizzi la STRUTTURA di UN solo file: capitoli/' + f.file + ' (' + f.genere + ').',
      'Lente: ' + l.titolo + '.',
      'Prima leggi nel file ' + RICERCA + ' le sezioni da "Il lettore continua quando ha una domanda aperta" fino a "Ripasso e richiami" compresa. Poi leggi il file per intero, dall inizio alla fine, prima di segnalare qualsiasi cosa.',
      'Non segnalare frasi lunghe o parole difficili: le ha già controllate un altra revisione. Qui conta come sono disposte le parti del capitolo.',
      'CRITERI:\n' + l.criteri,
      GRAVITA,
      'Per ogni segnalazione dai: il controllo (numero e nome del criterio), la sezione (titolo del paragrafo più vicino), una citazione esatta che indichi il punto, il problema in 1-2 frasi, il tipo di intervento e una proposta concreta (che cosa spostare, tagliare o aggiungere, e dove). Se scrivi una frase nuova, rispetta la voce del libro e non inventare fatti, cifre o nomi.',
      'In "nota_genere" spiega in una frase come hai adattato i criteri a questo tipo di file.',
      REGOLE_COMUNI,
    ].join('\n\n'),
    { label: l.chiave + ':' + f.sigla, phase: 'Lenti', schema: FINDINGS_SCHEMA }
  ).then(r => r ? r.segnalazioni.map(s => Object.assign({ lente: l.chiave }, s)) : []))).then(liste => ({
    segnalazioni: liste.filter(Boolean).flat(),
  })),

  // Verifica: 3 scettici per le segnalazioni ALTA, 1 per le altre
  (lenti, f) => parallel(lenti.segnalazioni.map((s, i) => () => {
    const n = s.gravita === 'ALTA' ? 3 : 1
    return parallel(Array.from({ length: n }, (_, k) => () => agent(
      [
        'Sei un verificatore scettico (n. ' + (k + 1) + '). Il tuo compito è provare a SMONTARE questa segnalazione di struttura sul file capitoli/' + f.file + '.',
        'Segnalazione: ' + JSON.stringify(s),
        'Passi da seguire:',
        '1. Cerca la citazione con grep -F nel file. Se non c è parola per parola, citazione_trovata = false.',
        '2. Leggi il contesto ampio (almeno la sezione intera, e le sezioni prima e dopo). Il problema è reale per un manager di PMI che legge la sera? Oppure il testo lo risolve poco prima o poco dopo (domanda già posta, ritorno alla scena più avanti, promessa mantenuta in un altra sezione)?',
        '3. La proposta peggiorerebbe il testo, introdurrebbe fatti nuovi o romperebbe la voce del libro?',
        'Se hai dubbi, smontata = true. Indica la gravità che ritieni corretta e il motivo in 1-2 frasi.',
        'Non modificare nessun file.',
      ].join('\n'),
      { label: 'verifica:' + f.sigla + ':' + (i + 1) + '.' + (k + 1), phase: 'Verifica', schema: VERDICT_SCHEMA, effort: 'medium' }
    ))).then(voti => {
      const v = voti.filter(Boolean)
      const trovata = v.length > 0 && v.every(x => x.citazione_trovata)
      const regge = v.filter(x => !x.smontata).length
      const confermata = trovata && (n === 3 ? regge >= 2 : regge === 1)
      const gravita = confermata ? (v.find(x => !x.smontata) || v[0]).gravita_corretta : s.gravita
      return { s: Object.assign({}, s, { gravita: gravita }), confermata: confermata, motivi: v.map(x => x.motivo) }
    })
  })).then(giudizi => {
    const g = giudizi.filter(Boolean)
    return {
      confermate: g.filter(x => x.confermata).map(x => x.s),
      scartate: g.filter(x => !x.confermata).map(x => ({ controllo: x.s.controllo, sezione: x.s.sezione, motivi: x.motivi })),
    }
  }),

  // Incrocio con il report di frase di Haiku
  (ver, f) => agent(
    [
      'Leggi reports/leggibilita/' + f.sigla + '_leggibilita.md: contiene gli interventi di frase numerati [01], [02], ... sul file capitoli/' + f.file + '.',
      'Queste sono le segnalazioni di STRUTTURA confermate sullo stesso file:',
      JSON.stringify(ver.confermate),
      'Leggi il glossario proposto in ' + GLOSSARIO_FILE + ': per ogni termine tecnico indica la parola scelta e le varianti da eliminare. Se il file manca, segnalalo nel motivo di ogni intervento e non usare lo stato "correggere" per i sinonimi.',
      'Per OGNI intervento di frase decidi lo stato:',
      '- "sospendere": il paragrafo in cui si trova verrebbe tagliato, spostato o riscritto da una segnalazione di struttura. Correggere la frase adesso sarebbe lavoro sprecato.',
      '- "correggere": la proposta di Haiku alterna sinonimi di un termine tecnico del glossario, oppure contraddice una segnalazione di struttura. Scrivi in "correzione" la proposta corretta, che usa il termine scelto.',
      '- "tenere": tutto il resto. In questo caso "correzione" è una stringa vuota.',
      'Indica il motivo in una frase. Non modificare nessun file.',
    ].join('\n\n'),
    { label: 'incrocio:' + f.sigla, phase: 'Incrocio', schema: MAPPING_SCHEMA, effort: 'medium' }
  ).then(m => ({ ver: ver, mappa: m ? m.interventi : [] })),

  // Report per file
  (dati, f) => agent(
    [
      'Scrivi il file reports/struttura/' + f.sigla + '_struttura.md, in italiano semplice, per un autore che non è un programmatore. Data: ' + DATA + '.',
      'File analizzato: capitoli/' + f.file + ' (' + f.genere + ').',
      'Segnalazioni confermate dai verificatori: ' + JSON.stringify(dati.ver.confermate),
      'Segnalazioni scartate dai verificatori: ' + JSON.stringify(dati.ver.scartate),
      'Stato degli interventi di frase di Haiku: ' + JSON.stringify(dati.mappa),
      'STRUTTURA DEL FILE:',
      '# Struttura e tenuta del lettore — ' + f.file,
      '## Sintesi: 4-6 righe con il giudizio complessivo, il numero di segnalazioni (ALTA, MEDIA, BASSA) e la cosa più importante da fare.',
      '## Curva della tensione: i punti della curva descritti dalla lente architettura, se ci sono.',
      '## Interventi di struttura: ordinati da ALTA a BASSA. Per ognuno: numero [S01] e così via, gravità, lente, evidenza (solida, moderata o mestiere), sezione, citazione in blocco >, problema, intervento proposto.',
      '## Registro delle promesse e delle domande aperte: tabella con promessa o domanda | dove si apre | dove si chiude (oppure "MAI").',
      '## Interventi di frase di Haiku: tre elenchi (da tenere, da sospendere, da correggere) con numero e motivo. Per quelli da correggere scrivi anche la nuova proposta.',
      '## Ordine di lavoro consigliato: prima gli interventi di struttura ALTA, poi gli interventi di frase da tenere e da correggere, poi il resto.',
      '## Scartate dai verificatori: numero e una riga per ciascuna.',
      'Non modificare nessun file in capitoli/. Restituisci come testo finale 3 righe: percorso del file, numero di segnalazioni confermate per gravità, numero di interventi Haiku da tenere, sospendere e correggere.',
    ].join('\n\n'),
    { label: 'report:' + f.sigla, phase: 'Report', effort: 'medium' }
  ).then(txt => ({
    sigla: f.sigla,
    confermate: dati.ver.confermate.length,
    alta: dati.ver.confermate.filter(s => s.gravita === 'ALTA').length,
    media: dati.ver.confermate.filter(s => s.gravita === 'MEDIA').length,
    bassa: dati.ver.confermate.filter(s => s.gravita === 'BASSA').length,
    scartate: dati.ver.scartate.length,
    tenere: dati.mappa.filter(m => m.stato === 'tenere').length,
    sospendere: dati.mappa.filter(m => m.stato === 'sospendere').length,
    correggere: dati.mappa.filter(m => m.stato === 'correggere').length,
    sintesi: txt,
  }))
)

const fatti = risultati.filter(Boolean)
const mancanti = SELEZIONE.filter(f => !fatti.find(r => r.sigla === f.sigla)).map(f => f.sigla)
if (mancanti.length) log('ATTENZIONE: file non completati in questo lotto: ' + mancanti.join(', '))

return {
  lotto: 'capitoli',
  file_completati: fatti.map(r => r.sigla),
  mancanti: mancanti,
  per_file: fatti.map(r => ({
    sigla: r.sigla, alta: r.alta, media: r.media, bassa: r.bassa, scartate: r.scartate,
    haiku_tenere: r.tenere, haiku_sospendere: r.sospendere, haiku_correggere: r.correggere,
  })),
}
}

// ---------- LOTTO indice: legge dal disco i report di tutti i lotti ----------
phase('Report')
const indice = await agent(
  [
    'Scrivi reports/struttura/00_INDICE_STRUTTURA.md in italiano semplice. Data: ' + DATA + '.',
    'Leggi tutti i report in reports/struttura/ con nome SIGLA_struttura.md (le sigle attese sono: ' + FILES.map(f => f.sigla).join(', ') + ') e il file ' + GLOSSARIO_FILE + '.',
    'Se manca il report di qualche sigla, elencala in cima in grassetto come "lotto non ancora eseguito" e prosegui con gli altri.',
    'Ricava i numeri contando le voci nei report: interventi di struttura per gravità [S01], [S02] e così via; scartate dai verificatori; interventi Haiku da tenere, sospendere e correggere.',
    'CONTENUTO:',
    '## Quadro generale: tabella con file | ALTA | MEDIA | BASSA | scartate | Haiku da tenere / sospendere / correggere | link al report.',
    '## Classifica di priorità: ordina prima per numero di ALTA, poi per totale. Prefazione ed Epilogo sono già i file più difficili a livello di frase (Gulpease 43 e 44): a parità di gravità strutturale vanno per primi.',
    '## Problemi ricorrenti di struttura: quelli che tornano in 3 o più file, con dove compaiono e una regola pratica per ciascuno.',
    '## Promesse non mantenute in tutto il libro: un elenco unico.',
    '## Le 10 correzioni di struttura più urgenti del libro.',
    '## Prossimi passi: 1) l autore approva il glossario; 2) applica gli interventi di struttura ALTA; 3) applica gli interventi di frase da tenere e da correggere; 4) rilancia la revisione di frase solo sui paragrafi riscritti.',
    'Non modificare nessun file in capitoli/. Restituisci come testo finale 5 righe di sintesi.',
  ].join('\n\n'),
  { label: 'indice', phase: 'Report' }
)
return { lotto: 'indice', sintesi: indice }
```

---

LOTTO: glossario + capitoli CAP01 CAP02 CAP03

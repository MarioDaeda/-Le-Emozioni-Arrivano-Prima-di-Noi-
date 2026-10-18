# PROMPT — Test di struttura a basso consumo, CAP01–CAP03 (Sonnet 5.5, ultracode)

> **Come lanciarlo.** Apri una sessione **nuova** di Claude Code nella cartella `Libro Emozioni`. Scegli il modello **Sonnet 5.5** con effort **medio**. Incolla tutto ciò che sta sotto la linea, a partire dalla parola **ultracode**.
>
> **Cosa cambia rispetto al prompt completo** (`prompt/revisione/PROMPT_REVISIONE_STRUTTURA_SONNET_ULTRACODE.md`):
> 1. **Verifica a gruppi.** Uno scettico per ogni lente controlla tutte le segnalazioni di quella lente in una sola lettura del capitolo. Un secondo scettico riguarda solo le segnalazioni ALTA.
> 2. **Gli agenti non rileggono il report di ricerca.** I criteri sono già scritti nel prompt di ogni lente.
> 3. **Haiku fa i passaggi meccanici.** Glossario, incrocio con gli interventi di Haiku e scrittura dei report. Sonnet resta su lenti e verifica.
> 4. **Glossario sui soli 3 capitoli.** È parziale e verrà rifatto quando lancerai il libro intero.
> 5. **Massimo 8 segnalazioni per lente.**
>
> **Correzioni dopo il primo test (18 ottobre 2026):**
> - gli agenti non scrivono file: restituiscono il testo, e lo salva la sessione principale (Haiku si rifiutava di creare i file `.md`);
> - niente ripresa per rigenerare un singolo report (la ripresa aveva rifatto tutte le fasi);
> - il secondo verificatore non è più spinto a declassare le ALTA a MEDIA;
> - le lenti non propongono contenuti inventati e non hanno una quota fissa di ALTA.
>
> In tutto sono circa **25 agenti**, contro i 110 circa del prompt completo. **Nessun file in `capitoli/` viene modificato.**

---

ultracode

## Compito

Esegui con lo strumento **Workflow** lo script qui sotto, così com'è, con `args` = `{"data": "<data di oggi in formato AAAA-MM-GG>"}`. Non riscrivere lo script e non cambiare modelli o effort degli agenti.

**Gli agenti non scrivono file.** Il workflow restituisce il testo del glossario in `glossario_md` e quello di ogni report in `completati[i].markdown`. Sei tu, nella sessione principale, a salvarli con lo strumento Write, esattamente come arrivano, nei percorsi indicati in `percorso`. L'utente chiede espressamente questi file.

**Ripresa.** Usa `resumeFromRunId` solo se il workflow si interrompe prima di finire. Non usarlo mai per rigenerare un singolo report: la ripresa può rifare tutte le fasi e cambiare i numeri. Se un report manca o è vuoto, scrivilo tu dai dati del journal del workflow (il file `journal.jsonl` indicato nella notifica di fine), senza lanciare altri agenti.

Alla fine:
1. Controlla con `git status --short capitoli/` che nessun capitolo sia stato modificato. I file che iniziano con `._` sono metadati di macOS e vanno ignorati.
2. Controlla che esistano questi file in `reports/struttura/`:
   - `GLOSSARIO_PROPOSTO_CAP01-03.md`
   - `CAP01_struttura.md`
   - `CAP02_struttura.md`
   - `CAP03_struttura.md`
3. Rispondi in chat con al massimo 8 righe:
   - le segnalazioni confermate e quelle scartate, per capitolo;
   - gli interventi di Haiku da tenere, da sospendere e da correggere;
   - i percorsi dei file.

## Script

```javascript
export const meta = {
  name: 'struttura-test-risparmio-cap01-03',
  description: 'Test di struttura a basso consumo su CAP01-CAP03: glossario parziale, 3 lenti, verifica a gruppi, incrocio con i report di frase',
  phases: [
    { title: 'Glossario', detail: 'un agente Haiku sui 3 capitoli', model: 'haiku' },
    { title: 'Lenti', detail: '3 lenti di struttura per capitolo' },
    { title: 'Verifica', detail: 'uno scettico per lente, piu uno sulle ALTA' },
    { title: 'Report', detail: 'incrocio e report con Haiku', model: 'haiku' },
  ],
}

const FILES = [
  { sigla: 'CAP01', file: 'CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md' },
  { sigla: 'CAP02', file: 'CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md' },
  { sigla: 'CAP03', file: 'CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md' },
]
const DATA = (args && args.data) ? args.data : 'data non indicata'
const GLOSSARIO_FILE = 'reports/struttura/GLOSSARIO_PROPOSTO_CAP01-03.md'
const MAX_PER_LENTE = 8

const REGOLE = [
  'REGOLE:',
  '- Non modificare MAI nessun file in capitoli/. Leggi soltanto.',
  '- Il lettore è un manager o imprenditore di PMI: colto, non specialista, legge la sera ed è stanco.',
  '- Le citazioni devono essere copiate ESATTAMENTE dal capitolo, da 8 a 30 parole.',
  '- Leggi il capitolo una volta sola, per intero. Non leggere altri file se non è richiesto.',
].join('\n')

// ---------- Schemi ----------
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

const MD_SCHEMA = {
  type: 'object',
  properties: { markdown: { type: 'string' } },
  required: ['markdown'],
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

// ---------- Lenti ----------
const LENTI = [
  {
    chiave: 'curiosita',
    titolo: 'Curiosità, domande aperte e promesse',
    criteri: [
      '1. DOMANDA PRIMA DELLA SPIEGAZIONE: ogni spiegazione scientifica o concettuale è preceduta da una domanda concreta del lettore o di un personaggio (un vuoto specifico e colmabile, Loewenstein 1994; evidenza solida)?',
      '2. DOMANDE CHIUSE: ogni domanda aperta riceve risposta entro il capitolo o in un punto dichiarato? Segnala i cicli aperti abbandonati.',
      '3. PROMESSE: ogni "come vedremo", "più avanti", "nel prossimo capitolo" viene mantenuto? Compila il campo "promesse", indicando dove ognuna si chiude oppure "MAI".',
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
      '4. DETTAGLI SEDUCENTI: aneddoti, dati o descrizioni interessanti che non portano il concetto, il personaggio o la trama (Rey 2012; Sundararajan & Adesope 2020; evidenza solida). Proponi di tagliarli o di legarli al concetto.',
      '5. DUE CASI PER PRINCIPIO: i principi chiave sono mostrati con almeno due casi da confrontare (Gentner, Loewenstein & Thompson 2003)?',
      '6. ASTRATTO SENZA CONCRETO: concetti chiave che restano astratti per l intera sezione.',
    ].join('\n'),
  },
  {
    chiave: 'architettura',
    titolo: 'Aperture, chiusure, stacchi, tensione, strumenti, ripasso',
    criteri: [
      '1. APERTURA: le prime 5-8 righe mettono un personaggio in azione, o pongono un problema concreto? (regola di mestiere)',
      '2. CHIUSURA: il capitolo chiude con un gancio leggero in avanti e con il punto chiaro? Non serve un cliffhanger forte (Wirz et al. 2023).',
      '3. STACCHI DI SEZIONE: la sezione successiva riparte con un motivo per continuare? Il lettore capisce subito dove e quando si trova e chi parla?',
      '4. CURVA DELLA TENSIONE: compila il campo "curva_tensione" con 4-6 punti. Segnala i tratti lunghi senza tensione né domanda.',
      '5. MOSTRARE PRIMA DI NOMINARE: le emozioni sono mostrate con corpo, gesti e azioni prima di essere nominate o spiegate?',
      '6. STRUMENTO AZIONABILE: lo strumento pratico del capitolo è mostrato mentre un personaggio lo usa, ed è abbastanza preciso da poterlo applicare lunedì mattina?',
      '7. RIPASSO E RICHIAMI: ci sono domande di richiamo a fine capitolo, o richiami ai capitoli precedenti? Indica dove aggiungerli (Dunlosky et al. 2013; evidenza solida).',
    ].join('\n'),
  },
]

const GRAVITA = [
  'GRAVITÀ: ALTA = probabile punto di abbandono, oppure il concetto chiave non arriva. MEDIA = la lettura rallenta o la tensione cala. BASSA = migliorabile.',
  'Massimo ' + MAX_PER_LENTE + ' segnalazioni, le più gravi. Non devi arrivare al massimo: segnala solo problemi reali. Non c è un numero atteso di ALTA, possono essere zero o molte. In "scartate" indica quante altre ne hai lasciato fuori.',
  'PROPOSTE: preferisci spostare, tagliare, unire o riformulare ciò che c è già. Non proporre scene, personaggi, battute, casi o fatti nuovi. Se l unico rimedio è aggiungere materiale nuovo, scrivilo come domanda per l autore ("Serve un secondo caso qui?") e non scrivere il testo.',
  'Prima di segnalare, controlla che il testo non risolva già il problema poco prima o poco dopo: una domanda già posta, un ritorno alla scena, una promessa mantenuta altrove.',
  'Compila i campi "curva_tensione" e "promesse" solo se i tuoi criteri li chiedono; altrimenti lasciali vuoti.',
].join('\n')

// ---------- Glossario parziale: un solo agente Haiku ----------
phase('Glossario')
const glossarioOut = await agent(
  [
    'Leggi per intero questi 3 file: ' + FILES.map(f => 'capitoli/' + f.file).join(', ') + '.',
    'Prepara in Markdown, in italiano semplice, il contenuto del file ' + GLOSSARIO_FILE + '. NON scrivere file: restituisci il testo nel campo "markdown", e lo salverà la sessione principale. In cima metti in grassetto: "BOZZA PARZIALE (solo CAP01-CAP03): da rifare sul libro intero e da far approvare all autore".',
    'Contenuto:',
    '1. Tabella dei termini tecnici (psicologia, neuroscienze, finanza, gestione): termine scelto | varianti o sinonimi usati per lo stesso concetto, da eliminare | definizione proposta di una riga, concreta | prima comparsa (capitolo e sezione) | definito bene alla prima comparsa? (sì/no) | occorrenze.',
    '2. Tabella delle parole vaghe usate spesso ("sistemico", "relazionale" e simili): parola | occorrenze per capitolo | alternative concrete.',
    'Regola: per i termini TECNICI si usa sempre la stessa parola in tutto il libro, senza alternare sinonimi. Le parole VAGHE si riducono.',
    'Al massimo 30 termini tecnici e 15 parole vaghe.',
    '- Non modificare nessun file in capitoli/.',
  ].join('\n\n'),
  { label: 'glossario', phase: 'Glossario', model: 'haiku', effort: 'medium', schema: MD_SCHEMA }
)
const glossarioMd = glossarioOut ? glossarioOut.markdown : ''
if (!glossarioMd) log('ATTENZIONE: glossario vuoto')

// ---------- Pipeline per capitolo ----------
const risultati = await pipeline(
  FILES,

  // Lenti (Sonnet): 3 letture indipendenti
  (f) => parallel(LENTI.map(l => () => agent(
    [
      'Sei un editor di sviluppo per la saggistica narrativa italiana. Analizzi la STRUTTURA di capitoli/' + f.file + '.',
      'Lente: ' + l.titolo + '. Non segnalare frasi lunghe o parole difficili: le ha già controllate un altra revisione.',
      'CRITERI:\n' + l.criteri,
      GRAVITA,
      'Per ogni segnalazione dai: il controllo (numero e nome del criterio), la sezione (il titolo più vicino), una citazione esatta che indichi il punto, il problema in 1-2 frasi, il tipo di intervento e una proposta concreta (che cosa spostare, tagliare o aggiungere, e dove). Non inventare fatti, cifre o nomi.',
      REGOLE,
    ].join('\n\n'),
    { label: l.chiave + ':' + f.sigla, phase: 'Lenti', schema: FINDINGS_SCHEMA }
  ).then(r => r ? Object.assign({ lente: l.chiave }, r) : null))),

  // Verifica a gruppi (Sonnet): uno scettico per lente, poi uno solo sulle ALTA
  (lenti, f) => {
    const valide = lenti.filter(Boolean)
    const curva = (valide.find(x => x.lente === 'architettura') || {}).curva_tensione || []
    const promesse = (valide.find(x => x.lente === 'curiosita') || {}).promesse || []
    return parallel(valide.filter(x => x.segnalazioni.length).map(x => () => agent(
      [
        'Sei un verificatore scettico. Prova a SMONTARE ognuna di queste segnalazioni di struttura sul file capitoli/' + f.file + ' (lente: ' + x.lente + ').',
        'Segnalazioni, numerate da 0:\n' + x.segnalazioni.map((s, i) => i + ') ' + JSON.stringify(s)).join('\n'),
        'Per ciascuna:',
        '1. Cerca la citazione con grep -F nel file. Se non c è parola per parola, citazione_trovata = false.',
        '2. Il problema è reale per un manager di PMI che legge la sera? Oppure il testo lo risolve poco prima o poco dopo (domanda già posta, ritorno alla scena, promessa mantenuta altrove)?',
        '3. La proposta peggiorerebbe il testo o inventerebbe fatti nuovi?',
        'Se hai dubbi, smontata = true. Restituisci un verdetto per ogni indice, con la gravità che ritieni corretta e il motivo in una frase.',
        REGOLE,
      ].join('\n\n'),
      { label: 'verifica:' + f.sigla + ':' + x.lente, phase: 'Verifica', schema: VERDICTS_SCHEMA, effort: 'medium' }
    ).then(v => {
      const verd = v ? v.verdetti : []
      return x.segnalazioni.map((s, i) => {
        const d = verd.find(z => z.indice === i)
        const ok = !!d && d.citazione_trovata && !d.smontata
        return { s: Object.assign({ lente: x.lente }, s, { gravita: ok ? d.gravita_corretta : s.gravita }), ok: ok, motivo: d ? d.motivo : 'nessun verdetto' }
      })
    }))).then(gruppi => {
      const tutte = gruppi.filter(Boolean).flat()
      return { tutte: tutte, curva: curva, promesse: promesse }
    })
  },

  // Secondo scettico solo sulle ALTA sopravvissute
  (ver, f) => {
    const alte = ver.tutte.filter(x => x.ok && x.s.gravita === 'ALTA')
    if (!alte.length) return Object.assign({}, ver, { secondo: 'nessuna ALTA da ricontrollare' })
    return agent(
      [
        'Sei un secondo verificatore scettico, indipendente dal primo. Queste segnalazioni di gravità ALTA sul file capitoli/' + f.file + ' sono state confermate una volta. Prova a smontarle, oppure a dimostrare che la gravità corretta è MEDIA.',
        'Segnalazioni, numerate da 0:\n' + alte.map((x, i) => i + ') ' + JSON.stringify(x.s)).join('\n'),
        'Giudica la gravità in modo neutrale, con le definizioni date: ALTA = probabile punto di abbandono, oppure il concetto chiave del capitolo non arriva; MEDIA = la lettura rallenta o la tensione cala. Mantieni ALTA se il criterio è soddisfatto, declassa solo se non lo è. Restituisci un verdetto per ogni indice.',
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
      return Object.assign({}, ver, { secondo: 'ricontrollate ' + alte.length + ' ALTA' })
    })
  },

  // Incrocio + report (Haiku), in un solo agente
  (ver, f) => {
    const conf = ver.tutte.filter(x => x.ok).map(x => x.s)
    const scart = ver.tutte.filter(x => !x.ok).map(x => ({ controllo: x.s.controllo, sezione: x.s.sezione, motivo: x.motivo }))
    return agent(
      [
        'Prepara in Markdown il contenuto del report reports/struttura/' + f.sigla + '_struttura.md, in italiano semplice, per un autore che non è un programmatore. Data: ' + DATA + '.',
        'NON scrivere file: restituisci il testo completo nel campo "markdown", e lo salverà la sessione principale. Nei campi tenere, sospendere e correggere metti i conteggi degli interventi di Haiku.',
        'Leggi SOLO il file reports/leggibilita/' + f.sigla + '_leggibilita.md (interventi di frase numerati [01], [02] e così via). Non rileggere il capitolo.',
        'Glossario proposto (termine scelto e varianti da eliminare):\n' + (glossarioMd || '(glossario non disponibile: non usare lo stato "da correggere" per i sinonimi)'),
        'Segnalazioni di struttura confermate: ' + JSON.stringify(conf),
        'Scartate dai verificatori: ' + JSON.stringify(scart),
        'Curva della tensione: ' + JSON.stringify(ver.curva),
        'Promesse e domande aperte: ' + JSON.stringify(ver.promesse),
        'Per OGNI intervento di frase del report di Haiku decidi lo stato:',
        '- "da sospendere": il suo paragrafo verrebbe tagliato, spostato o riscritto da una segnalazione di struttura (confronta sezione e citazione).',
        '- "da correggere": la proposta alterna sinonimi di un termine tecnico del glossario, o contraddice una segnalazione di struttura. Scrivi la proposta corretta.',
        '- "da tenere": tutto il resto.',
        'STRUTTURA DEL FILE:',
        '# Struttura e tenuta del lettore — ' + f.file,
        '## Sintesi: 4-6 righe con il giudizio, i numeri (ALTA, MEDIA, BASSA, scartate) e la cosa più importante da fare.',
        '## Curva della tensione',
        '## Interventi di struttura: da ALTA a BASSA; per ognuno [S01] e così via, gravità, lente, evidenza, sezione, citazione in blocco >, problema, intervento proposto.',
        '## Registro delle promesse e delle domande aperte: tabella con promessa | dove si apre | dove si chiude (oppure MAI).',
        '## Interventi di frase di Haiku: tre elenchi (da tenere, da sospendere, da correggere) con numero e motivo in una riga; per quelli da correggere, la nuova proposta.',
        '## Ordine di lavoro consigliato',
        '## Scartate dai verificatori: una riga ciascuna.',
        'Non modificare nessun file.',
      ].join('\n\n'),
      { label: 'report:' + f.sigla, phase: 'Report', model: 'haiku', effort: 'medium', schema: REPORT_SCHEMA }
    ).then(rep => ({
      sigla: f.sigla,
      alta: conf.filter(s => s.gravita === 'ALTA').length,
      media: conf.filter(s => s.gravita === 'MEDIA').length,
      bassa: conf.filter(s => s.gravita === 'BASSA').length,
      scartate: scart.length,
      percorso: 'reports/struttura/' + f.sigla + '_struttura.md',
      markdown: rep ? rep.markdown : '',
      haiku: rep ? { tenere: rep.tenere, sospendere: rep.sospendere, correggere: rep.correggere } : null,
    }))
  }
)

const fatti = risultati.filter(Boolean)
const mancanti = FILES.filter(f => !fatti.find(r => r.sigla === f.sigla)).map(f => f.sigla)
if (mancanti.length) log('ATTENZIONE: capitoli non completati: ' + mancanti.join(', '))
const vuoti = fatti.filter(r => !r.markdown).map(r => r.sigla)
if (vuoti.length) log('ATTENZIONE: report vuoti, da scrivere dal journal: ' + vuoti.join(', '))
return { glossario_percorso: GLOSSARIO_FILE, glossario_md: glossarioMd, completati: fatti, mancanti: mancanti, report_vuoti: vuoti }
```

---
name: editing-creativo-e-dialoghi
description: Framework integrato di editing letterario, developmental editing, subtext analysis, deep POV e verifica dell'autenticita dei dialoghi per narrativa industriale e saggi d'impresa.
---
# SKILLS.md — FRAMEWORK INTEGRATO DI EDITING LETTERARIO E REVISIONE DIALOGHI
## Raccolta Ufficiale delle Migliori Skills Open-Source da GitHub per la Revisione Narrativa
### Fonti Primarie: `danjdewhurst/story-skills` • `danielmiessler/fabric` • `Ckokoski/AuthorAgent`
**Applicazione:** Perplexity Pro (Claude 3.5 Sonnet / Claude 3.7 / Claude Opus) & Manoscritto *«Le Emozioni Arrivano Prima di Noi»*

---

> **ISTRUZIONE PER PERPLEXITY PRO / CLAUDE OPUS:**  
> Questo documento definisce le regole peritali, i criteri di scansione e i protocolli di editing che devi applicare durante l'analisi, il grilling e la riscrittura dei capitoli del libro *«Le Emozioni Arrivano Prima di Noi»*.  
> Non limitarti a commenti generici: applica rigorosamente i test tecnici (Tag-Swap Test, Filter Words Scan, Subtext Negotiation, Try/Fail Pressure, Beat Economy) riportati di seguito.

---

# PARTE 1: DIALOGUE, SUBTEXT & VOICE DIFFERENTIATION
*(Fonte originale GitHub: `danjdewhurst/story-skills/skills/scene-craft/references/dialogue-subtext.md`)*

### 1.1 Il Sottotesto come Input Strutturale (Subtext as Planning Input)
Il sottotesto è la distanza incolmabile tra ciò che viene detto a voce e ciò che ciascun personaggio desidera realmente. Prima di valutare qualsiasi conversazione, analizza per ciascun partecipante:
- **Said Want (Obiettivo Dichiarato):** ciò che il personaggio afferma di volere nella scena (l'alibi logico o professionale).
- **Hidden Want (Obiettivo Nascosto):** ciò che desidera realmente a livello emotivo, viscerale o identitario, ma che non oserebbe mai confessare apertamente (approvazione, sicurezza, vendetta, controllo, terrore del fallimento).
- **Why They Can't Say It (Il Motivo dell'Evasione):** orgoglio, paura della sanzione, perdita di leverage negoziale, vergogna. Questo motivo genera ogni singola esitazione, deviazione o sarcasmo.

> **Regola Aurea:** Quando l'obiettivo dichiarato coincide perfettamente con l'obiettivo nascosto, il dialogo è privo di sottotesto. Se un personaggio in officina o in riunione dice esattamente ciò che prova, la scena sta fallendo: o il personaggio mente, o deve schermarsi.

### 1.2 Il Dialogo come Negoziazione (Dialogue as Negotiation)
Ogni scambio verbale in azienda deve funzionare come una negoziazione sotto tensione, **mai come una sessione di Domanda & Risposta (Q&A)**. Ogni battuta deve compiere una di queste quattro azioni tattiche:
1. **Probe (Sondare):** testare l'interlocutore per estrarre informazioni, individuare debolezze o verificare le sue intenzioni.
2. **Parry (Parare/Deviare):** deviare una domanda scomoda senza rivelare nulla (rispondere con un'altra domanda, fare silenzio, cambiare argomento).
3. **Advance (Avanzare):** concedere un dato o un compromesso parziale solo per ottenere in cambio una leva più importante.
4. **Feint (Fingere):** fingere di cedere o acconsentire mentre in realtà si sta preparando una manovra difensiva o di contro-attacco.

> **Segnale d'Allarme:** Se i personaggi si alternano semplicemente a scambiarsi informazioni tecniche o pedagogiche per spiegarle al lettore, non è una conversazione: è un interrogatorio didascalico mascherato. Riscrivere immediatamente introducendo attrito.

### 1.3 La Ricetta di Differenziazione delle Voci (Voice Differentiation Recipe)
Ciascun personaggio deve possedere un'impronta vocale (*fingerprint*) basata su 4 componenti verificabili:
1. **Verbal Tic (Tic Verbale / Intercalare):** una parola ricorrente, un intercalare da officina o un avvio di frase tipico (usato con parsimonia, mai come caricatura).
2. **Preferenza Sintattica:** frasi secche e frammentate (operatori stanchi, tecnici pragmatici) vs periodi complessi ricchi di subordinate e subordinate ipotetiche (consulenti, venditori, manager che cercano di coprirsi).
3. **Argomento Rifugio sotto Stress:** quando viene messo alle strette, su cosa devia l'attenzione? (Silvano devia sulle ore mandrino e sui trucioli; Valerio sul codice fornitore; Sara sulla famiglia; Marco sulla chiusura del conto).
4. **Argomento Rifiutato:** cosa rifiuta categoricamente di discutere, e cosa fa quando viene toccato quel tasto? (ammutolisce, attacca, abbandona la stanza).

### 1.4 Il "Tag-Swap Test" (La Prova di Scambio delle Battute)
Rimuovi i nomi dei personaggi e i verbi di dialogo (*disse*, *rispose*). Prendi solo le battute nude. Se un lettore non è in grado di capire chi sta parlando basandosi unicamente sul ritmo, sul vocabolario e sulla postura sintattica, **le voci sono piatte e confuse**. Riscrivere differenziando il dominio lessicale (termini di fabbrica vs termini commerciali).

### 1.5 Beat Economy (Economia dei Gesti e delle Pause)
- Massimo **3 battute parlate consecutive** prima di inserire un'azione fisica (*beat*) o un ancoraggio sensoriale.
- L'azione fisica deve portare sottotesto (incrociare le braccia mentre si dice *"va tutto bene"*; far scorrere il calibro a vuoto mentre si ascolta un ordine assurdo).
- Negli scontri accesi: permettere interruzioni, frasi troncate e sovrapposizioni. Le persone che litigano in fabbrica o in riunione non aspettano il proprio turno con cortesia: **rispondono a ciò che hanno *creduto di sentire*, non alle parole esatte dell'altro**.

---

# PARTE 2: DEEP POV & DISTANZA PSICHICA
*(Fonte originale GitHub: `danjdewhurst/story-skills/skills/scene-craft/references/deep-pov.md`)*

### 2.1 Livelli di Distanza Psichica (Zoom Level)
1. **Osservatore Distante:** *"L'imprenditore sedeva al tavolo da due ore."* (esterno, asettico).
2. **Interiorità Lieve:** *"Andrea era stanco, e Luca non aveva ancora guardato il foglio."* (nome + interpretazione superficiale).
3. **Terza Persona Vicina (Close Third):** *"Andrea controllò l'orologio. Le dieci e diciassette. Luca non parlava. Ancora niente."* (la voce interiore inizia a contaminare il testo).
4. **Deep POV (Punto di Vista Profondo):** *"Le dieci e diciassette. Quel silenzio era una trappola. Quante volte ancora doveva rifare quei conti?"* (percezione pura senza alcun filtro narrativo).

### 2.2 Lista Nera dei "Filter Words" da Espungere
I verbi di percezione inseriscono un vetro trasparente ma freddo tra il lettore e il corpo del personaggio. Cerca e abbatti:
- *Sentì / Provò / Sentiva* (es. *«Sentì la rabbia salirgli»* $\rightarrow$ *«Il sangue gli pulsò contro i timpani»*)
- *Sapeva / Si rese conto / Realizzò* (es. *«Capì che il pezzo era rovinato»* $\rightarrow$ *«Il calibro slittò di tre centesimi. Il pezzo era da buttare»*)
- *Notò / Vide / Udì / Scorse* (es. *«Vide la spia rossa lampeggiare»* $\rightarrow$ *«La spia a colonna lampeggiava di rosso a centro banco»*)

### 2.3 Divieto dei "Thought-Tags"
I pensieri in corsivo con il tag esplicito (*«"Mi sta prendendo in giro", pensò tra sé»*) sono rotelle di supporto. Nel Deep POV il pensiero è narrazione diretta non mediata: *«Quel bastardo sapeva benissimo che le ore non bastavano»*.

### 2.4 Il Filtro Professionale della Percezione
La percezione deve essere filtrata dal **mestiere, dalla storia e dalle paure** del personaggio:
- Un capofficina con 40 anni di tornio nota l'odore di emulsione andata a male, il sibilo sordo di un cuscinetto idrostatico che cede, il calore della ghisa.
- Un commercialista nota le scadenze Ri.Ba., i decimali non allineati e le firme mancanti sui borderò.
- Un programmatore nota la latenza del terminale e i server in affanno.  
Due personaggi nella stessa stanza **non devono mai notare le stesse cose**.

---

# PARTE 3: LINE EDITING, PRECISIONE & RITMO
*(Fonte originale GitHub: `danjdewhurst/story-skills/skills/line-editing/references/line-edit-checklist.md`)*

### 3.1 Chiarezza & Causalità Sequenziale
- **Ordine Naturale Azione-Reazione:** Scrivi causa prima dell'effetto.  
  *Debole:* *«Sussultò quando il mandrino si arrestò con un fischio.»*  
  *Forte:* *«Il mandrino si arrestò con un fischio idraulico. Silvano sussultò.»*
- **Soggetti Sepolti:** Togli le costruzioni passive o ritardate (*«Fu la vista di quel foglio a scatenare la lite»* $\rightarrow$ *«Quel foglio scatenò la lite»*).

### 3.2 Precisione Materica (Concrete over General)
- Sostituisci il nome generico con il nome esatto: non *"il metallo"*, ma *«la barra trafilata in lega 7075»*; non *"la macchina"*, ma *«il centro di lavoro a 5 assi Mori Seiki»*; non *"il documento"*, ma *«la scheda di autocontrollo dimensionale non validata»*.
- **Verbo Forte vs Avverbio Pigro:** Un verbo forte vince sempre su un verbo debole accompagnato da avverbio (*«camminò pesantemente»* $\rightarrow$ *«inciampò» / «marciò» / «pesò ogni passo»*).

### 3.3 Economia della Frase (Anti-Clutter)
- **Cancellare i Movimenti Inutili (Stage Directions):** Tagliare i micro-gesti meccanici tra una battuta e l'altra che non aggiungono tensione (*«si alzò dalla sedia, fece due passi verso la finestra, si voltò indietro e parlò»*).
- **Cancellare il "Double Telling":** Non nominare l'emozione se il corpo o il gesto l'ha già descritta chiaramente (*«Strinse i pugni fino a farsi sanguinare i palmi, furiosa per l'ingiustizia subita»* $\rightarrow$ togliere *«furiosa per l'ingiustizia subita»*, il pugno che sanguina basta e avanza).

### 3.4 Tabella di Differenziazione Vocale per Ruolo Industriale

| Ruolo & Estrazione | Lunghezza Frasi | Dominio Lessicale | Reazione sotto Stress | Cosa Non Dirà Mai |
| :--- | :--- | :--- | :--- | :--- |
| **Capofficina (Silvano)** | Brevi, assertive, troncate | Tolleranze, avanzamento al dente, usura placchette, truciolo | Ringhia numeri mandrino, minaccia dimissioni | Non userà termini astratti (*«validazione emotiva»*) |
| **Tecnica Senior (Marta)** | Piane, dense, essenziali | Dilatazione termica, azzeramento sonda, badge operatore | Silenzio glaciale, shutdown metabolico, gesti lenti | Non supplicherà mai per ottenere comprensione |
| **Direttore Commerciale (Fabio)**| Lunghe, piene di slancio | Margine lordo, quote, budget, clienti tedeschi, partnership | Minimizza i problemi, fa battute, promette miracoli | Non ammetterà di aver sbagliato tempi ciclo |
| **Fondatore/CEO (Andrea)** | Incalzanti, interrogative | Liquidità, delibera, responsabilità storica, fiducia | Sequestra la parola, accusa di tradimento velato | Non dirà *"ho paura di non farcela da solo"* |
| **Ingegnere Gestionale (Enrico)** | Fluide, analitiche | Algoritmo Monte Carlo, waterfall, pivot dinamica, scenario | Mostra grafici, si rifugia nella formula algebrica | Non riconoscerà la nebbia sporca dei mancati pagamenti |

---

# PARTE 4: STRUTTURA DELLA SCENA, TRY/FAIL & RED-TEAMING
*(Fonti originali GitHub: `danjdewhurst/story-skills/skills/scene-craft/references/try-fail.md` & `danielmiessler/fabric/data/patterns/t_red_team_thinking`)*

### 4.1 I 4 Esiti della Scena (Scene Outcomes)
Ogni scena deve chiudersi con uno di questi quattro esiti rispetto allo scopo del protagonista:

| Esito (`outcome`) | Significato Drammaturgico | Effetto sulla Tensione |
| :--- | :--- | :--- |
| `YES` | Obiettivo raggiunto pulito | **Azzera la tensione** (usare solo a fine libro) |
| `NO` | Obiettivo bloccato da un rifiuto | Mantiene la pressione costante |
| `YES-BUT` | Obiettivo raggiunto, ma a caro prezzo o creando un nuovo guaio | **Complica la vicenda e alza la posta** |
| `NO-AND` | Obiettivo fallito e la situazione peggiora drasticamente | **Massimo picco di drammaturgia e pressione** |

> **Regola per l'Atto I e II:** Vietati gli esiti `YES`. Se il protagonista trova subito una soluzione comoda, il capitolo muore prima di iniziare. Il Cap. 2 usa magistralmente il `YES-BUT` (Sara congeda Davide ottenendo sollievo immediato, ma l'esito differito è un `NO-AND`: blocco mandrino alle 19:42).

### 4.2 Le 5 Tappe Obbligatorie della Scena (The Five Commandments)
1. **Inciting Incident (Innesco):** rottura dell'equilibrio (una mail della banca, una frase passivo-aggressiva in riunione, una commessa impossibile).
2. **Progressive Complications (Complicazioni Crescenti):** ogni tentativo di gestire l'innesco si scontra con vincoli materiali (la macchina è satura, la banca chiede perizie, il personale piange).
3. **Crisis (Crisi / Bivio Tragico):** il protagonista deve scegliere tra due opzioni entrambe dolorose (*Best Bad Choice*).
4. **Climax (Azione Decisiva):** la presa di posizione corporea o comportamentale.
5. **Resolution (Nuovo Stato):** ciò che è cambiato irrevocabilmente nelle relazioni e nel bilancio.

### 4.3 Adversarial Red-Teaming dell'Atto IV (Verifica della Conciliazione)
Interroga a freddo l'accordo dell'Atto IV come farebbe un revisore contabile o un sindacalista disilluso:
- *L'antagonista ha ceduto perché è stato "illuminato" da una predica morale o perché è stato inchiodato a un dato fisico irrefutabile?*
- *L'accordo protegge la faccia dei partecipanti o li costringe all'umiliazione pubblica? (Se li umilia, l'accordo salterà in 48 ore).*
- *Qual è il costo materiale dell'accordo? Chi paga le ore straordinarie? Chi si assume la responsabilità legale del ritardo?*

---

# PARTE 5: PATTERN DI EDITING AVANZATO FABRIC
*(Fonte originale GitHub: `danielmiessler/fabric/data/patterns/improve_writing`)*

### 5.1 Protocollo di Bonifica del Testo
Quando revisioni un paragrafo:
1. Elimina ogni traccia di voce passiva burocratica non necessaria.
2. Taglia le metafore banali o da seminario motivazionale (*«remare tutti nella stessa direzione»*, *«fare squadra»*, *«pensare fuori dagli schemi»*). Se un manager le usa nel dialogo, deve essere chiaro che gli altri personaggi lo percepiscono come un venditore di fumo.
3. Rispetta la cadenza biologica del respiro: dopo una riga concitata a battito alto, usa frasi corte di arresto somatico.

---

# PARTE 6: PROTOCOLLO DI ESECUZIONE SU PERPLEXITY PRO CON CLAUDE OPUS

Quando esegui l'audit di un capitolo con Claude Opus, utilizza questa matrice standard di output per restituire il referto all'autore:

```markdown
### 🔬 REFERTO FORENSE DI EDITING: [CAPITOLO XX]

#### 1. VOICE DIFFERENTIATION & TAG-SWAP AUDIT (Voto 1-10)
- **Punti di Forza:** [Battute perfettamente ancorate al mestiere e al corpo]
- **Battute Artificiali Rilevate:**
  > *«[Citazione riga originale]»*
  - **Diagnosi:** [Perché suona come un saggio didattico o una consulenza da aula]
  - **Riscrittura Ruvida:** *«[Nuova battuta recitabile e intrisa di sottotesto]»*

#### 2. SUBTEXT & FILTER WORDS SCAN
- [Elenco dei verbi di filtro eliminati e sostituiti con dettagli viscerali]
- [Verifica del disallineamento tra Said Want e Hidden Want]

#### 3. TRY/FAIL & RED-TEAMING ATTO IV
- **Esito Narrativo:** [YES-BUT / NO-AND]
- **Tenuta dell'Accordo di Processo:** [Analisi della tenuta lunedì mattina in officina/ufficio]
- **Clausola Materiale di Salvaguardia:** [Eventuale vincolo contrattuale mancante da inserire]
```

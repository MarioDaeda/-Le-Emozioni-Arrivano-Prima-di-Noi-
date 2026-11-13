# Formattazione, tipografia, ritmo della prosa e controlli di superficie per la leggibilità del libro, più come far eseguire questi controlli a un LLM in modo affidabile

Contesto: saggistica narrativa in italiano sulle emozioni in azienda; lettori: manager e imprenditori di PMI. Legenda sulla forza delle prove: **[FORTE]** = esperimenti replicati o rassegne peer-reviewed; **[MEDIA]** = singoli studi controllati, oppure documentazione autorevole di strumenti o fornitori; **[DEBOLE]** = convenzione di mestiere, opinione, fonti secondarie. Riferimenti segnati "(bibl.)" = DOI o URL ricavato da conoscenza bibliografica, non riaperto in questa sessione: va verificato prima di citarlo.

---

## A1. Lunghezza dei paragrafi (stampa e schermo; scansione e chunking)

### Takeaway
Non esiste una soglia empirica valida per i paragrafi di un libro stampato. Le indicazioni "3-4 frasi" vengono dalla scrittura per il web e dalle guide giornalistiche **[DEBOLE/MEDIA]**. La regola che regge davvero è "un'idea per paragrafo, con la frase d'apertura che la dichiara". Per un libro conviene fissare una soglia di allerta (da trattare come segnale, non come errore), ad esempio più di 180-200 parole o più di 12 righe stampate, e controllare anche le sequenze di paragrafi lunghi.

### Cited Findings
- Sulle pagine web l'utente tende a scansionare. La statistica spesso attribuita a NN/g, "79% scansiona, 16% legge riga per riga", circola solo di seconda mano e non l'ho verificata sull'originale — [Utah IT, chunking](https://websites.it.utah.edu/announcements/posts/2025/chunking.php)
- Pratiche di chunking riportate dalle sintesi NN/g: paragrafi brevi separati da spazio bianco e righe di circa 50-75 caratteri — [Ulster blog, sintesi NN/g](https://blogs.ulster.ac.uk/nicolepicton/2022/02/04/ixd303-chunking-research/)
- Linea guida web universitaria: un'idea principale per paragrafo, con la prima frase che la enuncia — [SJSU Writing for the Web](https://sjsu.edu/digital/standards/writing-for-the-web.php)
- Raccomandazione di guide terze (non di NN/g): al massimo 3-4 frasi brevi per paragrafo sul web — [digital.gov Content Corner](https://digital.gov/2016/04/11/the-content-corner-will-you-read-this-entire-post)
- Sottotitoli descrittivi e brevi, elenchi e immagini spezzano il testo lungo (sintesi SEO di ricerche Nielsen; fonte secondaria) — [AIOSEO](https://aioseo.com/?p=225327)
- ProWritingAid segnala i paragrafi "a ritmo lento" (introspezione, antefatto). Il rischio indicato non è il singolo paragrafo ma una sequenza: "Too many slower paced paragraphs in a row and your reader's attention may wane" — [ProWritingAid Pacing Check](https://prowritingaid.com/art/344/How-to-use----The-Pacing-Check.aspx)

### Inferences
- Le prove sul web riguardano il comportamento di scansione su schermo. La saggistica narrativa si legge in modo lineare, quindi il limite di 3-4 frasi non si trasferisce tale e quale. Sugli e-reader (colonna stretta, testo ingrandito) un paragrafo da 200 parole può occupare un'intera schermata. È un argomento in più per tenere una soglia di allerta.
- Criteri operativi proposti (calibrabili): segnalare i paragrafi oltre 200 parole come **informazione** e quelli oltre 300 come **da rivedere**. Segnalare poi più di tre paragrafi consecutivi oltre 150 parole senza dialogo né scena ("muro di testo"), e più di quattro paragrafi consecutivi di una sola frase, che producono un effetto da post LinkedIn e tolgono autorevolezza. Tutte le soglie sono euristiche di mestiere, non dati empirici.

### Gaps
- Non ho trovato l'articolo originale NN/g sul chunking (i risultati erano solo sintesi), né studi controllati sulla lunghezza dei paragrafi nei libri stampati.
- Non ho trovato guide giornalistiche italiane con soglie esplicite.

---

## A2. Titoli e sottotitoli (ricerca sul signaling)

### Takeaway
L'effetto dei segnali testuali (titoli, anteprime, riassunti) sul ricordo dell'organizzazione e dei temi è tra i più solidi in psicologia della lettura **[FORTE]**. Il beneficio è maggiore con argomenti poco familiari e con temi trattati brevemente. Per i manager di PMI, su cui la psicologia delle emozioni è terreno poco familiare, i sottotitoli dovrebbero aiutare.

### Cited Findings
- Rassegna di Lorch (1989), "Text-signaling devices and their effects on reading and memory processes", Educational Psychology Review 1:209-234: i segnali (titoli, anteprime, riassunti, enfasi tipografica) migliorano il ricordo delle informazioni segnalate e dell'organizzazione del testo — DOI (bibl.) [10.1007/BF01326639](https://doi.org/10.1007/BF01326639)
- Lorch & Lorch (1996): i titoli facilitano il ricordo degli argomenti **non familiari** ma non di quelli familiari. Nel riassunto aumentano l'inclusione di un tema solo quando è trattato brevemente — [UKY, Effects of headings on text recall and summarization](https://scholars.uky.edu/en/publications/effects-of-headings-on-text-recall-and-summarization/)
- Lorch, Lemarié & Chen (2013): con i titoli la memoria dei sottotemi è migliore. Per i fatti non c'è differenza tra titoli e frasi d'anteprima — [UKY, Signaling topic structure via headings or preview sentences](https://scholars.uky.edu/en/publications/signaling-topic-structure-via-headings-or-preview-sentences/)
- Lorch & Lorch (1985): con i segnali il ricordo libero complessivo migliora, e il beneficio è maggiore per chi ricorda meglio — [UKY, Effects of organizational signals on free recall](https://scholars.uky.edu/es/publications/effects-of-organizational-signals-on-free-recall-of-expository-te/)
- Studio su studenti universitari: i segnali modificano la strategia di codifica del lettore. Chi aveva i titoli e/o un addestramento ricordava meglio i temi e la loro organizzazione — [UKY, Effects on recall of signals to text organization](https://scholars.uky.edu/es/publications/effects-on-recall-of-signals-to-text-organization/)
- Lemarié, Lorch & Péry-Woodley (2012, Discours): quadro teorico dei titoli come segnali; i titoli migliorano la memoria dell'organizzazione — [DOAJ, Discours 2012](https://doaj.org/article/b268e54e7dcb49e7b7daa223464636d6)
- Hartley & Trueman (1982), "The effects of summaries on the recall of information from prose: five experimental studies", Human Learning 1:63-82. I risultati non sono stati recuperati in questa sessione; c'è solo il riferimento — [Springer, voce bibliografica citante](https://link.springer.com/article/10.1007/BF03186769)
- Studio con 194 studenti: un riassunto prima del testo, sia a elenco sia a panoramica, aumenta il ricordo, soprattutto delle parti finali del racconto — [Springer BF03186769](https://link.springer.com/article/10.1007/BF03186769)

### Inferences
- La frequenza dei sottotitoli nella saggistica narrativa non ha basi empiriche. Una prassi ragionevole è un sottotitolo ogni 1.500-3.000 parole (circa 6-12 pagine), ai cambi di tema o di atto, coerente con la struttura per atti del progetto. Sottotitoli più fitti rompono l'immersione narrativa.
- I sottotitoli devono essere descrittivi o evocativi ma interpretabili. Poiché il beneficio è massimo sui temi brevi e poco familiari, dove compare un concetto scientifico nuovo (es. interocezione, ipotesi del marcatore somatico) conviene un sottotitolo o una frase d'anteprima esplicita.
- Controllo LLM: verificare che ogni sottotitolo predica correttamente il contenuto della sezione (accordo tra titolo e contenuto), più un conteggio deterministico delle parole tra sottotitoli.

### Gaps
- Non ho trovato una meta-analisi formale sul signaling. Si può valutare la letteratura multimedia (Mayer, "signaling principle"), fuori dal mio perimetro.
- Non ho trovato studi specifici sui titoli nella saggistica narrativa rispetto ai testi espositivi scolastici: quasi tutti gli esperimenti usano testi espositivi brevi e studenti.

---

## A3. Spazio bianco, lunghezza della riga, tipografia, elenchi contro prosa, grassetto e corsivo

### Takeaway
Su schermo le righe lunghe (circa 100 caratteri) si leggono più in fretta, ma i lettori preferiscono righe di 45-72 caratteri, con circa 55 percepito come il più comodo. La comprensione resta costante **[MEDIA-FORTE]**. Sui corpi testo per il web, leggibilità e comprensione crescono fino a circa 18 pt **[MEDIA]**. Gli elenchi migliorano il ricordo ma, nell'unico studio controllato trovato, non la persuasione **[DEBOLE-MEDIA]**.

### Cited Findings
- Dyson & Kipping (1998): righe da 100 caratteri lette più velocemente di quelle da 25, a comprensione costante. Le righe lunghe sono giudicate le meno facili, quelle moderate (55 cpl) le più facili, e il giudizio soggettivo non correla con la prestazione — [Visible Language, Dyson & Kipping](https://journals.uc.edu/index.php/vl/article/view/5671)
- Rassegna Dyson (2004), Behaviour & Information Technology: la variabile critica è il numero di caratteri per riga. Si legge più veloce a circa 100 cpl, si preferisce 45-72 cpl, e i risultati non sono del tutto coerenti tra studi per differenze di compito e misure — [PDF Dyson 2004](https://stu.westga.edu/~ssynan1/literacy/Dyson.pdf); DOI (bibl.) [10.1080/01449290410001715714](https://doi.org/10.1080/01449290410001715714); sintesi: [Human Factors International](https://humanfactors.com/newsletters/optimal_line_length.html); [Weinschenk, 100 Things #18](https://oreilly.com/library/view/100-things-every/9780132658638/ch18.html)
- Rello, Pielot & Marcos (2016), "Make It Big!", CHI 2016, pp. 3637-3648: 104 partecipanti, eye tracking, corpi da 10 a 26 pt, interlinea da 0,8 a 1,4. Leggibilità soggettiva e oggettiva e comprensione migliorano fino a 18 pt. Interlinea troppo stretta o troppo larga peggiora la comprensione — [DBLP Rello](https://dblp.uni-trier.de/pid/60/4144.html); sintesi: [BYU Editing Research](https://editingresearch.byu.edu/?p=10398); DOI (bibl.) [10.1145/2858036.2858204](https://doi.org/10.1145/2858036.2858204)
- Lavoro di Rello sui lettori con dislessia: 18 pt ottimale; font sans serif e monospaziati migliori dei corsivi — [UPF repository, How to present more readable text for people with dyslexia](https://repositori.upf.edu/items/e0ca6f40-a0fa-490f-9d03-53d043270deb/full)
- Elenchi contro prosa: in uno studio online (N=123, tesi Radboud) elenchi numerati o puntati migliorano il ricordo rispetto al paragrafo, ma non la persuasione percepita. Numerato e puntato si equivalgono — [Radboud thesis](https://theses.ubn.ru.nl/items/8e131990-9803-42de-a737-7e7e73362c7f)
- Opinione: gli elenchi eliminano i connettivi logici ("perché", "ma") e possono lasciare il lettore senza i nessi — [Writing Skills](https://www.writing-skills.com/?p=4534) **[DEBOLE]**
- L'enfasi tipografica (grassetto, corsivo) è un tipo di segnale incluso nella rassegna di Lorch (1989): favorisce il ricordo dell'informazione segnalata — DOI (bibl.) [10.1007/BF01326639](https://doi.org/10.1007/BF01326639)

### Inferences
- In un libro stampato la lunghezza della riga è una decisione dell'impaginatore. I formati tipici della saggistica italiana (14x21 o 15x23 cm, corpo 10,5-12 pt) danno di solito circa 60-75 cpl, nella fascia preferita. Negli e-book la riga dipende dal lettore. Il testo quindi non deve contare su effetti di impaginazione: niente "come si vede nella colonna a destra".
- Grassetto e corsivo: l'enfasi segnala solo se è rara. Se tutto è evidenziato, niente lo è (inferenza dalla logica del signaling, non quantificata). Criterio proposto: in prosa narrativa il grassetto va riservato a box e titoli. Corsivo per parole straniere non acclimatate, titoli di opere ed enfasi occasionale (indicativamente al massimo una enfasi ogni 300-500 parole).
- Elenchi: la saggistica narrativa dovrebbe tenerli fuori dal corpo narrativo e confinarli in box o riepiloghi di fine capitolo, dove il ricordo conta più della persuasione.

### Gaps
- Gli studi su lunghezza della riga e corpo riguardano lo schermo (Dyson) o il web (Rello). Non ho trovato studi recenti equivalenti sulla stampa.
- Non ho trovato studi quantitativi sull'uso eccessivo del grassetto.

---

## A4. Variazione della lunghezza delle frasi e ritmo (burstiness, Provost, paratassi contro ipotassi)

### Takeaway
L'idea di variare la lunghezza delle frasi è un consiglio di mestiere diffuso (il passo di Gary Provost), non un risultato sperimentale. Non ho trovato prove peer-reviewed dirette sulla preferenza dei lettori per la varianza **[DEBOLE]**. "Burstiness" è soprattutto un termine del rilevamento dei testi generati da IA. È però misurabile in modo deterministico (deviazione standard e coefficiente di variazione delle lunghezze di frase) ed è un utile segnale contro la prosa monotona tipica degli LLM.

### Cited Findings
- Studio di psicofisica (PLOS ONE 2023, "Omit needless words: Sentence length perception"): i lettori stimano la lunghezza di una frase rispetto a 17 parole in modo rapido e preciso, contando le righe visive anziché le parole. La percezione della lunghezza è quindi legata alla resa visiva — [PMC9955962](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9955962/)
- La "burstiness" (variazione della lunghezza delle frasi) è descritta da fonti commerciali come tratto distintivo della scrittura umana rispetto a quella degli LLM. La fonte è un blog di un fornitore, non uno studio sui lettori **[DEBOLE]** — [DEV Community](https://dev.to/checkcalc/the-burstiness-factor-how-variation-in-sentence-length-beats-ai-detectors-2fg)
- Opinione: a stancare il lettore è la mancanza di variazione, non la frase lunga in sé **[DEBOLE]** — [Pat Thomson](https://patthomson.net/2017/03/13/academic-sentences-keepyourreaderawake/)
- Hemingway Editor: anche secondo la documentazione, le frasi lunghe possono funzionare bene nella narrazione o nelle catene logiche, e non tutte le segnalazioni vanno corrette — [Hemingway, Readability docs](https://hemingwayapp.com/help/docs/readability)
- ProWritingAid Pacing Check: secondo descrizioni di terzi offre informazioni sulla varietà delle frasi e un grafico del ritmo — [Jerry Jenkins review](https://jerryjenkins.com/?p=8494)

### Inferences
- Il passo di Provost ("This sentence has five words…", tratto da *100 Ways to Improve Your Writing*, 1985) è citatissimo ma, essendo protetto da copyright, va solo parafrasato: una sequenza di frasi della stessa lunghezza diventa monotona come un rumore meccanico, mentre alternare brevi, medie e lunghe crea musica. Non ho verificato la fonte primaria in questa sessione.
- Tradizione italiana: la paratassi (coordinazione, frasi brevi) è associata a scorrevolezza e modernità giornalistica; l'ipotassi (subordinazione) alla precisione argomentativa ma anche al "burocratese". Per i manager di PMI conviene una base paratattica con ipotassi controllata (al massimo 2 livelli di subordinazione) nelle spiegazioni scientifiche. Questa è sintesi di conoscenza editoriale: nella ricerca non ho trovato una fonte specifica.
- Metriche deterministiche proposte, per capitolo e per finestre di circa 500 parole:
  - lunghezza media delle frasi in parole: per la saggistica divulgativa italiana, fascia indicativa 15-22;
  - percentuale di frasi oltre 35 parole: allerta se supera il 10%;
  - percentuale di frasi oltre 50 parole: allerta per ogni singola occorrenza;
  - coefficiente di variazione (deviazione standard divisa per la media): allerta se inferiore a circa 0,45, segno di ritmo piatto. Soglia euristica da calibrare sul testo stesso e su 2-3 saggi italiani di riferimento;
  - sequenze di 4 o più frasi consecutive con lunghezza entro ±3 parole l'una dall'altra.
- Queste soglie non hanno basi empiriche: vanno calibrate eseguendo lo script su capitoli già approvati del libro e su testi modello.

### Gaps
- Non ho trovato studi peer-reviewed che misurino la preferenza dei lettori per la varianza della lunghezza delle frasi.
- Non ho trovato fonti accademiche italiane online (es. Serianni, Cortelazzo) su paratassi e ipotassi nella prosa divulgativa, né il testo originale di Provost.

---

## A5. Transizioni, connettivi, segnaletica, cambi di argomento bruschi

### Takeaway
Anteprime, riassunti e frasi di raccordo sono segnali al pari dei titoli e ne condividono i benefici sul ricordo dell'organizzazione **[FORTE per il signaling in generale]**. Gli elenchi puntati sopprimono i connettivi **[DEBOLE]**.

### Cited Findings
- Frasi d'anteprima ed equivalenti dei titoli producono benefici simili sulla memoria dei fatti — [UKY, Lorch et al. 2013](https://scholars.uky.edu/en/publications/signaling-topic-structure-via-headings-or-preview-sentences/)
- La rassegna di Lorch 1989 tratta segnali come anteprime, riassunti, parole di segnalazione e frasi di raccordo — DOI (bibl.) [10.1007/BF01326639](https://doi.org/10.1007/BF01326639)
- I connettivi si perdono passando alla forma a elenco — [Writing Skills](https://www.writing-skills.com/?p=4534) **[DEBOLE]**
- READ-IT (Dell'Orletta, Montemagni, Venturi, 2011) valuta la leggibilità dell'italiano su tratti lessicali, morfosintattici e sintattici, oltre a quelli superficiali — [ACL Anthology W11-2308](https://preview.aclanthology.org/stats/W11-2308/)
- Esistono proposte di indici di leggibilità italiani ispirati a Coh-Metrix, che include misure di coesione, oltre a Gulpease — [Polimi, OJS 2019](https://re.public.polimi.it/bitstream/11311/1126446/1/OJS_2019070210422800.pdf)

### Inferences
- Controllo operativo adatto a un LLM (è giudizio semantico, non conteggio): per ogni confine tra paragrafi e tra sezioni, il modello indica se c'è continuità e di che tipo (logica, temporale, tematica, contrasto), oppure un salto. Per ogni salto deve citare le ultime 10 parole del paragrafo precedente e le prime 10 del successivo, che uno script verifica.
- Controllo deterministico complementare: frequenza dei connettivi italiani da un elenco chiuso ("tuttavia", "quindi", "infatti", "inoltre", "d'altra parte", "insomma"…), per individuare sia l'assenza sia l'abuso. Il "quindi" a inizio frase ripetuto è un tic frequente. Proposta: allerta se lo stesso connettivo apre più di 2 frasi in 500 parole.

### Gaps
- Non ho trovato studi specifici sulla densità ottimale dei connettivi nella prosa italiana.

---

## A6. Ripetizioni, variazione elegante, cliché, riempitivi

### Takeaway
I correttori automatici (ProWritingAid Echoes/Repeats) cercano la ripetizione ravvicinata entro pochi paragrafi e l'abuso di una parola sull'intero testo, e quello è il modello operativo da seguire **[MEDIA, documentazione]**. La scuola redazionale italiana condanna le "ripetizioni" ravvicinate. La tradizione anglosassone (Fowler) mette invece in guardia dalla "elegant variation", cioè sinonimi forzati per non ripetere. Il compromesso: ripetere i termini tecnici (stabilità terminologica, cruciale in un libro con concetti scientifici) e variare le parole comuni non tecniche.

### Cited Findings
- ProWritingAid Echoes: evidenzia parole e frasi ripetute entro pochi paragrafi. All Repeats trova parole e frasi abusate nell'intero manoscritto — [ProWritingAid Repeats/Echoes](https://prowritingaid.com/art/345/How-to-use...-The-Repeats-Check.aspx)
- ProWritingAid "sticky sentences": le glue words sono le parole funzionali più frequenti. Media consigliata sotto il 40% sull'intero testo; singole frasi tipicamente tra 30 e 50%; il report segnala le frasi con glue index oltre il 60% — [ProWritingAid Sticky Sentence Report](https://prowritingaid.com/art/347/How-to-use----The-Sticky-Sentence-Report.aspx); un vecchio eBook indicava meno del 45% per frase — [ProWritingAid eBook PDF](https://cdn.prowritingaid.com/ebook/ProWritingAid_EBook.pdf); un test informale su autori famosi trova capitoli spesso oltre il 45% ma nessuno oltre il 50% — [Live Write Thrive](https://www.livewritethrive.com/2017/03/09/5-things-an-editing-tool-taught-me-that-might-help-you/)
- Hemingway segna gli avverbi in blu, il passivo in verde e le parole complesse con alternative più semplici in viola — [Hemingway, Highlighted issues](https://4.hemingwayapp.com/help/docs/highlighted-issues)

### Inferences
- Il criterio "glue words" di ProWritingAid è tarato sull'inglese. In italiano articoli, preposizioni articolate e clitici alzano la quota di parole funzionali, quindi la soglia del 40% non va trasferita senza calibrazione.
- Fowler, *Modern English Usage* (1926), voce "elegant variation": condanna il ricorso a sinonimi solo per evitare la ripetizione. Fonte bibliografica nota, non riaperta in questa sessione; voce introduttiva: [Wikipedia, Elegant variation](https://en.wikipedia.org/wiki/Elegant_variation) (bibl.).
- Controllo deterministico proposto per le ripetizioni (italiano): lemmatizzazione (es. spaCy `it_core_news_*`), poi segnalazione dei lemmi di contenuto (nomi, verbi, aggettivi, avverbi; escluse le stopword) ripetuti entro una finestra di 50-80 parole, o 2 o più volte nella stessa frase. Va inserita una lista bianca dei termini tecnici del libro (emozione, amigdala, interocezione…) e dei nomi dei personaggi. Il risultato va all'LLM, che decide caso per caso se la ripetizione è intenzionale (anafora, enfasi) o va corretta.
- Riempitivi e avverbi italiani da sorvegliare con lista chiusa e conteggio per 1.000 parole: "assolutamente", "sostanzialmente", "praticamente", "fondamentalmente", "letteralmente", "effettivamente", "decisamente", "sicuramente", "semplicemente", "davvero", "proprio", "un po'", "in qualche modo", "di fatto", "in realtà", "a livello di", "andare a + infinito" ("andiamo a vedere"), "piuttosto che" in senso disgiuntivo (uso censurato dalla norma). Proposta: allerta se un singolo riempitivo supera 1 occorrenza ogni 1.000 parole, o se gli avverbi in "-mente" superano circa l'1,5% delle parole. Le soglie sono euristiche.
- Cliché e frasi fatte, aggiungendo quelli tipici degli LLM in italiano: "nel cuore di", "un viaggio", "non è solo X, è Y", "in un mondo in cui", "giocare un ruolo chiave", "a 360 gradi", "mettersi in gioco", "fare la differenza", "la vera sfida". Serve una lista chiusa con corrispondenza regex. L'LLM entra in gioco solo per varianti non coperte, sempre con citazione esatta.

### Gaps
- Non ho trovato una fonte autorevole italiana online (Treccani o Crusca) con regole quantitative sulle ripetizioni o una lista canonica dei riempitivi. Le liste sopra sono prassi redazionale.
- Non ho trovato strumenti italiani equivalenti a ProWritingAid con report sulle ripetizioni, salvo i correttori basati su Gulpease (vedi B3).

---

## A7. Formattazione del dialogo e chiarezza dell'attribuzione

### Takeaway
Non ho trovato prove empiriche nella ricerca. Valgono le convenzioni editoriali italiane: in un singolo testo si usa un solo sistema di virgolette (caporali « » più frequenti nell'editoria libraria, oppure lineette o virgolette alte), in modo coerente, con attribuzione chiara.

### Cited Findings
- Nessuna fonte verificata in questa sessione sulla formattazione del dialogo.

### Inferences
- Controlli deterministici: un solo stile di virgolette per il dialogo in tutto il manoscritto; virgolette aperte e chiuse bilanciate; punteggiatura coerente prima e dopo la battuta. Battute consecutive senza attribuzione oltre 4, con due o più parlanti in scena, vanno segnalate come rischio di "chi sta parlando?".
- Controllo LLM: per ogni battuta il modello identifica il parlante. Se non può farlo con certezza dal testo, lo segnala citando la battuta esatta. È lo stesso test che farebbe un lettore.
- Etichette di attribuzione: preferire "dice/disse" e i gesti d'azione ai verbi enfatici ("sibilò", "ruggì"); segnalare gli avverbi attaccati ai verbi dichiarativi ("disse nervosamente"). È convenzione di mestiere, coerente con l'avverbio segnalato da Hemingway — [Hemingway, Highlighted issues](https://4.hemingwayapp.com/help/docs/highlighted-issues).

### Gaps
- Non ho trovato fonti specifiche: servirebbero manuali redazionali italiani (es. Lesina, *Il nuovo manuale di stile*; norme redazionali degli editori) non consultati in questa sessione.

---

## A8. Elenchi, box, riquadri, riepiloghi e "key takeaways" nei libri di business

### Takeaway
I riassunti posti prima o dopo un testo migliorano il ricordo **[MEDIA-FORTE, letteratura sui segnali]**. Gli elenchi migliorano il ricordo ma non necessariamente la persuasione **[DEBOLE-MEDIA]**. Non ho trovato studi specifici sui box "key takeaways" nei libri di business.

### Cited Findings
- I riassunti a elenco o a panoramica migliorano il ricordo, soprattutto delle parti finali — [Springer BF03186769](https://link.springer.com/article/10.1007/BF03186769)
- Hartley & Trueman 1982: cinque esperimenti sugli effetti dei riassunti sul ricordo della prosa (contenuti non recuperati qui) — [Springer, riferimento](https://link.springer.com/article/10.1007/BF03186769)
- Elenchi: ricordo migliore, persuasione invariata — [Radboud thesis](https://theses.ubn.ru.nl/items/8e131990-9803-42de-a737-7e7e73362c7f)
- I riassunti rientrano nella rassegna sui segnali di Lorch 1989 — DOI (bibl.) [10.1007/BF01326639](https://doi.org/10.1007/BF01326639)

### Inferences
- Per un libro sulle emozioni rivolto ai manager, un riepilogo breve a fine capitolo (3-5 punti) e un eventuale box "In azienda" o "Prova questo" sono coerenti con la letteratura sui segnali, a condizione che non interrompano la scena narrativa a metà. Box e riquadri vanno posti ai confini di sezione.
- Controllo: ogni punto del riepilogo deve corrispondere a un contenuto effettivamente presente nel capitolo. L'LLM indica il passaggio sorgente con citazione esatta e uno script verifica la stringa, evitando riepiloghi che introducono affermazioni nuove o non supportate (rilevante per il registro delle affermazioni scientifiche del progetto).

### Gaps
- Nessuno studio trovato sull'efficacia dei box o riquadri nei libri di business per adulti, né sull'effetto dei box sull'immersione nella saggistica narrativa.

---

## A9. Sigle e acronimi, numeri in cifre o in lettere, parole straniere (anglicismi)

### Takeaway
Sugli anglicismi, la Crusca (Gruppo Incipit, nato dopo la petizione di Annamaria Testa del 2015) propone alternative italiane senza "fare guerra all'inglese". Il Devoto-Oli offre equivalenti per oltre 200 anglicismi **[MEDIA, fonti secondarie]**. Per numeri e sigle non ho trovato norme Crusca online: valgono le norme redazionali.

### Cited Findings
- Il Gruppo Incipit della Crusca monitora i neologismi anglicizzanti e propone sostituti italiani. È nato dopo la petizione "Un intervento per la lingua italiana" (2015, circa 70.000 firme) — [Crusca, risposta di Marazzini (PDF)](https://accademiadellacrusca.it/sites/www.accademiadellacrusca.it/files/page/2015/03/10/rispostamarazzini.pdf); [Tecnica della Scuola](https://www.tecnicadellascuola.it/basta-anglicismi-esasperati-riappropriarsi-della-lingua-italiana)
- La sezione "Per dirlo in italiano" del Nuovo Devoto-Oli (2017) offre equivalenti per oltre 200 anglicismi. Molte sostituzioni proposte non hanno attecchito — [Rotary, Bombi 2023 (PDF)](https://triestealtoadriatico.rotary2060.org/images/foto/20230329_bombi.pdf)
- Esistono linee guida sull'uso degli anglicismi nella comunicazione trasparente, basate sul lavoro di Incipit e su iniziative di Francia, Spagna e Svizzera — [Meglio l'italiano o l'itanglese?](https://prestatest.bazzacco.net/libri/546031-meglio-l-italiano-o-l-itanglese-linee-guida-sull-uso-di-anglicismi-nella-comunicazione-trasparente-9788869395208.html)
- La Crusca non ha un ruolo normativo ufficiale, a differenza delle accademie francese e spagnola — [Rivista Tradurre](https://rivistatradurre.it/sprovveduti-innovativi-o-libertari/?pdf=8394)

### Inferences
- Criteri operativi per il libro, da convenzione redazionale:
  - Anglicismi: tenere quelli acclimatati e senza vero equivalente (manager, team, marketing, feedback, stress, budget) in tondo, invariabili al plurale (*i manager*, non *i managers*). Sostituire quelli evitabili (meeting → riunione, deadline → scadenza, skill → competenze, mindset → mentalità; ma "mindset" può restare se è termine tecnico citato). Usare il corsivo per le parole straniere non acclimatate.
  - Controllo deterministico: estrazione delle parole non presenti in un dizionario italiano, contro una lista bianca degli anglicismi ammessi. Per ognuna si riportano frequenza e prima occorrenza; allerta se il totale supera circa 5 per 1.000 parole (soglia euristica).
- Sigle: sciogliere alla prima occorrenza in ogni capitolo, con la sigla tra parentesi; maiuscole senza punti (PMI, non P.M.I.); controllare che ogni sigla sia sciolta prima del suo primo uso.
- Numeri: prassi editoriale italiana diffusa scrivere in lettere i numeri da uno a dieci (o fino a cento) e le cifre tonde in contesto narrativo; cifre per percentuali, dati statistici, date, misure, età precise in contesto tecnico; coerenza "%" contro "per cento" nell'intero libro; separatore delle migliaia con punto (1.200) e decimale con virgola (3,5). Nessuna fonte verificata qui: va fissata nella guida stilistica del progetto e verificata con regex.

### Gaps
- Non ho trovato norme Crusca o Treccani online sui numeri in cifre o in lettere. La ricerca suggeriva le consulenze linguistiche della Crusca, non consultate.
- La pagina ufficiale del Gruppo Incipit con i comunicati non è stata aperta.

---

## B1. Affidabilità degli LLM nella valutazione di leggibilità e stile; modalità di errore note

### Takeaway
GPT-4 Turbo e GPT-4o mini stimano la leggibilità percepita dagli umani meglio delle formule classiche (r ≈ 0,74-0,76 su 4.724 brani inglesi) **[MEDIA-FORTE]**. Sbagliano però nei conteggi (lettere, parole, sillabe), tendono a essere più indulgenti degli umani, e come giudici mostrano bias noti di posizione, prolissità e auto-preferenza **[FORTE per i bias, MEDIA per la leggibilità]**. Conclusione operativa: affidare all'LLM il giudizio, agli script il conteggio.

### Cited Findings
- Trott & Rivière (2024), "Measuring and Modifying the Readability of English Texts with GPT-4": su 4.724 brani (CLEAR corpus), le stime zero-shot di GPT-4 Turbo e GPT-4o mini correlano con i giudizi umani a r = 0,76 e 0,74, meglio delle formule tradizionali e di vari indici psicolinguistici. Un esperimento preregistrato (N=59) mostra però che molta varianza dei giudizi umani resta inspiegata — [arXiv 2410.14028](https://arxiv.org/html/2410.14028v1)
- Lavoro del 2025: le metriche di leggibilità superficiali correlano poco con le valutazioni umane, soprattutto sui testi tecnici; analisi cross-dataset di metriche senza riferimento — [arXiv 2510.15345](https://arxiv.org/pdf/2510.15345)
- Rooein et al. (2024), riportato di seconda mano: combinare prompt sì/no con metriche convenzionali dà correlazioni con gli umani più alte delle due cose separate — citato in [arXiv 2510.15345](https://arxiv.org/pdf/2510.15345) (da verificare sull'originale)
- Valutazione zero-shot della leggibilità con LLM (2026) — [arXiv 2604.24470](https://arxiv.org/pdf/2604.24470) (non approfondito)
- Indulgenza: sulla leggibilità del codice gli LLM giudicano leggibile il 68,1% dei frammenti Java, contro il 48,9% degli umani (Python 70,9% contro 55,1%; CUDA 49,4% contro 16,2%) — [arXiv 2510.16579](https://arxiv.org/html/2510.16579v1)
- Errori di conteggio: gli LLM falliscono nel contare lettere e caratteri. Il ruolo della tokenizzazione è dibattuto: per alcuni è la causa principale ([Cosma et al. 2025, arXiv 2505.14172](https://arxiv.org/html/2505.14172v1)); altri trovano errori simili anche con input diviso in caratteri, attribuendo il problema al processo di conteggio ([arXiv 2412.18626](https://arxiv.org/html/2412.18626v1)). CharBench (AAAI 2026) è nato per dirimere la questione — [arXiv 2508.02591](https://arxiv.org/pdf/2508.02591). Il ragionamento esplicito è il rimedio più robusto, a costo di token — [Xu & Ma, arXiv 2410.14166](https://arxiv.org/pdf/2410.14166)
- Bias dell'LLM come giudice (Zheng et al. 2023, MT-Bench/Chatbot Arena): bias di posizione, di prolissità e di auto-preferenza. GPT-4 concorda con le preferenze umane oltre l'80% delle volte, quanto due umani tra loro — DOI/URL (bibl.) [arXiv 2306.05685](https://arxiv.org/abs/2306.05685); sintesi secondaria con cifre (stesso verdetto solo nel 65% delle coppie a ordine invertito; auto-preferenza +10% GPT-4, +25% Claude-v1, non dimostrata in modo conclusivo) — [Grepture](https://grepture.com/blog/llm-as-a-judge-bias) **[cifre da verificare sul paper]**
- Rassegna sui metodi "LLMs-as-judges" — [arXiv 2412.05579](https://arxiv.org/html/2412.05579v2)
- Valutazioni di rilevanza fatte da LLM non sostituiscono ancora quelle umane — [arXiv 2412.17156](https://arxiv.org/html/2412.17156)

### Inferences
- Modalità di errore da presidiare in un controllo editoriale con LLM:
  1. conteggi errati di parole, sillabe e frasi: mai chiederli al modello;
  2. citazioni allucinate o "aggiustate": la frase segnalata non esiste o è parafrasata;
  3. severità incoerente tra capitoli o tra esecuzioni;
  4. eccesso di segnalazioni, tipico di prompt del tipo "trova i problemi", dove il modello trova sempre qualcosa;
  5. indulgenza o piaggeria verso testi che "suonano" fluenti, specie se generati da LLM della stessa famiglia (auto-preferenza; plausibile, non dimostrato per la prosa);
  6. degrado su testi lunghi: le segnalazioni si concentrano all'inizio. Il fenomeno è noto come "lost in the middle" (Liu et al. 2023, [arXiv 2307.03172](https://arxiv.org/abs/2307.03172) (bibl.)).
- I dati sono quasi tutti sull'inglese. Per l'italiano non ho trovato studi che validino LLM contro giudizi umani di leggibilità: va calibrato in proprio.

### Gaps
- Nessuno studio trovato su LLM e valutazione stilistica della prosa narrativa italiana.
- Le cifre sui bias di Zheng et al. vengono da sintesi secondarie: va verificata la tabella originale.

---

## B2. Buone pratiche: script deterministici più giudizio LLM, citazioni verificate, rubriche, suddivisione, calibrazione

### Takeaway
L'architettura raccomandata è ibrida. Uno script calcola tutte le metriche contabili (lunghezze, Gulpease, ripetizioni, riempitivi, sigle, numeri). L'LLM riceve le metriche e il testo diviso in blocchi, e giudica secondo una rubrica con esempi ancorati e scale piccole a numeri interi. Ogni segnalazione deve contenere una citazione letterale, che uno script confronta con il testo; le segnalazioni con citazioni non trovate vengono scartate. La calibrazione si fa contro un piccolo campione annotato da un umano **[MEDIA-FORTE: documentazione Anthropic e letteratura sui giudici LLM]**.

### Cited Findings
- Anthropic, "Reduce hallucinations": consentire al modello di dichiarare incertezza; per documenti lunghi (oltre circa 20k token) fargli estrarre citazioni parola per parola prima del compito; verificare ogni affermazione con una citazione a supporto e ritirarla se non la trova — [Claude Docs, Reduce hallucinations](https://platform.claude.com/en/docs/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- La vecchia pagina Anthropic suggerisce controlli programmatici: corrispondenza esatta delle stringhe o percentuale di sovrapposizione tra citazioni e documento originale — [Anthropic, Minimizing hallucinations](https://docs.anthropic.com/claude/docs/claude-is-hallucinating)
- Combinare segnali LLM e metriche convenzionali migliora la correlazione con gli umani (Rooein et al. 2024, di seconda mano) — [arXiv 2510.15345](https://arxiv.org/pdf/2510.15345)
- Rubriche strette con scala a interi piccoli e motivazione scritta: in un cookbook Hugging Face la correlazione giudice-umano sale da 0,567 a 0,843 (riportato di seconda mano) — [Grepture](https://grepture.com/blog/llm-as-a-judge-bias) **[DEBOLE: fonte secondaria]**
- Validazione: su compiti ben definiti i giudici raggiungono un kappa di Cohen di circa 0,6-0,8 con gli umani; sotto circa 0,6 la rubrica va rivista. Fonti divulgative: l'ordine di grandezza è plausibile, le soglie sono di mestiere — [FutureAGI, best practices](https://futureagi.com/blog/llm-as-judge-best-practices-2026); [ZeroEntropy](https://www.zeroentropy.dev/concepts/llm-as-judge/) **[DEBOLE]**
- Contro il bias di posizione nei confronti a coppie: invertire l'ordine e contare un esito solo se è coerente nelle due versioni — [Klu glossary](https://klu.ai/glossary/llm-as-a-judge); Zheng et al. (bibl.) [arXiv 2306.05685](https://arxiv.org/abs/2306.05685)
- Il ragionamento esplicito migliora i conteggi, ma resta meno affidabile del codice — [arXiv 2410.14166](https://arxiv.org/pdf/2410.14166)

### Inferences
Protocollo operativo proposto per il libro:
1. **Fase deterministica (Python).** Segmentazione in frasi con spaCy italiano. Le abbreviazioni ("dott.", "S.p.A.", "ecc.") vanno gestite, altrimenti i conteggi si falsano. Lo script calcola, per capitolo e per finestre di 500 parole: Gulpease; lunghezza media delle frasi, deviazione standard e coefficiente di variazione; percentuale di frasi oltre 35 e oltre 50 parole; parole per paragrafo; ripetizioni di lemmi entro 60 parole; frequenza dei riempitivi; avverbi in -mente; anglicismi fuori lista bianca; sigle non sciolte; stile delle virgolette; formato dei numeri. Output in JSON con identificativi di paragrafo stabili (es. `cap01_p047`).
2. **Fase LLM, per blocchi.** Blocchi di una scena o di 1.500-3.000 parole, con circa 200 parole di sovrapposizione e contesto (titolo del capitolo, riassunto di 100 parole del blocco precedente). Il modello riceve la rubrica e le metriche del blocco già calcolate, che non deve ricalcolare. Valuta solo dimensioni semantiche: chiarezza delle transizioni, attribuzione dei dialoghi, coerenza tra sottotitolo e contenuto, ripetizioni intenzionali o meno, cliché fuori lista, densità concettuale, eccesso di astrazione.
3. **Output strutturato obbligatorio.** Per ogni segnalazione: `{id_paragrafo, citazione_esatta (≤25 parole), categoria, severità 1-3, motivazione, proposta}`. Va permesso esplicitamente "nessun problema rilevante", contro l'eccesso di segnalazioni.
4. **Verifica.** Uno script cerca `citazione_esatta` nel paragrafo indicato, dopo normalizzazione di spazi e apostrofi tipografici. Le segnalazioni non trovate vengono scartate e registrate come errore del giudice. Il tasso di citazioni non verificabili è una metrica di qualità dell'esecuzione.
5. **Rubrica ancorata.** Per ogni severità, 1-2 esempi reali tratti dal libro (un'ancora "1 = cosmetico", una "3 = il lettore si perde"). Scala piccola a interi, motivazione prima del punteggio.
6. **Calibrazione.** Annotare a mano 30-50 paragrafi. Eseguire il giudice e misurare l'accordo: kappa o accordo percentuale per categoria. Ripetere 2-3 volte con temperatura bassa per misurare la stabilità e tenere solo le segnalazioni ricorrenti. Rifare la calibrazione quando si cambia modello o prompt.
7. **Ruolo del giudice.** Smistamento, non verdetto: la decisione finale resta all'autore o all'editor, coerente con la documentazione di Hemingway e ProWritingAid, secondo cui non tutte le segnalazioni vanno corrette.
- È preferibile usare come giudice un modello diverso da quello che ha generato o riscritto il testo, per ridurre l'auto-preferenza (inferenza da Zheng et al.).

### Gaps
- Non ho trovato studi che quantifichino il tasso di citazioni allucinate in compiti di revisione stilistica, né valori di accordo LLM-umano specifici per l'editing di prosa italiana.
- La pagina OpenAI sul prompt engineering non è stata consultata.

---

## B3. Strumenti esistenti (Hemingway, ProWritingAid, Grammarly, equivalenti italiani): metriche e soglie

### Takeaway
Hemingway usa un grado scolastico statunitense (obiettivo predefinito: grado 9) e colori per frasi difficili, avverbi, passivo e parole complesse. ProWritingAid offre report su sticky sentences (glue words: media sotto il 40%, frase segnalata oltre il 60%), pacing, echoes/repeats e varietà delle frasi. Per l'italiano lo standard è il Gulpease (formula basata sulle lettere, scala 0-100), affiancato da READ-IT (ILC-CNR) e dal software Corrige, basato su Gulpease **[MEDIA, documentazione]**.

### Cited Findings
- Hemingway: il punteggio è un grado scolastico, con obiettivo predefinito al grado 9 (media degli adulti USA; cambiarlo è una funzione premium). Giallo = frase difficile, rosso = molto difficile; il segnale scatta quando la frase supera il livello obiettivo. Le correzioni suggerite sono dividere le frasi e ridurre le congiunzioni. Punteggi e segnalazioni sono solo una guida — [Hemingway, Readability](https://hemingwayapp.com/help/docs/readability); [Hemingway, Highlighted issues](https://4.hemingwayapp.com/help/docs/highlighted-issues); [APS accessibility](https://www.aps.edu/accessibility-at-aps/accessibility-tools/hemingway-app)
- ProWritingAid Sticky Sentences: media dei glue words sotto il 40%; frase segnalata oltre il 60%; alcune frasi sono "sticky" per necessità — [ProWritingAid help](https://prowritingaid.com/art/347/How-to-use----The-Sticky-Sentence-Report.aspx); [definizione di sticky sentence](https://prowritingaid.com/grammar/1000165/What-is-a-sticky-sentence)
- ProWritingAid Pacing: evidenzia i paragrafi lenti (introspezione, antefatto) e consiglia di inserire azione tra paragrafi lenti consecutivi — [ProWritingAid Pacing](https://prowritingaid.com/art/344/How-to-use----The-Pacing-Check.aspx)
- ProWritingAid Echoes e All Repeats: ripetizioni entro pochi paragrafi e abuso sull'intero testo — [ProWritingAid Repeats](https://prowritingaid.com/art/345/How-to-use...-The-Repeats-Check.aspx); uso per revisioni profonde — [ProWritingAid deep edits](https://prowritingaid.com/art/1067/using-prowritingaid-for-deep-edits.aspx)
- Gulpease: 89 + 300 × (frasi/parole) − 10 × (lettere/parole). Scala 0-100, valori più alti = più facile. Un testo è facile se supera 80 per chi ha la licenza elementare, 60 per la media, 40 per la superiore. Attribuito a Lucisano e Piemontese (GULP, La Sapienza), con datazione oscillante tra 1987 e 1988 — [Diacronia (PDF)](https://www.diacronia.ro/indexing/details/V4852/pdf); [l'Unità 1997, archivio](https://archivio.unita.news/assets/main/1997/03/08/page_013.pdf); [ALT, arXiv 2210.00553](https://arxiv.org/pdf/2210.00553)
- Il Flesch adattato all'italiano (Flesch-Vacca) è meno affidabile; discussione divulgativa — [SupportHost](https://supporthost.com/it/flesch-reading-ease-in-italiano-e-la-sua-affidabilita)
- READ-IT: primo strumento avanzato per la leggibilità dell'italiano (raw text, lessico, morfosintassi, sintassi); valuta documenti e singole frasi; la leggibilità dipende fortemente dal genere testuale — [ACL W11-2308](https://preview.aclanthology.org/stats/W11-2308/); [CNR, Assessing document and sentence readability](https://iris.cnr.it/handle/20.500.14243/260898); [W12-2206](https://preview.aclanthology.org/moar-dois/W12-2206.pdf)
- Corrige è un software basato su Gulpease; READ-IT è utile per i testi giuridici — [Italiano LinguaDue 2022, DOAJ](https://doaj.org/article/485613c5c2a0471ab0185e8990609754)
- Intervista a Emanuela Piemontese (coautrice del Gulpease) — [Palestra della scrittura](https://www.palestradellascrittura.it/?p=4826)

### Inferences
- Per i manager di PMI, in genere diplomati o laureati, un Gulpease di capitolo tra circa 50 e 60 è un obiettivo ragionevole: la soglia 60 rende il testo facile per chi ha la licenza media, quindi c'è margine. Valori sotto 45 su una finestra di 500 parole segnalano passaggi da controllare. Va ricordato che il Gulpease misura solo lunghezza di parole e frasi, non coesione né densità concettuale: la bassa correlazione delle metriche superficiali con il giudizio umano sui testi tecnici è documentata in [arXiv 2510.15345](https://arxiv.org/pdf/2510.15345).
- Il grado di Hemingway e i glue words di ProWritingAid sono tarati sull'inglese: per l'italiano conviene replicarne la logica (frase oltre soglia, quota di parole funzionali, paragrafi lenti) con soglie ricalibrate sul corpus di riferimento.
- Grammarly offre metriche di leggibilità, ma il supporto pieno è per l'inglese. Non verificato in questa sessione.

### Gaps
- Grammarly non è stato verificato (supporto per l'italiano e metriche).
- Non ho trovato strumenti commerciali italiani che replichino i report di ProWritingAid su pacing e ripetizioni. Esistono altri correttori italiani basati su Gulpease (es. strumenti web "leggibilità Gulpease"), non verificati.
- Non ho verificato se READ-IT sia ancora accessibile online come servizio.

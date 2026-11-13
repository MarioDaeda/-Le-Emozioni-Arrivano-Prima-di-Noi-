# Metriche di leggibilità per l'italiano, vocabolario di base e linguaggio chiaro: controlli quantitativi e lessicali applicabili a un libro di saggistica narrativa per imprenditori e manager di PMI

Nota di metodo: le fonti primarie consultate per intero sono il paper READ-IT (Dell'Orletta, Montemagni, Venturi 2011), le "30 regole" di Cortelazzo e Pellegrino (2002), la "Guida alla scrittura" del Politecnico di Milano (2002), l'articolo di De Mauro su Internazionale (2016), la tesi di dottorato Francalanci (Univ. Firenze) che ricostruisce la storia di Flesch-Vacca e Gulpease, il paper Tint 2.0 (2018) e la guida UE "How to write clearly" (ed. EN). I testi di Direttiva Frattini, Direttiva Baccini, Codice Cassese, Manuale Fioritto e ISO 24495-1 (a pagamento) NON sono stati letti in originale: le note su di essi si basano su fonti secondarie e sono marcate come tali.

---

## 1. Indice Gulpease e Flesch-Vacca: formule, fasce, confronto, limiti

### Takeaway
Il Gulpease (Lucisano & Piemontese 1988) è l'unico indice tarato direttamente sull'italiano, usa lettere e non sillabe (quindi è facile da calcolare con uno script), e le sue soglie sono 80/60/40 per lettori con istruzione elementare/media/superiore. È preferito al Flesch-Vacca perché più stabile e automatizzabile, ma ha un potere predittivo solo moderato: è tarato su studenti, non su adulti, e misura soltanto la lunghezza di parole e frasi.

### Cited Findings
**Formula Gulpease**
- Formula: `G = 89 + (300 × n_frasi − 10 × n_lettere) / n_parole`. La scala va da 0 a 100, dove 100 è la leggibilità massima. L'indice nasce nel 1988 dal GULP (Gruppo Universitario Linguistico Pedagogico) della Sapienza di Roma, su dati raccolti nel 1986-87. Riferimento: Lucisano P., Piemontese M.E., "GULPEASE: una formula per la predizione della difficoltà dei testi in lingua italiana", *Scuola e città*, XXXIX, n. 3, 1988, pp. 110-124 — [Wikipedia IT, Indice Gulpease](https://it.wikipedia.org/wiki/Indice_Gulpease)
- Forma equivalente, usata nello studio originale: `G = 89 − LP/10 + 3·FR`, dove LP = lettere ogni 100 parole e FR = frasi ogni 100 parole. La definizione delle variabili viene dalla legenda della tabella dello studio GULP riportata nella tesi — [Francalanci, tesi Univ. Firenze](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- Le parole si misurano in lettere e non in sillabe, proprio per rendere più facile il calcolo automatico — [SupportHost](https://supporthost.com/it/flesch-reading-ease-in-italiano-e-la-sua-affidabilita); [Wikipedia IT](https://it.wikipedia.org/wiki/Indice_Gulpease)

**Fasce interpretative**
- Fasce per livello di istruzione: un testo sopra 80 è compreso facilmente da chi ha la licenza elementare, sopra 60 da chi ha la licenza media, sopra 40 da chi ha il diploma superiore — [Wikipedia IT](https://it.wikipedia.org/wiki/Indice_Gulpease); [PuntoSicuro](https://www.puntosicuro.it/magazine/view-pdf/l-importanza-della-leggibilita-dei-testi-nella-formazione-per-la-sicurezza-AR-21964/); [l'Unità 1997](https://archivio.unita.news/assets/main/1997/03/08/page_013.pdf)
- Scala in 5 classi di difficoltà riportata nella tesi Francalanci: >80 molto facile; 79-60 facile; 59-50 difficile; 49-35 molto difficile; <35 quasi incomprensibile — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- La tesi collega le soglie anche a tre tipi di lettura, sul modello del cloze test. Per un dato livello di istruzione (l'esempio è la licenza media): sopra la soglia (>60) il lettore legge in autonomia ("livello di lettura indipendente"); tra 59 e 40 ha bisogno di aiuto ("livello di lettura scolastica"); sotto 40 prova frustrazione ("livello di frustrazione") — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- Cortelazzo e Pellegrino scrivono che un testo che arriva a 60 "è leggibile autonomamente da chi abbia la licenza media". Per i testi della PA, dai contenuti complessi, considerano attestarsi intorno a 50 "un buon risultato", e dicono che le loro stesse 30 regole stanno intorno a 50. Attenzione: lo stesso PDF descrive per errore la scala al contrario (0 = massima leggibilità), in contrasto con tutte le altre fonti — [Cortelazzo & Pellegrino, 30 regole](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)

**Validità e limiti**
- Lo studio GULP ha validato l'indice con prove cloze e prove a scelta multipla. La correlazione tra cloze e scelta multipla è 0,93, e la soglia del cloze segue il modello anglosassone (35/45/55% di completamenti corretti = frustrazione/scolastica/indipendente). La tesi si chiede se queste soglie valgano anche per l'italiano — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- Correlazioni con i punteggi cloze su 48 testi (24 di storia, 24 di scienze): Flesch 0,61; GULPEASE 0,61. Le varianti con vocabolario di base o sintassi andavano peggio: GULPSINT 0,20; SOLOBASE 0,32; GULPBASE 0,52. A parità di correlazione, Gulpease mostra "maggiore stabilità" mentre Flesch "tende a sovrastimare la difficoltà". La tesi conclude che il potere predittivo delle formule cala man mano che diventano più complesse — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- Limite chiave: la scala "è tarata su bambini e ragazzi in età scolare e mancano invece verifiche sistematiche ed estese su gruppi di adulti". Secondo la tesi le soglie restano "accettabili" per adulti con istruzione medio-bassa, ma i livelli del 1988 probabilmente non rispecchiano quelli attuali — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- Limite generale di tutte le formule tradizionali: usano la lunghezza della frase come indicatore della complessità sintattica e la lunghezza della parola come indicatore della difficoltà lessicale, e nessuna delle due ipotesi vale sempre. READ-IT cita studi che dimostrano sperimentalmente l'inaffidabilità di queste metriche — [Dell'Orletta et al. 2011, READ-IT](https://aclanthology.org/W11-2308.pdf)
- Cortelazzo e Pellegrino avvertono che gli indici valutano "la semplicità della sintassi e del lessico di un testo, non la correttezza della disposizione delle informazioni" — [30 regole](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)

**Flesch-Vacca (Franchina-Vacca)**
- Roberto Vacca ha adattato il Reading Ease di Flesch (1949) tenendo conto che le parole italiane hanno in media circa il 40% di sillabe in più di quelle inglesi. Nella formula, IL = indice di leggibilità, W = sillabe ogni 100 parole, S = parole per frase, e 206 è la costante. Valerio Franchina l'ha inserita nel suo word processor del 1972. Nel 1986 Franchina ha ricalcolato i coefficienti con una regressione su 22 testi scritti in parallelo in inglese e italiano dallo stesso autore. La correlazione con la versione inglese è salita da 0,9092 a 0,9398. Secondo gli esperimenti del GULP, però, la formulazione del 1972 "risulta più attendibile" — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- Formule riportate da Wikipedia IT: 1972 `F = 206 − 0,65·S − P`; 1986 `F = 217 − 1,3·S − 0,6·P`. Wikipedia indica S come "sillabe medie per parola" e P come "parole medie per frase" — [Wikipedia IT, Formula di Flesch](https://it.wikipedia.org/wiki/Formula_di_Flesch). **Incoerenza da segnalare.** Con S per parola (circa 2) la formula del 1972 darebbe circa 185, fuori scala. La tesi Francalanci definisce invece la variabile come sillabe *ogni 100 parole*, che dà valori sensati (con circa 225 sillabe ogni 100 parole e 20 parole per frase: 206 − 146 − 20 = 40). Per la formula del 1986, l'attribuzione di 1,3 e 0,6 alle due variabili su Wikipedia sembra invertita. 217 − 0,6·(sillabe/100 parole) − 1,3·(parole/frase) dà circa 56 con gli stessi dati, mentre la versione di Wikipedia dà un valore negativo. **Prima di usare la versione del 1986 bisogna verificarla sull'originale (Franchina & Vacca 1986).**
- La scala interpretativa del Flesch-Vacca che circola in Italia (100-90 elementare ... 30-0 post-laurea) deriva da testi inglesi, con i livelli scolastici USA convertiti in livelli italiani — [Wikipedia IT](https://it.wikipedia.org/wiki/Formula_di_Flesch)
- Limite pratico: contare le sillabe in modo automatico è difficile, e proprio per questo è nato il Gulpease — [SupportHost](https://supporthost.com/it/flesch-reading-ease-in-italiano-e-la-sua-affidabilita)

### Inferences
- Per il libro conviene il Gulpease: è deterministico, si calcola in poche righe di codice senza sillabatore ed è il riferimento di Cortelazzo, della Funzione Pubblica, di Corrige e di Tint. Il Flesch-Vacca va usato al massimo come controllo secondario, perché le formule circolano con coefficienti ambigui.
- Pubblico (manager e imprenditori con istruzione superiore o laurea): la soglia di "lettura indipendente" per il diploma è 40, ma un libro divulgativo dovrebbe puntare più in alto. Proposta operativa, *non validata*: Gulpease medio di capitolo ≥ 55 (con obiettivo intorno a 60, il livello della licenza media, cioè "facile" anche per chi è stanco o distratto) e nessun paragrafo sotto 45. I numeri vanno trattati come segnali e non come obiettivi da ottimizzare: il Gulpease si "migliora" anche spezzando frasi in modo artificioso, e questo può peggiorare la coesione.
- Implementazione (script):
  - `lettere` = solo caratteri alfabetici, accentate incluse, esclusi cifre e punteggiatura;
  - `parole` = token alfabetici, con gli apostrofi gestiti in modo coerente (per esempio "l'azienda" = 2 parole: va fissata una regola e mantenuta);
  - `frasi` = segmenti chiusi da . ! ? … (e, per convenzione, da ":" o ";" solo se si decide così; Gulpease in origine conta i punti fermi).
  - Il valore va calcolato per capitolo e per finestre mobili di circa 300 parole: le stime su testi brevi sono instabili (READ-IT nota che i metodi a livello di documento sono "unreliable for short texts").
  - Un LLM può fare il calcolo in modo affidabile solo eseguendo codice: non deve stimare a occhio.

### Gaps
- Non ho letto l'articolo originale di Lucisano & Piemontese (1988) né Franchina & Vacca (1986): i coefficienti del 1986 restano da verificare.
- Non ho trovato una validazione del Gulpease su lettori adulti né su saggistica divulgativa.
- Lo studio Sciumbata (2026, *Lebende Sprachen*) propone valori Gulpease di riferimento per Plain Language ed Easy Language in italiano, ma i numeri non erano accessibili — [arts.units.it](https://arts.units.it/handle/11368/3124598).

---

## 2. Strumenti più recenti: READ-IT, Corrige!/Èulogos CENSOR, Tint, Profiling-UD

### Takeaway
I tool di nuova generazione aggiungono a lunghezza di frase e parola tre famiglie di indicatori: lessicali (copertura del vocabolario di base, type/token, densità lessicale), morfosintattici (modi verbali) e sintattici (profondità dell'albero, catene di subordinate e di complementi, lunghezza delle dipendenze, rapporto subordinate/principali). In READ-IT il lessico porta l'accuratezza a livello di documento dal 77% al 95%. La sintassi è decisiva soprattutto a livello di frase: lì le sole lunghezze sono quasi inutili.

### Cited Findings
**READ-IT (ILC-CNR Pisa, 2011)**
- Classificatore SVM su testi con analisi a dipendenze. Valuta sia documenti sia singole frasi ed è pensato per la semplificazione di testi destinati a lettori con bassa alfabetizzazione o lieve disabilità cognitiva — [Dell'Orletta, Montemagni, Venturi 2011](https://aclanthology.org/W11-2308.pdf)
- Caratteristiche usate, in quattro gruppi — [READ-IT](https://aclanthology.org/W11-2308.pdf):
  - *Raw text*: lunghezza media della frase (parole) e della parola (caratteri).
  - *Lessicali*: percentuale di lemmi-tipo presenti nel Vocabolario di base De Mauro (versione 2000, circa 7.000 parole) e loro distribuzione nelle classi fondamentale / alto uso / alta disponibilità; Type/Token Ratio calcolato su campioni di uguale lunghezza.
  - *Morfosintattiche*: probabilità degli unigrammi di parti del discorso; densità lessicale (parole piene, cioè verbi, nomi, aggettivi e avverbi, sul totale dei token); distribuzione dei modi verbali (indicatore specifico dell'italiano).
  - *Sintattiche*: probabilità dei tipi di dipendenza; profondità massima dell'albero; profondità media delle "catene" di complementi retti da un nome (complementi preposizionali, modificatori); numero di predicati verbali e loro arità; rapporto tra subordinate e principali; posizione della subordinata rispetto alla principale (quelle postverbali sono più facili, secondo Miller & Weinert 1998); profondità delle catene di subordinate incassate; lunghezza dei legami di dipendenza, misurata in parole tra la testa e il dipendente.
- Corpora: *La Repubblica* (difficile) contro *Due Parole* (mensile di facile lettura scritto da linguisti con lessico e sintassi controllati, Piemontese 1996). Differenze misurate tra i due corpora: altezza media dell'albero 5,71 contro 3,67; sintagmi verbali per frase 2,40 contro 1,25; profondità delle catene di complementi 1,44 contro 1,30; principali/subordinate 65,1/34,9% contro 79,7/20,3%. Il paper riporta anche una "percentuale di parole del VdB" di 4,14% (Rep) contro 48,04% (2Par). Il valore è anomalo se letto come copertura: probabilmente si riferisce a una specifica feature distributiva, quindi non va usato come benchmark — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- Risultati, documenti (638 documenti, validazione incrociata a 5 fold): modello Base (solo lunghezze, equivalente approssimativo del Gulpease) 76,65%; Lessicale 95,45%; Morfosintattico 98,12%; Sintattico 97,02% — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- Risultati, frasi: Base 59,6%; Lessicale 61,6%; Morfosintattico 76,1%; Sintattico 78,2%. Su insiemi di frasi della stessa lunghezza (8-30 parole), il modello basato solo sulle lunghezze "non è in grado di identificare frasi facili". Gli autori concludono che le caratteristiche sintattiche "hanno un ruolo fondamentale" nella valutazione a livello di frase — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- La scala di READ-IT va da 0 (facile) a 100 (difficile) ed esprime una percentuale di difficoltà, non livelli di istruzione — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf). Nel 2018 aveva una demo online gratuita ma non era disponibile offline — [Tint 2.0, CLiC-it 2018](https://aclanthology.org/2018.clicit-1.55.pdf)
- Un follow-up del 2014 ha trovato che i giudizi di leggibilità dipendono fortemente dal genere testuale — [CNR](https://explore.cnr.it/resource/item/108571)

**Èulogos CENSOR / Corrige!Leggibilità**
- Nascono da due tesi seguite da De Mauro e Piemontese (Amizzoni 1991, calcolo automatico del Gulpease; Mastidoro 1991, rilevamento automatico del tasso di vocabolario di base). Dal 1999 Èulogos CENSOR è un servizio via email che restituisce statistiche, leggibilità per testo e per singola frase, liste di frequenza e confronto con il VdB tramite lemmatizzazione. È stato usato per il Premio Chiaro! (Funzione Pubblica, 2003). Poi è stato sostituito da Corrige!Leggibilità, a pagamento, con prova gratuita fino a 5.000 parole e un resoconto HTML con dati per frase e per parola — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf). Cortelazzo e Pellegrino lo segnalavano all'indirizzo www.eulogos.it/censor — [30 regole](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)

**Tint (FBK, Palmero Aprosio & Moretti)**
- Pipeline NLP italiana open source (GPL, Java) basata su Stanford CoreNLP — [arXiv 1609.06204](https://arxiv.org/pdf/1609.06204)
- Il modulo di leggibilità di Tint 2.0 calcola: numero di parole piene; sillabazione; frasi sotto una lunghezza fissata; distribuzione dei token per parte del discorso; TTR sui lemmi; quantità di coordinate e subordinate e loro rapporto; profondità media e massima dell'albero; Gulpease a livello di documento; difficoltà del testo basata sulle liste del vocabolario di base De Mauro. Riconosce anche più di 13.450 polirematiche e i tempi verbali composti — [Tint 2.0](https://aclanthology.org/2018.clicit-1.55.pdf)

**Profiling-UD (ItaliaNLP Lab, 2020)**
- Estrae più di 130 caratteristiche linguistiche su più livelli. È multilingue perché si basa su Universal Dependencies. Brunato, Cimino, Dell'Orletta, Montemagni, Venturi, LREC 2020, pp. 7145-7151 — [ACL Anthology 2020.lrec-1.883](https://aclanthology.org/2020.lrec-1.883)

**Coease**
- Strumento citato nella tesi Francalanci. Restituisce più indici distinti, senza un valore globale, rapportati ai tre livelli scolastici (primaria, secondaria di I e di II grado), ed è tarato anche sulle prove INVALSI — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)

### Inferences
- Le caratteristiche di READ-IT, Tint e Profiling-UD si replicano con un parser UD (Stanza, spaCy `it_core_news_lg`, UDPipe) e ciascuna diventa un controllo per frase che uno script può segnalare:
  1. profondità dell'albero > 6 (il valore medio di Repubblica è 5,71);
  2. più di 2 verbi finiti o sintagmi verbali per frase (Rep 2,40, 2Par 1,25);
  3. subordinate oltre il 35% delle proposizioni (oltre il livello di Repubblica);
  4. subordinata in posizione preverbale ("Qualora..., ...") combinata con una frase lunga;
  5. catene di subordinate di profondità ≥ 3;
  6. catene di complementi nominali di profondità ≥ 3 ("la valutazione dell'impatto della gestione delle emozioni del team");
  7. legami di dipendenza molto lunghi, per esempio soggetto e verbo separati da più di 10 parole (indicatore di un inciso lungo).
  Tutte queste soglie sono *euristiche derivate dai benchmark Rep/2Par*, non valori validati.
- Per un pubblico istruito non serve arrivare al livello di Due Parole. Un obiettivo ragionevole è stare sotto i valori medi di Repubblica in profondità sintattica e nel rapporto di subordinazione.
- La lezione centrale di READ-IT per il libro: un buon Gulpease medio non garantisce frasi facili. Le frasi difficili si individuano con la sintassi, frase per frase.

### Gaps
- Non ho verificato lo stato attuale (2026) delle demo online di READ-IT e Corrige, né i prezzi.
- Non ho trovato l'elenco completo delle 130 caratteristiche di Profiling-UD (sta nel paper LREC).
- Non ho verificato quale versione del VdB (1980 o 2016) usi Tint.

---

## 3. Nuovo vocabolario di base della lingua italiana (De Mauro 2016)

### Takeaway
L'NVdB conta circa 7.500 lemmi in tre fasce: circa 2.000 fondamentali, che coprono l'86% delle occorrenze dei testi; circa 3.000 di alto uso, che aggiungono il 6%; circa 2.500 di alta disponibilità. Il controllo operativo naturale è la percentuale di parole piene lemmatizzate fuori dal VdB. È un indicatore utile, ma la sua capacità predittiva è dimostrata male nei testi tecnici o specialistici.

### Cited Findings
- Dimensioni dell'NVdB (2016): fondamentale (FO) circa 2.000 parole (in neretto tondo); alto uso (AU) circa 3.000 (in tondo chiaro); alta disponibilità (AD) circa 2.500 (in corsivo chiaro). De Mauro parla di "circa settemila" parole in tutto — [De Mauro, Internazionale, 23/12/2016](https://internazionale.it/opinione/tullio-de-mauro/2016/12/23/il-nuovo-vocabolario-di-base-della-lingua-italiana)
- Copertura: FO = 86% delle occorrenze; AU = 6%; il restante 8% è costituito da circa 28.000 altre parole, comprese alcune AD — [De Mauro, Internazionale](https://internazionale.it/opinione/tullio-de-mauro/2016/12/23/il-nuovo-vocabolario-di-base-della-lingua-italiana)
- Corpus: 18.843.459 occorrenze in sei categorie di dimensioni simili: stampa, saggistica (inclusi i manuali), letteratura, spettacolo (copioni di film e teatro), comunicazione mediata dal computer, parlato trascritto. Sono stati esclusi nomi propri, numeri e simboli; i lemmi seguono il GRADIT; l'uso è calcolato come frequenza × dispersione; c'è stata una verifica manuale — [Internazionale](https://internazionale.it/opinione/tullio-de-mauro/2016/12/23/il-nuovo-vocabolario-di-base-della-lingua-italiana). I testi del corpus sono tutti successivi al 2000 — [Linguistik Online](https://bop.unibe.ch/linguistik-online/article/download/10197/13193/45293)
- Le parole AD sono poco frequenti nell'uso ma "avvertite come comuni" dai parlanti, e si possono individuare solo con indagini sui parlanti — [Il Post](https://www.ilpost.it/2016/12/29/nuovo-vocabolario-lingua-italiana/); [Linguistik Online](https://bop.unibe.ch/linguistik-online/article/download/10197/13193/45293)
- Il VdB del 1980 aveva un corpus di circa 500.000 occorrenze e contava circa 2.000 FO, 2.750 AU e 2.300 AD (circa 7.050 in totale) — [Internazionale](https://internazionale.it/opinione/tullio-de-mauro/2016/12/23/il-nuovo-vocabolario-di-base-della-lingua-italiana)
- **Dove trovare la lista**: l'elenco alfabetico completo è pubblicato in PDF da Internazionale (link breve http://intern.az/1PH2). Le parti del discorso seguono il GRADIT e il dizionario di Internazionale (dizionario.internazionale.it) — [Internazionale](https://internazionale.it/opinione/tullio-de-mauro/2016/12/23/il-nuovo-vocabolario-di-base-della-lingua-italiana)
- Uso come regola di stile: "Quanto meno numerose sono in un testo le parole del vocabolario di base, tanto meno numerose sono le persone in grado di comprenderlo". Le parole rare e i forestierismi irrinunciabili vanno spiegati con parole comuni alla prima occorrenza — [Cortelazzo & Pellegrino, regola 26](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)
- Evidenza contraria o di limite: nello studio GULP sui testi di storia e scienze il vocabolario di base "non ha alcun valore predittivo" nei testi scientifici e ne ha un po' nei testi storici. Le varianti di Gulpease con il VdB (SOLOBASE r = 0,32; GULPBASE r = 0,52) non superano il Gulpease semplice (0,61). Spiegazione proposta: nei linguaggi speciali "i vocaboli di base sono utilizzati con significati particolari" — [Francalanci](https://flore.unifi.it/bitstream/2158/1218395/1/tesi_Francalanci_fronte_retro.pdf)
- Evidenza a favore: in READ-IT, aggiungere le caratteristiche lessicali (VdB + TTR) alle sole lunghezze porta l'accuratezza a livello di documento dal 76,65% al 95,45% — [READ-IT](https://aclanthology.org/W11-2308.pdf)

### Inferences
- Controllo operativo per script o LLM:
  1. lemmatizzare con Stanza, spaCy o Tint;
  2. tenere solo le parole piene (NOUN, VERB, ADJ, ADV), esclusi nomi propri, numeri e sigle;
  3. calcolare la percentuale fuori da FO, quella fuori da FO+AU e quella fuori dal VdB intero;
  4. elencare i lemmi fuori VdB con frequenza e prima occorrenza.
  Visto che FO+AU coprono circa il 92% delle occorrenze di un corpus misto, un capitolo divulgativo con molto più del 10-15% di occorrenze di parole piene fuori dal VdB merita una revisione. *La soglia è un'inferenza, non è validata.*
- Il controllo più utile per il libro non è la percentuale complessiva, ma la lista dei termini fuori VdB. Per ognuno si decide: (a) sostituire con una parola comune; (b) tenere e definire alla prima occorrenza (per esempio "amigdala", "interocezione", "rimuginio"); (c) tenere perché è gergo noto al pubblico PMI (per esempio "fatturato", "margine", "cash flow").
- Attenzione al limite "significati speciali": parole di base come *emozione*, *affetto*, *attenzione* o *valutazione* sono nel VdB ma in psicologia hanno accezioni tecniche (per esempio "affetto" in senso psicologico). Il controllo VdB non le segnala, quindi serve un controllo semantico da parte dell'LLM: "parola comune usata in senso tecnico senza definizione".

### Gaps
- Non ho trovato percentuali di copertura VdB misurate su saggistica divulgativa o giornalistica italiana da usare come benchmark per un singolo testo (De Mauro dà solo dati sull'intero corpus).
- Non ho verificato se esista una versione digitale strutturata dell'NVdB (CSV con la fascia per ogni lemma). Il PDF va convertito.

---

## 4. Linee guida italiane di semplificazione: Codice di stile, Manuale di stile, Direttive Frattini e Baccini, Cortelazzo-Pellegrino, ITTIG-Crusca, Piemontese

### Takeaway
Le regole italiane convergono su pochi controlli verificabili. Frasi di circa 25 parole al massimo (da evitare quelle di 40 parole e oltre), una informazione per frase, poche subordinate e poche forme implicite (gerundio, participio, infinito), incisi spostati in fondo, frasi affermative senza doppie negazioni, forma attiva con il soggetto espresso, niente impersonale né nominalizzazioni, indicativo preferito a congiuntivo e condizionale, connettivi semplici, parole comuni o del VdB, tecnicismi spiegati, sigle sciolte alla prima occorrenza, niente stereotipi burocratici. Sono regole di esperti (practitioner) e non risultati sperimentali, salvo i rimandi a Gulpease e VdB.

### Cited Findings
**Cortelazzo & Pellegrino, "30 regole per scrivere testi amministrativi chiari"** (Guida agli Enti Locali, n. 20, 25/5/2002; base del manuale *Guida alla scrittura istituzionale*, Laterza 2003) — [PDF unifg](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf); [scheda del libro](https://search.ub.tum.de/vufind/Record/DE-604.BV017321979)
- Gli autori le presentano come "mai regole imperative": vanno scelte in base al caso.
- Destinatario di riferimento: chi ha frequentato la scuola dell'obbligo (regola 1).
- **Regola 12**: "intorno alle 25 parole il limite da non valicare"; le frasi da evitare sono quelle di "40, 70, anche 90 parole". Non tutte le frasi lunghe sono uguali: una frase di 34 parole con un elenco finale è più facile di una di 34 parole con subordinate e incisi. Due rimedi: eliminare le parole superflue o dividere la frase.
- **Regola 13**: una frase, una sola informazione (esempio: 44 parole riscritte in 2 frasi da 19).
- **Regola 14**: limitare le subordinate. L'esempio ha 3 livelli di subordinazione incassata.
- **Regola 15**: limitare le proposizioni implicite (infinito, participio, gerundio). Il soggetto del gerundio può essere ambiguo, e così il suo legame logico ("girando a destra" vale "se giri" o "quando giri"?). Le frasi esplicite sono più trasparenti.
- **Regola 16**: limitare gli incisi, che separano soggetto e verbo, verbo e oggetto, nome e complemento. Rimedio: spostarli alla fine della frase.
- **Regola 17**: preferire le frasi affermative ("solo l'intestatario può..." invece di "persone diverse dall'intestatario non possono...").
- **Regola 18**: preferire la forma attiva. Il passivo senza agente nasconde l'autore. Il passivo è accettabile se l'agente è ignoto o ovvio, o se serve a mantenere lo stesso tema all'inizio di frasi consecutive.
- **Regola 19**: evitare l'impersonale ("Si precisa che...", "si fa presente"); al suo posto usare la prima persona plurale o un soggetto esplicito.
- **Regola 20**: evitare le nominalizzazioni ("la percezione dell'integrazione salariale non comporta l'instaurazione..." diventa "I lavoratori che ricevono... non instaurano..."). Effetto doppio: più astrazione e più densità.
- **Regola 21**: esprimere il soggetto, perché il soggetto sottinteso costringe a ricordarlo da una frase all'altra; preferire che il soggetto sia chi agisce.
- **Regola 22**: preferire l'indicativo a congiuntivo e condizionale ("Se..." invece di "Qualora... sia" o "Nel caso in cui... fosse").
- **Regola 23**: preposizioni e congiunzioni semplici ("per" invece di "al fine di", "allo scopo di"; "se" invece di "nel caso in cui", "a condizione che", "sempreché").
- **Regola 24**: tecnicismi solo se necessari, spiegati alla prima occorrenza. Da evitare anche gli pseudo-tecnicismi ("corrispondere" le imposte, "porre in essere", "esondare").
- **Regola 25**: evitare gli stereotipi ("Con la presente si comunica", "in ottemperanza a").
- **Regola 26**: parole comuni o del VdB. Burocratismi da sostituire: rammentare → ricordare, riscontro → risposta, ovvero → oppure, erogare → versare. Forestierismi (meeting, budget, stage) e latinismi (de facto) da sostituire con l'equivalente italiano.
- **Regola 27**: parole concrete e verbi semplici invece di locuzioni verbali ("provvedere al pagamento" → pagare; "procedere all'annullamento" → annullare).
- **Regola 28**: parole dirette, senza eufemismi ("trapasso" → morte), senza perifrasi, senza litoti ("non impossibile" → possibile).
- **Regola 29**: sigle sciolte; alla prima occorrenza forma estesa + (SIGLA); grafia coerente.
- **Regola 30**: controllare la leggibilità rileggendo con gli occhi del destinatario, facendo leggere a un collega esterno e calcolando il Gulpease.
- Regole grafiche: margini ≥ 25 mm, righe di 60-72 caratteri, interlinea al 120%, corpo 12-14, maiuscolo solo in titoli di massimo 5 parole, un solo elemento in neretto per testo.

**Politecnico di Milano, "Guida alla scrittura e alla gestione dei testi amministrativi" (2002)** — [PDF](https://www.areacre.polimi.it/pubblicazioni/guidascrittura.pdf)
- "Frasi con più di 25 parole sono difficili da capire e ricordare". Tre consigli: una sola informazione o tema per frase; dividere la frase lunga in più principali con poche coordinate e subordinate; spezzare le "catene di parole", cioè sequenze senza verbo ("quanto previsto da, in materia di, a pena di decadenza del, sulla base di, in ottemperanza a"). Esempio: 42 parole e 3 temi riscritte in 3 frasi da 9, 12 e 20 parole.
- Forma attiva come prevalente: il passivo appesantisce soprattutto nelle ipotetiche. Forma positiva preferibile. Tecnicismi e metafore abusate da evitare, con il consiglio di far leggere il testo ad altri. Sigle esplicitate alla prima occorrenza. Definizioni "implicite" inserite nel testo ("il comodato, o prestito gratuito").

**Direttiva Frattini (8 maggio 2002, "Semplificazione del linguaggio dei testi amministrativi", progetto Chiaro!)** — fonti *secondarie*
- Otto pagine con consigli sulla scelta e organizzazione dei contenuti e sullo stile — [Falcone, Amministrazione in cammino (LUISS)](https://amministrazioneincammino.luiss.it/wp-content/uploads/2010/04/14960_falcone.pdf); [html.it](https://www.html.it/pag/15842/testi-amministrativi-accessibili-teoria/)
- Sintesi didattiche riportano: frasi oltre 25 parole difficili; una informazione per frase; limitare sigle e abbreviazioni — [Istituto Calvino, slide](https://www.istitutocalvino.edu.it/old/wp-content/uploads/2008/09/comscuola_1.pdf). *Non verificato sul testo della direttiva.*

**Direttiva Baccini (2005)** — fonti *secondarie*
- Data indicata come 24 ottobre 2005 dalla dispensa Sapienza; un articolo Unimi indica invece l'8 maggio 2005 (discrepanza da verificare). Collega la leggibilità alla brevità di parole e frasi e raccomanda il linguaggio comune e "soprattutto" il vocabolario di base — [Sapienza, linee guida testi](https://www.uniroma1.it/sites/default/files/allegati/linee_guida_testi.pdf); [riviste.unimi](https://riviste.unimi.it/index.php/promoitals/article/download/23830/21241/71344)
- Una rassegna accademica segnala il rischio che le direttive del 2002 e del 2005 portino a un impoverimento della lingua — [riviste.unimi](https://riviste.unimi.it/index.php/promoitals/article/download/23830/21241/71344)

**Codice di stile (Cassese, 1993) e Manuale di stile (Fioritto, 1997)**
- Codice di stile delle comunicazioni scritte ad uso delle amministrazioni pubbliche, promosso dal ministro della Funzione Pubblica Sabino Cassese, Roma, Istituto Poligrafico dello Stato, 1993. *Manuale di stile. Strumenti per semplificare il linguaggio delle amministrazioni pubbliche*, a cura di A. Fioritto, Dipartimento della Funzione Pubblica, Bologna, Il Mulino, 1997 — [Sapienza, Scrivere con Sapienza 2021](https://www.uniroma1.it/sites/default/files/field_file_allegati/scrivereconsapienza_2021.pdf); [riviste.unimi](https://riviste.unimi.it/index.php/promoitals/article/download/23828/21239/71340). *Non ho trovato online regole puntuali citabili da questi due testi.*

**ITTIG-CNR e Accademia della Crusca, "Guida alla redazione degli atti amministrativi. Regole e suggerimenti" (Firenze, 2011)**
- Prodotta da un gruppo promosso da ITTIG e Crusca; la parte linguistica è di A. Frati e S. Iannizzotto; il modello è il manuale delle Regioni *Regole e suggerimenti per la redazione dei testi normativi* (2007) — [Crusca, presentazione della parte linguistica](https://accademiadellacrusca.it/sites/www.accademiadellacrusca.it/files/page/2014/01/10/la_parte_linguistica_della_guida.pdf); PDF completo ospitato da [Regione Siciliana](https://www.regione.sicilia.it/system/files/2022-12/Guida%20alla%20redazione%20degli%20atti%20amministrativi%20del%20CNR%20in%20collaborazione%20con%20Accademia%20della%20Crusca.pdf)
- Indice delle regole linguistiche: stile; brevità del periodo; connessioni tra frasi; coordinazione; enumerazioni; condizionali e congiunzioni; frasi negative; modi, tempi e persone; dovere/potere; attivo, passivo e impersonale; pronomi; scelta delle parole; termini tecnici; polisemia e definizioni; arcaismi, latinismi e neologismi; forestierismi; nomi di mestiere; coerenza terminologica; sigle; maiuscole; punteggiatura; numeri; date; unità di misura; verifica finale — [Crusca](https://accademiadellacrusca.it/sites/www.accademiadellacrusca.it/files/page/2014/01/10/la_parte_linguistica_della_guida.pdf)
- Esempio di regola (n. 7): "Preferire, quando è possibile, le frasi affermative" ed "Evitare le frasi con la doppia negazione". La negazione può avere valore attenuativo e indurre letture possibiliste ("ingresso non autorizzato" contro "è vietato l'ingresso"). Esempio di riscrittura di un "Considerato che...": da 73 a 37 parole — [Crusca](https://accademiadellacrusca.it/sites/www.accademiadellacrusca.it/files/page/2014/01/10/la_parte_linguistica_della_guida.pdf)

**Piemontese / Due Parole**
- *Due Parole* è il "Mensile di facile lettura" ideato da Emanuela Piemontese (Sapienza), con un titolo ispirato a De Mauro — [Palestra della scrittura, intervista](https://www.palestradellascrittura.it/?p=4826). Era scritto in lingua controllata nel lessico e nella sintassi (Piemontese 1996) ed è il corpus "facile" di READ-IT — [READ-IT](https://aclanthology.org/W11-2308.pdf). *Non ho trovato online le regole puntuali di "Capire e farsi capire" (Piemontese 1996).*

### Inferences
- Checklist automatizzabile ricavata da queste regole, con i livelli di evidenza:
  - (a) frase > 25 parole = avviso, > 40 = errore (regola condivisa da Cortelazzo, Polimi e Frattini; evidenza da esperti);
  - (b) più di 1 subordinata incassata = avviso;
  - (c) gerundio o participio presente/passato in funzione di subordinata, soprattutto a inizio frase o in catena (≥ 2 forme implicite nella stessa frase) = avviso;
  - (d) inciso tra virgole, parentesi o lineette che separa soggetto e verbo, lungo più di 8 parole = avviso;
  - (e) doppia negazione o litote = errore;
  - (f) passivo senza complemento d'agente = avviso, da valutare;
  - (g) "si" impersonale o passivante seguito da verbi di comunicazione ("si precisa / si evidenzia / si sottolinea / si ritiene") = errore di stile;
  - (h) nominalizzazioni rilevate tramite suffissi (-zione, -mento, -tura, -anza/-enza, -ità) retti da verbi generici (effettuare, procedere a, provvedere a, porre in essere, dare luogo a, mettere in atto, svolgere un'attività di) = errore;
  - (i) connettivi complessi da una lista nera (al fine di, nel caso in cui, qualora, in ordine a, in merito a, relativamente a, in ottemperanza a, sulla base di, a fronte di) = avviso;
  - (j) sigla senza scioglimento alla prima occorrenza = errore;
  - (k) forestierismo con equivalente italiano corrente, da una lista curata, = avviso;
  - (l) congiuntivo introdotto da congiunzione complessa = avviso.
- Per un libro, a differenza di un atto amministrativo, alcune regole vanno temperate: la prima persona e il "noi" sono consigliati; alcune frasi lunghe ben costruite, con elenchi o coordinate, sono accettabili (Cortelazzo stesso distingue i casi); la variazione della lunghezza delle frasi serve al ritmo narrativo.

### Gaps
- Testi originali di Frattini 2002, Baccini 2005, Codice Cassese 1993, Manuale Fioritto 1997 e Piemontese 1996 non consultati: le loro regole puntuali non sono verificate.
- Non ho trovato regole italiane specifiche sulla scrittura dei numeri (cifre o lettere) oltre all'indice della guida ITTIG-Crusca, che dedica una sezione a "Scrittura dei numeri" ma il cui contenuto non ho letto.

---

## 5. ISO 24495-1:2023 ed EU "How to write clearly": principi trasferibili all'italiano

### Takeaway
La norma ISO definisce il linguaggio chiaro con quattro principi incentrati sul lettore: rilevante, reperibile, comprensibile, utilizzabile. Solo circa il 7% delle sue indicazioni riguarda la scelta delle parole, e la norma non fissa soglie di lunghezza della frase. La guida della Commissione UE dà invece cifre concrete: in media 20 parole per frase, documenti al massimo di 15 pagine, verbi al posto dei sostantivi, forma attiva con l'agente nominato.

### Cited Findings
- ISO 24495-1:2023 *Plain language — Part 1: Governing principles and guidelines*: principi e linee guida per documenti in linguaggio chiaro, soprattutto testuali, cartacei o digitali — [Standards NZ](https://www.standards.govt.nz/shop/iso-24495-12023)
- I quattro principi: "Readers get what they need" (relevant); "Readers can easily find what they need" (findable); "Readers can easily understand what they find" (understandable); "Readers can easily use the information" (usable). La norma ha circa 485 indicazioni, di cui solo il 7% sulla scelta delle parole ("using words that your readers know", "using clear sentences"), e non contiene regole sulla lunghezza delle frasi — [IPLF, ISO standard](https://www.iplfederation.org/iso-standard/)
- Struttura delle linee guida: Principio 1 = identificare i lettori, il loro scopo e il contesto; Principio 2 = struttura, information design, titoli; Principio 3 = scelta delle parole, chiarezza di frasi e paragrafi, tono, coesione; Principio 4 = valutazione continua, test con i lettori, monitoraggio dell'uso — [Standards Australia AS ISO 24495.1](https://store.standards.org.au/product/as-iso-24495-1-2024); [iiiD](https://perspectives.iiid.net/iso-plain-language-standard/)
- La norma è stata redatta da esperti di 25 paesi e 19 lingue e si basa su una definizione di plain language adottata nel 2014 — [iTeh](https://iteh.es/catalog/standards/iso/5266c5b6-e44a-4e68-9600-82b2a8932fc2/iso-24495-1-2023); [IPLF](https://www.iplfederation.org/iso-standard/)
- Altre parti: Parte 2 (comunicazione giuridica) pubblicata ad agosto 2025; Parte 3 (scrittura scientifica, per lettori con istruzione e formazione diverse) pubblicata a maggio 2026; altre parti in sviluppo (certificazione, document design) — [IPLF](https://www.iplfederation.org/iso-standard/). *La Parte 3 potrebbe interessare per la divulgazione scientifica sulle emozioni.*
- Guida UE "How to write clearly" (DG Traduzione), 10 suggerimenti: pensare prima di scrivere; mettere al centro il lettore; dare forma al documento; KISS; strutturare le frasi; "Cut out excess nouns — verb forms are livelier"; essere concreti e non astratti; "Prefer active verbs to passive — and name the agent"; attenzione a falsi amici, gergo e abbreviazioni; rivedere e controllare. Cifre indicative: "1 document = 15 pages at the most; 1 sentence = 20 words on average (but sprinkle in a few short sentences!)". Esempi di de-nominalizzazione: "carry out an evaluation of" → evaluate; "give consideration to" → consider. Il passivo resta ammesso quando l'agente è ovvio — [EU, How to write clearly (EN, 2011/2020)](https://www.cef-see.org/mnt/webdata/static/fisr/2020_How%20to%20write%20clearly.pdf). Esiste un'edizione italiana, "Scrivere chiaro", con il suggerimento 8: "Preferite la forma attiva dei verbi, accertandovi che sia chiaro il soggetto" — [unisi.it](https://www.unisi.it/sites/default/files/allegati/how_to_write_clearly_it.pdf)

### Inferences
- Dall'ISO arrivano soprattutto controlli non lessicali, utili a un LLM per capitolo:
  - c'è un "perché dovrebbe importarti" iniziale, cioè la rilevanza per il lettore PMI;
  - i titoli e i sottotitoli permettono di trovare le informazioni (reperibilità);
  - c'è un riepilogo o una "cosa fare lunedì mattina" (utilizzabilità);
  - il testo viene provato con lettori reali (la norma richiede il test con i lettori).
  Per il libro questo significa un piccolo panel di 3-5 imprenditori o manager che leggono un capitolo e rispondono a domande di comprensione (una sorta di cloze o domande aperte). È l'unico controllo con validità diretta.
- La media UE di 20 parole e il tetto italiano di 25 sono compatibili. Proposta: media del capitolo tra 15 e 20 parole, 90° percentile ≤ 30, nessuna frase oltre 40 senza giustificazione (per esempio un elenco).

### Gaps
- Testo completo della ISO 24495-1 non consultato (a pagamento). Non ho verificato se esista la traduzione UNI.
- Non ho verificato se il PDF italiano dell'UE e quello del 2020 riportino cifre identiche (20 parole, 15 pagine).

---

## 6. Problemi tipici dell'italiano: nominalismo, burocratese, si impersonale o passivante, catene di gerundi e participi, enclitiche, incisi, "antilingua"

### Takeaway
I difetti specifici dell'italiano scritto formale sono ben descritti. Le nominalizzazioni sono spesso rette da verbi vuoti. L'impersonale e il "si" nascondono l'agente. Le forme implicite (gerundio, participio) rendono ambigui soggetto e legame logico. Incisi lunghi separano soggetto e verbo. Ci sono connettivi complessi, congiuntivi evitabili, catene di complementi senza verbo, pseudo-tecnicismi ed eufemismi, cioè l'"antilingua" di Calvino. Quasi tutti si possono intercettare con espressioni regolari o con l'analisi sintattica.

### Cited Findings
- **Antilingua**: Italo Calvino, "L'antilingua", *Il Giorno*, 3 febbraio 1965. Un brigadiere trascrive la deposizione di un testimone (la cantina, la stufa, il fiasco di vino) trasformando ogni parola concreta in burocratese ("dichiara d'essere casualmente incorso nel rinvenimento di un quantitativo di prodotti vinicoli"). Calvino lo chiama "terrore semantico", cioè la fuga da ogni parola che abbia di per sé un significato. Secondo lui l'antilingua è scritta da avvocati, funzionari, ministeri e redazioni — [Il Post](https://www.ilpost.it/2018/05/09/come-non-scrivere/); [Internazionale, "Il terrore semantico"](https://www.internazionale.it/opinione/giulia-zoli/2012/07/05/il-terrore-semantico); [Filodiritto](https://www.filodiritto.com/italo-calvino-lantilingua-giuridica). Le citazioni circolano con piccole varianti: per citazioni esatte va usata l'edizione delle opere di Calvino.
- **Nominalizzazione**: lo scritto usa più sostantivi del parlato, lo scritto amministrativo ancora di più. Effetto: più astrazione e frasi dense — [Cortelazzo & Pellegrino, r. 20](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf). Locuzioni verbali astratte da sostituire: "provvedere alla copertura assicurativa" → assicurare; "prendere in esame" → esaminare (r. 27) — [ibid.](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf). Esempio tipico: "effettuare il pagamento" → pagare — [lentepubblica](https://lentepubblica.it/?p=433397)
- **Catene di parole senza verbo**: "quanto previsto da, in materia di, a pena di decadenza del, sulla base di, in ottemperanza a, a motivo di, in conseguenza del" — [Polimi](https://www.areacre.polimi.it/pubblicazioni/guidascrittura.pdf). READ-IT misura lo stesso fenomeno come "catene di complementi incassati retti da un nome" (Repubblica 1,44 contro Due Parole 1,30) — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- **Si impersonale**: "Si precisa che...", "Si fa altresì presente..."; a volte è modestia, spesso è reticenza ("con la presente si respinge la richiesta"). Va sostituito con la 1ª persona plurale o con un soggetto esplicito — [Cortelazzo & Pellegrino, r. 19](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)
- **Passivo** senza agente che nasconde l'autore ("le tasse sono state aumentate") — [r. 18](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf); l'UE dice "name the agent" — [EU](https://www.cef-see.org/mnt/webdata/static/fisr/2020_How%20to%20write%20clearly.pdf)
- **Gerundio e participio**: "L'italiano burocratico fa grande uso del gerundio perché permette di costruire frasi più compatte, ma anche più complesse". Il soggetto del gerundio può essere ambiguo ("...definite dalle singole amministrazioni prevedendo..."), e così il tipo di legame (condizionale o temporale) — [r. 15](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf). READ-IT usa la distribuzione dei modi verbali come indicatore specifico dell'italiano — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- **Incisi**: interrompono legami stretti (nome e complemento, soggetto e verbo, verbo e oggetto); il rimedio è spostarli in fondo — [r. 16](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf). La lunghezza dei legami di dipendenza predice la complessità sintattica (Lin 1996; Gibson 1998, citati da READ-IT) — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- **Subordinata preverbale** ("Qualora..., i Dirigenti...") più difficile della postverbale (Miller & Weinert 1998, in READ-IT) — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- **Soggetto sottinteso** (pro-drop) a lungo raggio, che costringe a ricordare il soggetto da una frase all'altra — [r. 21](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)
- **Pseudo-tecnicismi, stereotipi, eufemismi**: "corrispondere", "porre in essere", "esondare", "competente carta da bollo", "Con la presente siamo a comunicarvi", "trapasso" — [r. 24, 25, 28](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)
- **Forestierismi**: la Crusca (Gruppo Incipit, 2022) ha criticato una circolare ministeriale per termini come "preparedness" e "readiness" — [Il Fatto Quotidiano](https://www.ilfattoquotidiano.it/2022/08/25/la-crusca-contro-i-ministeri-per-la-circolare-incomprensibile-su-scuola-e-covid-troppe-parole-inglesi-e-linguaggio-oscuro/6773850/). Nel 2020 Funzione Pubblica e Crusca hanno firmato un accordo contro il burocratese — [Italia Oggi via segretaricomunalivighenzi](https://www.segretaricomunalivighenzi.it/?p=12445)

### Inferences
- Pattern regex e analisi sintattica per uno script, tutti euristici:
  - verbi vuoti + nominalizzazione: `\b(effettu|proced|provved|pon|d[aà]r|mett|svolg|esplet|attu)\w*\s+(a(l|lla|ll')?|in|un[a']?|l[a'])?\s*\w+(zione|zioni|mento|menti|tura|anza|enza|ità)\b`;
  - si + verbi di comunicazione: `\bsi\s+(precisa|evidenzia|sottolinea|ritiene|rileva|fa presente|comunica|ribadisce)\b`;
  - enclitiche burocratiche: `\b\w+(asi|esi|isi)\b` filtrato su una lista (trattasi, allegasi, dicesi, vedasi, rendesi, ritiensi);
  - gerundi: `\b\w+(ando|endo)\b`, con conteggio per frase e segnalazione se ≥ 2 o se in apertura di frase;
  - participi assoluti a inizio frase: "Considerato che", "Visto", "Premesso che", "Fatto salvo";
  - congiunzioni complesse: lista nera (qualora, nel caso in cui, laddove, ove, allorché, onde, al fine di, in ordine a, in merito a, a fronte di, ai sensi di);
  - litoti e doppie negazioni: `\bnon\s+(in|im|ir|dis)\w+\b` e "non ... non";
  - sigle: `\b[A-Z]{2,}\b` senza forma estesa nei 200 caratteri precedenti alla prima occorrenza.
- Le enclitiche arcaiche (trattasi, allegasi) sono un tratto noto del burocratese, ma *non ho trovato una fonte autorevole che le tratti esplicitamente*: vedi Gaps. In un libro su emozioni e PMI saranno rare. Il rischio più probabile è il "gergo aziendale-anglo" (engagement, mindset, leadership, burnout, feedback), da gestire con la lista fuori VdB.
- Compiti adatti all'LLM, non allo script: trovare l'antilingua semantica (astrazioni senza referente concreto, per esempio "la dimensione emotiva della governance relazionale"); proporre la riscrittura con verbo + soggetto agente; verificare che ogni astrazione sia ancorata a un esempio concreto o a una scena (coerente con la regola 27 "parole concrete" e con l'UE "be concrete, not abstract").

### Gaps
- Nessuna fonte autorevole trovata sulle enclitiche burocratiche (trattasi, allegasi) come categoria nelle linee guida: probabilmente sono trattate nella sezione "Arcaismi, latinismi" della guida ITTIG-Crusca, ma non l'ho verificato.
- Nessuno studio quantitativo trovato su frequenze di nominalizzazioni, gerundi o si impersonale nella saggistica italiana da usare come benchmark.

---

## 7. Benchmark: lunghezza media della frase e Gulpease di prosa giornalistica e saggistica italiana

### Takeaway
Non ho trovato benchmark sistematici e recenti sulla lunghezza media della frase nei quotidiani o nella saggistica divulgativa italiana. Le cifre disponibili sono indicazioni di esperti (25 parole al massimo; 20 di media nella guida UE), un test Gulpease del 1997 su quattro quotidiani (45-56), le misure sintattiche Repubblica/Due Parole di READ-IT e circa 35 parole per periodo nell'italiano parlamentare (Europarl).

### Cited Findings
- Test de *l'Unità* (1997) sullo stesso articolo (notizia Enel) in quattro quotidiani: Corriere della Sera 56,13; La Stampa 51,55; La Repubblica 45,23; l'Unità 44,78. È un solo testo per testata, quindi non è generalizzabile — [l'Unità, 8/3/1997](https://archivio.unita.news/assets/main/1997/03/08/page_013.pdf) (dati riportati da una sintesi del motore di ricerca; il PDF non è stato riletto).
- Testi della PA con contenuti complessi: un Gulpease intorno a 50 è già "un buon risultato"; le 30 regole stesse stanno intorno a 50 — [Cortelazzo & Pellegrino](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf)
- Corpus Europarl: l'italiano ha circa 35 parole per periodo contro 24,1 del danese. L'autore avverte che il numero di parole per frase "non è necessariamente indicativo" di complessità — [Korzen, Atti SLI LIV](https://www.societadilinguisticaitaliana.net/wp-content/uploads/2022/11/023_Korzen_Atti_LIV_Congresso_SLI.pdf)
- Repubblica contro Due Parole (READ-IT): altezza dell'albero 5,71 contro 3,67; sintagmi verbali per frase 2,40 contro 1,25; subordinate 34,9% contro 20,3% — [READ-IT](https://aclanthology.org/W11-2308.pdf)
- Indicazioni normative: in media 20 parole per frase (UE) — [EU](https://www.cef-see.org/mnt/webdata/static/fisr/2020_How%20to%20write%20clearly.pdf); circa 25 parole come limite (Cortelazzo, Polimi, Frattini come riportata) — [30 regole](https://www.unifg.it/sites/default/files/2021-06/30_reg_txt_amm_chr_0.pdf); [Polimi](https://www.areacre.polimi.it/pubblicazioni/guidascrittura.pdf)
- Uno studio del 2022 sui siti istituzionali italiani ha trovato, con il Gulpease, "barriere significative" alla comprensione, soprattutto per gli utenti meno istruiti — [Italiano LinguaDue 2022, DOAJ](https://doaj.org/article/485613c5c2a0471ab0185e8990609754) (solo abstract).
- Studi esistenti ma non accessibili: Gallitelli, Laurenti, Parks su *Tradurre* confrontano la lunghezza media del periodo nei romanzi italiani e in quelli tradotti dall'inglese (corpus di 5.471.600 token) — [Tradurre](https://rivistatradurre.it/romanzi-italiani-e-romanzi-tradotti-dallinglese/); Sciumbata (2023) ha analizzato Due Parole, due quotidiani e il parlato — [arts.units.it](https://arts.units.it/handle/11368/3051299) (accesso chiuso).

### Inferences
- Per avere un benchmark affidabile e coerente con il libro, conviene costruirlo: applicare lo stesso script (Gulpease, distribuzione della lunghezza delle frasi, percentuale fuori VdB, profondità sintattica) a 3-5 saggi divulgativi italiani di successo su temi vicini (business, psicologia) e a un campione di articoli de *Il Sole 24 Ore*, e confrontare il manoscritto con queste distribuzioni. È più difendibile di qualsiasi soglia astratta.
- Valori obiettivo provvisori per il libro, da sostituire con il benchmark costruito:
  - Gulpease di capitolo ≥ 55 (sopra i quotidiani del 1997, sotto il "facile" di Due Parole);
  - media di 15-20 parole per frase, con alta varianza (frasi brevi alternate);
  - 90° percentile ≤ 30 parole;
  - frasi > 40 parole ≤ 1-2% del totale;
  - subordinate ≤ 30% delle proposizioni;
  - profondità media dell'albero < 5.

### Gaps
- Nessun dato sistematico e recente trovato su lunghezza media della frase o Gulpease della saggistica divulgativa italiana o della stampa economica.
- I numeri dell'Unità del 1997 vengono dal riassunto del motore di ricerca: andrebbero riletti sul PDF originale.
- Lo studio *Tradurre* e il capitolo Sciumbata 2023 contengono probabilmente cifre utili, ma non le ho estratte (il PDF di *Tradurre* ha una codifica che non sono riuscito a decodificare; Sciumbata è ad accesso chiuso).

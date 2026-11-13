# Guida ai criteri di revisione dei capitoli

Aggiornata al 13 novembre 2026. Ricava i criteri dalla revisione dei capitoli 1, 2 e 3: ramo `claude/ecstatic-ramanujan-j1mpzn`, schede dell'autore sul commit `9c724e6`. Serve a rivedere i capitoli successivi con gli stessi criteri.

Da usare insieme a [`PROMPT_REVISIONE_CAPITOLO.md`](PROMPT_REVISIONE_CAPITOLO.md), il prompt che si dà al modello un capitolo alla volta.

## 1. Che cosa è il libro e per chi si rivede

*Le Emozioni Arrivano Prima di Noi* è saggistica narrativa sulle emozioni nel lavoro, per manager e imprenditori di PMI. Il lettore è colto ma non specialista, e legge la sera, stanco. Ogni capitolo alterna una storia di filiera (Omnia, O.M.P. Precision, NexSys, LogiDistretto, Studio Colombo) e la spiegazione di ciò che è accaduto.

**Scopo della revisione.** Un capitolo deve essere:
- chiaro per chi lo legge;
- prudente sulla scienza e sui personaggi;
- coerente con gli altri capitoli;
- scritto con la stessa voce.

Non si riscrive il libro: si toglie ciò che pesa, ciò che è falso o non verificato e ciò che dice più di quanto il testo sappia.

## 2. Gerarchia delle fonti

1. **Canone dei capitoli 1-3:** il testo rivisto in `capitoli/` (revisione di novembre). L'ambientazione resta quella veronese dei capitoli. `reports/correzioni/BIBBIA_CANONICA.md` e `MAPPA_TERRITORIALE.md` (bonifica di ottobre, rami `bonifica/*`) sono **solo da consultare**.
2. `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md`: personaggi, età, ruoli, cifre, date.
3. `progetto/03_GUIDA_STILISTICA.md`: voce, «tu», tono, aperture, scene, dialoghi, ritmo.
4. `riferimenti/CONTEXT.md` e il glossario confermato del capitolo 3, voci G1-G14 in `reports/struttura/CAP03_REGISTRO_MODIFICHE.md`.
5. Fonti scientifiche: `progetto/06_REGISTRO_DELLE_FONTI.md`, `progetto/07_REGISTRO_DELLE_AFFERMAZIONI_SCIENTIFICHE.md`, `progetto/10_FONTI_CAPITOLO_1.md`, `progetto/16_FONTI_CAPITOLO_2.md`, `riferimenti/DOSSIER_FONTI_TEMATICHE_CAPITOLI.md`.

Se due fonti si contraddicono, non si sceglie in silenzio: si segnala all'autore.

## 3. Le regole che non cambiano

1. **Non inventare.** Niente fatti, cifre, nomi, battute, scene o riferimenti scientifici nuovi. Si può tagliare, spostare, unire, dividere e riformulare. Unica eccezione: una battuta costruita **solo** con fatti già presenti nel capitolo, dichiarata nel registro. Esempio nel cap. 3: «Quello che so è che manca qualcosa sulla perizia e che giovedì devo pagare centotrentottomila euro. Tutto il resto lo temo.»
2. **Le decisioni sono dell'autore.** Se serve materiale nuovo o una scelta di merito, si domanda e si aspetta.
3. **Prima la struttura, poi le frasi.** Un intervento di frase su un paragrafo che la struttura ha già riscritto è «superato».
4. **La voce resta quella del libro.** Una frase più semplice deve sembrare scritta dallo stesso autore.
5. **Si tocca un solo capitolo.** Le incoerenze con altri capitoli si annotano, non si correggono.

## 4. I criteri, in dieci famiglie

Gli esempi «prima → dopo» sono veri: si ritrovano con `git diff 9c724e6 -- capitoli/`.

### C1. Personaggi: ipotesi, non certezze
- Intenzioni, cause e diagnosi sugli altri diventano **ipotesi o domande**. Il narratore non legge nella mente dei personaggi.
- Un personaggio non descrive ciò che non ha visto né sentito.
- Le certezze di un personaggio restano sue: il testo le marca come sue.
- Esempi:
  - cap. 1: «Zucchero sull'offesa» diventa «Per Andrea era zucchero sull'offesa».
  - cap. 1: «Dalla bocca di nessuno dei due era uscita una sillaba» diventa «Di quello che si erano detti, Andrea non aveva sentito una sillaba».
  - cap. 1: Elena non attribuisce più cause certe («hai la gastrite… ti aspetti che…»). Le trasforma in domanda: «Quanto può aver pesato, oggi?».
  - cap. 2: «Davide era fuggito via» diventa «era uscito». Roberto non descrive più il viso di Sara, che non aveva visto: descrive il tono della telefonata.

### C2. Scienza: prudenza e misura
- **Modelli come modelli:** Barrett è un «modello teorico influente»; per LeDoux, «secondo il suo modello».
- Studi su animali o di laboratorio si dichiarano tali. Esempi: LeDoux, studi «soprattutto sugli animali»; Vervliet, «partecipanti sani», proposta «con cautela».
- **Niente numeri né neurotrasmettitori di enfasi** (bpm, noradrenalina, cortisolo, «da settanta a centotrenta»).
- **Niente formule spettacolari:** «collasso metabolico», «droga biologica», «potente ricompensa biologica», «declinazione perfetta».
- Sistema 1 e Sistema 2 di Kahneman **non sono personaggi**: «Non sappiamo che cosa sia accaduto davvero nella sua testa».
- Si distingue ciò che il racconto mostra, ciò che il modello propone e ciò che non si può sapere.
- **Pochi autori per capitolo.** Il libro non ha note: un nome che non regge da solo nel testo si toglie (Lakoff, cap. 1). Ogni autore citato deve essere nelle schede delle fonti. Se manca, si segnala, come per Watzlawick.

### C3. Dettagli tecnici, normativi e giuridici non verificati
- Ciò che non è verificato si toglie o si rende generico. Esempi:
  - cap. 3: niente «Fondo Centrale di Garanzia», «circolare ministeriale», «ente certificatore di terzo livello», «Corte dei Conti», «Fascicolo FCG-…», «fuori sacco». La Bignami motiva il rinvio senza norme: «abbiamo prestato il denaro su una stima che nessuno ha controllato».
  - cap. 2: tolti l'«Addendum Formale… al CCNL», la sospensione di trenta giorni e il licenziamento automatico per giusta causa. Ora «la contestazione riprende il suo corso».
- Conseguenze disciplinari, sanitarie, contabili e bancarie precise si rimettono solo dopo la verifica di un professionista. Si segnalano nel registro alla voce «Per l'autore».

### C4. Densità tecnica e descrittiva
- Via marchi, specifiche, linguaggi di programmazione e arredi che non servono alla trama. Esempi:
  - cap. 2: Mori Seiki, ethernet, 7075-T6, «Ra 1.4 / Ra 0.8», che diventano «rugosità quasi doppia rispetto al limite prescritto»;
  - cap. 3: Rust, MacBook, Archimede.
- Restano i dettagli che spiegano la trama. Esempio: la sonda non tarata del cap. 2, che prepara la diagnosi di Marta.
- Via le iperboli somatiche: «detonazione nucleare», «voragine di disonore», denti che battono. Resta **un** segnale corporeo dominante, coerente con il registro della continuità (per Sara, lo stomaco).

### C5. Finali e accordi non consolatori
- Niente unanimità («Diciotto mani si alzarono all'unisono» diventa «Accettarono.»), né trasformazioni definitive del personaggio.
- L'accordo dell'Atto IV è una **proposta sobria**:
  - dati, regole o perimetri operativi;
  - accordo raggiunto, firme apposte e adempimenti futuri distinti tra loro;
  - nessuna etichetta come «Contratto di Salvaguardia di Processo», tolta anche dalla prefazione.
- Le soluzioni non producono cifre da giustificare. Esempio, cap. 3: gli stipendi «in due tempi», senza 50% e senza saldo rinviato.

### C6. Rischio reale ed esito non accertato
- Il capitolo deve reggere anche se l'esito fosse stato sfavorevole. Esempio, cap. 3: il rischio di liquidità è reale, il rifiuto e il fallimento non sono accertati.
- Domanda cardine, nella stessa forma in teoria, scena ed esercizio: **«A che cosa sta reagendo il mio corpo in questo preciso istante: a un fatto presente, a un rischio plausibile o a un esito che sto dando per accertato?»**
- Nell'esercizio la qualità della scelta si distingue dall'esito.

### C7. Struttura del capitolo
- Via le ripetizioni: una distinzione si spiega una volta; i riepiloghi della scena non si ripetono.
- Le sezioni ridondanti si fondono. Esempio, cap. 1: «L'emozione è reale» confluita in «Il segnale è reale, la causa va verificata».
- Ingresso nella teoria esplicito: si parte dalla scena o da un'obiezione del personaggio, poi il concetto.
- Esempi pochi e diversi: in cap. 1 restano la coppia e l'amico.
- **Apparati finali uniformi:**
  - «## Mettilo in pratica» con passi numerati, eventualmente seguito da una domanda (cap. 2: «Mettilo in pratica: chi paga il sollievo?»);
  - «## Da ricordare» con 4-5 punti;
  - un raccordo al capitolo successivo, senza l'etichetta del ponte né il titolo «Apparati operativi e continuità».
- **Esercizio** allineato ai gesti e alle parole della scena, con una domanda di verifica. Esempio, cap. 1: «Quale informazione potresti cercare per distinguere fra le due spiegazioni?».
- **Mappa minima:** una riga in grassetto, non una formula LaTeX, che in impaginazione rischia di uscire come codice grezzo.

### C8. Coerenza interna
- Giorni e date tornano col calendario. Esempio, cap. 3: venerdì 21, quindi il 27 è giovedì.
- Tornano anche orari, turni, cronologie e oggetti in scena:
  - cap. 1: il coltello, posato una sola volta;
  - cap. 2: il lotto «partito», non «pronto»; i turni di Davide; lo straordinario di Marta.
- Un solo nome per la stessa cosa: un'unica perizia («del software») e un'unica banca nel capitolo.
- Glossario: le scelte confermate (G1-G14) si applicano. Esempi: «circuito difensivo di sopravvivenza», «panico da anticipazione», «fatto osservabile», «fidi».
- Ogni cifra o nome tolto si giustifica nel registro.

### C9. Frase e leggibilità
- Si spezzano le frasi lunghe dove ostacolano la lettura, non per alzare il numero.
- Le metriche (`strumenti/metriche_leggibilita.py`) sono un controllo:
  - capitoli 1-3 rivisti: Gulpease da 58,7 a 64,3; frasi oltre 35 parole tra 1,6% e 4,5%;
  - capitoli 4-9: Gulpease tra 48,9 e 52,9; frasi oltre 35 parole tra 10% e 15%;
  - prefazione ed epilogo: Gulpease 41-42; frasi oltre 35 parole circa 32%.
- Dialoghi: battute brevi, gesti tra una battuta e l'altra, attribuzioni solo se servono. Una battuta-saggio si divide in più interventi; esempio: la proposta di Sara a Marta nel cap. 2.
- Il «tu» al lettore va usato con misura: invita, non accusa né diagnostica (guida stilistica, § 3).

### C10. Processo e tracciabilità
- Un ramo per capitolo; un commit per la struttura e uno per frasi e glossario, oppure un commit per scheda.
- **Due fermate per l'autore:**
  - la prima dopo la diagnosi (scheda e domande);
  - la seconda dopo l'applicazione (testo, registro, punti aperti).
- **Verifica dei fatti** con `git diff`: ogni cifra, data e nome che manca deve risultare «tolto di proposito».
- **Registro** `reports/struttura/CAPxx_REGISTRO_MODIFICHE.md` con queste sezioni: interventi (punto, stato, nota), verifica dei fatti, metriche prima e dopo, «Per l'autore», e rifiniture successive.

## 5. Procedura per un capitolo

1. Leggere il capitolo intero, poi le fonti del § 2 e i registri dei capitoli 1-3, che sono il modello.
2. Misurare il capitolo con `python3 strumenti/metriche_leggibilita.py capitoli/<file>`.
3. **Diagnosi:** compilare una scheda numerata. Ogni punto ha passo citato, criterio violato, proposta e domanda per l'autore se serve. Massimo 8-10 punti, dal più grave.
4. **Prima fermata:** l'autore approva, corregge o respinge i punti.
5. Applicare prima i punti di struttura, poi quelli di frase e glossario.
6. Verificare i fatti, rifare le metriche e controllare i raccordi con il capitolo precedente e il successivo.
7. Scrivere il registro delle modifiche.
8. **Seconda fermata:** l'autore rilegge. Le rifiniture si annotano nel registro.

## 6. Checklist finale

- [ ] Nessun fatto, cifra, nome, scena o fonte nuova.
- [ ] Ogni elemento tolto è dichiarato nel registro.
- [ ] Intenzioni e diagnosi sui personaggi sono ipotesi; nessuno descrive ciò che non ha visto.
- [ ] La scienza è presentata come modello; nessun numero o neurotrasmettitore di enfasi; autori citati presenti nelle fonti.
- [ ] Nessun dettaglio normativo, giuridico o bancario non verificato.
- [ ] Finale sobrio, accordo come proposta, rischio separato dall'esito.
- [ ] Apparati: «Mettilo in pratica», «Da ricordare» (4-5 punti), raccordo senza etichetta.
- [ ] Calendario, orari, turni, oggetti e glossario coerenti.
- [ ] Metriche prima e dopo riportate.
- [ ] La voce è quella del libro: letto ad alta voce, il capitolo regge.

## 7. Punti aperti ereditati

Da sapere prima di rivedere i capitoli 4-9, la prefazione e l'epilogo:
- **Banca.**
  - Il cap. 1 cita «Mediocredito» (la firma di Andrea); il cap. 3 ha scelto «Banca Popolare del Distretto» per NexSys. Se sono due istituti diversi va bene, ma va confermato.
  - Il cap. 5 alterna Banca Popolare e Mediocredito e nomina il Fondo Centrale di Garanzia, che il cap. 3 non cita più.
- **Glossario.** «La fucina dell'ansia predittiva», nell'ultima riga del cap. 2, non segue G7 («panico da anticipazione»). Il glossario G1-G14 va esteso e approvato sul libro intero; `reports/struttura/GLOSSARIO_PROPOSTO_CAP01-03.md` è solo una bozza.
- **Fonti.** Watzlawick resta nel testo per decisione dell'autore, che lo scheda in `progetto/10_FONTI_CAPITOLO_1.md` § 8.4. Le formulazioni su LeDoux, Barrett e Damasio nel cap. 3 vanno verificate sulle fonti.
- **Cap. 2.** Non è chiaro se il trasportatore di LogiDistretto delle 06:00 e il «corriere tedesco» delle 06:20 siano lo stesso. L'indennità di 350 euro e gli orari di Marta vanno confermati.
- **Lavoro della bonifica di ottobre.** I rami `bonifica/*` contengono correzioni ai capitoli 4-9 e all'epilogo (anni dell'azione, tolleranze, parco macchine, Zantedeschi, Deep POV) su un'altra ambientazione. Si possono consultare come elenco di problemi già individuati, ma le soluzioni territoriali non si applicano.

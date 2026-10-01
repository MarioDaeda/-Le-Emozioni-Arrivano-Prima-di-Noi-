# Proposte — Cap.05 «La solitudine dell'accentratore e la trappola della prima delega»

Stato: APPROVATA DALL'AUTORE — APPLICATA

File: `capitoli/CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md` (righe attuali, branch `bonifica/06-proposte`).

Il passo è nell'Atto III (teoria, L142–188) e negli apparati (L276, L293): qui la saggistica è ammessa (ADR 0002). Non si toccano scene, numeri o luoghi.

**Applicazione congiunta.** P2-19.Cap05 (L150) e P3-19.Cap05-b (L148) riguardano lo stesso blocco. Vanno approvati insieme o respinti insieme, perché L148 termina con i due punti che introducono la citazione. In fondo al file c'è il testo combinato pronto.

**Fonti consultate.**
- `DOSSIER_FONTI_TEMATICHE_CAPITOLI.md` (righe 40 e 244). Attribuisce la frase a Damasio, *Feeling & Knowing* (2021), «PDF p. 75». Riporta l'originale inglese: «In its unerring push for economy, nature did not bother to create new devices to handle the goodness or badness of our personal psychology or social condition. It makes do with the same mechanisms…».
- La cartella `fonti/biblioteca/` citata dal dossier non è presente nel repository, quindi non è stato possibile controllare il passo.
- Edizione italiana verificata in rete (solo titolo ed editore): A. Damasio, *Sentire e conoscere. Storia delle menti coscienti*, Adelphi, Milano 2022 (trad. di Isabella C. Blum). Non si indicano pagine: non sono state verificate.

---

## P2-19.Cap05 — Citazione virgolettata attribuita a Damasio (L150)
- Problema:
  - La citazione è in blocco, tra virgolette, senza edizione né pagina.
  - L'unico riscontro disponibile (il dossier) indica una pagina di PDF, non di edizione, e non è verificabile nel repository.
  - Il testo italiano non è una traduzione fedele dell'inglese riportato dal dossier: «unerring» (infallibile) diventa «implacabile»; «the same mechanisms» diventa «gli stessi meccanismi arcaici dell'omeostasi», con «arcaici» aggiunto; «nuovi dispositivi neurali» aggiunge «neurali».
  - La citazione non coincide nemmeno con l'edizione italiana Adelphi, che non è stata consultata.
  - Per la regola B19, una frase non verificabile con pagina ed edizione va convertita in parafrasi senza virgolette, con rinvio bibliografico.
- Passo attuale (riga 150): «> *«La natura, nella sua implacabile spinta all'economia, non si è data la pena di creare nuovi dispositivi neurali per gestire la bontà o la cattiveria della nostra condizione psicologica o sociale. Fa uso degli stessi meccanismi arcaici dell'omeostasi...»*»
- Proposta (paragrafo normale, non più blocco citazione, senza virgolette): «In *Sentire e conoscere* Damasio osserva che la natura, per economia, non ha creato dispositivi nuovi per gestire il bene o il male della nostra condizione psicologica e sociale: si serve degli stessi meccanismi che regolano la vita del corpo, ed è per questo che anche le situazioni sociali possono produrre dolore o piacere (A. Damasio, *Feeling & Knowing. Making Minds Conscious*, 2021; trad. it. *Sentire e conoscere. Storia delle menti coscienti*, Adelphi, 2022).»
- Motivazione:
  - La parafrasi conserva il contenuto che il dossier documenta (economia della natura, riuso dei meccanismi omeostatici, dolore e piacere sociali) senza attribuire a Damasio parole esatte non verificate.
  - Toglie «arcaici» e «neurali», che non risultano dall'originale riportato.
  - Il rinvio bibliografico è completo di autore, titolo, anno ed editore italiano, senza pagina inventata.
  - Grado di certezza sul contenuto: medio-alto. È coerente con la tesi di Damasio sull'omeostasi socioculturale (anche *Lo strano ordine delle cose*, 2018) e con il passo inglese del dossier.
  - Grado di certezza sulla formulazione esatta e sulla pagina: non verificabile.
- Alternativa (facoltativa): conservare la citazione virgolettata **solo** se l'autore la verifica sull'edizione Adelphi 2022, con la traduzione di Blum alla lettera e il numero di pagina. Forma: «*«…»* (A. Damasio, *Sentire e conoscere*, Adelphi, 2022, p. [da verificare])». In questo caso «implacabile», «arcaici» e «neurali» vanno sostituiti con le parole dell'edizione.
- Rischi / impatti su altri capitoli:
  - Lo stesso passo inglese (con la frase su vergogna e tradimento) è alla base di Cap.07 L128 (P2-19.Cap07). Conviene adottare la stessa forma di rinvio bibliografico nei due capitoli.
  - Il master `LIBRO_COMPLETO_…md` L1646 riporta la stessa citazione: andrà riallineato quando si rigenera il master. Non è oggetto di questa fase.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

## P3-19.Cap05 — Pertinenza della voce C19 al Cap.05

Verifica dei quattro tipi di problema C19 nel Cap.05:
- formule di Lazarus: **assenti**;
- «quiet quitting»: **assente**;
- dACC, dolore sociale, Eisenberger e Lieberman: **assenti**. La ricerca di «Lazarus», «quiet quitting», «dACC», «dolore sociale», «Eisenberger» e «Lieberman» nel Cap.05 non dà risultati;
- **sovrapposizione presentata come identità** e **attribuzione a Damasio di tesi non sue**: **presenti** in L146, L148, L152, L276 e L293.

Il libro estende il quadro omeostatico di Damasio al «ruolo professionale» e allo «status» dell'imprenditore. Damasio non ha formulato né dimostrato questa estensione, mentre il testo la presenta come sua e come coincidenza esatta di circuiti. Le parti su Porges (L158–160: neurocezione, sicurezza / pericolo / minaccia alla vita, complesso vagale ventrale, freno vagale) sono attribuzioni standard e non richiedono interventi.

### P3-19.Cap05-a — «Salvaguardia omeostatica del ruolo sociale teorizzata da Damasio»
- Problema: Damasio non ha teorizzato una «salvaguardia omeostatica del ruolo sociale». È un'estensione del libro costruita sul suo lavoro (omeostasi, marcatori somatici, omeostasi socioculturale). Anche la «neurocezione di pericolo da perdita di controllo» non è una formalizzazione di Porges: è l'applicazione della neurocezione (che è di Porges) alla delega.
- Passo attuale (riga 146): «è una disfunzione sistemica innescata dalla collisione tra due dispositivi neurobiologici primari: la **salvaguardia omeostatica del ruolo sociale** teorizzata da **Antonio Damasio** e la **neurocezione di pericolo da perdita di controllo** formalizzata da **Stephen W. Porges**.»
- Proposta: «è una disfunzione sistemica innescata dalla collisione tra due dispositivi neurobiologici primari: la **difesa omeostatica del ruolo sociale**, un'estensione che questo libro ricava dal lavoro di **Antonio Damasio** sull'omeostasi, e la **neurocezione di pericolo** descritta da **Stephen W. Porges**, qui applicata alla perdita di controllo.»
- Motivazione: distingue ciò che è degli autori (omeostasi, neurocezione) da ciò che è un'estensione del libro (ruolo sociale, perdita di controllo). Grado di certezza: alto.
- Rischi / impatti su altri capitoli: nessuno.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

### P3-19.Cap05-b — «Damasio dimostra che i circuiti … coincidono esattamente»
- Problema: è una sovrapposizione presentata come identità, con un verbo, «dimostra», più forte delle fonti. Damasio sostiene che le situazioni psicologiche e sociali *accedono* ai meccanismi dell'omeostasi. Non afferma che i circuiti della sopravvivenza «coincidono esattamente» con quelli dello status e del «ruolo professionale», categoria che non usa. Il «ruolo professionale» è l'estensione del libro.
- Passo attuale (riga 148): «Nelle sue opere seminali — da *L'errore di Cartesio* (1994) a *Feeling & Knowing* (2021) — Antonio Damasio dimostra che i circuiti neurali responsabili della sopravvivenza biologica dell'organismo coincidono esattamente con quelli deputati alla conservazione dello status sociale e del ruolo professionale:»
- Proposta: «Nelle sue opere — da *L'errore di Cartesio* (1994) a *Sentire e conoscere* (*Feeling & Knowing*, 2021) — Antonio Damasio sostiene che la regolazione della vita non dispone di un apparato separato per le faccende sociali: i meccanismi che valutano lo stato dell'organismo vengono reclutati, in parte, anche dalle situazioni psicologiche e sociali. Questo libro ne trae un'ipotesi di lavoro: lo status e il ruolo professionale possono attivare gli stessi allarmi corporei che segnalano un pericolo fisico.»
- Motivazione: «sostiene» e «in parte» sostituiscono «dimostra» e «coincidono esattamente», secondo la formula prudente chiesta dal registro («circuiti in parte sovrapposti»). L'estensione al ruolo è dichiarata come ipotesi del libro. Il titolo italiano dell'edizione Adelphi è affiancato all'originale. La frase non termina più con i due punti, così da reggere la parafrasi di P2-19.Cap05. Grado di certezza: alto sulla correzione del verbo; medio-alto sulla sintesi della tesi di Damasio.
- Rischi / impatti su altri capitoli: va applicata insieme a P2-19.Cap05 (vedi testo combinato).
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

### P3-19.Cap05-c — «codificati a livello dell'insula e della corteccia prefrontale ventromediana come indicatori primari di sopravvivenza biologica»
- Problema: è una localizzazione neuroanatomica presentata come dato acquisito («sono codificati»), senza fonte e attribuita implicitamente a Damasio. Insula e corteccia prefrontale ventromediana hanno un ruolo nella rappresentazione degli stati corporei e nei marcatori somatici (Damasio 1994; Bechara e Damasio). Non esiste però un risultato che mostri che «controllo», «primato tecnico» e «reputazione» vi siano codificati «come indicatori primari di sopravvivenza biologica».
- Passo attuale (riga 152): «Il controllo totale sulle decisioni, il primato tecnico e la reputazione di infallibilità di fronte alla comunità territoriale non rappresentano fattori accessori di prestigio: sono codificati a livello dell'insula e della corteccia prefrontale ventromediana come **indicatori primari di sopravvivenza biologica**.»
- Proposta: «Il controllo totale sulle decisioni, il primato tecnico e la reputazione di infallibilità di fronte alla comunità territoriale non rappresentano fattori accessori di prestigio: il corpo li tratta **come se fossero questioni di sopravvivenza**. A valutarli concorrono, in parte, gli stessi circuiti che leggono lo stato viscerale dell'organismo e che Damasio collega ai marcatori somatici, come l'insula e la corteccia prefrontale ventromediana.»
- Motivazione: conserva la tesi del capitolo e il grassetto, ma con «come se» e «in parte». Riconduce l'insula e la corteccia prefrontale ventromediana al ruolo che la letteratura attribuisce loro: stati corporei e marcatori somatici. Grado di certezza: medio-alto.
- Rischi / impatti su altri capitoli:
  - L154 («minaccia mortale alla sopravvivenza del Sé nel ruolo (*role survival threat*)») e L177 («*role survival threat*») usano un'etichetta inglese che sembra un termine tecnico della letteratura, mentre è del libro. Si suggerisce di togliere il corsivo inglese o di segnalarlo come etichetta propria, per esempio «(quella che qui chiamiamo minaccia al ruolo)». Non è proposto come obbligatorio.
  - L'Epilogo (Toolkit L431) e P3-19.Toolkit hanno un problema analogo di attribuzione a Damasio, da trattare nel rispettivo file.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

### P3-19.Cap05-d — Massima: «Il cervello confonde la sopravvivenza biologica con la sopravvivenza nel ruolo (*Damasio*)»
- Problema: la massima attribuisce a Damasio, con l'autore tra parentesi, l'estensione al ruolo. Afferma inoltre come fatto che i «circuiti prefrontali» decodificano l'errore del delegato come «minaccia mortale».
- Passo attuale (riga 293): «* **Il cervello confonde la sopravvivenza biologica con la sopravvivenza nel ruolo (*Damasio*).** L'errore del delegato viene decodificato dai circuiti prefrontali come una minaccia mortale al proprio status e alla propria autorevolezza, scatenando reazioni somatiche difensive sproporzionate.»
- Proposta: «* **Il corpo può trattare una minaccia al ruolo come una minaccia alla sopravvivenza (estensione da *Damasio*).** L'errore del delegato può essere vissuto come un pericolo grave per il proprio status e la propria autorevolezza, e scatenare reazioni somatiche difensive sproporzionate.»
- Motivazione: «può» sostituisce «confonde», «estensione da» sostituisce l'attribuzione diretta, e cade la localizzazione «circuiti prefrontali». Il contenuto operativo della massima resta invariato. Grado di certezza: alto.
- Rischi / impatti su altri capitoli: nessuno.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

### P3-19.Cap05-e — (facoltativa) Intestazione del passaggio 3 del protocollo
- Problema: è la stessa attribuzione diretta, nell'intestazione del protocollo operativo.
- Passo attuale (riga 276): «3. **SIGNIFICATO ATTRIBUITO (La minaccia alla sopravvivenza nel ruolo - Damasio):**»
- Proposta: «3. **SIGNIFICATO ATTRIBUITO (La minaccia al ruolo - estensione da Damasio):**»
- Motivazione: è la stessa formula di -a e -d, per coerenza interna.
- Rischi / impatti su altri capitoli: nessuno.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

---

## Testo combinato L148–L150 (se si approvano P2-19.Cap05 e P3-19.Cap05-b)

Sostituisce le righe 148 e 150 attuali (la riga vuota 149 resta):

«Nelle sue opere — da *L'errore di Cartesio* (1994) a *Sentire e conoscere* (*Feeling & Knowing*, 2021) — Antonio Damasio sostiene che la regolazione della vita non dispone di un apparato separato per le faccende sociali: i meccanismi che valutano lo stato dell'organismo vengono reclutati, in parte, anche dalle situazioni psicologiche e sociali. Questo libro ne trae un'ipotesi di lavoro: lo status e il ruolo professionale possono attivare gli stessi allarmi corporei che segnalano un pericolo fisico.

In *Sentire e conoscere* Damasio osserva che la natura, per economia, non ha creato dispositivi nuovi per gestire il bene o il male della nostra condizione psicologica e sociale: si serve degli stessi meccanismi che regolano la vita del corpo, ed è per questo che anche le situazioni sociali possono produrre dolore o piacere (A. Damasio, *Feeling & Knowing. Making Minds Conscious*, 2021; trad. it. *Sentire e conoscere. Storia delle menti coscienti*, Adelphi, 2022).»

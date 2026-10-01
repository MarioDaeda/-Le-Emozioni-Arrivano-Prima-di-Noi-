# Proposte — Cap.03 «La cassa che brucia e il panico da anticipazione»

Stato: APPROVATA DALL'AUTORE — APPLICATA

File: `capitoli/CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` (righe attuali, branch `bonifica/06-proposte`).

Vincoli rispettati (Fase 4, Bibbia 16):
- delibera esecutiva giovedì 27 novembre (L216 «giovedì mattina»; L220 «Il 27 novembre … il fido era deliberato»);
- accredito venerdì 28 alle 16:30 (L222);
- saldo degli stipendi «il lunedì successivo»;
- invariati il fido di 300.000 €, i diciotto programmatori, Mediocredito e la Bignami.

POV: Marco, Atto IV, Deep POV Grado 4. La percezione passa dal suo mestiere: pipeline, test, cron.

---

## P2-11.Cap03-a — Lo scaglionamento non è unanime: un'obiezione e un costo
- Problema: l'Atto IV chiude in modo consolatorio (ADR 0002, Modello B). Tutti e diciotto accettano «all'unisono» di ricevere metà stipendio, senza attrito, e il costo della crisi di liquidità si azzera. Un dipendente con una rata in scadenza il primo del mese, o con un'esperienza precedente di stipendi rinviati, obietterebbe. E la fiducia, quando c'è, ha un prezzo.
- Passo attuale (riga 220): «Il 27 novembre Marco dovette riunire i suoi diciotto programmatori nell'open space: guardandoli negli occhi con trasparenza assoluta, spiegò che il fido era deliberato ma che l'erogazione materiale sarebbe avvenuta venerdì 28. Chiese a ciascuno di loro di accettare lo scaglionamento dello stipendio in due rate: il 50% quel giorno stesso (attraverso le ultime riserve di cassa) e il saldo il lunedì successivo. Diciotto mani si alzarono all'unisono in segno di fiducia. Nessuno si licenziò, nessun sindacato bloccò i tornelli, nessun server venne spento.»
- Proposta: «Il 27 novembre Marco dovette riunire i suoi diciotto programmatori nell'open space: guardandoli negli occhi con trasparenza assoluta, spiegò che il fido era deliberato ma che l'erogazione materiale sarebbe avvenuta venerdì 28. Chiese a ciascuno di loro di accettare lo scaglionamento dello stipendio in due rate: il 50% quel giorno stesso (attraverso le ultime riserve di cassa) e il saldo il lunedì successivo. Le mani si alzarono a scatti, non insieme. Marco le contò come contava i test verdi della pipeline: quindici. Dal fondo, accanto al rack, il più anziano del backend parlò senza alzarsi. «Il primo mi parte la rata del mutuo, Marco. E "lunedì" me l'hanno già detto una volta, in un'altra azienda.» Altre due mani restarono giù, senza una parola, e pesarono di più. Quella sera, alle 21:40, partì un bonifico dal conto personale di Marco a quello di NexSys, causale *finanziamento soci*: la seconda metà dei tre stipendi, subito. Nessun server venne spento. Marco rimase a fissare la ricevuta più a lungo di quanto avesse fissato la mail della Bignami.»
- Motivazione:
  - Inserisce l'obiezione e il costo chiesti dal registro: lo scaglionamento non unanime (15 su 18) e una contropartita materiale, pagata da Marco con denaro personale (finanziamento soci, strumento tipico delle PMI in tensione di cassa).
  - Le date fissate restano intatte (27 delibera, 28 accredito, saldo lunedì).
  - L'obiezione ha sottotesto («"lunedì" me l'hanno già detto»): attacca la credibilità di Marco senza aggressività.
  - La chiusa resta in Deep POV, sul corpo e sul gesto, senza massime.
  - Si toglie «Nessuno si licenziò, nessun sindacato bloccò i tornelli», che chiudeva tutti i rischi in una riga.
  - Il bonifico personale rende anche più verosimile la copertura parziale con «le ultime riserve di cassa», dato il saldo di 12.740,22 € di L14. Non si aggiungono importi nuovi.
- Alternativa (facoltativa), con un costo più duro in organico, da usare solo se l'autore accetta un residuo che i capitoli successivi non riprendono: dopo «… in un'altra azienda.» sostituire il seguito con «Altre due mani restarono giù. Il lunedì successivo, insieme al saldo, sulla scrivania di Marco arrivò la lettera di dimissioni di uno dei cinque periti assunti in primavera: preavviso di un mese, nessuna spiegazione. Nessun server venne spento. Ma nell'open space, da quel giorno, c'era una postazione con il monitor rivolto verso il muro.»
- Rischi / impatti su altri capitoli:
  - Nessun capitolo successivo menziona l'unanimità o lo scaglionamento. La ricerca di «scaglion», «diciotto mani» e «diciotto programmatori» trova solo Cap.03 L220.
  - Apparati del Cap.03 (L247 «il fido è stato approvato 48 ore dopo»): invariati.
  - Il personaggio «il più anziano del backend» resta senza nome, per non introdurre un nome nuovo nella Bibbia.
  - Se si sceglie l'Alternativa, il numero dei dipendenti di NexSys (18) resta valido nel Cap.03, ma un eventuale riferimento successivo a «diciotto» andrebbe verificato. Oggi non ce ne sono.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

## P2-11.Cap03-b — Esito non definitivo: togliere «per il resto della sua vita professionale»
- Problema: la chiusa trasforma l'apprendimento di un episodio in una conversione permanente («per il resto della sua vita professionale»). È un esito consolatorio, contrario al Modello B, e la tesi stessa del capitolo lo contraddice: il corpo reagisce comunque, si può solo revocargli la delega di comando (L170).
- Passo attuale (riga 226): «Non aveva smesso di essere un imprenditore consapevole che fare impresa significa camminare ogni giorno sull'orlo del baratro della liquidità. Aveva smesso, però, per il resto della sua vita professionale, di scambiare il panico biologico della propria immaginazione con la realtà dei fatti.»
- Proposta: «Non aveva smesso di essere un imprenditore consapevole che fare impresa significa camminare ogni giorno sull'orlo del baratro della liquidità. Non aveva smesso nemmeno di avere paura: la fitta sarebbe tornata alla prossima mail del venerdì sera, puntuale come un cron job. Ma tra la fitta e il tasto di invio, adesso, c'era uno spazio di dieci secondi: il tempo di rileggere le parole scritte, non quelle immaginate, e di fare una domanda.»
- Motivazione: elimina la conversione definitiva. Lascia il residuo somatico (la paura tornerà) e mostra un guadagno limitato e concreto, uno spazio di dieci secondi. Riprende la tesi di L170 («non elimina la paura: le revoca la delega di comando») e il gesto mancato di L55 (il tasto di invio della PEC). Il lessico (cron job) viene dal mestiere di Marco.
- Alternativa (facoltativa): «… Aveva imparato, però, una cosa sola, e non era detto che la ricordasse alla prossima mail del venerdì sera: rileggere le parole scritte prima di rispondere a quelle immaginate.»
- Rischi / impatti su altri capitoli: nessuno. L224 («Il suo cuore batteva a ritmo normale. Lo stomaco non bruciava più.») può restare: descrive il momento dell'accredito, non uno stato permanente. Se si approva -a, l'autore valuti se aggiungere a L224 un residuo («Lo stomaco non bruciava più, o quasi.»). Non è proposto come obbligatorio.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

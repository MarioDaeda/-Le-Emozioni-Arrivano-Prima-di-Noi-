# Proposte — Cap.06 «La guerra dei territori e i dati come armi»

Stato: APPROVATA DALL'AUTORE — APPLICATA

File: `capitoli/CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` (righe verificate sul testo attuale, dopo le Fasi 4 e 5).

## Verifica preliminare dei calcoli (sui numeri attuali del capitolo)

Il capitolo non dichiara la spesa annua, ma la si ricava dai dati del testo (L25, L141, L279):

| Grandezza | Calcolo | Valore |
|---|---|---|
| Spesa storica annua (listino di distretto) | 78.400 / 0,114 | ≈ 687.700 € |
| Spesa annua con Ferrometalli Sebina (Brescia) | 687.700 − 78.400 | ≈ 609.300 € |
| Spesa annua con Trafilerie Venete (+5% su Brescia) | 609.300 × 1,05 | ≈ 639.800 € |
| Risparmio lordo Trafilerie Venete rispetto allo storico | 687.700 − 639.800 | ≈ 47.900 € → «48.000 €» del testo: **corretto** (arrotondamento) |
| Sfrido 0,2% sulla spesa Trafilerie Venete | 639.800 × 0,002 | ≈ **1.280 €** |
| Sfrido 0,2% sulla spesa storica (base massima plausibile) | 687.700 × 0,002 | ≈ 1.375 € |
| Base che darebbe 1.500 € allo 0,2% | 1.500 / 0,002 | 750.000 € (nessuna grandezza del capitolo vi corrisponde) |

Esito: il 48.000 € è coerente; l'1.500 € non è lo 0,2% di nessuna base del capitolo (lo 0,2% vale tra circa 1.220 e 1.375 €, a seconda della base; sulla base corretta, la spesa Trafilerie Venete, circa 1.280 €). Il netto «46.500 €» dipende da quel 1.500 € ed è ripreso nel Toolkit (vedi Rischi).

Il resto della catena regge: 78.400 − 92.650 = −14.250 € (L57, L128, L225, L273); 114 h × 70 €/h = 7.980 € (L55, L273); 84 + 58 = 142 colli, 59,2% + 40,8% = 100% (L51-53).

## P3-16-a — Sfrido 0,2% «pari a € 1.500»

- Problema: lo 0,2% di sfrido è dichiarato «pari a € 1.500», ma sulla spesa annua implicita con Trafilerie Venete (≈ 639.800 €) vale circa 1.280 €; anche sulla base più larga (spesa storica ≈ 687.700 €) non supera 1.375 €. Il dato contabile, proprio nella scena in cui il capitolo insegna a «disarmare il dato», non torna.
- Passo attuale (riga 279): «Dedotto lo 0,2% di sfrido fisiologico e tolleranza dimensionale a nostro carico pari a **€ 1.500**, il beneficio netto consolidato reale per l'azienda è di **€ 46.500 all'anno**.»
- Proposta (soluzione A, consigliata perché lascia invariati 1.500 € e 46.500 € in tutto il libro): «Dedotti lo sfrido fisiologico dello 0,2%, circa milletrecento euro sul valore annuo della fornitura, e una riserva per gli scarti dimensionali a nostro carico, in tutto una stima prudenziale di **€ 1.500**, il beneficio netto consolidato reale per l'azienda è di **€ 46.500 all'anno**.»
- Motivazione: il passo già distingueva due voci («sfrido fisiologico *e* tolleranza dimensionale a nostro carico»); la proposta rende esplicita la scomposizione (≈ 1.280 € di sfrido arrotondati a «circa milletrecento», più ≈ 200 € di riserva per scarti) e dichiara il 1.500 € come stima prudenziale, che è ciò che un ingegnere gestionale presenterebbe a verbale. Nessuna cifra canonica cambia.
- Alternativa (soluzione B, prescrizione letterale del registro): «Dedotto lo 0,2% di sfrido fisiologico a nostro carico, pari a circa **€ 1.300** sul valore annuo della fornitura, il beneficio netto consolidato reale per l'azienda è di circa **€ 46.700 all'anno**.» In questo caso va modificata anche la riga 287: «Con quarantaseimila e cinquecento euro di risparmio netto certificato» → «Con quarantaseimilasettecento euro di risparmio netto certificato».
- Rischi / impatti su altri capitoli: con la soluzione A nessun impatto. Con la soluzione B vanno riallineate le occorrenze di 1.500 € e 46.500 € in `capitoli/EPILOGO_E_TOOLKIT_OPERATIVO.md` (L64 «utile netto TCO di 46.500 euro»; L232 «sfrido allo 0,2% (1.500 €)»; L233 «48.000 € meno 1.500 € di sfrido = 46.500 €/anno»; L235 «46.500 euro all'anno»; L429 «+46.500€/anno») e la riga 287 di questo capitolo. Materia contabile: i valori sono ricostruiti per via aritmetica dal testo; non serve un parere professionale, salvo che l'autore voglia dichiarare una spesa annua diversa.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

## P3-16-b — Barre «pelate» in classe h7

- Problema: la pelatura (scortecciatura al tornio) produce di norma barre in classe di tolleranza h9-h11; la classe h7 sul diametro si ottiene con la rettifica senza centri (barre rettificate). «Barre pelate in h7» è un'incongruenza tecnica che un lettore del settore coglie subito.
- Passo attuale (riga 279): «Tuttavia, l'indice di conformità dimensionale è del 99,8% con barre pelate e forate in classe di tolleranza h7.»
- Proposta: «Tuttavia, l'indice di conformità dimensionale è del 99,8% con barre rettificate e forate in classe di tolleranza h7.»
- Motivazione: modifica minima di una parola, coerente con la prescrizione del registro («barre rettificate h7») e con le righe 283 («Lavorano con tolleranza h7 senza sgarrare») e Toolkit L232 («barre calibrate h7»), che restano valide. Il contrasto con la Ferrometalli Sebina (Toolkit L232: «tolleranza h11», tipica di trafilato/pelato) diventa tecnicamente sensato.
- Alternativa (facoltativa): «… con barre tonde rettificate in classe di tolleranza h7 e barre forate a tolleranza garantita da capitolato.» (Più prudente sulle barre forate in titanio, per le quali la classe h7 da rettifica è possibile ma meno corrente; allunga però la battuta.)
- Rischi / impatti su altri capitoli: nessuno sulle tolleranze canoniche (Bibbia voce 4: 2 µm Kuka, 6 µm Hydac riguardano i pezzi finiti, non le barre grezze; h7 su un diametro di 30-50 mm vale 25 µm circa ed è coerente con un semilavorato da rilavorare). Nota collaterale, non oggetto della voce: alla stessa riga «tolleranze millimetriche garantite per i torni dell'officina» sottostima la precisione (h7 è nell'ordine dei centesimi); l'autore può valutare «tolleranze di barra garantite per i torni dell'officina». Dato tecnico di prassi siderurgica (EN 10278): grado di certezza alto; conferma facoltativa con un tecnico di trafileria.
- Decisione dell'autore: [x] APPROVATA  [ ] APPROVATA CON MODIFICHE  [ ] RESPINTA

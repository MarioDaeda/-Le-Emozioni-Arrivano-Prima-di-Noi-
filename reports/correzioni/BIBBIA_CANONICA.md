# Bibbia canonica — dati contesi (v2, decisioni dell'autore del 2026-10-01)

Fonte delle voci: `reports/correzioni/REGISTRO_ANOMALIE.tsv`. Ogni voce fissa il valore che tutti i file di `capitoli/` devono adottare nelle fasi di correzione.

**Precedenza.** Con la fase Governance (branch `bonifica/03-governance`) ADR 0001, ADR 0002 e CONTEXT.md sono allineati a questa Bibbia su tolleranze (G1), sede e territorio (G3), parco macchine e attribuzioni a Damasio (G5). La precedenza provvisoria decade: Bibbia e governance coincidono. Per i conflitti residui vale la governance aggiornata.

**Stato.** Le voci territoriali sono APPROVATE secondo `MAPPA_TERRITORIALE.md` (D1, D2 e D3 approvate). Tutte le voci sono APPROVATE, compresa T5 (D1).

## 1. Regola temporale

**Regola generale — APPROVATA:**
- **si eliminano** gli anni civili che collocano esplicitamente l'azione. Esempi: «Budget Consolidato 2027», «Organigramma 2027», «Convention 2027-2030», il protocollo del bando con l'anno, «busta paga di aprile 2027 / settembre 2027» (che diventano «aprile» e «settembre»);
- **si conservano:**
  - gli anni biografici, storici, societari, contrattuali, contabili e documentali;
  - gli anni che identificano il periodo di maturazione di un premio o un esercizio già concluso;
  - i mesi e le scadenze («19 dicembre», «27 novembre», «aprile», «settembre»).

Ammessi esplicitamente, se usati con queste funzioni:
- 2011 (fondazione di Omnia);
- 2004 (assunzione di Marta);
- 1998 e '99, 2006, 2018 (storia di Dario e delle convention);
- 1997 (incidente di Silvano);
- 2016 (fiera di Hannover);
- **«premio di risultato del 2025»** (riferimento documentale al periodo di maturazione, non datazione della scena).

Timeline interna, non esplicitata nel testo: venerdì 14/11/2025 → venerdì 6/03/2026. → P2-01

## 2. Dati canonici

| # | Tema | Valore canonico | Fonte o motivo | Voci |
|---|---|---|---|---|
| 2 | Omnia: fondazione | 2011; «quindici anni» di sodalizio tra Andrea e Luca | maggioranza del testo (Cap.05, Cap.07, Cap.08) | P2-02 |
| 2b | Omnia: luogo d'origine | Fondata nel 2011 in **«un garage della Bolognina, a Bologna»**; nelle occorrenze successive «il garage della Bolognina». Nessuna via, civico o attività reale; nessuna caratterizzazione storica, operaia o industriale della Bolognina senza fonte verificata | D2, decisione dell'autore | P2-02 |
| 3 | Istituto di credito di NexSys e della rete | **Mediocredito** (filiale grandi imprese; funzionaria Bignami, analista Marangoni); nessuna «Banca Popolare». Filiale a **Bologna**, centro storico, palazzo ottocentesco in mattoni e arenaria, senza via reale. **Terminologia (D3):** «Mediocredito» = banca narrativa (mai «Mediocredito Centrale»); «Fondo di garanzia» = garanzia pubblica; «gestore del Fondo di garanzia» = soggetto amministrativo, solo se indispensabile. Al gestore non si attribuisce il merito creditizio, che resta della banca | ADR 0001:13; mandato; Cap.01, Cap.05; D3 | P2-09 |
| 4 | Tolleranze dimensionali | **Boccole Kuka in ergal: tolleranza dimensionale critica 0,002 mm (2 µm).** **Distributori Hydac in titanio grado 5: tolleranza dimensionale critica 0,006 mm (6 µm).** Le due tolleranze **non** si uniformano. «Lavorazioni al centesimo» è ammesso solo come riferimento generale alle lavorazioni ordinarie | decisione dell'autore | P2-06 |
| 4b | Rugosità | Grandezza **distinta** dalla tolleranza dimensionale: boccole Kuka Ra ≤ 0,8 µm (scarto a Ra 1,4). Non si scrivono mai frasi che confondano rugosità e tolleranza | decisione dell'autore; Cap.02 | P2-06 |
| 4c | Certificazione | Le misure nell'ordine dei micron richiedono **controllo termico** (sala metrologica a 20 °C, pezzo stabilizzato) e **strumentazione adeguata**: micrometro millesimale, comparatore, CMM, tastatore con ripetibilità ≤ 1 µm. **Mai** calibro o micrometro centesimale per certificare pezzi a 2 o 6 µm | decisione dell'autore | P2-06 |
| 5 | Materiali | Boccole Kuka (bracci robotici): ergal 7075-T6, Ø 130 mm. Distributori Hydac: titanio grado 5 | Cap.02, Cap.04 | P2-07 |
| 6 | Parco macchine di O.M.P. Precision | 44 macchine utensili: 22 centri Mori Seiki a 5 assi, 12 torni a fantina mobile, 10 rettifiche; 120 dipendenti | Cap.04; ADR 0001 (numero totale) | P2-05 |
| 7 | Climatizzazione | Capannone **non** climatizzato (circa 10 °C d'inverno, circa 40 °C d'estate); climatizzata a 20 °C solo la sala metrologica (coerente con 4c) | Cap.02, Cap.07, Cap.09 | P2-08 |
| 8 | Sede di O.M.P. Precision | **Area industriale a nord di Cesena, tra Via Emilia e A14**, senza frazione né via reale; retro del capannone su un raccordo ferroviario dismesso | Mappa territoriale | P3-28 |
| 9 | Paolo Zantedeschi | «Paolo Zantedeschi è commercialista e revisore legale. È il consulente storico di Omnia per gli aspetti societari, fiscali e di controllo. In precedenza ha svolto incarichi professionali esterni e circoscritti per O.M.P. Precision, senza esserne dipendente né revisore interno.» | formula dell'autore | P2-03 |
| 10 | Davide | 28 anni, collaudatore, laurea triennale in ingegneria dei materiali, contratto a termine | Cap.02 | P2-04 |
| 11 | Silvano Spinelli | 58 anni, capofficina, «quarant'anni di mestiere, trentaquattro in O.M.P.»; pensione nella primavera successiva | Cap.04 + Pref/Cap.07 | P3-08 |
| 12 | Elena (Colombo) | Moglie di Andrea; guida lo Studio Colombo & Associati, consulenza del lavoro e di rete; non è commercialista né studio legale. Sede dello studio: **Bologna**, centro | ADR 0001:15; Mappa territoriale | P3-29 |
| 13 | LogiDistretto | Direttore operativo Claudio Marcolini. Sede: **Ravenna, area portuale e intermodale** (Canale Candiano, senza terminal nominato); sala riunioni «Adriatico» | Mappa territoriale | P3-30 |
| 14 | Denominazioni | **NexSys Automation**; **Omnia S.r.l.** (forma breve «Omnia» ammessa nel parlato e nella narrazione); **O.M.P. Precision**; **LogiDistretto**; **Studio Colombo & Associati**. Si eliminano «NexSys Solutions» e «Omnia Servizi» (anche «Omnia Servizi Direzionali») dalle fonti canoniche | decisione dell'autore | P3-26f |
| 15 | Commessa Hydac | 300 distributori, 50 min/pezzo, 250 ore; fabbisogno del cliente 50 + 250; accordo: primo lotto di 40 pezzi entro il 18/12 (33 h 20 min su 34 h di riserva), 260 dal 20/01; penale 3.000 €/giorno; valore 140.000 € | Cap.04 dopo A02 | P1-02, P1-01 |
| 16 | Fido NexSys | 300.000 € (garanzia pubblica del **Fondo di garanzia**; cfr. voce 3); supplemento istruttorio sulla perizia del software; delibera esecutiva giovedì 27/11 | Cap.03 | P2-10, P1-01 |
| 17 | Parentele | Marta è **figlia** di Gianni Bellamoli | Cap.07 | P1-01 |

## 2b. Dati territoriali (da `MAPPA_TERRITORIALE.md`)

| # | Tema | Valore canonico | Stato |
|---|---|---|---|
| T1 | Sede di NexSys Automation | Rimini, stecca direzionale Archimede (fittizia), presso il casello di Rimini Nord; origine «in un garage a Rimini» | APPROVATA |
| T2 | Sede di Omnia S.r.l. | Bologna, zona industriale, palazzina sulla tangenziale; nessuna via reale | APPROVATA |
| T3 | Abitazioni | Andrea ed Elena sui colli sopra Bologna; Marco e Giulia a Rimini; Sara alla periferia di Cesena (comune non specificato); Silvano in campagna tra Cesena e Forlì; Davide e Marta nell'area cesenate | APPROVATA |
| T4 | Scena del Cap.03 | Parco XXV Aprile (Rimini); Marecchia, Piazza sull'Acqua e Ponte di Tiberio solo se percepibili dalla scena, senza infodump | APPROVATA |
| T5 | Scena del Cap.07 e residenza di Gianni | **Darsena di città, Ravenna**: banchina sul Canale Candiano, acqua ferma, ciminiere della zona portuale e binari dello scalo merci; Gianni (ex tornitore delle officine dello scalo ferroviario, fittizie) abita a Ravenna | APPROVATA (D1) |
| T6 | Scala della rete | «Distretto» = filiera regionale Bologna–Romagna (circa 115 km), non distretto comunale | APPROVATA |
| T7 | Regola Livello 2 | Nessun ospedale, banca, ente o impresa reale associato a eventi negativi; bando e portale restano generici («la Regione») | APPROVATA |
| T8 | Gastronomia | Livello minimo: bollito con salsa verde, Sangiovese, mostarda; nessun repertorio turistico o folkloristico | APPROVATA |

## 3. Effetti noti sul testo (promemoria per le fasi di correzione)

- Cap.07: le boccole Kuka «a sei micron» diventano **2 µm** (voce 4).
- Cap.04: i distributori Hydac «a sei micron» sono già conformi.
- Cap.02: «quattro millesimi», «a centesimi», «micrometro centesimale» e «calibro digitale» vanno riallineati alle voci 4, 4b e 4c.
- Cap.09 e Toolkit: «due micron» va verificato rispetto al pezzo citato (Kuka 2 µm, Hydac 6 µm).
- Cap.03, Cap.05 e master: «NexSys Solutions» e «Omnia Servizi» vanno sostituiti (voce 14).

## 4. Punto aperto segnalato all'autore

La proposta territoriale cita «NexSys **Solutions**: Rimini», ma la voce 14 fissa «NexSys **Automation**». Risolto: la Mappa territoriale adotta «NexSys Automation».

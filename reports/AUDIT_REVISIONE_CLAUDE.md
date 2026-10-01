# REFERTO DI AUDIT FINALE

## Identificazione dell'opera

- **Titolo:** *Le Emozioni Arrivano Prima di Noi* — Anatomia delle fratture relazionali nell'ecosistema d'impresa.
- **Testo canonico esaminato:** directory `capitoli/` sul branch `main`, commit `1f51621` (2026-10-01), dichiarata dall'autore «versioni definitive divise»: 11 file (Prefazione, Capitoli 1–9, Epilogo & Toolkit), 3.617 linee. Frontespizio e Indice: righe 1–53 del master unificato.
- **Master unificato:** `LIBRO_COMPLETO_LE_EMOZIONI_ARRIVANO_PRIMA_DI_NOI.md` su `main` (commit `b767fd1`, blob `56315a7`, SHA-256 `16520c5a…9d093`): 3.714 linee, 70.821 parole (conteggio `\w+`; 68.775 con `wc`). Il corpo di ogni sezione coincide con il file corrispondente in `capitoli/`. Il mandato indicava circa 73.611 parole e 3.792 linee: valori del master precedente (branch `revisioni-deep-pov`, blob `100c6bd`), superato dalla versione su `main`.
- **Data del referto:** 2026-10-01.

## Mandato e perimetro

Audit forense integrale, avversariale e non a campione su Prefazione, Capitoli 1–9, Epilogo e Toolkit, articolato in quattro pilastri (lore e timeline; algebra industriale e fact-checking; Deep POV di Grado 4; architettura dei cinque atti e toolkit), con Red Team dei P1 e verdetto per l'invio all'impaginazione. Il manoscritto e la governance non sono stati modificati.

**Gerarchia delle fonti applicata.** La directory `revisioni-deep-pov/` indicata nel mandato intermedio non esiste: esisteva la directory `revisioni/` sul branch `revisioni-deep-pov`. Il successivo chiarimento dell'autore ha designato `capitoli/` su `main` come testo definitivo. Mappa di autorità:

| Sezione | File canonico | File precedente | Motivo della precedenza | Stato |
|---|---|---|---|---|
| Frontespizio e Indice | master L1–53 | — | nessun file in `capitoli/` | NON REVISIONATA — fonte: manoscritto unificato |
| Prefazione | `capitoli/PREFAZIONE_METODOLOGICA.md` | master L54–211 | dichiarazione dell'autore; corpo identico | REVISIONE CANONICA |
| Capitoli 1–9 | `capitoli/CAPITOLO_0N_….md` | master; `revisioni/2026-09-2x_CAPITOLO_0N_…` | dichiarazione dell'autore; commit `1f51621` posteriore | REVISIONE CANONICA |
| Epilogo e Toolkit | `capitoli/EPILOGO_E_TOOLKIT_OPERATIVO.md` | master L3249–3714; `revisioni/2026-09-30_EPILOGO…` | idem | REVISIONE CANONICA |

Nota: `revisioni/` contiene ancora versioni dichiarate «definitive» dei Capitoli 2, 3 e 4 con testo diverso dal canone (similarità 0,00–0,07; nel Cap. 2 d'archivio Davide è un impiegato HR). Non sono state usate come canone e non generano anomalie del testo, ma vanno archiviate per evitare confusione.

## Documenti esaminati

| Documento | Esito lettura |
|---|---|
| `CONTEXT.md` (99 linee) | integrale; identico su `main` e `revisioni-deep-pov` |
| `docs/adr/0001-ecosistema-distrettuale-meccatronico.md` | integrale |
| `docs/adr/0002-modello-b-fratture-organizzative.md` | integrale |
| `docs/adr/0003-architettura-toolkit-operativo-io-altri-altro.md` | integrale |
| `.agents/skills/editing-creativo/SKILL.md` | integrale |
| `capitoli/` (11 file) | integrale |
| Master L1–53 (Frontespizio, Indice) | integrale |

Conflitti di governance rilevati: **G1** tolleranze (ADR0001:12 «centesimo di millimetro» contro CONTEXT:93-95 e ADR0002:14 «2 micron») → B06; **G3** ADR0001:12 colloca O.M.P. a «Quinzano d'Oglio / Verona», comune in provincia di Brescia, mentre il testo la colloca a Verona Est → C28; **G5** CONTEXT:18/34 attribuisce a Damasio il «carico allostatico» e la «Sopravvivenza nel Ruolo» → C22; ADR0001:12 «44 macchine a 5 assi» contro C04 L12 (22 centri a 5 assi su 44 macchine) → B05. La precedenza adottata (CONTEXT + ADR0002 su ADR0001 per le tolleranze) è motivata in B06.

## Metodo e limiti

Sei fasi sequenziali con checkpoint compatti versionati: pre-flight e governance; lettura integrale del canone con estrazione di lore e calendario; algebra (ricalcolo di tutte le grandezze citate, con formula); Deep POV (scansioni lessicali deterministiche sugli Atti I, II e IV con esclusione dei dialoghi, ricerca di thought-tag, sequenze dialogiche > 3 battute senza beat, lessico neuro-teorico in scena, poi verifica manuale di ogni occorrenza); architettura (mappatura dei cinque atti per capitolo, verifica di Atto IV e Atto V, confronto puntuale scheda per scheda); Red Team dei P1, deduplicazione, ricontrollo di righe ed estratti con script.

I Capitoli 1, 2 e 3 sono stati letti integralmente nella versione del master precedente e poi verificati sulle differenze riga per riga rispetto al canone (Cap. 1: 3 righe; Cap. 2: 37; Cap. 3: 21): la copertura del canone è quindi integrale. Gli altri capitoli e il Toolkit sono stati letti integralmente nel canone.

Verifiche esterne (consultate il 2026-10-01), limitate ai fatti non verificabili internamente:
1. bauma (fiera triennale, aprile; 2025 → 2028): https://bauma.de/en/trade-fair/press/press-releases/detail/bauma-2025-final-report.html; https://en.wikipedia.org/wiki/Bauma_(trade_fair) → C11.
2. Lazarus, *Core Relational Theme* della rabbia («a demeaning offense against me and mine»): https://en.wikipedia.org/wiki/Core_relational_theme → B20 (confermato anche internamente da C04 L179).
3. Quinzano d'Oglio, provincia di Brescia: https://www.tuttitalia.it/lombardia/52-quinzano-d-oglio/ → C28.

Punti valutati su conoscenza tecnica o bibliografica generale, senza fonte esterna consultata, e quindi marcati PROBABILE: polizza D&O, prassi sanitaria nella crisi ipertensiva con deficit visivo, istituti giuslavoristici (B17, B18); tolleranze tipiche delle barre pelate (C16); attribuzioni scientifiche (C19, C22).

## Executive verdict

**NON IDONEO ALL'IMPAGINAZIONE.** Tre anomalie bloccanti confermate dal Red Team:

1. **A01 — Toolkit incompatibile con i capitoli.** Le nove schede, il Protocollo dei 180 secondi e la Tabella sinottica attribuiscono ai casi numeri, date, citazioni e relazioni che i capitoli smentiscono: fido da 150.000 € invece di 300.000 €; consegna Hydac «venerdì alle 16:00» con «120 ore» libere invece del 19 dicembre con 34 h; Marta «nipote» di Gianni invece che figlia; citazioni di Silvano e Marta inesistenti; 498.700 € presentati come «debito taciuto».
2. **A02 — Calcolo di capacità falso nella risoluzione del Cap. 4.** I 50 distributori «perfettamente assorbibili nelle 34 ore di riserva» richiedono 41,7 ore di mandrino.
3. **A03 — Materiale di lavorazione interno nel testo canonico.** Sette capitoli (e il master) contengono le «Note di Lavorazione e Registro di Continuità», con codici scena, percorsi di file e affermazioni false sui capitoli.

Tutti e tre sono bonificabili senza riprogettare l'opera. La narrazione è solida: cinque atti presenti in tutti i nove capitoli, Atto V completo, filter words quasi assenti, nessun thought-tag. Restano però 21 anomalie P2, in particolare su continuità (anno narrativo, anzianità di Omnia, Zantedeschi, istituto di credito), coerenza tecnica (tolleranze, parco macchine, materiali, climatizzazione) e Atti IV consolatori in quattro capitoli.

## Quadro sintetico dei quattro pilastri

| Pilastro | Ambito verificato | Esito | P1 | P2 | P3 | Note |
|---|---|---|---:|---:|---:|---|
| 1 — Lore e continuità temporale | 30+ personaggi, calendario 14/11/2025 → 6/03/2026, luoghi | CONFORME CON RISERVE | 0 | 6 | 12 | anno narrativo incoerente (B01), anzianità Omnia, Zantedeschi, banca |
| 2 — Algebra industriale e fact-checking | tutte le grandezze numeriche e tecniche; 3 verifiche esterne | NON CONFORME | 1 | 8 | 9 | A02; tolleranze/strumenti; parco macchine; citazioni non verificabili |
| 3 — Purismo stilistico e Deep POV | Atti I, II, IV dei 9 capitoli | CONFORME CON RISERVE | 0 | 5 | 4 | residui concentrati nei Capp. 1, 2 e 4 |
| 4 — Architettura e toolkit | 5 atti × 9 capitoli; Atto V; 9 schede; protocollo; tabella | NON CONFORME | 2 | 2 | 6 | A01 e A03; Atti IV consolatori (B11) |
| **Totale** | | | **3** | **21** | **31** | 55 anomalie, deduplicate |

## Pilastro 1 — Lore e continuità temporale

**Anagrafiche verificate (tutte conformi al dossier salvo dove indicato):** Andrea Vettori 45 anni, fondatore e AD di Omnia (C01 L9; C05 L9); Luca Marangon 43 anni, socio al 50%, COO (C01 L13; C08 L105); Sara 39 anni, responsabile HR di O.M.P. (C02 L8), in azienda da tre anni (C09 L99); Davide 28 anni, collaudatore, laurea triennale (C02 L18) — ma «vent'anni» e «perito» in C09 e nel Toolkit (B04); Marco Vantini 30 anni, 72%, amministratore unico (C03 L12) — società «NexSys Solutions» nel testo e «NexSys Automation» in ADR e master (C26); Silvano Spinelli capofficina, 58 anni, 34 anni in fabbrica (C04 L10) contro «quarant'anni» in Pref L46 e C07 L11 (C08); Marta Bellamoli 48 anni, 22 anni in O.M.P. dal 2004, da capotecnica a Quadro e direttrice dell'Accademia Tecnica (C02 L64; C07 L9, L216-218); Valerio Guidotti, Acquisti e Supply Chain O.M.P. (C06 L13); Claudio Marcolini, Direttore Operativo di LogiDistretto (C06 L15), con sede a Sommacampagna o all'Interporto (C30); ing. Gianluca Moretti 36 anni, ex Magneti Marelli, Head of Operations, introdotto nel Cap. 7 (C07 L17, L24, L154); Dario Meneghelli 52 anni, 28 anni in O.M.P. (C09 L41) — il dato del dossier «padre morto al tornio» compare solo nel Toolkit (S9 L310), non nel Cap. 9 (A01); Elena (Colombo), moglie di Andrea da undici anni (C05 L104), alla guida dello Studio Colombo (ruolo oscillante: C29); Enrico De Marchi 27 anni, ingegnere gestionale e controller junior (C05 L15); Paolo Zantedeschi, profilo incompatibile tra C06 e C01/C08 (B03). Altri: Fabio Bressan, Luisa, Roberto, Giulia, Gianni Bellamoli, Bignami, Marangoni, Bortoluzzi (solo in `revisioni/`), AD di O.M.P. senza nome.

**Calendario ricostruito (anno 2025-2026 dedotto dalle coppie data-giorno, tutte esatte):** Cap. 1 senza data → Cap. 2 ven 14/11 → Cap. 3 ven 21/11–gio 27/11 → Cap. 4 lun 1/12–mar 2/12 → Cap. 5 gio 11/12–ven 12/12 → Cap. 6 mer 14/01–gio 15/01 → Cap. 7 ven 23/01–lun 26/01 → Cap. 8 lun 9/02–mer 11/02 → Cap. 9 mer 4/03–ven 6/03. Passaggio da novembre a fine inverno coerente con luce, freddo, nevischio e abbigliamento, salvo C23 (tuta estiva a marzo). I raccordi relativi («la settimana prima», «due settimane prima», «congelato da quattro mesi») sono esatti. Anomalie: anno narrativo contraddetto dalle etichette 2026/2027 (B01), calendario di erogazione del Cap. 3 (B10), raccordi minori (C06, C13, C18, C21).

## Pilastro 2 — Algebra industriale e fact-checking

| Grandezza | Formula / verifica | Esito |
|---|---|---|
| Bando 180.000 €, scadenza 23:59 (C08 L7-11) | 18:28 + 5 h 31 min = 23:59; invio 23:44 | ✓ |
| Apex 3,2 M€, Polonia (C02 L10) | — | ✓ (Toolkit S3/Tab: «in NexSys» ✗, A01) |
| Fido NexSys 300.000 € (C03 L16) | Toolkit S3: 150.000 € | ✓ / ✗ A01 |
| Burn rate 42.250 €/mese; uscite 138.000 € il 27; saldo 12.740,22 € (C03 L12-14) | fabbisogno 138.000 − 12.740,22 = 125.259,78 €; afflussi impliciti 138.000 − 42.250 = 95.750 €/mese | ✓ coerente |
| Tasso 5,85% (C05 L47, L54, L236) | 5,85 − 3 = 2,85 ≈ «tre punti» (L112) ⇒ usato come tasso complessivo; costo mensile su 300.000 € = 1.462,50 € solo se il tasso valesse per il fido NexSys | NON VERIFICABILE — dato mancante: tasso del fido NexSys; terminologia C14 |
| Gap Omnia 498.700 € (C05 L53-55) | 410.500 − (−88.200) = 498.700 € | ✓ |
| Hydac: 300 pz × 50 min (C04 L55) | 15.000 min = 250 h; 125 h per macchina | ✓ |
| Saturazione (C04 L21-23) | 2.078 / 2.112 = 98,39% | ✓ |
| Ore da assegnare a 2 macchine (C04 L250) | 125 h / 24 h = 5,2 giorni (testo: «diciotto giorni pieni») | ✗ A02 |
| Primo lotto nella riserva (C04 L275) | 50 × 50 min = 41,7 h > 34 h | ✗ A02 |
| Penale 3.000 €/giorno (C04 L51, L254) | 3.000 × 10 = 30.000 € | ✓ (L77 «duemila» ✗, C10) |
| Ferrometalli (C06 L51-57) | 58 + 84 = 142; 40,8% / 59,2%; 114 h × 70 €/h = 7.980 €; 78.400 − 92.650 = −14.250 €/anno | ✓ |
| Trafilerie Venete +5% (C06 L279) | B = 78.400 / 0,114 = 687.719 €; risparmio = B × (1 − 0,886 × 1,05) = 47.932 ≈ 48.000 €/anno | ✓ |
| Sfrido 0,2% = 1.500 € (C06 L279) | 0,2% × 639.786 = 1.280 €; 0,2% × 687.719 = 1.375 € | ✗ lieve, C16 |
| Netto 46.500 €/anno (C06 L279) | 48.000 − 1.500 = 46.500 €/anno | ✓ (nel Toolkit «utile netto consolidato» e «risparmio lordo logistico», A01) |
| Sosta 70 €/h; Ra 0,8 / Ra 1,4 (C02 L12) | — | ✓ |
| Contrazione termica (C02 L233) | 130 mm × 23,4·10⁻⁶ K⁻¹ × 10 K = 0,030 mm = «tre centesimi» | ✓ |
| 35 °C / 2 µm | presenti solo nel Toolkit (L64, L260) e in C09 L278; C07 = 6 µm, gennaio | ✗ A01 / B06 |
| Premio 2.600 € (C09 L53, L228) | 1.300 + 1.300 = 2.600 €; costo totale = 2.600 × N (N non dichiarato; con 120 dipendenti = 312.000 €) | NON VERIFICABILE — dato mancante: platea |
| Caffè 40 → 55 cent (C09 L53, L172) | +15 cent | ✓ |
| Convention 15.000 € + 3.000 € (C09 L17, L234) | 18.000 € | ✓ aritmetica; logica C24 |
| Parole della mail (C03 L25) | 45 | ✓ |
| Parole della replica di Luca (C08 L77) | 15, non 14 | ✗ C20 |

Plausibilità industriale: a parte A02, sono critici il conflitto sulle tolleranze e sulla risoluzione degli strumenti (B06), il parco macchine (B05), il materiale delle boccole (B07) e la climatizzazione (B08). Sul piano giuridico-sanitario: B17, B18. Sul piano bibliografico: B19, B20, C19, C22.

## Pilastro 3 — Purismo stilistico e Deep POV

- **Filter words in narrazione** (Atti I, II, IV, dialoghi esclusi): residui solo in C02 L24, L56, L80; C03 L33, L178, L182; C04 L12, L226. Capitoli 5–9: zero. «Guardò» è trattato come azione, non come filtro.
- **Thought-tag:** nessuna occorrenza. I pensieri in corsivo non taggati (C02 L38, C03 L35, C04 L71, C05 L84) sono ammessi come discorso diretto libero.
- **Infiltrazione saggistica e metalabel in scena:** concentrate nel Cap. 4 (B12) e nel Cap. 2 (B13); Atto II del Cap. 1 (B14); residui minori in C03, C05, C07, C09 (C09).
- **Kitchen Test:** Elena è credibile nei Capp. 1, 8 e 9 e didattica in C05 L138; Zantedeschi (Cap. 6) supera il test; Silvano è credibile; Luisa (C04) e Roberto (C02 L146) falliscono parzialmente (B16).
- **Beat economy:** violazioni in C04 L133-141 e L147-155 (B15) e in C01 L67-73 (C05). Gli altri capitoli rispettano il limite di tre battute.
- **Scelta autoriale difendibile (non anomalia):** il Cap. 9 è al presente con focalizzazione esterna corale (ADR0002:11, narrazione corale e multiprospettica).

## Pilastro 4 — Architettura e toolkit

| Cap. | Atto I | Atto II | Atto III | Atto IV | Atto V (protocollo 7 passi / Da Ricordare / ponte) | Esito Atto IV |
|---:|---|---|---|---|---|---|
| 1 | L3-50 | L51-120 | L121-220 | L221-266 | L267 / L283 / L290-296 | sobrio, contrattuale ✓ |
| 2 | L6-83 | L84-161 | L162-204 | L205-256 | L259 / L281 / L291 | sobrio ✓ |
| 3 | L6-58 | L59-128 | L129-173 | L174-229 | L232 / L253 / L263 | consolatorio (B11) |
| 4 | L6-98 | L99-170 | L171-217 | L218-296 | L299 / L321 / L331 | consolatorio + A02 |
| 5 | L3-87 | L88-141 | L142-191 | L192-265 | L268 / L290 / L300 | YES-BUT ✓ |
| 6 | L3-87 | L88-129 | L130-236 | L237-307 | L308 / L331 / L342-350 | sobrio ✓ |
| 7 | L3-77 | L78-117 | L118-170 | L171-255 | L258 / L318 / L328 | esito pieno (B11) |
| 8 | L3-68 | L69-122 | L123-167 | L168-242 | L245 / L305 / L315 | riconciliazione emotiva (B11) |
| 9 | L3-72 | L73-140 | L141-188 | L189-281 | L284 / L306 / L316 | tregua armata ✓ |

Tutti i nove capitoli presentano la sequenza funzionale dei cinque atti e un Atto V completo: protocollo in sette passi, «Da Ricordare» e ponte specifico. I nove ponti formano una progressione coerente (C17: dettaglio non corrispondente nel ponte 6 → 7). Le difformità formali sono un'etichetta d'atto non uniforme (C01 e C06 hanno un Atto V senza numerazione) e l'apparato interno «4. Note di Lavorazione» in sette capitoli (A03). Toolkit: architettura IO • ALTRI • ALTRO rispettata in tutte le schede e nel protocollo (ADR0003), ma i contenuti fattuali sono incompatibili con i capitoli (A01) e la respirazione «4-7-8» è descritta come 4-2-7 (B21).

## Matrice completa delle anomalie

Totali: **P1 3 — P2 21 — P3 31** (55 anomalie). Le righe si riferiscono ai file in `capitoli/` su `main` (`1f51621`), salvo diversa indicazione.

| ID | Priorità | Stato | Pilastro | Capitolo/Sezione | Linee | Evidenza | Discrepanza | Impatto | Prescrizione |
|---|---|---|---|---|---|---|---|---|---|
| A03 | P1 | CONFERMATA | 4 Architettura/Toolkit | Capp. 2-5, 7-9 | v. Discrepanza | «citato a riga 14 del Capitolo 8 (`bozze_capitoli/CAPITOLO_08_IL_GELO_TRA_PARI.md`) (C07 L356)» | Sette capitoli canonici (e il master) contengono sezioni di lavorazione interne: codici scena, percorsi di file, «riga 14», «bozza preliminare del brief», «sinossi primordiale», «ADR 0001», e asserzioni false sui capitoli (C02 L317: Kuka nel piano del Cap. 1; C07 L353: Marta nel Cap. 6 ed «emigrazione in Svizzera»; C08 L341: «sussurro esausto» di Luca; C09 L350: Enrico «perito»). Assenti in C01 e C06. | Il testo destinato all'impaginazione stamperebbe materiale non editoriale e affermazioni contraddittorie; impedisce la consegna senza una decisione editoriale. | Espungere integralmente le sezioni «4. Note di Lavorazione…» da C02 (L303-320), C03 (L277-293), C04 (L345-360), C05 (L314-326), C07 (L342-360), C08 (L329-346), C09 (L337-350) e dal master; se si vuole un apparato di fonti, crearne uno […] |
| A02 | P1 | CONFERMATA | 2 Algebra/Fact-check | Cap. 4 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L250–275 | «perfettamente assorbibile nelle 34 ore di riserva tecnica dell'officina senza toccare Kuka» | L'accordo dell'Atto IV assegna 50 distributori alla riserva di 34 h: 50 × 50 min = 2.500 min = 41,7 h > 34 h (e la riserva guasti si azzera). L250: «due macchine a cinque assi che abbiamo libere» contro la saturazione dichiarata (L23 residuo 34 h; L47 isole 3-4 al 99%); «diciotto giorni pieni lavorando ventiquattr'ore»: 125 h per macchina / 24 h = 5,2 giorni. | La lezione del capitolo (feasibility check fondato sui numeri) poggia su un calcolo falso: errore matematico con effetto diretto sulla risoluzione. | L275: ridurre il primo lotto a 40 pezzi (40 × 50 min = 33,3 h) oppure dichiarare che le 7,7 h eccedenti sono coperte da straordinario/terzista e che la riserva guasti scende a zero (rischio residuo esplicito). L250: «sono centoventicinque […] |
| A01 | P1 | CONFERMATA | 4 Architettura/Toolkit | Toolkit | `EPILOGO_E_TOOLKIT_OPERATIVO.md` L43–434 | «ha semplicemente chiesto un'integrazione di bilancio prima di deliberare l'estensione del fido di 150.000 euro» | Schede e micro-richiami dichiarano un capitolo d'origine e «Fatti della Telecamera», ma riportano numeri, date, citazioni e relazioni incompatibili con i capitoli: S3 fido 150.000 € e «integrazione di bilancio» (C03: 300.000 €, perizia del software); S4 consegna «entro venerdì alle 16:00» e «120 ore» libere (C04: 19 dicembre, riserva 34 h); S8 «2004», «due periti in uno scantinato», ALTRO non corrispondente all'accordo; S9 pagamento «entro fine mese» (C09: aprile/settembre); F1 «martedì» (C08: lunedì); F2 Gianni «nipote» (Marta è la figlia), «saletta sindacale» (mensa), citazione inesistente; F3 498.700 € come «debito taciuto» (C05: effetto dei parametri 3%/60 gg); F4 citazioni di Silvano e Marta assenti dai capitoli; Tab. «buco Apex in NexSys». | Lo strumento operativo smentisce la narrazione da cui dichiara di derivare; il lettore che verifica trova fatti falsi: invalida l'architettura IO•ALTRI•ALTRO (ADR0003). | Riallineare ogni «Fatti della Telecamera», micro-richiamo e citazione al testo canonico: S3 → 300.000 € e supplemento istruttorio sulla perizia; S4 → 19 dicembre e 34 h di riserva; S8 → 2011, garage di via Tombetta, ALTRO = i 4 punti […] |
| B02 | P2 | CONFERMATA | 1 Lore/Timeline | Pref., Capp. 1, 5, 7, 8, Toolkit | v. Discrepanza | «I primi contratti firmati nel 2011 dentro un garage gelato di via Tombetta (C08 L37)» | Fondazione 2011/15 anni (C05 L7, L13, L128, L152; C07 L334; C08 L37, L81, L113, L180) contro «vent'anni» (Pref L45; C01 L29; C05 L224 nello stesso capitolo; Toolkit L59, L202). Origine: «scantinato» (Pref L45; Toolkit L289) contro «garage di via Tombetta» (C05 L132; C08 L37). | Contraddizione biografica sui protagonisti. | Uniformare a 15 anni/2011 e al garage di via Tombetta in Pref L45, C01 L29, C05 L224, Toolkit L59, L202, L289. |
| B06 | P2 | CONFERMATA | 2 Algebra/Fact-check | Opera / governance G1 | v. Discrepanza | «Qui dentro i pezzi girano a centesimi (C02 L227)» | Il conflitto di governance si riflette nel testo: Pref L46 «centesimo»; C02 L10 «quattro millesimi» vs L227 «centesimi» e L78 «micrometro centesimale» per certificare i pezzi; C04 L55/L85 Hydac «sei micron» (CONTEXT: 2 µm); C07 L161/199/232/246 «sei micron» e L252 azzeramento «a sei micron con precisione centesimale»; C08 L11 «tolleranze centesimali»; C09 L278 «due micron»; Toolkit 2 µm/35 °C; Manifesto L450 «centesimo». | Verità industriale (ADR0002) non garantita; incoerenza tecnica ricorrente. | Governance: allineare ADR0001:12 a CONTEXT:93 (0,002 mm su Kuka/Hydac). Testo: usare la tolleranza canonica per i pezzi critici e «centesimi» solo per lavorazioni non critiche; sostituire micrometro centesimale/calibro (C02 L78, L92) e […] |
| B20 | P2 | CONFERMATA | 2 Algebra/Fact-check | Prefazione | `PREFAZIONE_METODOLOGICA.md` L91 | «La **rabbia** scatta davanti a una *demanding offense*» | La formula di Lazarus è «a demeaning offense against me and mine»; «demanding» ne altera il senso. Lo stesso libro la cita correttamente in C04 L179. | Errore concettuale nella sezione teorica fondativa. | «davanti a una *demeaning offense against me and mine* (un'offesa svilente contro di me e ciò che è mio)». |
| B14 | P2 | CONFERMATA | 3 Deep POV | Cap. 1 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L97–119 | «Una telecamera, naturalmente, non distribuisce la verità intera» | Il narratore espone il metodo della telecamera (L97, L107-119: «La separazione si vede meglio cambiando registro ai verbi…», «Il pensiero critico cominciava da lì…») dentro la scena di cucina. | Infiltrazione saggistica nell'Atto II. | Spostare L109-117 nella sezione «Il processo invisibile» (Atto III) o ridurle a un beat in scena. |
| B16 | P2 | CONFERMATA | 3 Deep POV | Capp. 2, 4, 5 | v. Discrepanza | «Delegare non è un atto di fede mistica: è un metodo di ingegneria relazionale (C05 L138)» | C02 L146 Roberto presenta come fatto uno stato interno («prova una stretta acuta allo stomaco»), contraddicendo il metodo; C04 L155, L161 Luisa espone teoria degli incentivi e diagnosi; C05 L138 Elena parla da formatrice. | Personaggi ventriloqui dell'autore. | Riformulare le tre battute in lingua di mestiere e sottotesto (es. Elena: la scadenza, il foglio dei vincoli mai consegnato), lasciando la teoria all'Atto III. |
| B13 | P2 | CONFERMATA | 3 Deep POV | Cap. 2 | `CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L24–235 | «Era la sensazione fisiologica intollerabile della crudeltà» | L24 «Sembrava»; L38 etichetta astratta dopo i sintomi; L213 («Il corpo non risponde alle riflessioni razionali…») saggistica nell'Atto IV; L225 interiorità di Marta nel POV di Sara; L231 commento autoriale; L235 spiegazione onnisciente delle tre menti. | Distanza narrativa nei passaggi chiave. | Tagliare L38 seconda frase, L213 seconda e terza frase, L231; trasformare L235 in percezione di Sara limitata a ciò che vede; L225 esteriorizzare. |
| B17 | P2 | PROBABILE | 2 Algebra/Fact-check | Cap. 2 | `CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L241 | «firma di un Addendum Formale di Addestramento Tecnico al CCNL Metalmeccanico» | Un «addendum al CCNL» non si stipula individualmente; la «sospensione di trenta giorni» della contestazione confligge con l'immediatezza disciplinare; il «licenziamento per giusta causa» per un controllo saltato è sproporzionato; il patto ignora il contratto a termine in scadenza (L18) e prevede l'affiancamento «sul turno del mattino» per un collaboratore del turno delle 14 che accompagna il padre alle 5:30 (L32). | Atto IV meno credibile proprio sul piano «contrattuale». | «Addendum individuale (patto formativo)»; procedura disciplinare con tempi coerenti; sanzione conservativa progressiva al posto della giusta causa; aggiungere la clausola sul rinnovo del contratto a termine e l'orario compatibile. |
| B11 | P2 | CONFERMATA | 4 Architettura/Toolkit | Capp. 3, 4, 7, 8 | v. Discrepanza | «Aveva smesso, però, per il resto della sua vita professionale, di scambiare il panico (C03 L226)» | C03 L220 unanimità («Diciotto mani… all'unisono»), L226 conversione definitiva; C04 L238 «non succederà mai più», L291 «pacificato», L293; C07 L209-238 esito pieno (Moretti capitola, l'AD approva in sei secondi +28%, autorità «insindacabile») e L213 «il veleno… era svanito»; C08 L196-235 perdono, abbraccio e riconciliazione in 24 ore. | Viola il modello dell'Atto IV in 4 capitoli (elementi contrattuali presenti, registro consolatorio). | C03: inserire un'obiezione e un costo (scaglionamento non unanime), togliere «per il resto della sua vita»; C04: togliere «mai più» e «pacificato», lasciare rabbia residua e rischio della riserva; C07: aggiungere una contropartita o un […] |
| B09 | P2 | CONFERMATA | 1 Lore/Timeline | Capp. 3, 5, Pref. | `CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` L14–178 | «La sede direzionale della Banca Popolare del Distretto in Corso Cavour» | In C03 il conto e il fido sono «presso Mediocredito» (L14) ma la trattativa avviene alla «Banca Popolare del Distretto» con la stessa funzionaria (L178); C05 alterna Banca Popolare (L11, L43, L47, L102, L240) e Mediocredito (L102, L220, L236) per lo stesso spread; Pref L47 «Banca Popolare». | Istituto non identificabile; incoerenza su un perno della trama finanziaria. | Adottare Mediocredito per fido NexSys e linee di rete; correggere C03 L178 (e note), C05 L11, L43, L47, L124, L128, L196, L240, Pref L47. |
| B10 | P2 | CONFERMATA | 1 Lore/Timeline | Cap. 3 | `CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` L75–222 | «Quando giovedì 27 alle 16:30 squillò il telefono e la Bignami confermò l'accredito» | Il 27 è giovedì (L14) ma Marco teme il fallimento «mercoledì mattina» (L75); la delibera è «esecutiva giovedì mattina» (L216); ai dipendenti si annuncia l'erogazione «venerdì 28» con stipendio al 50% e saldo lunedì (L220); l'accredito arriva giovedì 27 alle 16:30 (L222). | Sequenza contraddittoria che svuota lo scaglionamento. | L75 «giovedì mattina»; scegliere una sola data di erogazione: o venerdì 28 (togliere L222 «giovedì 27…») o giovedì sera, con saldo anticipato al venerdì. |
| B01 | P2 | CONFERMATA | 1 Lore/Timeline | Opera (Capp. 4-9) | v. Discrepanza | «sarà erogato nella busta paga di aprile 2027 (C09 L228)» | Le coppie data-giorno fissano la storia tra novembre 2025 e marzo 2026 (14/11 ven, 1/12 lun, 11/12 gio, 14/01 mer, 23/01 ven, 9/02 lun, 4/03 mer) e il premio è «del 2025»; ma compaiono «budget 2026» a dicembre (C04 L264), «Budget Consolidato 2027» (C05 L11, L196, L260), «ORGANIGRAMMA 2027» (C07 L7), «VR-2027» (C08 L7), «CONVENTION 2027-2030» (C09 L10) e il patto paga «aprile 2027» (C09 L228) mentre Dario minaccia «Se ad aprile» (L250). | Il patto risolutivo del Cap. 9 risulterebbe differito di 13 mesi; anno narrativo non ricostruibile. | Fissare l'anno narrativo 2025-2026 e correggere: C04 L264 «budget 2025»; C05 «Budget Consolidato 2026»; C07 L7 «2026»; C08 protocollo «VR-2026-…»; C09 L10 «2026-2029»; C09 L228 «aprile 2026 … settembre 2026». |
| B08 | P2 | CONFERMATA | 2 Algebra/Fact-check | Cap. 4 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L12 | «La temperatura interna era stabilizzata a venti gradi centigradi esatti» | C04 dichiara il capannone climatizzato a 20 °C, mentre C02 L233 (dieci gradi; contrazione di 3 centesimi), C07 L66/L209 (gelo d'inverno, «sotto i dieci gradi») e C09 L49 (quaranta gradi d'estate, servono raffrescatori) lo descrivono non climatizzato. | Contraddice il presupposto tecnico del Cap. 2 e il patto del Cap. 9. | C04 L12: limitare la climatizzazione alla sala metrologica/collaudo o eliminarla. |
| B12 | P2 | CONFERMATA | 3 Deep POV | Cap. 4 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L12–260 | «il corpo di Silvano fu squassato da una detonazione neurosimpatica violentissima» | Etichette cliniche e commenti autoriali in scena: L12 «sembrava», L59, L61 («tremila hertz», «centoventi pulsazioni»), L69 («cono percettivo»), L83 («identità professionale»), L85 («impulso motorio»), L87, L95 («ultimo neurone»), L157, L226 («codificata come una violazione territoriale»), L236 («domanda di processo»), L242, L260 («punto cieco»). | Rompe il Deep POV nel capitolo più tecnico. | Sostituire ogni etichetta con percezione o azione dal mestiere di Silvano (rumore, mani, pezzo); eliminare metriche non percepibili (hertz, pulsazioni) e il lessico del metodo nelle scene. |
| B15 | P2 | CONFERMATA | 3 Deep POV | Cap. 4 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L133–155 | «Bene. Poi?» | Due sequenze di 5 battute consecutive senza beat fisico (L133-141; L147-155, solo attribuzioni «la corresse», «ringhiò»). | Interrogatorio didascalico. | Inserire beat materiali (minestra, cucchiaio, sigaretta, piattino) a L137 e L151; sostituire le attribuzioni di L149/L153 con gesti. |
| B19 | P2 | PROBABILE | 2 Algebra/Fact-check | Capp. 5, 7, 8, 9 | v. Discrepanza | «Il dolore dell'esclusione sociale o del tradimento fiduciario è processato come un danno tissutale severo (C07 L128)» | Citazioni virgolettate attribuite ad autori reali senza riferimento puntuale e non riconducibili a testi noti: Damasio (C05 L150; C07 L128), Kahneman/Bloom (C08 L131: la seconda frase non è nell'originale), Lazarus & Folkman (C09 L160). | Rischio di attribuzione apocrifa in un'opera di saggistica. | Verificare sulle edizioni (pagina) o convertire in parafrasi senza virgolette con rinvio bibliografico. |
| B03 | P2 | CONFERMATA | 1 Lore/Timeline | Cap. 6 | `CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L96–104 | «per ventotto anni Direttore Amministrativo di O.M.P. Precision prima di andare in pensione tre anni prima» | C06 lo presenta come ex Direttore Amministrativo di O.M.P. in pensione e «ragioniere capo in fabbrica per quarant'anni»; C01 L247 è consulente esterno incaricato della verifica, C08 L59 «commercialista storico di Omnia». | Personaggio incompatibile tra capitoli. | In C06 L96/L104 riformulare: «commercialista storico di Omnia e revisore, per anni consulente amministrativo di O.M.P.»; eliminare «Direttore Amministrativo… in pensione». |
| B07 | P2 | CONFERMATA | 2 Algebra/Fact-check | Cap. 7 | `CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md` L161–199 | «scarti seriali sulle boccole in titanio a sei micron» | C07 rende le boccole Kuka «in titanio» e associa «boccole» anche a Hydac (che in C04 sono distributori); L252 parla invece di «alluminio». | Incoerenza tecnica tra capitoli. | C07 L161 e L199: «boccole in ergal per Kuka e distributori in titanio per Hydac». |
| B18 | P2 | PROBABILE | 2 Algebra/Fact-check | Cap. 8 | `CAPITOLO_08_IL_GELO_TRA_PARI.md` L200–225 | «coperto da polizza assicurativa D&O» | L200: crisi ipertensiva 180/100 con perdita del visus e consiglio del medico di «andare a casa al buio» (prassi: invio urgente in pronto soccorso), mentre Luca va a prendere il figlio (L27); L222: comunicare al Collegio Sindacale la mail come «mero disguido tecnico» (dichiarazione non veritiera); L225: il «Sabbatical Medico» coperto da polizza D&O (responsabilità degli amministratori, non copertura sanitaria/reddituale). | La «verità contrattuale» dell'accordo è viziata. | L200: il medico lo manda in PS, Luca rifiuta e chiama la moglie per il figlio; L222: «dichiarando superata la comunicazione e confermando la collegialità»; L225: polizza key-man/income protection al posto di D&O. |
| B04 | P2 | CONFERMATA | 1 Lore/Timeline | Cap. 9, Toolkit | `CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L125–274 | «E a Davide, che ha vent'anni e da stamattina guarda il tornio come se fosse una gabbia» | C09 L125 gli attribuisce vent'anni; C09 L274 e Toolkit L121 lo chiamano «perito». | Incoerenza anagrafica e di formazione. | C09 L125 «che ha ventotto anni»; C09 L274 e Toolkit L121 «collaudatore». |
| B05 | P2 | CONFERMATA | 2 Algebra/Fact-check | Cap. 9 / ADR 0001 | `CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L274 | «novantotto macchine utensili girano a regime» | C09 cita 98 macchine contro 44. Inoltre ADR0001 parla di «44 macchine a 5 assi Mori Seiki», C04 L12 di 22 centri a cinque assi + 12 torni + 10 rettifiche. | Dato industriale contraddittorio. | C09 L274 «quarantaquattro macchine»; aggiornare ADR0001:12 in «44 macchine utensili, di cui 22 centri Mori Seiki a 5 assi». |
| B21 | P2 | CONFERMATA | 4 Architettura/Toolkit | Toolkit | `EPILOGO_E_TOOLKIT_OPERATIVO.md` L42 | «trattieni l'aria per 2 secondi, espira dalla bocca socchiusa per 7 secondi» | La tecnica etichettata «4-7-8» è descritta come 4-2-7; la riduzione di «10–15 battiti al minuto» non ha fonte. | Strumento operativo errato nel punto più usato del toolkit. | «Inspira per 4 secondi, trattieni per 7, espira per 8» (un ciclo ≈ 19 s, quindi «circa due cicli nei primi 30-40 secondi»); togliere «10–15 battiti» o citarne la fonte. |
| C08 | P3 | CONFERMATA | 1 Lore/Timeline | Pref., Capp. 4, 7 | v. Discrepanza | «capofficina con quarant'anni di mestiere nel sangue (Pref L46)» | Pref L46 e C07 L11 «quarant'anni» vs C04 L10/L121 «trentaquattro anni» (58 anni d'età). | Basso. | Uniformare (es. «quarant'anni di mestiere, trentaquattro in O.M.P.»). |
| C29 | P3 | CONFERMATA | 1 Lore/Timeline | Pref., Capp. 3, 4 | v. Discrepanza | «lo studio legale di Elena Colombo (C03 L214)» | Elena è «consulente del lavoro e commercialista» (Pref L49), «studio legale» (C03 L51, L214), «consulente di governance di rete» (C04 L224). | Basso. | Uniformare: «Studio Colombo & Associati, consulenza del lavoro e di rete». |
| C25 | P3 | CONFERMATA | 4 Architettura/Toolkit | Prefazione | `PREFAZIONE_METODOLOGICA.md` L49–139 | «le 22:45 davanti allo schermo di un computer mentre il bilancio provvisorio mostra un disallineamento di 140.000 euro» | L139 promette scene inesistenti (06:40 sul piazzale; 22:45 con 140.000 €); L51 la commessa promessa «dal commerciale di Omnia» (C04: Fabio, O.M.P.); L49 Elena «commercialista» (C08: Zantedeschi). | Basso. | Sostituire con esempi reali (10:17 sala riunioni; 18:47 mail della banca; 19:14 cella F148). |
| C01 | P3 | CONFERMATA | 3 Deep POV | Cap. 1 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L41 | «, Zucchero sull'offesa.» | Maiuscola dopo virgola e frase nominale monca. | Basso. | «…dalla responsabilità decisionale: zucchero sull'offesa.» |
| C02 | P3 | CONFERMATA | 3 Deep POV | Cap. 1 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L45 | «La frase era falsa, e nella stanza lo era per tutti, Andrea compreso.» | Il narratore certifica lo stato di tutti i presenti. | Basso. | Ridurre al POV di Andrea («La frase era falsa, e Andrea lo sapeva»). |
| C05 | P3 | CONFERMATA | 3 Deep POV | Cap. 1 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L67–73 | «Stavamo per decidere.» | Quattro battute consecutive senza beat. | Basso. | Inserire un gesto di Elena o di Andrea a L71. |
| C03 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 1 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L81–89 | «Sprezzante come? Parole, volume, faccia» | Il coltello è posato (L57), poi «fermo a mezz'aria» (L81) senza ripresa, poi «riprese» (L89); Elena dice «Sprezzante» ma Andrea aveva detto solo «Male» (L79). | Basso. | L81 «riprese il coltello»; L89 «Male come?» o far dire ad Andrea «sprezzante». |
| C04 | P3 | CONFERMATA | 2 Algebra/Fact-check | Cap. 1 | `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L247 | «due per mille al giorno sull'importo non erogato» | «Non erogato» è lessico del credito; per un ordine di fornitura: importo non consegnato/non evaso. | Basso. | «sull'importo non consegnato». |
| C06 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 2 | `CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L74–223 | «Il corriere tedesco è passato alle sei e venti.» | L74 trasportatore LogiDistretto alle 06:00 vs L219 «corriere tedesco» alle 06:20; L78 turno di Marta finito alle 19:30 e «passaggio consegne per il terzo turno» alle 19:42; timbratura 21:05 (L92) vs «tre ore» (L195, L223, L275); L223 «ieri sera» per un colloquio delle 16:30. | Basso. | Uniformare vettore e orari; «ieri pomeriggio». |
| C07 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 2 | `CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L76 | «Silvano, il caporeparto» | Altrove «capofficina» (Pref L25, L46; C07 L38; C09). | Basso. | «il capofficina». |
| C09 | P3 | CONFERMATA | 3 Deep POV | Capp. 3, 5, 7, 9 | v. Discrepanza | «Il punto cieco di Marco si spalancò (C03 L212)» | C03 L97 («corteccia cerebrale»), L182 («noradrenalina nel sangue»), L212; C05 L62 («Il terrore biologico dell'espropriazione territoriale»), L218; C07 L213; C09 L69 (tesi autoriale nell'Atto I). | Basso. | Sostituire con percezioni o tagliare. |
| C10 | P3 | PROBABILE | 2 Algebra/Fact-check | Cap. 4 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L41–195 | «Roba che ci ripaga un terzo del buco lasciato da Apex!» | L77 «penale da duemila euro» e «Millecinquecento blocchi» (contratto: 3.000 €/g, 300 pezzi); L41 140.000 € = 4,4% di 3,2 M€, non un terzo (iperbole possibile); L195 «danno economico da 140.000 euro» = ricavo, non danno (MOL 38% = 53.200 €). | Basso. | L77 «tremila», «trecento blocchi»; L195 «una perdita di 140.000 euro di fatturato». |
| C11 | P3 | CONFERMATA | 2 Algebra/Fact-check | Cap. 4 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L41–258 | «la presentazione dei nuovi escavatori alla fiera Bauma di Monaco a fine gennaio» | bauma è triennale e si tiene in aprile (2025, poi 2028): non a fine gennaio 2026; contratto firmato «a Francoforte» (L41, L151, L238) vs «sei andato a Stoccarda» (L77); «franco fabbrica a Stoccarda» (L51) è un uso improprio dell'Incoterm EXW. | Basso. | Fiera generica («una fiera di settore a fine gennaio»); un'unica città; «reso franco destino Stoccarda». |
| C12 | P3 | CONFERMATA | 4 Architettura/Toolkit | Cap. 4 | `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L306 | «il tabellone Kanban saturo al 98,4%» | Nel capitolo lo strumento è il Gantt dell'APS. | Basso. | «il Gantt dell'APS». |
| C30 | P3 | CONFERMATA | 1 Lore/Timeline | Capp. 5, 6, Epilogo | v. Discrepanza | «del polo logistico di LogiDistretto, a Sommacampagna (C06 L5)» | Sommacampagna (C05 L11; C06 L5) vs Interporto Quadrante Europa (Epilogo L9). | Basso. | Uniformare la sede. |
| C13 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 5 | `CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md` L43–128 | «un perito appena uscito dall'università» | L43 addendum «venerdì scorso» (C03: mercoledì 26 novembre); L60 Sara (HR) congela acquisti di titanio (acquisti = Valerio); L84 notte in ufficio vs L96-132 notte nello studio di casa; L128 Enrico «perito» (laurea magistrale). | Basso. | Correggere data e ruolo; raccordo spaziale; «un ingegnere appena uscito dall'università». |
| C14 | P3 | CONFERMATA | 2 Algebra/Fact-check | Cap. 5 | `CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md` L47–236 | «lo spread territoriale è del 5,85%» | 5,85% è usato come tasso complessivo (L54 «SCONTO 5,85%», L112 errore di «tre punti» rispetto al 3%), ma chiamato «spread». | Basso. | «il tasso effettivo è del 5,85%». |
| C15 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 6 | `CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L9–128 | «sedevano sei persone» | L9 sei persone ma cinque presenti; L74 «novantaquattro bancali» (84); L94 polsino macchiato di caffè mai versato; L112 Paolo non conosce Marcolini; L128 Paolo cita 14.250 € senza aver sentito 92.650 €. | Basso. | Correggere numeri e raccordi. |
| C16 | P3 | PROBABILE | 2 Algebra/Fact-check | Cap. 6 | `CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L279 | «Dedotto lo 0,2% di sfrido fisiologico e tolleranza dimensionale a nostro carico pari a € 1.500» | 0,2% della spesa implicita (≈ 640.000-690.000 €) = 1.280-1.375 €, non 1.500; barre «pelate» in h7 (pelatura tipica h9-h11; h7 richiede rettifica). | Basso. | «pari a circa 1.300 €» (o dichiarare la base); «barre rettificate h7». |
| C17 | P3 | CONFERMATA | 4 Architettura/Toolkit | Cap. 6 | `CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L346 | «una pacca sulla spalla e una targa di ringraziamento» | In C07 non c'è alcuna targa. | Basso. | «due pacche sulla spalla e una promozione morale». |
| C19 | P3 | PROBABILE | 2 Algebra/Fact-check | Capp. 5, 7, Epilogo | v. Discrepanza | «un dolore biologicamente e chimicamente indistinguibile da una lacerazione muscolare (C07 L130)» | C07 L122/L130 sovrapposizione dolore sociale/fisico presentata come identità; L134 «loss of an irrevocable commitment» (Lazarus: «irrevocable loss»); L148 «quiet quitting» = sabotaggio; Epilogo L16 attribuisce a Damasio i risultati su dACC/insula (Eisenberger & Lieberman). | Basso. | Attenuare («circuiti in parte sovrapposti»); correggere le formule e le attribuzioni. |
| C18 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 7 | `CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md` L9–250 | «lavorando tre notti consecutive a dieci gradi» | L9 «tre notti» (C02: una sera/notte); L175 «cambio turno delle nove»; L250 «emulsione a quaranta gradi» un mattino di gennaio. | Basso. | «una notte intera»; allineare turni; «emulsione tiepida». |
| C22 | P3 | PROBABILE | 2 Algebra/Fact-check | Capp. 8, 9 / CONTEXT | v. Discrepanza | «emorragia allostatica permanente (*allostatic load*) (C09 L154)» | Il carico allostatico è attribuito a Damasio (C09 L154; CONTEXT:18) o a Sterling & Eyer 1988 (C08 L139); il concetto è di McEwen & Stellar (1993); anche «Sopravvivenza nel Ruolo» non è un termine di Damasio (CONTEXT:34). | Basso. | Correggere CONTEXT:18/:34 e C08 L139, C09 L154 (McEwen; allostasi: Sterling & Eyer). |
| C21 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 8 | `CAPITOLO_08_IL_GELO_TRA_PARI.md` L39–119 | «Da diciotto mesi Luca tirava il freno» | L39 «diciotto mesi» vs L83 «quindici mesi… da quando abbiamo perso Apex» (Apex perso ~9 mesi prima); L73/L115 «stufa in maiolica» vs C05 L96 «stufa a pellet» nello stesso studio; L109 moglie «Claudia» omonima della Bignami; L113 «Avete cinquant'anni» (45 e 43); L119 Elena conosce l'orario di Luca senza fonte. | Basso. | Allineare i dettagli. |
| C20 | P3 | CONFERMATA | 2 Algebra/Fact-check | Cap. 8 | `CAPITOLO_08_IL_GELO_TRA_PARI.md` L77 | «un messaggio di quattordici parole» | La replica citata conta 15 parole (il libro fa del conteggio un metodo in C03). | Basso. | «quindici parole». |
| C23 | P3 | CONFERMATA | 1 Lore/Timeline | Cap. 9 | `CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L19–145 | «Sulle braccia scoperte dalla tuta estiva a maniche corte» | L19 «l'intero turno di produzione» = 120 sedie (= organico totale); L21-23 «sirena delle dieci e mezzo» ma alle 10:28 l'AD parla da 50 minuti; L41 tuta estiva il 4 marzo sotto la pioggia; L145 l'articolo AMR 1998 definito «monografia». | Basso. | Correggere i dettagli. |
| C24 | P3 | PROBABILE | 2 Algebra/Fact-check | Cap. 9 | `CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L223–234 | «I quindicimila euro risparmiati dall'azzeramento dei gadget» | L223 «R.S.U.» non presente; firmano Silvano (capofficina) e Marta (Quadro dal C07) come «delegati di reparto»; L234 i 15.000 € sono già stati spesi (L17) e non possono essere «risparmiati». | Basso. | Far firmare un delegato RSU; «quindicimila euro stanziati dal fondo di presidenza in sostituzione delle convention dei prossimi tre esercizi». |
| C31 | P3 | CONFERMATA | 4 Architettura/Toolkit | Epilogo | `EPILOGO_E_TOOLKIT_OPERATIVO.md` L15–450 | «un maestro d'officina con ventotto anni di reparto si vede scavalcato da un giovane manager esterno» | L15 fonde Dario (28 anni) e Marta (scavalcata, 22 anni); L450 «boccola aerospaziale» e «quote al centesimo di millimetro». | Basso. | «una capotecnica con ventidue anni di reparto»; «boccola per robot» e tolleranza canonica. |
| C26 | P3 | CONFERMATA | 4 Architettura/Toolkit | Opera (formale) | v. Discrepanza | «convocaiamoci formalmente domani mattina alle 08:30 (Toolkit L389)» | BOM a inizio C08 (L1); grassetto su battute non-domande (C08 L83, L93, L97, L196, L200); intestazioni dell'Atto V non uniformi (C01 L267/L283 e C06 L308/L331 «##» minuscolo vs «### 1.» negli altri); refusi Toolkit L82 «DISINNEZCO», L389 «convocaiamoci», troncamento L335 «irrevers.»; Indice master L37 «commessa aeronautica» (assente in C05); «NexSys Solutions» (C03, C05) vs «NexSys Automation» (ADR, master L10); «Omnia Servizi» vs «Omnia S.r.l.». | Basso. | Pulizia redazionale secondo foglio di stile unico. |
| C27 | P3 | CONFERMATA | 4 Architettura/Toolkit | Master, Pref., Epilogo | v. Discrepanza | «(formalizzato nell'Architectural Decision Record 0002) (Pref L27)» | Master L6, Pref L27, L41, Epilogo L11 citano gli ADR di progetto, ignoti al lettore. | Basso. | Eliminare i riferimenti agli ADR o sostituirli con un rinvio alla Prefazione. |
| C28 | P3 | CONFERMATA | 1 Lore/Timeline | ADR 0001 | `docs/adr/0001-ecosistema-distrettuale-meccatronico.md` L12 | «O.M.P. Precision S.r.l. (Quinzano d'Oglio / Verona)» | Quinzano d'Oglio è in provincia di Brescia; il testo colloca O.M.P. a Verona Est (C07 L74 San Michele Extra; C09 L77, L99 Porta Vescovo, via dell'Artigianato). | Nessun impatto sul testo; errore nella governance. | Correggere ADR0001:12 in «Verona Est (San Michele Extra)». |

## Prescrizioni P1

- **A03 — Apparato «4. Note di Lavorazione e Registro di Continuità»** (v. Discrepanza; stato CONFERMATA). Vincolo: Pref L106-143 (Atto V = protocollo, Da Ricordare, ponte); ADR0002:17. Verifica: Lettura integrale; grep su «Codice Scena», «Note di Lavorazione».
  - Prescrizione: Espungere integralmente le sezioni «4. Note di Lavorazione…» da C02 (L303-320), C03 (L277-293), C04 (L345-360), C05 (L314-326), C07 (L342-360), C08 (L329-346), C09 (L337-350) e dal master; se si vuole un apparato di fonti, crearne uno unico a fine volume («Note e fonti»), privo di codici interni e verificato.
  - Occorrenze collegate: C02 L303-320; C03 L277-293; C04 L345-360; C05 L314-326; C07 L342-360; C08 L329-346; C09 L337-350
- **A02 — Cap. 4 — Atto IV e Atto II** (`CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L250–275; stato CONFERMATA). Vincolo: ADR0002:14 (verità industriale); CONTEXT:77 (Feasibility Check). Verifica: Ricalcolo da dati interni (L20-23, L47, L55, L250, L275).
  - Prescrizione: L275: ridurre il primo lotto a 40 pezzi (40 × 50 min = 33,3 h) oppure dichiarare che le 7,7 h eccedenti sono coperte da straordinario/terzista e che la riserva guasti scende a zero (rischio residuo esplicito). L250: «sono centoventicinque ore per macchina, più di cinque giorni pieni a ventiquattr'ore: giorni che non abbiamo, le due cinque assi sono sature fino al 22», eliminando «che abbiamo libere».
  - Occorrenze collegate: L55 («sedici ore al giorno»: iperbole difendibile; «diciotto giorni lavorativi»: conteggio lasco); L20-27 perimetro APS non verificabile; Toolkit S4 (A01)
- **A01 — Toolkit (schede, Protocollo 180 s, Tabella)** (`EPILOGO_E_TOOLKIT_OPERATIVO.md` L43–434; stato CONFERMATA). Vincolo: ADR0003:15 (schede «tarate sui 9 capitoli»); CONTEXT:65 (Disciplina della Telecamera = fatti registrabili). Verifica: Confronto riga per riga scheda/capitolo (04_ARCHITETTURA_TOOLKIT.md); 14 incongruenze indipendenti.
  - Prescrizione: Riallineare ogni «Fatti della Telecamera», micro-richiamo e citazione al testo canonico: S3 → 300.000 € e supplemento istruttorio sulla perizia; S4 → 19 dicembre e 34 h di riserva; S8 → 2011, garage di via Tombetta, ALTRO = i 4 punti dell'accordo C08 L222-225; S9 → tranche aprile/settembre; L43 → lunedì; L52 → «la figlia», mensa, citazione C07 L104; L59 → 498.700 € come effetto dei parametri errati; L64 → domande effettive (C04 L238, C07 L199); L419-420 → Apex cliente perso da O.M.P. Rimuovere i fatti assenti dai capitoli (S6 L229, S8 L286, S9 L310) o introdurli nei capitoli.
  - Occorrenze collegate: S1 L89/L94; S2 L121-127; S6 L213/L233; S7 L251/L260; Tab. L413, L431, L434; L15

## Prescrizioni P2

- **B02 — Anzianità e origine di Omnia** (v. Discrepanza; stato CONFERMATA). Vincolo: Continuità lore. Verifica: Confronto occorrenze.
  - Prescrizione: Uniformare a 15 anni/2011 e al garage di via Tombetta in Pref L45, C01 L29, C05 L224, Toolkit L59, L202, L289.
  - Occorrenze collegate: Toolkit L289 «2004» (A01)
- **B06 — Tolleranze e strumenti di misura (conflitto di governance G1)** (v. Discrepanza; stato CONFERMATA). Vincolo: ADR0001:12 («centesimo di millimetro») vs CONTEXT:93-95 e ADR0002:14 (2 micron, «Avoid: tolleranza centesimale»). Verifica: Confronto governance/testo; risoluzione strumentale (0,01 mm non verifica 2-6 µm).
  - Prescrizione: Governance: allineare ADR0001:12 a CONTEXT:93 (0,002 mm su Kuka/Hydac). Testo: usare la tolleranza canonica per i pezzi critici e «centesimi» solo per lavorazioni non critiche; sostituire micrometro centesimale/calibro (C02 L78, L92) e «precisione centesimale» (C07 L252) con strumenti adeguati (micrometro millesimale, comparatore, tastatore con ripetibilità ≤ 1 µm, CMM); correggere Pref L46, C02 L227, C04 L55/L85, C07 L161/199/232/246, C08 L11, Manifesto L450.
  - Occorrenze collegate: Conflitto G1 (00_PRE_FLIGHT)
- **B20 — Prefazione — Core Relational Theme della rabbia** (`PREFAZIONE_METODOLOGICA.md` L91; stato CONFERMATA). Vincolo: Fact-checking (Lazarus 1991); coerenza interna (C04 L179). Verifica: Verifica esterna: https://en.wikipedia.org/wiki/Core_relational_theme (consultata 2026-10-01) + C04 L179.
  - Prescrizione: «davanti a una *demeaning offense against me and mine* (un'offesa svilente contro di me e ciò che è mio)».
- **B14 — Cap. 1 — saggistica nell'Atto II** (`CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L97–119; stato CONFERMATA). Vincolo: ADR0002:17 (teoria solo in Atti III e V). Verifica: Lettura.
  - Prescrizione: Spostare L109-117 nella sezione «Il processo invisibile» (Atto III) o ridurle a un beat in scena.
- **B16 — Kitchen test — battute didattiche** (v. Discrepanza; stato CONFERMATA). Vincolo: SKILL 1.2 (dialogo come negoziazione, non lezione). Verifica: Kitchen test.
  - Prescrizione: Riformulare le tre battute in lingua di mestiere e sottotesto (es. Elena: la scadenza, il foglio dei vincoli mai consegnato), lasciando la teoria all'Atto III.
- **B13 — Cap. 2 — POV e saggistica in scena** (`CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L24–235; stato CONFERMATA). Vincolo: ADR0002:13, :17; SKILL 3.3 (double telling). Verifica: Lettura + scansione.
  - Prescrizione: Tagliare L38 seconda frase, L213 seconda e terza frase, L231; trasformare L235 in percezione di Sara limitata a ciò che vede; L225 esteriorizzare.
- **B17 — Cap. 2 — plausibilità giuridica del patto con Davide** (`CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L241; stato PROBABILE). Vincolo: ADR0002:14 (verità materiale). Verifica: Conoscenza giuslavoristica generale (non verificata esternamente).
  - Prescrizione: «Addendum individuale (patto formativo)»; procedura disciplinare con tempi coerenti; sanzione conservativa progressiva al posto della giusta causa; aggiungere la clausola sul rinnovo del contratto a termine e l'orario compatibile.
- **B11 — Atto IV — chiusure consolatorie** (v. Discrepanza; stato CONFERMATA). Vincolo: Pref L131 («NESSUN LIETO FINE»), L142 («Non esistono conversioni miracolose, abbracci consolatori»); SKILL 4.1/4.3. Verifica: Lettura Atti IV; red-team SKILL 4.3.
  - Prescrizione: C03: inserire un'obiezione e un costo (scaglionamento non unanime), togliere «per il resto della sua vita»; C04: togliere «mai più» e «pacificato», lasciare rabbia residua e rischio della riserva; C07: aggiungere una contropartita o un limite (decorrenza differita, periodo di verifica, firma congiunta sul fermo lotti) e togliere L213; C08: sostituire perdono/abbraccio con un gesto materiale e un residuo (recesso non ancora ritirato, visita medica in sospeso).
  - Occorrenze collegate: C05 e C09 conformi
- **B09 — Istituto di credito (NexSys / rete)** (`CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` L14–178; stato CONFERMATA). Vincolo: ADR0001:13 (Mediocredito/FCG); mandato (fido presso Mediocredito). Verifica: Confronto occorrenze.
  - Prescrizione: Adottare Mediocredito per fido NexSys e linee di rete; correggere C03 L178 (e note), C05 L11, L43, L47, L124, L128, L196, L240, Pref L47.
  - Occorrenze collegate: C01 L105 «Mediocredito»
- **B10 — Calendario di cassa del Cap. 3** (`CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md` L75–222; stato CONFERMATA). Vincolo: Coerenza temporale. Verifica: Calendario 2025.
  - Prescrizione: L75 «giovedì mattina»; scegliere una sola data di erogazione: o venerdì 28 (togliere L222 «giovedì 27…») o giovedì sera, con saldo anticipato al venerdì.
- **B01 — Calendario globale (anno)** (v. Discrepanza; stato CONFERMATA). Vincolo: Coerenza cronologica. Verifica: Calendario perpetuo; confronto etichette.
  - Prescrizione: Fissare l'anno narrativo 2025-2026 e correggere: C04 L264 «budget 2025»; C05 «Budget Consolidato 2026»; C07 L7 «2026»; C08 protocollo «VR-2026-…»; C09 L10 «2026-2029»; C09 L228 «aprile 2026 … settembre 2026».
  - Occorrenze collegate: C07 Note L355 «primavera 2027»
- **B08 — Climatizzazione del capannone O.M.P.** (`CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L12; stato CONFERMATA). Vincolo: Continuità ambientale. Verifica: Confronto capitoli.
  - Prescrizione: C04 L12: limitare la climatizzazione alla sala metrologica/collaudo o eliminarla.
- **B12 — Cap. 4 — metalabel e neurolessico in Atti I e IV** (`CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L12–260; stato CONFERMATA). Vincolo: ADR0002:13 (Deep POV Grado 4), ADR0002:17 (purezza Atti I, II, IV). Verifica: Scansione lessicale + lettura.
  - Prescrizione: Sostituire ogni etichetta con percezione o azione dal mestiere di Silvano (rumore, mani, pezzo); eliminare metriche non percepibili (hertz, pulsazioni) e il lessico del metodo nelle scene.
  - Occorrenze collegate: Revisione alternativa in revisioni/2026-09-29_CAPITOLO_04 già priva di questi residui
- **B15 — Cap. 4 — beat economy nell'Atto II** (`CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L133–155; stato CONFERMATA). Vincolo: SKILL 1.5 (max 3 battute senza beat). Verifica: Scansione deterministica + verifica manuale.
  - Prescrizione: Inserire beat materiali (minestra, cucchiaio, sigaretta, piattino) a L137 e L151; sostituire le attribuzioni di L149/L153 con gesti.
  - Occorrenze collegate: C01 L67-73 (P3 C05)
- **B19 — Citazioni dirette non verificabili** (v. Discrepanza; stato PROBABILE). Vincolo: Fact-checking; Pref L57 (pilastri scientifici). Verifica: Confronto con le opere citate per quanto noto; NON VERIFICABILE ESTERNAMENTE nelle edizioni.
  - Prescrizione: Verificare sulle edizioni (pagina) o convertire in parafrasi senza virgolette con rinvio bibliografico.
  - Occorrenze collegate: C05 L148 «coincidono esattamente» (overclaim)
- **B03 — Profilo di Paolo Zantedeschi** (`CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L96–104; stato CONFERMATA). Vincolo: Continuità personaggi (mandato: commercialista e revisore). Verifica: Confronto C01/C06/C08.
  - Prescrizione: In C06 L96/L104 riformulare: «commercialista storico di Omnia e revisore, per anni consulente amministrativo di O.M.P.»; eliminare «Direttore Amministrativo… in pensione».
  - Occorrenze collegate: C06 L112 («Non so chi sia Marcolini»)
- **B07 — Materiale delle boccole Kuka** (`CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md` L161–199; stato CONFERMATA). Vincolo: C02 L12, L233 (boccole in 7075-T6/ergal). Verifica: Confronto C02/C04/C07.
  - Prescrizione: C07 L161 e L199: «boccole in ergal per Kuka e distributori in titanio per Hydac».
  - Occorrenze collegate: C07 L252
- **B18 — Cap. 8 — plausibilità sanitaria e giuridica dell'Atto IV** (`CAPITOLO_08_IL_GELO_TRA_PARI.md` L200–225; stato PROBABILE). Vincolo: ADR0002:14. Verifica: Conoscenza tecnica generale (non verificata esternamente).
  - Prescrizione: L200: il medico lo manda in PS, Luca rifiuta e chiama la moglie per il figlio; L222: «dichiarando superata la comunicazione e confermando la collegialità»; L225: polizza key-man/income protection al posto di D&O.
- **B04 — Profilo di Davide** (`CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L125–274; stato CONFERMATA). Vincolo: Continuità personaggi (C02 L18: 28 anni, laurea triennale, collaudatore). Verifica: Confronto C02/C09/Toolkit.
  - Prescrizione: C09 L125 «che ha ventotto anni»; C09 L274 e Toolkit L121 «collaudatore».
  - Occorrenze collegate: Toolkit L121
- **B05 — Parco macchine O.M.P.** (`CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L274; stato CONFERMATA). Vincolo: ADR0001:12 (44 macchine); C02 L10; C04 L12; C07 L60. Verifica: Confronto occorrenze e governance.
  - Prescrizione: C09 L274 «quarantaquattro macchine»; aggiornare ADR0001:12 in «44 macchine utensili, di cui 22 centri Mori Seiki a 5 assi».
- **B21 — Protocollo 180 s — respirazione 4-7-8** (`EPILOGO_E_TOOLKIT_OPERATIVO.md` L42; stato CONFERMATA). Vincolo: CONTEXT:50 (IO = espirazione prolungata 4-7-8). Verifica: Confronto con CONTEXT e con la stessa etichetta.
  - Prescrizione: «Inspira per 4 secondi, trattieni per 7, espira per 8» (un ciclo ≈ 19 s, quindi «circa due cicli nei primi 30-40 secondi»); togliere «10–15 battiti» o citarne la fonte.
  - Occorrenze collegate: S1 L92 «Espira per 7 secondi»

## Prescrizioni P3

- **C08 — Anzianità di Silvano** (v. Discrepanza; stato CONFERMATA). Vincolo: Continuità. Verifica: Confronto.
  - Prescrizione: Uniformare (es. «quarant'anni di mestiere, trentaquattro in O.M.P.»).
- **C29 — Ruolo professionale di Elena** (v. Discrepanza; stato CONFERMATA). Vincolo: ADR0001:15 (diritto del lavoro e consulenza di rete). Verifica: Confronto.
  - Prescrizione: Uniformare: «Studio Colombo & Associati, consulenza del lavoro e di rete».
- **C25 — Prefazione — esempi non corrispondenti** (`PREFAZIONE_METODOLOGICA.md` L49–139; stato CONFERMATA). Vincolo: Coerenza Prefazione/capitoli. Verifica: Confronto.
  - Prescrizione: Sostituire con esempi reali (10:17 sala riunioni; 18:47 mail della banca; 19:14 cella F148).
- **C01 — Cap. 1 — refuso** (`CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L41; stato CONFERMATA). Vincolo: Correttezza formale. Verifica: Lettura.
  - Prescrizione: «…dalla responsabilità decisionale: zucchero sull'offesa.»
- **C02 — Cap. 1 — intrusione onnisciente** (`CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L45; stato CONFERMATA). Vincolo: Deep POV. Verifica: Lettura.
  - Prescrizione: Ridurre al POV di Andrea («La frase era falsa, e Andrea lo sapeva»).
- **C05 — Cap. 1 — beat economy** (`CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L67–73; stato CONFERMATA). Vincolo: SKILL 1.5. Verifica: Scansione + verifica.
  - Prescrizione: Inserire un gesto di Elena o di Andrea a L71.
- **C03 — Cap. 1 — continuità di scena** (`CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L81–89; stato CONFERMATA). Vincolo: Continuità. Verifica: Lettura.
  - Prescrizione: L81 «riprese il coltello»; L89 «Male come?» o far dire ad Andrea «sprezzante».
- **C04 — Cap. 1 — terminologia penale** (`CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md` L247; stato CONFERMATA). Vincolo: Precisione terminologica. Verifica: Lettura.
  - Prescrizione: «sull'importo non consegnato».
- **C06 — Cap. 2 — raccordi orari e logistici** (`CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L74–223; stato CONFERMATA). Vincolo: Continuità. Verifica: Lettura.
  - Prescrizione: Uniformare vettore e orari; «ieri pomeriggio».
- **C07 — Cap. 2 — ruolo di Silvano** (`CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md` L76; stato CONFERMATA). Vincolo: Terminologia di ruolo. Verifica: Confronto.
  - Prescrizione: «il capofficina».
- **C09 — Residui di metalabel minori** (v. Discrepanza; stato CONFERMATA). Vincolo: ADR0002:13. Verifica: Scansione lessicale.
  - Prescrizione: Sostituire con percezioni o tagliare.
- **C10 — Cap. 4 — cifre nelle battute** (`CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L41–195; stato PROBABILE). Vincolo: Coerenza numerica. Verifica: Ricalcolo.
  - Prescrizione: L77 «tremila», «trecento blocchi»; L195 «una perdita di 140.000 euro di fatturato».
- **C11 — Cap. 4 — luoghi e fiera** (`CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L41–258; stato CONFERMATA). Vincolo: Fact-checking. Verifica: Verifica esterna: https://bauma.de/en/trade-fair/press/press-releases/detail/bauma-2025-final-report.html (2026-10-01).
  - Prescrizione: Fiera generica («una fiera di settore a fine gennaio»); un'unica città; «reso franco destino Stoccarda».
- **C12 — Cap. 4 — Mettilo in pratica** (`CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md` L306; stato CONFERMATA). Vincolo: Coerenza interna. Verifica: Confronto.
  - Prescrizione: «il Gantt dell'APS».
- **C30 — Sede di LogiDistretto** (v. Discrepanza; stato CONFERMATA). Vincolo: ADR0001:14 (Interporto Quadrante Europa). Verifica: Confronto.
  - Prescrizione: Uniformare la sede.
- **C13 — Cap. 5 — raccordi** (`CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md` L43–128; stato CONFERMATA). Vincolo: Continuità. Verifica: Lettura.
  - Prescrizione: Correggere data e ruolo; raccordo spaziale; «un ingegnere appena uscito dall'università».
- **C14 — Cap. 5 — tasso vs spread** (`CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md` L47–236; stato CONFERMATA). Vincolo: Terminologia finanziaria. Verifica: Ricalcolo 5,85 − 3 = 2,85.
  - Prescrizione: «il tasso effettivo è del 5,85%».
- **C15 — Cap. 6 — micro-continuità** (`CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L9–128; stato CONFERMATA). Vincolo: Continuità. Verifica: Lettura.
  - Prescrizione: Correggere numeri e raccordi.
- **C16 — Cap. 6 — sfrido e tolleranza barre** (`CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L279; stato PROBABILE). Vincolo: Coerenza numerica/tecnica. Verifica: Ricalcolo da base B = 78.400/0,114.
  - Prescrizione: «pari a circa 1.300 €» (o dichiarare la base); «barre rettificate h7».
- **C17 — Ponte Cap. 6 → Cap. 7** (`CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md` L346; stato CONFERMATA). Vincolo: Coerenza ponte. Verifica: Confronto.
  - Prescrizione: «due pacche sulla spalla e una promozione morale».
- **C19 — Precisione scientifica (sovra-affermazioni)** (v. Discrepanza; stato PROBABILE). Vincolo: Fact-checking. Verifica: Lettura critica.
  - Prescrizione: Attenuare («circuiti in parte sovrapposti»); correggere le formule e le attribuzioni.
  - Occorrenze collegate: C05 L148
- **C18 — Cap. 7 — raccordi** (`CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md` L9–250; stato CONFERMATA). Vincolo: Continuità. Verifica: Lettura.
  - Prescrizione: «una notte intera»; allineare turni; «emulsione tiepida».
- **C22 — Attribuzione del «carico allostatico» (governance G5)** (v. Discrepanza; stato PROBABILE). Vincolo: Fact-checking; CONTEXT:18, :34. Verifica: Conoscenza bibliografica generale.
  - Prescrizione: Correggere CONTEXT:18/:34 e C08 L139, C09 L154 (McEwen; allostasi: Sterling & Eyer).
- **C21 — Cap. 8 — micro-continuità** (`CAPITOLO_08_IL_GELO_TRA_PARI.md` L39–119; stato CONFERMATA). Vincolo: Continuità. Verifica: Confronto.
  - Prescrizione: Allineare i dettagli.
- **C20 — Cap. 8 — conteggio parole** (`CAPITOLO_08_IL_GELO_TRA_PARI.md` L77; stato CONFERMATA). Vincolo: Coerenza numerica. Verifica: Conteggio script.
  - Prescrizione: «quindici parole».
- **C23 — Cap. 9 — raccordi** (`CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L19–145; stato CONFERMATA). Vincolo: Continuità. Verifica: Lettura.
  - Prescrizione: Correggere i dettagli.
- **C24 — Cap. 9 — patto: firmatari e fonte dei 15.000 €** (`CAPITOLO_09_IL_CINISMO_DI_REPARTO.md` L223–234; stato PROBABILE). Vincolo: Coerenza contrattuale. Verifica: Lettura.
  - Prescrizione: Far firmare un delegato RSU; «quindicimila euro stanziati dal fondo di presidenza in sostituzione delle convention dei prossimi tre esercizi».
- **C31 — Epilogo — sintesi imprecise** (`EPILOGO_E_TOOLKIT_OPERATIVO.md` L15–450; stato CONFERMATA). Vincolo: Coerenza Epilogo/capitoli. Verifica: Confronto.
  - Prescrizione: «una capotecnica con ventidue anni di reparto»; «boccola per robot» e tolleranza canonica.
- **C26 — Uniformazione editoriale** (v. Discrepanza; stato CONFERMATA). Vincolo: Uniformità. Verifica: Grep + lettura.
  - Prescrizione: Pulizia redazionale secondo foglio di stile unico.
- **C27 — Riferimenti interni di governance nel testo** (v. Discrepanza; stato CONFERMATA). Vincolo: Uniformità/pubblicabilità. Verifica: Grep.
  - Prescrizione: Eliminare i riferimenti agli ADR o sostituirli con un rinvio alla Prefazione.
- **C28 — Governance — sede O.M.P. (G3)** (`docs/adr/0001-ecosistema-distrettuale-meccatronico.md` L12; stato CONFERMATA). Vincolo: Coerenza governance/testo. Verifica: Verifica esterna: https://www.tuttitalia.it/lombardia/52-quinzano-d-oglio/ (2026-10-01).
  - Prescrizione: Correggere ADR0001:12 in «Verona Est (San Michele Extra)».

## Verifica Epilogo e nove schede

L'Epilogo (L7-21) riprende i nove casi senza happy ending ed è coerente con il Modello B, salvo le sintesi imprecise di C31 e il riferimento all'ADR (C27). Il Protocollo dei 180 secondi (L25-66) rispetta la triade IO • ALTRI • ALTRO, ma contiene micro-richiami errati (A01) e una respirazione errata (B21).

| Scheda | Capitolo | Punto di svolta | Asse IO/ALTRI/ALTRO | Corrispondenza | Anomalia |
|---|---:|---|---|---|---|
| 1 — Sospetto tra pari (L77) | 1 | verifica mirata Zantedeschi, doppia firma, regola > 100k | presenti tutti e tre | parziale: motivazione di Luca alterata (L94), citazione parafrasata (L89) | A01 (collegata); C26 «DISINNEZCO» |
| 2 — Fuga dal conflitto (L104) | 2 | patto di affiancamento sull'isola 4, checkpoint MES 15:00 | presenti | parziale: Davide «perito», causa («utensile slittato») e «40 pezzi» non corrispondenti | B04, A01 |
| 3 — Panico da anticipazione (L131) | 3 | domanda di processo alla banca, controfirma di rete | presenti | **non corrispondente**: 150.000 € e «integrazione di bilancio» contro 300.000 € e perizia del software; Apex attribuito a NexSys | A01 |
| 4 — Commerciale contro produzione (L158) | 4 | rimodulazione 50 + 250, Feasibility Check | presenti | **non corrispondente**: «venerdì alle 16:00», «120 ore» contro 19 dicembre e 34 h | A01, A02 |
| 5 — Accentratore e delega (L185) | 5 | scheda dei vincoli a tre stadi | presenti | corrispondente (salvo «vent'anni di impresa», B02) | B02 |
| 6 — Guerra dei dati (L212) | 6 | TCO, Trafilerie Venete, MBO comune | presenti | parziale: Claudio «in O.M.P.», «tre notti» inesistenti, etichetta «risparmio lordo logistico» | A01 |
| 7 — Riconoscenza negata (L239) | 7 | domanda del pulsante rosso, tre condizioni, addendum | presenti | parziale: «vent'anni», «2 micron a trentacinque gradi» contro 22 anni e 6 µm a gennaio | A01, B06 |
| 8 — Gelo tra soci (L266) | 8 | lettera stracciata, accordo a quattro pilastri | presenti | **non corrispondente**: «2004», «scantinato», ALTRO diverso dall'accordo | A01, B02 |
| 9 — Cinismo di reparto (L293) | 9 | patto di trasparenza in quattro punti | presenti | **non corrispondente**: pagamento «entro fine mese» contro aprile/settembre; fatti aggiunti (padre di Dario, scarti aumentati) | A01, B01 |

Numero di schede: 9 su 9 ✓. Corrispondenza piena: 1 su 9.

## Limitazioni e punti non verificabili

- Le citazioni virgolettate attribuite a Damasio, Kahneman/Bloom e Lazarus & Folkman (B19) non sono state verificate sulle edizioni: NON VERIFICABILE ESTERNAMENTE.
- Non verificabili per dati mancanti: perimetro dell'APS (C04 L20-27); tasso del fido NexSys; platea e costo totale del premio (C09); base di calcolo dello sfrido (C06).
- La circolare ministeriale sull'asseverazione dei software (C03) è un elemento di finzione non verificabile, trattato come scelta autoriale.
- Il working tree locale del branch di lavoro non è stato aggiornato a `main` (merge vietato): il canone è stato letto dai blob Git in sola lettura. Questo non ha limitato la copertura.
- Su `main` esiste già un altro referto (`reports/2026-09-30_REFERTO_AUDIT_FINALE_OPERA_COMPLETA.md`, commit `b767fd1`), non considerato in questo audit, che è indipendente.

## Checklist di copertura

- [x] Prefazione letta
- [x] Capitolo 1 letto
- [x] Capitolo 2 letto
- [x] Capitolo 3 letto
- [x] Capitolo 4 letto
- [x] Capitolo 5 letto
- [x] Capitolo 6 letto
- [x] Capitolo 7 letto
- [x] Capitolo 8 letto
- [x] Capitolo 9 letto
- [x] Epilogo letto
- [x] Toolkit letto
- [x] `CONTEXT.md` letto
- [x] ADR 0001 letto
- [x] ADR 0002 letto
- [x] ADR 0003 letto
- [x] skill editoriale letta
- [x] Pilastro 1 completato
- [x] Pilastro 2 completato
- [x] Pilastro 3 completato
- [x] Pilastro 4 completato
- [x] controllo trasversale completato
- [x] P1 sottoposti a Red Team
- [x] numeri di riga ricontrollati (script)
- [x] estratti ricontrollati (script, verbatim)
- [x] conteggi P1/P2/P3 riconciliati (3/21/31)
- [x] nove schede verificate
- [x] referto validato
- [x] stato Git controllato

## Verdetto finale di collaudo

**NON IDONEO ALL'IMPAGINAZIONE.**

Motivazione: tre P1 confermati e non bonificati (A01 Toolkit incompatibile con i capitoli; A02 errore di capacità nella risoluzione del Cap. 4; A03 apparato di lavorazione interno nel testo canonico). Il verdetto è coerente con la matrice. Dopo la bonifica dei tre P1 e la correzione delle anomalie P2 di continuità e di coerenza tecnica (B01–B10), l'opera è candidabile a un collaudo di conferma con esito atteso «IDONEO ALL'IMPAGINAZIONE CON RISERVA».

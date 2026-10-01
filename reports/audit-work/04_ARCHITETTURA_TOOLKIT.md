# 04 ARCHITETTURA E TOOLKIT (capitoli/EPILOGO_E_TOOLKIT_OPERATIVO.md, 462 l.)
## Struttura toolkit
- §1 Epilogo 7-21 | §2 Protocollo 180 s 25-66 (4 fasi) | §3 Nove schede 70-318 (S1 77, S2 104, S3 131, S4 158, S5 185, S6 212, S7 239, S8 266, S9 293) | §4 10 frasi 320-401 | §5 Tabella sinottica 405-440 | §6 Manifesto 444-462.
- 9 schede ✓; ciascuna con IO/ALTRI/ALTRO ✓ (ADR0003 ✓); ciascuna con "Caso di Riferimento: Capitolo N" + nomi + "Fatti della Telecamera".
## Incongruenze toolkit ↔ capitoli (candidato P1 TOOL-01, sistemico)
- L43 F1: Andrea "alle 18:28 di martedì" vs C08 L5 lunedì 9/02.
- L52 F2: Dario "sul tavolo della saletta sindacale" vs C09 mensa; Gianni "rifiuta il melodramma del nipote" (Marta è la FIGLIA, C07 L86) + citazione «Dov'è il foglio con la firma? Chi ha approvato il cambio di procedura?» ≠ C07 L104.
- L59 F3: Enrico "Andrea gli aveva taciuto il debito di 498.700 euro con Mediocredito" vs C05 L53-55 (498.700 = discrepanza prodotta dai parametri 3%/60 gg); Luca "vent'anni di bilanci" (C08: 15); saturazione 98% "con il titanio per Hydac" (C04: Kuka/Apex).
- L64 F4: citazione di Silvano «Quanti pezzi all'ora... emulsione a dieci gradi... dodici minuti» assente da C04 (Silvano in C04: pugno, insulti; poi domanda su lotti parziali L238); Marta «fungo rosso... 2 micron sui 35 gradi» ≠ C07 L199 (deriva termica, gennaio, 6 µm), "vent'anni di officina" (22).
- S1 L89 citazione parafrasata come virgolettato; L94 Luca "esposizioni bancarie che non comprende fino in fondo" vs C01 L235 motivazione di Luca (coinvolgimento, rischio sulla sua gente); L82 refuso "DISINNEZCO".
- S2 L121 Davide "perito", "utensile slittato... non ha premuto lo stop" vs C02 (sonda/offset, schede MES non caricate, padre in chemio); L124 "lotto di 40 pezzi bloccato prima della spedizione" (C02: lotto scartato; lotto 180 spedito); L125 "penali da centomila euro" (C02: 800 €/h); L127 "valore nominale 0,8" (Ra 0,8 = limite massimo).
- S3 L132 + Tab L419-420 "buco Apex da 3,2M€ in NexSys" (Apex = cliente perso da OMP, C02 L10); L151 "integrazione di bilancio prima di deliberare l'estensione del fido di 150.000 euro" vs C03: supplemento istruttorio sulla perizia del software, fido 300.000 € (mandato: 300.000).
- S4 L170 "minacce di sciopero" (C04: dimissioni); L175 movente Fabio diverso da C04 L264; L178/L181 "consegna ... entro venerdì alle 16:00", "capacità disponibile sulle 5 assi di sole 120 ore", "120 ore mandrino libere da qui a venerdì" vs C04: 19 dicembre, riserva 34 h; terzista "di Quinzano" (nuovo).
- S5 L202 "vent'anni di impresa" (cluster 15/20).
- S6 L213 "Claudio del Magazzino in O.M.P. Precision" (Claudio = LogiDistretto); L229 "tre notti sotto l'acqua all'Interporto" (assente); L233 "risparmio lordo logistico di 48.000 €" (48.000 = risparmio d'acquisto vs storico, non logistico) + "utile netto consolidato" (C06: "beneficio netto"); h11 non presente in C06 (P3).
- S7 L251 "vent'anni di fedeltà" (22); L260/L262 "2 micron ... trentacinque gradi" vs C07 6 µm, gennaio.
- S8 L278 "diffida formale dell'avvocato" (C08: mail di Andrea con avvocato in copia); L286 "contabilità arretrata di quattro mesi" (assente); L289 "Non siamo più nel 2004 ... due periti in uno scantinato" vs C08 2011, garage via Tombetta; "dieci milioni di fatturato" (nuovo); ALTRO "Ristrutturazione quote operative, delega peritale esterna" ≠ accordo C08 L222-225.
- S9 L305 "dopo mesi di cassa integrazione", "aumentano gli scarti" (C09: boicottaggio straordinari del sabato); L310 "il padre morto d'infarto al tornio" (non presente in C09 = aggiunta non guadagnata); L316 "calendario dei pagamenti ... entro fine mese" vs C09 L228 (aprile/settembre).
- Tab L413 C1 "Sospetto di frode su bilancio" (C01: verifica di un piano d'investimento); L431 "2 micron"; L434 "stralcio PEC" (C08: e-mail).
- §4 L389 refuso "convocaiamoci"; L335 troncamento "irrevers."; L392 frase 9 attribuita al "(Capitolo 4)" (non pronunciata in C04).
## Governance nel toolkit
- L42 "Schema 4-7-8" descritto come inspirazione 4 s, apnea 2 s, espirazione 7 s (= 4-2-7) vs etichetta e CONTEXT:50 (4-7-8) → P2; "abbattendo la frequenza cardiaca di 10–15 battiti" quantificazione non supportata (P3).
- L11 "formalizzata nell'ADR 0002" (riferimento interno di progetto nel testo pubblicato) → cluster FORM.
- L15 "maestro d'officina con ventotto anni di reparto ... scavalcato da un giovane manager esterno" (fonde Dario 28 anni con Marta scavalcata) P3. L16 dACC/insula attribuite a Damasio (Eisenberger & Lieberman) P3.
- L450 "quote al centesimo di millimetro" (G1); "boccola aerospaziale" P3.
## Epilogo
- Coerente col Modello B; nessun nuovo personaggio; ripresa dei 9 casi ✓; nessun happy ending.

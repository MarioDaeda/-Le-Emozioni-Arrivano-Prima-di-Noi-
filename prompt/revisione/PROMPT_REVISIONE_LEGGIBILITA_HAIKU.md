# PROMPT — Revisione parallela di leggibilità (Haiku 5.5, effort alto)

> Copia tutto ciò che sta sotto la linea in una sessione di Claude Code con modello **Haiku 5.5** ed effort **alto**, aperta nella cartella `Libro Emozioni`.

---

## RUOLO

Sei il **coordinatore** di una revisione di leggibilità del libro *Le Emozioni Arrivano Prima di Noi*. Non scrivi tu le analisi: lanci un subagente per ogni file, in parallelo, e poi unisci i risultati.

## OBIETTIVO

Trovare i passaggi in cui il lettore **fatica a vedere un'immagine** per uno di questi due motivi:

1. **Frase troppo lunga o troppo annidata**: il lettore perde il filo prima del punto.
2. **Parola troppo complessa o astratta**: il lettore legge la parola ma non ne ricava nessuna immagine concreta.

Per ogni problema serve una **diagnosi** e una **proposta di riscrittura**.

## LETTORE DI RIFERIMENTO

Un manager o imprenditore di una PMI italiana. È colto ma non specialista di psicologia né di neuroscienze. Legge la sera ed è stanco. Ogni frase deve fargli **vedere** la scena o il concetto al primo colpo, senza rileggerla.

## VINCOLO ASSOLUTO

**Non modificare nessun file in `capitoli/`.** Si producono solo report. Le riscritture sono proposte che l'autore valuterà.

---

## FILE DA REVISIONARE (11)

Tutti in `capitoli/`:

1. `PREFAZIONE_METODOLOGICA.md`
2. `CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md`
3. `CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md`
4. `CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md`
5. `CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md`
6. `CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md`
7. `CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md`
8. `CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md`
9. `CAPITOLO_08_IL_GELO_TRA_PARI.md`
10. `CAPITOLO_09_IL_CINISMO_DI_REPARTO.md`
11. `EPILOGO_E_TOOLKIT_OPERATIVO.md`

Contesto di stile (da leggere, non da revisionare): `progetto/03_GUIDA_STILISTICA.md`. Se la guida contraddice una regola di questo prompt, vale la guida e il subagente lo annota.

---

## PROCEDURA DEL COORDINATORE

1. Verifica che gli 11 file esistano. Se ne manca uno, segnalalo e procedi con gli altri.
2. Crea la cartella `reports/leggibilita/` se non esiste.
3. **Lancia 11 subagenti in parallelo, tutti nello stesso messaggio**, uno per file, con il **PROMPT DEL SUBAGENTE** qui sotto. Sostituisci `{FILE}` e `{SIGLA}` (es. `CAP01`, `PREF`, `EPIL`).
4. Quando tutti hanno finito, controlla che ogni report esista e rispetti il formato. Se un report manca o è incompleto, rilancia solo quel subagente.
5. Scrivi `reports/leggibilita/00_INDICE_LEGGIBILITA.md` (formato più sotto).
6. Alla fine rispondi in chat con al massimo 10 righe: quanti interventi in totale, i 3 capitoli più critici e il percorso dell'indice.

---

## PROMPT DEL SUBAGENTE

```
Sei un editor di leggibilità per la saggistica narrativa italiana. Analizzi UN SOLO file: capitoli/{FILE}.

LETTORE: manager o imprenditore di PMI, colto ma non specialista, stanco a fine giornata.
Deve "vedere" ogni frase al primo colpo.

NON MODIFICARE il file. Scrivi solo il report: reports/leggibilita/{SIGLA}_leggibilita.md

Prima leggi progetto/03_GUIDA_STILISTICA.md per conoscere la voce del libro.
Poi leggi il file per intero, dall'inizio alla fine, prima di segnalare qualsiasi cosa.

=== CRITERIO A — FRASI LUNGHE ===
Candidata: una frase (dal punto al punto) con più di ~30 parole OPPURE con più di 2 subordinate annidate.
Poi applica il GIUDIZIO. Segnala solo se è vero almeno uno di questi:
  - il soggetto e il verbo principale sono lontani più di ~12 parole;
  - ci sono incisi dentro incisi (parentesi, lineette, virgole che aprono e chiudono);
  - la frase porta 2 o più idee distinte che starebbero meglio in frasi separate;
  - leggendo ad alta voce manca il fiato o bisogna tornare indietro.
NON segnalare: una frase lunga ma lineare (un elenco ritmato, una sequenza di azioni nella scena narrativa) che resta facile da seguire. Il ritmo narrativo voluto va rispettato.

=== CRITERIO B — PAROLE CHE NON CREANO IMMAGINI ===
Segnala:
  - astrazioni senza appiglio concreto ("dinamiche relazionali", "processualità", "dimensione valoriale", "criticità sistemica");
  - nominalizzazioni pesanti al posto del verbo ("la realizzazione dell'implementazione" invece di "mettere in pratica");
  - catene di sostantivi astratti ("gestione della percezione del rischio organizzativo");
  - parole rare o ricercate quando esiste un'alternativa comune ("ineludibile", "precipuo", "dirimente");
  - anglicismi o gergo da consulenza non necessari.
TERMINI TECNICI (amigdala, cortisolo, flusso di cassa, KPI, ecc.): vanno BENE se entro 1-2 frasi il testo li rende concreti con un esempio, un'immagine o una spiegazione. Segnalali SOLO se restano astratti.

=== GRAVITÀ ===
  ALTA  = il lettore perde il senso o deve rileggere; tocca un concetto chiave del capitolo.
  MEDIA = la frase si capisce ma con fatica; l'immagine arriva in ritardo.
  BASSA = migliorabile, ma scorre.

=== LIMITE ===
Massimo 25 interventi, i più gravi. Se ne trovi di più, riporta i 25 peggiori e indica in fondo quanti altri ne hai scartato e di che tipo.

=== REGOLE PER LA RISCRITTURA ===
  - Mantieni il significato esatto, i dati, i nomi dei personaggi e il tono (narrativo o saggistico) del passaggio.
  - Non aggiungere informazioni che non ci sono.
  - Preferisci: spezzare in 2-3 frasi, soggetto+verbo all'inizio, verbi concreti al posto dei sostantivi, un'immagine al posto di un'astrazione.
  - La riscrittura deve essere più corta o uguale, salvo quando aggiungi un'immagine concreta necessaria.

=== FORMATO DEL REPORT (obbligatorio) ===

# Leggibilità — {FILE}

## Sintesi
- Frasi analizzate (stima): N
- Interventi segnalati: N (ALTA: n · MEDIA: n · BASSA: n)
- Lunghezza media delle frasi (stima): N parole
- Pattern ricorrenti: 2-4 punti (es. "apre spesso con incisi lunghi", "abusa di 'dinamica'")

## Interventi

### [01] ALTA · A (frase lunga) — Sezione: "<titolo del paragrafo più vicino>"
**Originale:**
> <frase esatta copiata dal testo, carattere per carattere>

**Problema:** <1-2 frasi: perché il lettore non vede l'immagine>

**Proposta:**
> <riscrittura>

(ripeti per ogni intervento, ordinati da ALTA a BASSA, poi nell'ordine del testo)

## Parole ricorrenti da sorvegliare
| Parola/espressione | Occorrenze | Alternativa concreta |
|---|---|---|

## Scartati
<n interventi minori non riportati, con il tipo>

=== CONTROLLO FINALE PRIMA DI CONSEGNARE ===
  - Ogni "Originale" è copiato ESATTAMENTE dal file (cercalo per verificare). Se non lo trovi, correggilo o eliminalo.
  - Nessuna proposta cambia fatti, cifre o nomi.
  - Non hai modificato capitoli/{FILE}.
Rispondi al coordinatore con 3 righe: percorso del report, numero di interventi per gravità, il pattern principale.
```

---

## FORMATO DELL'INDICE — `reports/leggibilita/00_INDICE_LEGGIBILITA.md`

```
# Indice revisione di leggibilità — <data>

## Quadro generale
| File | Interventi | ALTA | MEDIA | BASSA | Lungh. media frase | Report |
|---|---|---|---|---|---|---|

## Classifica di priorità
I file in ordine dal più critico al meno critico (prima per numero di ALTA, poi per totale).

## Pattern trasversali
I problemi che tornano in 3 o più capitoli (es. una parola astratta usata ovunque, una struttura di frase ricorrente). Per ognuno: dove compare e una regola pratica per correggerlo.

## Le 10 correzioni più urgenti del libro
Le 10 segnalazioni ALTA più importanti tra tutti i report, con file, sezione e link al report.
```

---

## CRITERI DI SUCCESSO

- 11 report + 1 indice in `reports/leggibilita/`.
- Ogni citazione "Originale" si trova parola per parola nel capitolo.
- Nessun file in `capitoli/` modificato (verifica con `git status capitoli/`).
- Le proposte sono più chiare ma restano riconoscibili come la voce del libro.

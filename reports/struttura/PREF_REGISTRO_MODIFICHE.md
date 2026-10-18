# Registro delle modifiche: Prefazione metodologica

- Data: 2026-10-18
- Ramo: `revisione-pref` (da `riordino-cartella`, perché `main` non ha né il glossario né i report; non unito, nessun push)
- File modificato: `capitoli/PREFAZIONE_METODOLOGICA.md`
- Commit:
  1. `aa61ce4` revisione(pref): interventi di struttura
  2. `d1e8a90` revisione(pref): interventi di frase e glossario
  3. `e9edaa9` revisione(pref): ripristina as-if loop e bias nel diagramma
- Per vedere solo il lavoro di questo lotto: `git diff aa61ce4~1 -- capitoli/PREFAZIONE_METODOLOGICA.md`
- Decisioni dell'autore: D1 A, D2 A, D3 A

## Interventi di struttura

| Intervento | Stato | Nota |
|---|---|---|
| S01 Promessa in fondo | applicato | Promessa spostata in fondo alla sezione 1 («E io, che cosa ci faccio?»); nella sezione 6 resta un richiamo |
| S02 Sezione 4 senza domanda | applicato | Si apre con «Perché in riunione sbattiamo la cartellina prima di pensare?»; fisiologia ridotta (tolta la vasocostrizione splancnica) |
| S03 Modello A e postulati | applicato (D1 A) | Modello A ridotto a una frase; tre postulati tenuti, una riga ciascuno; tolto il rimando all'ADR 0002 |
| S04 Promessa tardiva | applicato | Assorbito da S01 |
| S05 Tono troppo sicuro | applicato | «Secondo una parte rilevante della ricerca»; «biosensori ad altissima precisione» → «segnali utili, da verificare prima di fidarsene» |
| S06 Barrett e Kahneman astratti | applicato | Una frase d'applicazione ciascuno, con materiale già nel testo (la frase del commerciale; Silvano) |
| S07 Silvano non riusato | applicato (D2 A) | Richiamato nell'Atto III fino a Emozione; Comportamento e Conseguenza non aggiunti |
| S08 Schede delle aziende | applicato (D3 A) | Schede ridotte al solo conflitto; tolti scantinato, trentadue dipendenti, dilatazione termica, mail della banca, buste paga, SAL |
| S09 Cinque Atti due volte | applicato | Tenuto il riquadro; elenco accorciato; Atto IV ridotto a tre idee |
| S10 Chiusura con «Buona lettura» | applicato | Chiusura con mappa minima, telecamera e domanda di processo |
| S11 Mappa minima in due versioni | applicato | Una sola formulazione a sei etichette (D9) in diagramma, riquadro e testo; aggiunta la domanda di richiamo |
| S12 Rimandi ADR | applicato | Tolti gli ADR 0001 e 0002; sezione 2 riaperta con la domanda sul sintomo |
| S13 Schema ripetuto | applicato | Risolto con S09 (conflitto S09/S13 deciso a favore di S09) |
| S14 Domanda di processo sepolta | applicato | Spostata nella sezione 6; nell'Atto III resta il rinvio |
| S15 Schede in elenco | applicato | Assorbito da S08 |
| S16 Seconda analogia | applicato | Tolti avvitatore e coppia di serraggio; resta il centro di lavoro |
| S17 Otto fratture | applicato | Ridotte a tre (Silvano, Marco, Andrea e Luca); le altre cinque rinviate al resto del libro |

## Interventi di frase

| Intervento | Stato | Nota |
|---|---|---|
| [01] Prima ancora che la neocorteccia | applicato | Proposta di Haiku, inserita nel paragrafo con [10] |
| [02] Avvitatore | superato | Tagliato da S16 |
| [03] Innesco | superato | Riscritto dal postulato 1 (D1 A) |
| [04] Otto fratture | superato | Sostituito da S17 |
| [05] Scheda di Omnia | superato | Ridotta da S08 |
| [06] Apertura sezione 4 | superato | Riscritta da S02 |
| [07] Sistema 1 confonde | applicato | Proposta di Haiku |
| [08] Promessa nella sezione 6 | superato | Spostata da S01; il testo della sezione 6 è nuovo |
| [09] Frizione sottile | applicato | Proposta di Haiku |
| [10] Fatto biologico | applicato | Proposta di Haiku, con la cautela di S05 |
| [11] Quando finalmente prendiamo la parola | applicato | Proposta di Haiku |
| [12] Sintomo di una frattura | applicato | Versione corretta del report («frattura organizzativa») |
| [13] ADR 0002 | applicato | Proposta di Haiku; «l'intera architettura di quest'opera adotta rigorosamente» → «il libro adotta» |
| [14] Vulnerabilità metabolica | superato | Frase riscritta nel postulato 2 (D1 A) |
| [15] Accetta di una tassonomia | superato | Riscritta nel postulato 3 |
| [16] Distretto | applicato | Proposta di Haiku, senza ADR 0001 |
| [17] Banca Popolare | superato | Scheda ridotta da S08 |
| [18] Fisiologia di Damasio | superato | Elenco ridotto da S02 |
| [19] Lazarus | applicato | Proposta di Haiku, con «tema relazionale centrale» (glossario 4) |
| [20] Predizione bayesiana | applicato | Versione corretta del report, con «cervello predittivo» |
| [21] Responsabilità e libertà | applicato | Proposta di Haiku |
| [22] Sistema 2 | applicato | Proposta di Haiku, con «pensiero lento, volontario» |
| [23] Sequestro attentivo | applicato | Citazione ancora identica dopo S09: vale l'eccezione del passo 3 |
| [24] Contratto di Salvaguardia | parziale | Frase già riscritta dall'Atto IV; applicato solo «perimetri operativi» → «confini del lavoro» |
| [25] Dischiuda la soglia | applicato | Citazione ancora identica: vale l'eccezione del passo 3 |

## Metriche

| | Prima | Dopo |
|---|---|---|
| Parole | 3085 | 2904 |
| Frasi | 97 | 125 |
| Media parole per frase | 31,8 | 23,2 |
| Frasi oltre 35 parole | 33% (32) | 16% (20) |
| Frasi oltre 50 parole | 19 | 8 |
| Gulpease | 41,3 | 48,3 |

## Eccezioni al glossario

Nessuna. Nel diagramma della sezione 4 ho usato le forme del glossario e riallineato i riquadri.

Aggiunte di definizioni dal glossario, tutte già approvate: omeostasi, euristica dell'affetto, Sistema 1 e 2, contratti psicologici. Tolto *demanding offense*. La «domanda di processo» (voce 12) è definita in sezione 6, con la domanda stessa.

## Non toccato, da decidere

Incongruenze di fatti notate in lettura e non corrette:

1. **Anni dei soci.** La sezione 1 parla di soci fondatori con «venticinque anni di successi condivisi». La sezione 3 dice che Omnia è «fondata vent'anni prima».
2. **Fondatori.** La scheda di Omnia diceva «fondata da Andrea e Luca» ma «passata da quattro pionieri». Nel testo ora c'è solo «fondata da Andrea e Luca»; il numero dei pionieri è stato tolto da S08. Va verificato nel registro di continuità.
3. **Tolleranze di OMP.** La sezione 3 parla di «tolleranze al centesimo di millimetro». `riferimenti/CONTEXT.md` fissa 2 micron per i pezzi in titanio (D1 del glossario). Dopo S08 la scheda non contiene più questa cifra, ma resta da decidere se serva una cifra nel libro.
4. **Settori di OMP.** La sezione 3 dice «oleodinamico e aerospaziale». CONTEXT.md parla di componenti medicali (Kuka) e idraulici (Hydac).
5. **Personaggi.** La sezione 6 nomina Sara e Dario, che la sezione 3 non presenta. Ho cercato Enrico, Dario e «trentadue dipendenti» nel registro di continuità senza trovare riscontri.
6. **Lazarus.** *Demanding offense* nel testo, *demeaning offense* nel glossario: risolta togliendo il termine inglese; resta da confermare il rimando se compare in CAP04.

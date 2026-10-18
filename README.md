# Le Emozioni Arrivano Prima di Noi

Cartella di lavoro del libro. Questa pagina dice dove sta ogni cosa e quale versione è quella corrente.

## Dove trovare cosa

| Cartella | Contenuto | Quando serve |
|---|---|---|
| `capitoli/` | **Testo definitivo**: prefazione, capitoli 1-9, epilogo e toolkit | Per leggere o correggere il libro |
| `progetto/` | Guida del progetto: linee guida, indice, personaggi, guida stilistica, matrice delle emozioni, registri (fonti, affermazioni, continuità), brief e manoscritti dei capitoli 1-2, stato di avanzamento, `sync_macro_to_files.py` | Per decidere voce, coerenza e metodo |
| `riferimenti/` | Glossario (`CONTEXT.md`), dossier delle fonti, mappa della filiera, matrice strutturale del capitolo 1, note di ricerca sulla leggibilità | Per controllare termini, fonti e fatti |
| `reports/` | Esiti delle revisioni: `audit/` (audit forensi e psicologico), `analisi_2026-10-12/`, `leggibilita/` (frasi), `struttura/` (struttura, glossario proposto, registro modifiche del capitolo 3) | Per vedere che cosa è stato controllato e deciso |
| `prompt/` | Prompt già usati o riutilizzabili, divisi in `stesura/`, `audit/`, `riscrittura/`, `revisione/` | Per rilanciare una revisione |
| `strumenti/` | `assemble_book.ps1` (assembla il libro), skill di editing creativo | Per automatismi |
| `docs/` | Decisioni di progetto (ADR) | Per capire perché il libro è impostato così |
| `fonti/` | Biblioteca e materiali di ricerca (non condivisa, esclusa da git) | Per consultare le fonti |
| `archivio/` | Versioni superate o generate: vedi sotto | Solo per recuperare il passato |

## Nell'archivio

- `bozze_capitoli/`: le bozze dei capitoli, diverse dal testo in `capitoli/`. `assemble_book.ps1` le legge ancora da qui.
- `LIBRO_COMPLETO_LE_EMOZIONI_ARRIVANO_PRIMA_DI_NOI.md`: il libro assemblato dalle bozze. È un file generato, non da modificare.
- `revisioni/`: riscritture e revisioni datate dei capitoli.
- `macro_radice/`: i cinque file "macro" che stavano nella radice. Sono diversi dai file con lo stesso nome in `progetto/`, che sono quelli da usare.
- `duplicati/`: copie identiche ad altri file (`SKILLS.md` e lo zip della skill).
- `old_submodule/`: il vecchio sottomodulo dismesso (escluso da git).
- `tmp/`: script e PDF temporanei.

## Flusso di lavoro per un capitolo

1. Si modifica il testo in `capitoli/`.
2. Le decisioni di voce e di coerenza si controllano in `progetto/03_GUIDA_STILISTICA.md` e `progetto/08_REGISTRO_DELLA_CONTINUITÀ.md`.
3. I prompt di `prompt/revisione/` producono report in `reports/leggibilita/` e `reports/struttura/`.
4. Le modifiche applicate si annotano in `reports/struttura/CAPxx_REGISTRO_MODIFICHE.md`.

## Da sapere

- `assemble_book.ps1` ha ancora il percorso base di Windows (`C:\Users\MARIO\Libro Emozioni`): va adattato prima di usarlo su questo computer.
- I report storici in `reports/` e le note in `.agents/` citano ancora i vecchi percorsi (per esempio `bozze_capitoli/`): sono registri di lavori già fatti e non sono stati modificati.

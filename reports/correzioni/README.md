# Bonifica editoriale — registro e metodo

Questa cartella contiene gli strumenti di lavoro della bonifica pianificata sul referto `reports/AUDIT_REVISIONE_CLAUDE.md`, che resta invariato.

## REGISTRO_ANOMALIE.tsv

- **Una riga per anomalia del referto (record PADRE o SINGOLA).** Sono 55: P1 3, P2 21, P3 31.
- **Sotto-voci per file (SOTTOVOCE)** per le anomalie che toccano più file: ogni intervento riguarda un solo file.
- **Nuovi ID:** `P1-01…`, `P2-01…`, `P3-01…`. La colonna `ID_REFERTO` conserva l'ID originale (A01, B06, C26…).
- **Capitoli:** si scrivono sempre `Cap.0N`. Questo elimina la collisione del referto tra gli ID P3 C01–C09 e le sigle dei capitoli.
- **C26 (uniformazione formale) è scomposta così:**

  | Sotto-voce | Contenuto |
  |---|---|
  | `a` | BOM del Cap.08 |
  | `b` | grassetti nel Cap.08 |
  | `c1`, `c2` | intestazioni Atto V dei Cap.01 e Cap.06 |
  | `d` | refusi del Toolkit |
  | `e` | indice del master |
  | `f1`–`f3` | nomi societari |

- **Classi:** FATTUALE, FORMALE, DEEP_POV, PROPOSTA (B11, B19: solo proposte da approvare), SPECIALISTICA (B17, B18, C16, C19, C22: nessuna applicazione automatica), GOVERNANCE.
- **Stati:** APERTA / IMPLEMENTATA — IN ATTESA DI RICOLLAUDO / CHIUSA (solo dopo il collaudo finale) / NON APPLICABILE.
- **P1 al 2026-10-01:** A02 (commit `441613c`) e A03 (commit `a69b8ef`) IMPLEMENTATE — IN ATTESA DI RICOLLAUDO; A01 APERTA.

I numeri di riga sono quelli del referto (canone `1f51621`): nei capitoli successivi ad A02/A03 possono essere slittati. Per localizzare i passi fanno fede gli estratti.

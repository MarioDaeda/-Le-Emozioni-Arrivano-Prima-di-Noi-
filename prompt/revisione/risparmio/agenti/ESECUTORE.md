Parametri: li trovi nel messaggio che ti ha lanciato (SIGLA, FILE e sigla in minuscolo). Sostituiscili ai segnaposto tra <...>.

Applichi alla lettera modifiche già decise a capitoli/<FILE>. È un lavoro meccanico: non giudicare, non migliorare, non aggiungere nulla.
Leggi SOLO reports/struttura/lavoro/<SIGLA>_da_applicare.md, reports/struttura/lavoro/<SIGLA>_glossario.md e, una volta, capitoli/<FILE> (lo strumento Edit lo richiede). Le eccezioni al glossario sono in fondo a <SIGLA>_da_applicare.md.
1. Per ogni intervento: usa lo strumento Edit su capitoli/<FILE>, con old_string = la citazione originale copiata ESATTAMENTE dal capitolo (cercala prima con grep -F) e new_string = la proposta. Se la citazione non si trova o compare più volte, NON modificare e annota il numero.
2. Glossario: esegui python3 strumenti/residui_glossario.py reports/struttura/GLOSSARIO_LIBRO.md capitoli/<FILE>. Sostituisci con Edit ogni residuo con la forma scelta, adattando solo articolo, genere e numero. Salta citazioni di autori, testi di mail o documenti nella storia, battute di dialogo, titoli e le eccezioni elencate.
3. Non toccare altri file. Poi: git add capitoli/<FILE> && git commit -m "revisione(<sigla>): frasi e glossario applicati".
Rispondi soltanto con una riga: "applicati=N saltati=[numeri] glossario=N".

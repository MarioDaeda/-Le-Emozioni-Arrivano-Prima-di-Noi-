# Lotto APPLICA (sessione Sonnet 5.5: struttura, fermate e revisione; Haiku esegue)

Input: una sola sigla. Output: il capitolo revisionato sul ramo `revisione-<sigla>` e `reports/struttura/<SIGLA>_REGISTRO_MODIFICHE.md`.

Leggi soltanto:
- il capitolo, **una volta**;
- `reports/struttura/lavoro/<SIGLA>_scheda.md`;
- `reports/struttura/lavoro/<SIGLA>_glossario.md`;
- `progetto/03_GUIDA_STILISTICA_SINTESI.md`.

Non leggere i report completi, il glossario completo, la guida completa o il registro della continuità. Dal registro prendi con grep solo il fatto che ti serve.

## 0. Preparazione (script e un subagente)
1. **Controlli.** Fermati e dimmelo se uno fallisce:
   - esiste `reports/struttura/<SIGLA>_struttura.md`;
   - esiste `progetto/03_GUIDA_STILISTICA_SINTESI.md`;
   - `git switch main` riesce;
   - `git status --short capitoli/<FILE>` è vuoto.
2. `git switch -c revisione-<sigla in minuscolo>`. Poi `mkdir -p reports/struttura/lavoro`.
3. **Script:**
   - `python3 strumenti/metriche_leggibilita.py capitoli/<FILE>`: annota il risultato;
   - `python3 strumenti/scheda_glossario.py <SIGLA> > reports/struttura/lavoro/<SIGLA>_glossario.md`.
4. **Scheda.** Lancia un subagente `model: "haiku"` con il prompt `Esegui prompt/revisione/risparmio/agenti/SCHEDA.md con SIGLA=<SIGLA>, FILE=<FILE>`. Se restituisce il testo invece di scriverlo, salvalo tu. Poi esegui `python3 strumenti/verifica_citazioni.py reports/struttura/lavoro/<SIGLA>_scheda.md capitoli/<FILE>`. Se una citazione non viene trovata, recuperala con grep dal report originale e correggila nella scheda.
5. Leggi i quattro file elencati in cima a questa pagina.

## 1. Prima fermata
Mostrami in una volta sola:
- **a.** le domande per l'autore, ognuna con 2–3 opzioni;
- **b.** i conflitti tra interventi;
- **c.** le eccezioni al glossario che proponi per questo file;
- **d.** le incongruenze di fatti. Prima controlla con `grep -n -A30 "Decisioni dell'autore" "progetto/08_REGISTRO_DELLA_CONTINUITÀ.md"` se sono già decise.

Poi **aspetta**. Le voci senza risposta restano come sono.

## 2. Struttura (tu)
1. Applica gli interventi [S..] confermati nell'ordine della scheda, con Edit sul solo tratto interessato.
2. Rileggi solo il paragrafo prima e quello dopo ogni intervento. Alla fine rileggi solo i punti di passaggio tra le sezioni toccate, con offset e limit: non il capitolo intero.
3. Gli interventi che non si possono applicare senza inventare vanno saltati e annotati.
4. `git add capitoli/<FILE>`, poi `git commit -m "revisione(<sigla>): interventi di struttura"`.

## 3. Frasi e glossario (Haiku esegue, tu rivedi)
1. `python3 strumenti/prepara_da_applicare.py reports/struttura/lavoro/<SIGLA>_scheda.md capitoli/<FILE> > reports/struttura/lavoro/<SIGLA>_da_applicare.md`. Lo script tiene solo gli interventi da tenere e da correggere la cui citazione esiste ancora, una volta sola, dopo il passo 2. Elenca gli altri come superati.
2. In fondo a `<SIGLA>_da_applicare.md` aggiungi, con Edit, una sezione `## Eccezioni al glossario` con le eccezioni decise al passo 1.
3. **Superati e sospesi ancora presenti** (nel riepilogo dello script): valuta tu, uno per uno, se ne serve uno adattato.
4. Lancia un subagente `model: "haiku"` con il prompt `Esegui prompt/revisione/risparmio/agenti/ESECUTORE.md con SIGLA=<SIGLA>, FILE=<FILE>, sigla=<sigla in minuscolo>`.
5. **Revisione.** Leggi solo `git diff --word-diff=plain -U1 HEAD~1 -- capitoli/<FILE>`. Correggi con Edit:
   - le frasi meno naturali dell'originale o fuori dalla voce;
   - i passaggi rotti tra una frase e l'altra;
   - le sostituzioni del glossario finite in eccezioni.
6. Commit con il solo capitolo: `revisione(<sigla>): revisione delle frasi`.

## 4. Verifica
1. `python3 strumenti/controllo_fatti.py capitoli/<FILE> main`. Ogni numero o nome proprio sparito deve essere stato tolto apposta da un intervento approvato. Se non lo è, ripristinalo con un commit.
2. `python3 strumenti/residui_glossario.py reports/struttura/GLOSSARIO_LIBRO.md capitoli/<FILE>`. Correggi i residui che non sono eccezioni.
3. Ripeti le metriche del passo 0.3. Non spezzare frasi solo per alzare il Gulpease.
4. Lancia un subagente `model: "haiku"` con il prompt `Esegui prompt/revisione/risparmio/agenti/LETTORE.md con FILE=<FILE>`.

## 5. Seconda fermata
Mostrami:
- le metriche prima e dopo;
- i numeri degli interventi applicati, saltati, superati e sospesi;
- l'esito del controllo dei fatti;
- i 3 punti del lettore stanco;
- `git log --oneline main..HEAD` e `git diff --stat main -- capitoli/<FILE>`;
- il comando `git diff main -- capitoli/<FILE>`, da lanciare io.

Poi **aspetta**. Applica le correzioni che ti chiedo, con un commit.

## 6. Registro e unione
1. Scrivi `reports/struttura/<SIGLA>_REGISTRO_MODIFICHE.md` nel formato di quello di CAP03:
   - intestazione con data, ramo e commit;
   - tabella degli interventi con stato e nota;
   - metriche;
   - eccezioni al glossario;
   - "Non toccato, da decidere".

   Fai un commit con il solo registro.
2. **Solo se ti scrivo "unisci":** `git switch main` e `git merge --no-ff revisione-<sigla>`.
3. Rispondi con 3 righe: stato, registro, messaggio della prossima sessione preso da `prompt/revisione/PROMPT_REVISIONE_LIBRO_RISPARMIO.md`.

# Assemble Master Book: Le Emozioni Arrivano Prima di Noi
$ErrorActionPreference = "Stop"

$baseDir = "C:\Users\MARIO\Libro Emozioni"
$bozzeDir = Join-Path $baseDir "bozze_capitoli"
$outputFile = Join-Path $baseDir "LIBRO_COMPLETO_LE_EMOZIONI_ARRIVANO_PRIMA_DI_NOI.md"

$sb = New-Object System.Text.StringBuilder

# 1. FRONT MATTER & INTRODUZIONE
$frontMatter = @"
# LE EMOZIONI ARRIVANO PRIMA DI NOI
## Anatomia delle fratture relazionali nell'ecosistema d'impresa: neuroscienze, appraisal cognitivo e telemetria dei comportamenti organizzativi

---

**Modello di Riferimento**: Modello B — Fratture Organizzative e Soggetti Complessi (ADR 0002)  
**Collana**: Saggistica Manageriale & Filosofia d'Impresa  
**Edizione**: Prima Edizione Integrale — Settembre 2026  
**Curatela Scientifica ed Editoriale**: Mario Daeda & Antigravity Research Lab  
**Ambiente Distrettuale**: Omnia S.r.l. • OMP Precision S.r.l. • NexSys Automation S.r.l. • LogiDistretto S.c.a.r.l. • Studio Colombo & Associati  

---

> *«Il corpo possiede una saggezza biologica immediata: avverte, contrae, protegge, prepara all'azione. Ma la mente, nel tentativo di spiegare quella stretta viscerale, costruisce narrazioni affrettate, attribuisce colpe e trasforma una sensazione interna in una condanna dell'altro. La sfida della leadership matura comincia quando smettiamo di usare il nostro allarme corporeo come un verdetto giuridico e iniziamo a interrogarlo come una bussola di processo.»*

---

## Indice Generale

- [Frontespizio e Colophon](#le-emozioni-arrivano-prima-di-noi)
- [Prefazione Metodologica: L'Invisibile nel Quotidiano d'Impresa](#prefazione-metodologica-linvisibile-nel-quotidiano-dimpresa)
  - [1. Perché questo libro: La frattura tra narrazione manageriale e realtà biologica](#1-perch%C3%A9-questo-libro-la-frattura-tra-narrazione-manageriale-e-realt%C3%A0-biologica)
  - [2. Il rifiuto del Modello A e la scelta del Modello B: Fratture Organizzative e Soggetti Complessi](#2-il-rifiuto-del-modello-a-e-la-scelta-del-modello-b-fratture-organizzative-e-soggetti-complessi)
  - [3. L'Ecosistema Distrettuale: Una Filiera Umana e Produttiva](#3-lecosistema-distrettuale-una-filiera-umana-e-produttiva)
  - [4. I Quattro Pilastri Scientifici: L'Integrazione Epistemologica](#4-i-quattro-pilastri-scientifici-lintegrazione-epistemologica)
  - [5. La Grammatica Operativa: La Struttura dei Cinque Atti](#5-la-grammatica-operativa-la-struttura-dei-cinque-atti)
  - [6. Come Leggere Questo Libro](#6-come-leggere-questo-libro)
- [Capitolo 1 — Le emozioni non arrivano a caso](#capitolo-1--le-emozioni-non-arrivano-a-caso)
  - *La frase nella sala riunioni: Andrea, Luca e il dubbio sull'investimento*
- [Capitolo 2 — Il sollievo fittizio e il costo dell'evitamento](#capitolo-2--il-sollievo-fittizio-e-il-costo-dellevitamento)
  - *Il colloquio rimandato: Sara, Davide, Marta e il debito relazionale*
- [Capitolo 3 — La cassa che brucia e il panico da anticipazione](#capitolo-3--la-cassa-che-brucia-e-il-panico-da-anticipazione)
  - *L'apertura di credito: Marco, NexSys Automation e la simulazione catastrofica*
- [Capitolo 4 — La promessa del commerciale e la macchina satura](#capitolo-4--la-promessa-del-commerciale-e-la-macchina-satura)
  - *L'ordine Hydac da centoquarantamila euro: Silvano, Fabio e la collisione tra vendita e officina*
- [Capitolo 5 — La solitudine dell'accentratore e la trappola della prima delega](#capitolo-5--la-solitudine-dellaccentratore-e-la-trappola-della-prima-delega)
  - *La commessa aeronautica: Andrea, Enrico e il terrore viscerale dell'espropriazione*
- [Capitolo 6 — La guerra dei territori e i dati come armi](#capitolo-6--la-guerra-dei-territori-e-i-dati-come-armi)
  - *I fogli Excel tra logistica e acquisti: Valerio, Claudio e la manipolazione delle scorte*
- [Capitolo 7 — La ferita della riconoscenza negata](#capitolo-7--la-ferita-della-riconoscenza-negata)
  - *La nomina scavalcata: Marta, l'ingegner Moretti e il collasso del contratto psicologico*
- [Capitolo 8 — Il gelo tra pari: la deriva tra soci fondatori](#capitolo-8--il-gelo-tra-pari-la-deriva-tra-soci-fondatori)
  - *L'illusione di intenzionalità: Andrea, Luca e l'incomunicabilità a metà del cammino*
- [Capitolo 9 — Il cinismo di reparto e l'anestesia difensiva](#capitolo-9--il-cinismo-di-reparto-e-lanestesia-difensiva)
  - *La convention aziendale e il "Progetto Fenice": Dario, l'officina e la trincea dell'indifferenza*
- [Epilogo & Toolkit Operativo di De-escalation](#epilogo--toolkit-operativo-di-de-escalation)
  - *Il Protocollo dei 180 Secondi*
  - *Le Dieci Frasi Tossiche e la loro Traduzione di Processo*
  - *La Matrice di Telemetria Emotiva Organizzativa*
  - *Manifesto Conclusivo: L'Impresa come Comunità di Senso e di Limite*

---

"@

[void]$sb.AppendLine($frontMatter)

# 2. PREFAZIONE METODOLOGICA
$prefPath = Join-Path $bozzeDir "PREFAZIONE_METODOLOGICA.md"
$prefContent = [System.IO.File]::ReadAllText($prefPath, [System.Text.Encoding]::UTF8)
[void]$sb.AppendLine($prefContent)
[void]$sb.AppendLine("`n---`n")

# 3. CAPITOLO 1
Write-Host "Appending CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md..."
$ch1Path = Join-Path $bozzeDir "CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md"
$ch1Content = [System.IO.File]::ReadAllText($ch1Path, [System.Text.Encoding]::UTF8)
# Normalizza i titoli di Atto V a livello H2 se necessario
$ch1Content = $ch1Content -replace "(?m)^# Mettilo in pratica", "## Mettilo in pratica"
$ch1Content = $ch1Content -replace "(?m)^# Da ricordare", "## Da ricordare"
[void]$sb.AppendLine($ch1Content)
[void]$sb.AppendLine("`n---`n")

# 4. CAPITOLI 2 - 9 & EPILOGO
$files = @(
    "CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md",
    "CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md",
    "CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md",
    "CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md",
    "CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md",
    "CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md",
    "CAPITOLO_08_IL_GELO_TRA_PARI.md",
    "CAPITOLO_09_IL_CINISMO_DI_REPARTO.md",
    "EPILOGO_E_TOOLKIT_OPERATIVO.md"
)

foreach ($f in $files) {
    Write-Host "Appending $f..."
    $filePath = Join-Path $bozzeDir $f
    $fileContent = [System.IO.File]::ReadAllText($filePath, [System.Text.Encoding]::UTF8)
    [void]$sb.AppendLine($fileContent)
    [void]$sb.AppendLine("`n---`n")
}

# 5. WRITE MASTER OUTPUT
Write-Host "Writing master book file: $outputFile..."
[System.IO.File]::WriteAllText($outputFile, $sb.ToString(), [System.Text.Encoding]::UTF8)

# 6. TELEMETRIA E VERIFICA
$finalContent = [System.IO.File]::ReadAllText($outputFile, [System.Text.Encoding]::UTF8)
$totalWords = ($finalContent -split '\s+').Count
$totalChars = $finalContent.Length
$totalLines = ($finalContent -split "`n").Count
$fileSizeKb = [Math]::Round((New-Object System.IO.FileInfo($outputFile)).Length / 1024, 2)

Write-Host "=========================================="
Write-Host "ASSEMBLAGGIO OPERA COMPLETATO CON SUCCESSO"
Write-Host "=========================================="
Write-Host "File generato: $outputFile"
Write-Host "Dimensione: $fileSizeKb KB"
Write-Host "Linee: $totalLines"
Write-Host "Caratteri: $totalChars"
Write-Host "Conteggio Parole Totale: $totalWords parole"
Write-Host "=========================================="

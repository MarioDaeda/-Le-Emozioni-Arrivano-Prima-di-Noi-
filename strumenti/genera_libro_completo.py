#!/usr/bin/env python3
"""Rigenera LIBRO_COMPLETO_LE_EMOZIONI_ARRIVANO_PRIMA_DI_NOI.md dalle bozze revisionate.

Fonte unica del testo: la cartella bozze_capitoli/. Uso:
    python3 strumenti/genera_libro_completo.py
"""
import re
from datetime import date
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
BOZZE = RADICE / "bozze_capitoli"
USCITA = RADICE / "LIBRO_COMPLETO_LE_EMOZIONI_ARRIVANO_PRIMA_DI_NOI.md"

ORDINE = [
    "PREFAZIONE_METODOLOGICA.md",
    "CAPITOLO_01_LE_EMOZIONI_NON_ARRIVANO_A_CASO.md",
    "CAPITOLO_02_IL_SOLLIEVO_FITTIZIO.md",
    "CAPITOLO_03_LA_CASSA_CHE_BRUCIA.md",
    "CAPITOLO_04_LA_PROMESSA_E_LA_MACCHINA.md",
    "CAPITOLO_05_LA_TRAPPOLA_DELLA_DELEGA.md",
    "CAPITOLO_06_LA_GUERRA_DEI_FOGLI_EXCEL.md",
    "CAPITOLO_07_LA_RICONOSCENZA_NEGATA.md",
    "CAPITOLO_08_IL_GELO_TRA_PARI.md",
    "CAPITOLO_09_IL_CINISMO_DI_REPARTO.md",
    "EPILOGO_E_TOOLKIT_OPERATIVO.md",
]

SOTTOTITOLI = {
    1: "La frase nella sala riunioni: Andrea, Luca e il dubbio sull'investimento",
    2: "Il colloquio rimandato: Sara, Davide, Marta e il debito relazionale",
    3: "L'apertura di credito: Marco, NexSys Solutions e la simulazione catastrofica",
    4: "L'ordine Hydac da 140.000 euro: Silvano, Fabio e lo scontro tra vendita e officina",
    5: "Il modello di cassa sbagliato: Andrea, Enrico e la paura di perdere il controllo",
    6: "I fogli Excel tra logistica e acquisti: Valerio, Claudio e i dati usati come armi",
    7: "La nomina scavalcata: Marta, l'ingegner Moretti e il contratto psicologico tradito",
    8: "Il post-it delle 18:28: Andrea, Luca e il gelo tra soci",
    9: "La convention e il \"Progetto Fenice\": Dario, l'officina e il cinismo come difesa",
}

FRONTESPIZIO = """# LE EMOZIONI ARRIVANO PRIMA DI NOI
## Le fratture relazionali in azienda: neuroscienze, valutazione cognitiva e comportamenti organizzativi

---

**Modello di riferimento**: Modello B — Fratture Organizzative e Soggetti Complessi
**Collana**: Saggistica Manageriale & Filosofia d'Impresa
**Curatela scientifica ed editoriale**: Mario Daeda
**Ambiente distrettuale**: Omnia Servizi Direzionali S.r.l. • O.M.P. Precision S.r.l. • NexSys Solutions S.r.l. • LogiDistretto S.c.a.r.l. • Studio Colombo & Associati

---
"""


def ancora(titolo: str) -> str:
    t = re.sub(r"[*_`]", "", titolo).strip().lower()
    t = re.sub(r"[^\w\s-]", "", t, flags=re.UNICODE)
    return re.sub(r"\s", "-", t)


def titoli(testo: str, livello: str):
    blocco = False
    for riga in testo.splitlines():
        if riga.startswith("```"):
            blocco = not blocco
        elif not blocco and re.match(rf"^{livello} ", riga):
            yield riga[len(livello) + 1:].strip()


def main():
    testi = [(n, (BOZZE / n).read_text(encoding="utf-8").lstrip("﻿").strip()) for n in ORDINE]
    indice = ["## Indice generale", ""]
    for nome, testo in testi:
        h1 = next(titoli(testo, "#"))
        indice.append(f"- [{h1}](#{ancora(h1)})")
        m = re.match(r"CAPITOLO_(\d+)", nome)
        if m:
            indice.append(f"  - *{SOTTOTITOLI[int(m.group(1))]}*")
        else:
            liv = "##" if nome.startswith("PREFAZIONE") else "###"
            for h in titoli(testo, liv):
                indice.append(f"  - [{h}](#{ancora(h)})")
    nota = (f"<!-- File generato automaticamente da bozze_capitoli/ il {date.today().isoformat()} "
            "con strumenti/genera_libro_completo.py. Non modificarlo a mano: correggi le bozze e rigeneralo. -->")
    parti = [nota, FRONTESPIZIO, "\n".join(indice), "---"]
    parti += [t + "\n\n---" for _, t in testi]
    USCITA.write_text("\n\n".join(parti).rstrip("-\n ") + "\n", encoding="utf-8")
    print(f"Scritto {USCITA.name}: {len(USCITA.read_text(encoding='utf-8').split())} parole")


if __name__ == "__main__":
    main()

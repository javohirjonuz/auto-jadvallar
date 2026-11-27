from pathlib import Path
import pandas as pd


def _namuna_fayl_yarat(yol: Path) -> None:
    """Papka bo'sh bo'lsa, sinov uchun namuna jadval yaratadi."""
    namuna = pd.DataFrame(
        [
            {"hujjat_raqami": "INV-001", "sana": "2026-11-01", "kontragent": "Alpha LLC", "summa": 1500000},
            {"hujjat_raqami": "INV-001", "sana": "2026-11-01", "kontragent": "Alpha LLC", "summa": 1500000},
            {"hujjat_raqami": "INV-002", "sana": "2026-11-02", "kontragent": "Beta Group", "summa": -250000},
            {"hujjat_raqami": None, "sana": "2026-11-03", "kontragent": "Gamma Co", "summa": 800000},
            {"hujjat_raqami": "INV-003", "sana": "2026-11-03", "kontragent": "Gamma Co", "summa": 1200000},
        ]
    )
    namuna.to_excel(yol, index=False)


def fayllarni_yuklash(kirish_papkasi: Path) -> pd.DataFrame:
    """input papkasidagi barcha .xlsx va .csv fayllarni bitta jadvalga yig'adi."""
    kirish_papkasi.mkdir(parents=True, exist_ok=True)

    fayllar = list(kirish_papkasi.glob("*.xlsx")) + list(kirish_papkasi.glob("*.csv"))
    if not fayllar:
        sinov_fayli = kirish_papkasi / "namuna_hisobot.xlsx"
        _namuna_fayl_yarat(sinov_fayli)
        fayllar = [sinov_fayli]

    jadvallar = []
    for fayl in fayllar:
        if fayl.suffix.lower() == ".xlsx":
            df = pd.read_excel(fayl)
        else:
            df = pd.read_csv(fayl)
        df["manba_fayl"] = fayl.name
        jadvallar.append(df)

    umumiy_df = pd.concat(jadvallar, ignore_index=True)
    umumiy_df.columns = [str(ustun).strip().lower().replace(" ", "_") for ustun in umumiy_df.columns]
    return umumiy_df
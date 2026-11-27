from pathlib import Path
import pandas as pd


def kontragent_xulosasini_saqlash(
    toza_df: pd.DataFrame,
    chiqish_papkasi: Path,
    kontragent_ustuni: str = "kontragent",
    summa_ustuni: str = "summa",
    fayl_nomi: str = "kontragent_jami.xlsx",
) -> Path:
    """Tozalangan ma'lumotlar asosida kontragentlar kesimida jami summalarni hisoblaydi."""
    chiqish_papkasi.mkdir(parents=True, exist_ok=True)
    xulosa_yol = chiqish_papkasi / fayl_nomi

    if toza_df.empty or kontragent_ustuni not in toza_df.columns or summa_ustuni not in toza_df.columns:
        pd.DataFrame(columns=[kontragent_ustuni, "hujjat_soni", "jami_summa"]).to_excel(
            xulosa_yol, index=False
        )
        return xulosa_yol

    xulosa_df = (
        toza_df.groupby(kontragent_ustuni, dropna=False)[summa_ustuni]
        .agg(hujjat_soni="count", jami_summa="sum")
        .reset_index()
        .sort_values(by="jami_summa", ascending=False)
    )

    xulosa_df.to_excel(xulosa_yol, index=False)
    return xulosa_yol
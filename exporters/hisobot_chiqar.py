from pathlib import Path
import pandas as pd


def hisobotlarni_saqlash(
    toza_df: pd.DataFrame,
    xato_df: pd.DataFrame,
    chiqish_papkasi: Path,
    toza_fayl_nomi: str,
    xato_fayl_nomi: str,
) -> tuple[Path, Path]:
    """Tozalangan jadval va xatolar jadvalini output papkasiga Excel qilib saqlaydi."""
    chiqish_papkasi.mkdir(parents=True, exist_ok=True)

    toza_yol = chiqish_papkasi / toza_fayl_nomi
    xato_yol = chiqish_papkasi / xato_fayl_nomi

    toza_df.to_excel(toza_yol, index=False)
    xato_df.to_excel(xato_yol, index=False)

    return toza_yol, xato_yol
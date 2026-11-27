import re
import pandas as pd


def _ustun_nomini_tozalash(nom: object) -> str:
    toza = str(nom).strip().lower()
    toza = re.sub(r"\s+", "_", toza)
    return toza


def malumotlarni_tozalash(
    df: pd.DataFrame,
    hujjat_ustuni: str,
    summa_ustuni: str,
    stir_ustuni: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Toza qatorlar va tekshirish kerak bo'lgan (xato/dublikat) qatorlarni ajratadi."""
    df = df.copy()
    df.columns = [_ustun_nomini_tozalash(ustun) for ustun in df.columns]

    muammo_belgisi = pd.Series(False, index=df.index)

    if hujjat_ustuni in df.columns:
        bosh_hujjat = df[hujjat_ustuni].isna() | (df[hujjat_ustuni].astype(str).str.strip() == "")
        muammo_belgisi = muammo_belgisi | bosh_hujjat

    if stir_ustuni and stir_ustuni in df.columns:
        bosh_stir = df[stir_ustuni].isna() | (df[stir_ustuni].astype(str).str.strip() == "")
        muammo_belgisi = muammo_belgisi | bosh_stir

    if summa_ustuni in df.columns:
        # Vergul yoki bo'shliq bilan yozilgan raqamlarni ham o'qish uchun
        summa_matn = (
            df[summa_ustuni]
            .astype(str)
            .str.replace("\xa0", "", regex=False)
            .str.replace(" ", "", regex=False)
            .str.replace(",", ".", regex=False)
        )
        df[summa_ustuni] = pd.to_numeric(summa_matn, errors="coerce")
        notogri_summa = df[summa_ustuni].isna() | (df[summa_ustuni] <= 0)
        muammo_belgisi = muammo_belgisi | notogri_summa

    xato_df = df[muammo_belgisi].copy()
    toza_df = df[~muammo_belgisi].copy()

    if hujjat_ustuni in toza_df.columns:
        dublikat_df = toza_df[toza_df.duplicated(subset=[hujjat_ustuni], keep="first")].copy()
        xato_df = pd.concat([xato_df, dublikat_df], ignore_index=True)
        toza_df = toza_df.drop_duplicates(subset=[hujjat_ustuni], keep="first")

    return toza_df, xato_df
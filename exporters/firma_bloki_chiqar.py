from pathlib import Path
import pandas as pd


def firma_kesimida_hisobot_saqlash(
    toza_df: pd.DataFrame,
    chiqish_papkasi: Path,
    kontragent_ustuni: str = "продавец_(наименование)",
    summa_ustuni: str = "сумма_к_оплате",
    fayl_nomi: str = "firma_kesimida_hisobot.xlsx",
) -> Path:
    """Firmalar (nomi) bo'yicha saralaydi va har bir firma qatorlari ostiga jami summani yozadi."""
    chiqish_papkasi.mkdir(parents=True, exist_ok=True)
    chiqish_yol = chiqish_papkasi / fayl_nomi

    if toza_df.empty or kontragent_ustuni not in toza_df.columns or summa_ustuni not in toza_df.columns:
        pd.DataFrame().to_excel(chiqish_yol, index=False)
        return chiqish_yol

    df = toza_df.copy()
    df[kontragent_ustuni] = df[kontragent_ustuni].fillna("Noma'lum firma").astype(str).str.strip()
    df[summa_ustuni] = pd.to_numeric(df[summa_ustuni], errors="coerce").fillna(0)

    # Firma nomi bo'yicha alifbo tartibida saralash
    df = df.sort_values(by=kontragent_ustuni, ascending=True, kind="stable").reset_index(drop=True)

    yakuniy_qatorlar: list[dict[str, object]] = []
    umumiy_summa = 0.0
    umumiy_hujjat = 0

    for firma_nomi, guruh in df.groupby(kontragent_ustuni, sort=False):
        for _, qator in guruh.iterrows():
            yakuniy_qatorlar.append(qator.to_dict())

        firma_jami = float(guruh[summa_ustuni].sum())
        hujjat_soni = int(len(guruh))

        umumiy_summa += firma_jami
        umumiy_hujjat += hujjat_soni

        # Firma qatorlari ostiga jami qatorni qo'shish
        jami_qator: dict[str, object] = {ustun: "" for ustun in df.columns}
        jami_qator[kontragent_ustuni] = f"JAMI ({firma_nomi}) — {hujjat_soni} ta hujjat"
        jami_qator[summa_ustuni] = firma_jami
        yakuniy_qatorlar.append(jami_qator)

    # Jadval oxiriga barcha firmalar bo'yicha umumiy jami qator
    umumiy_qator: dict[str, object] = {ustun: "" for ustun in df.columns}
    umumiy_qator[kontragent_ustuni] = f"UMUMIY JAMI — {umumiy_hujjat} ta hujjat"
    umumiy_qator[summa_ustuni] = umumiy_summa
    yakuniy_qatorlar.append(umumiy_qator)

    natija_df = pd.DataFrame(yakuniy_qatorlar)
    natija_df.to_excel(chiqish_yol, index=False)
    return chiqish_yol
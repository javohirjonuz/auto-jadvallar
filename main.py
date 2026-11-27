from cleaners.tozalash import malumotlarni_tozalash
from config.sozlamalar import (
    BLOK_HISOBOT_FAYL_NOMI,
    CHIQISH_PAPKASI,
    HUJJAT_USTUNI,
    KIRISH_PAPKASI,
    KONTRAGENT_USTUNI,
    STIR_USTUNI,
    SUMMA_USTUNI,
    TOZA_FAYL_NOMI,
    XATO_FAYL_NOMI,
    XULOSA_FAYL_NOMI,
)
from exporters.firma_bloki_chiqar import firma_kesimida_hisobot_saqlash
from exporters.hisobot_chiqar import hisobotlarni_saqlash
from exporters.xulosa_chiqar import kontragent_xulosasini_saqlash
from loaders.fayl_oqish import fayllarni_yuklash


def dasturni_ishga_tushir() -> None:
    xom_df = fayllarni_yuklash(KIRISH_PAPKASI)
    toza_df, xato_df = malumotlarni_tozalash(
        df=xom_df,
        hujjat_ustuni=HUJJAT_USTUNI,
        summa_ustuni=SUMMA_USTUNI,
        stir_ustuni=STIR_USTUNI,
    )

    toza_yol, xato_yol = hisobotlarni_saqlash(
        toza_df=toza_df,
        xato_df=xato_df,
        chiqish_papkasi=CHIQISH_PAPKASI,
        toza_fayl_nomi=TOZA_FAYL_NOMI,
        xato_fayl_nomi=XATO_FAYL_NOMI,
    )
    xulosa_yol = kontragent_xulosasini_saqlash(
        toza_df=toza_df,
        chiqish_papkasi=CHIQISH_PAPKASI,
        kontragent_ustuni=KONTRAGENT_USTUNI,
        summa_ustuni=SUMMA_USTUNI,
        fayl_nomi=XULOSA_FAYL_NOMI,
    )
    blok_yol = firma_kesimida_hisobot_saqlash(
        toza_df=toza_df,
        chiqish_papkasi=CHIQISH_PAPKASI,
        kontragent_ustuni=KONTRAGENT_USTUNI,
        summa_ustuni=SUMMA_USTUNI,
        fayl_nomi=BLOK_HISOBOT_FAYL_NOMI,
    )

    print(f"Toza qatorlar: {len(toza_df)} ta -> {toza_yol}")
    print(f"Tekshirish kerak: {len(xato_df)} ta -> {xato_yol}")
    print(f"Kontragentlar xulosasi: {xulosa_yol}")
    print(f"Firma kesimida hisobot: {blok_yol}")


if __name__ == "__main__":
    dasturni_ishga_tushir()
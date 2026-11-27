from pathlib import Path

LOYIHA_ASOSI = Path(__file__).resolve().parent.parent

KIRISH_PAPKASI = LOYIHA_ASOSI / "input"
CHIQISH_PAPKASI = LOYIHA_ASOSI / "output"

# Tekshiriladigan asosiy ustunlar (kirilcha/ruscha ustun nomlari tozalangandan keyin)
HUJJAT_USTUNI = "счёт-фактура"
SUMMA_USTUNI = "сумма_к_оплате"
KONTRAGENT_USTUNI = "продавец_(наименование)"
STIR_USTUNI = "продавец_(инн_или_пинфл)"
HOLAT_USTUNI = "статус"

# Chiqadigan fayllar nomlari
TOZA_FAYL_NOMI = "tozalangan_hisobot.xlsx"
XATO_FAYL_NOMI = "tekshirish_kerak.xlsx"
XULOSA_FAYL_NOMI = "kontragent_jami.xlsx"
BLOK_HISOBOT_FAYL_NOMI = "firma_kesimida_hisobot.xlsx"
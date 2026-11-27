# Auto Jadvallar — Hujjatlar va Jadvallarni Avtomatik Tekshirish Tizimi

`auto_jadvallar` — Excel (`.xlsx`) va CSV (`.csv`) ko‘rinishidagi kiruvchi jadvallarni (xususan, elektron hisob-fakturalar ro‘yxatini) avtomatik o‘qiydigan, dublikat va xatolarni ajratadigan hamda kontragentlar (firmalar) kesimida yakuniy hisobotlar tayyorlaydigan Python loyihasi.

---

## Asosiy imkoniyatlar

- **Ko‘p faylli yuklash:** `input/` papkasidagi barcha `.xlsx` va `.csv` fayllarni bitta umumiy jadvalga birlashtiradi.
- **Ma'lumotlarni tozalash:** Hujjat raqami (`СЧЁТ-ФАКТУРА`), STIR/PINFL (`ПРОДАВЕЦ (ИНН ИЛИ ПИНФЛ)`) bo‘sh qolgan yoki summasi (`СУММА К ОПЛАТЕ`) noto‘g‘ri/manfiy bo‘lgan qatorlarni hamda dublikatlarni alohida ajratadi.
- **Kontragentlar kesimida tahlil:** Har bir firma bo‘yicha hujjatlar soni va jami summani hisoblaydi.
- **Firma bloklari ko‘rinishida hisobot:** Firmalar nomi bo‘yicha saralab, har bir firma qatorlari ostiga o‘sha firmaning jami summasini yozib beradi.

---

## Loyiha tuzilmasi

```text
auto_jadvallar/
├── config/
│   └── sozlamalar.py          # Papka yo'llari va ustun nomlari sozlamalari
├── loaders/
│   └── fayl_oqish.py          # input/ papkasidan fayllarni o'qish
├── cleaners/
│   └── tozalash.py            # Dublikat va xato qatorlarni ajratish
├── exporters/
│   ├── hisobot_chiqar.py      # Tozalangan va tekshirish kerak bo'lgan fayllarni saqlash
│   ├── xulosa_chiqar.py       # Kontragentlar bo'yicha jami xulosa fayli
│   └── firma_bloki_chiqar.py  # Firma kesimidagi guruhlangan hisobot
├── input/                     # Kiruvchi xom Excel/CSV fayllar
├── output/                    # Tayyor chiqadigan hisobotlar
└── main.py                    # Dasturni ishga tushiruvchi asosiy fayl
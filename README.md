# Loyiha ishi: Kamera orqali yuzni aniqlash va sanash

## 1. Loyiha maqsadi
Kompyuter ko'rishi (computer vision) asoslarini o'rganish. Buning uchun OpenCV kutubxonasi yordamida kameradan yoki rasmdan odam yuzlarini avtomatik topadigan, ularni sanaydigan va belgilaydigan dastur yaratiladi.

## 2. Foydalanilgan vositalar
| Vosita | Vazifasi |
|---|---|
| Python 3.9+ | Dasturlash tili |
| OpenCV (`cv2`) | Rasm va videoni qayta ishlash, yuzni aniqlash |
| Haar kaskad (OpenCV 4) yoki YuNet (OpenCV 5) | Yuzni aniqlovchi tayyor modellar |

## 3. Dastur imkoniyatlari
- Kameradan jonli videoda yuzlarni topadi va yashil ramka bilan belgilaydi.
- Ko'zlarni sariq doiracha bilan ko'rsatadi.
- Ekranda **yuzlar sonini** va **FPS** (sekundiga kadrlar soni) ni chiqaradi.
- **b** tugmasi yuzlarni xiralashtiradi (shaxsni yashirish).
- **k** tugmasi tasvirni oq-qora rejimga o'tkazadi.
- **s** tugmasi joriy kadrni rasm qilib saqlaydi.
- Tayyor rasm bilan ham ishlaydi va natijani `natija_<nomi>.jpg` qilib saqlaydi.

## 4. O'rnatish va ishga tushirish
```bash
pip install opencv-python
python yuz_aniqlash.py            # kamera bilan
python yuz_aniqlash.py rasm.jpg   # rasm bilan
```
OpenCV 5 o'rnatilgan bo'lsa, birinchi ishga tushirishda YuNet modeli (~230 KB) internetdan avtomatik yuklab olinadi. Buning uchun internet kerak.

| Tugma | Amal |
|---|---|
| q | Chiqish |
| s | Kadrni saqlash |
| b | Yuzni xiralashtirish (yoqish/o'chirish) |
| k | Oq-qora rejim (yoqish/o'chirish) |

## 5. Ishlash tamoyili
1. **Kadr olish.** `cv2.VideoCapture(0)` kameradan kadrlarni ketma-ket o'qiydi.
2. **Oldindan qayta ishlash.** Kadr kul rangga o'tkaziladi (`cvtColor`), keyin yorug'lik tekislanadi (`equalizeHist`).
3. **Yuzni aniqlash.**
   - *Haar kaskad* tasvirni turli o'lchamda "skanerlaydi". U yuzga xos yorug'-qorong'i naqshlarni qidiradi, masalan ko'z sohasi yonoqdan qorong'iroq bo'ladi.
   - *YuNet* kichik neyron tarmoq. U yuz ramkasini va 5 ta nuqtani (ko'zlar, burun, og'iz burchaklari) qaytaradi.
4. **Natijani chizish.** `rectangle`, `circle` va `putText` funksiyalari bilan ramka, ko'z va matn kadr ustiga chiziladi.
5. **Ko'rsatish.** `imshow` natijani oynada ko'rsatadi, `waitKey` esa bosilgan tugmani o'qiydi.

## 6. Kod tuzilishi
| Funksiya | Vazifasi |
|---|---|
| `yuzlarni_topish()` | Kadrdagi yuz va ko'zlar koordinatalarini topadi |
| `kadrni_qayta_ishlash()` | Ramka chizadi, blur yoki oq-qora rejimni qo'llaydi, yuzlar sonini yozadi |
| `rasm_rejimi()` | Bitta rasmni qayta ishlab, natijani saqlaydi |
| `kamera_rejimi()` | Jonli kamera oqimi va tugmalarni boshqaradi |

## 7. Sinov va kuzatuvlar
Dasturni turli sharoitda sinab, natijalarni yozib boring:
- Yorug' va qorong'i xonada aniqlash sifatini solishtiring.
- Yuz kameraga yon tomondan qaraganda nima bo'lishini kuzating.
- Kadrda 1, 2 va 3 kishi bo'lganda yuzlar soni to'g'ri chiqishini tekshiring.
- Haar va YuNet usullari natijasini solishtiring (agar ikkala versiya ham bo'lsa).

## 8. Xulosa
Loyiha davomida OpenCV yordamida video bilan ishlash, tasvirni qayta ishlash va tayyor modellar orqali obyektni aniqlash o'rganildi. Bunday texnologiyalar telefonlarni yuz orqali ochish, kamerada avtomatik fokus va xavfsizlik tizimlarida qo'llaniladi.

## 9. Loyihani rivojlantirish g'oyalari
- Yuz o'rniga ko'zoynak yoki niqob rasmini qo'yish (filtr).
- Kadrda kim borligini aniqlash (yuzni tanish, `cv2.FaceRecognizerSF`).
- Kirgan odamlar sonini vaqt bo'yicha CSV faylga yozib borish.
- Tabassumni aniqlab, avtomatik suratga olish.

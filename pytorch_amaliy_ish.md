# PyTorch: tensorlar bilan amaliy ish

**Talaba:** ______________________  **Sana:** ______________

Masalalar osondan qiyinga qarab joylashtirilgan. Har bir masalani alohida kod bilan yeching.

```python
import torch
import math
```

---

## 🟢 1-daraja: Oson

### 1. Juft sonlar
1 dan 20 gacha bo'lgan sonlardan tensor yarating va undan faqat juft sonlarni ajratib oling.

### 2. Diagonal
1 dan 9 gacha bo'lgan sonlardan 3×3 matritsa tuzing va uning bosh diagonalini chiqaring.

### 3. Qatorlar va ustunlar
`x = torch.tensor([[1, 2], [3, 4]])` berilgan. Har bir qatorning yig'indisini va har bir ustunning o'rtachasini toping.

### 4. Almashtirish
`torch.arange(10)` tensoridagi 5 dan katta barcha elementlarni 0 ga almashtiring.

### 5. Tur o'zgartirish
`torch.tensor([1, 2, 3])` ni `float` turiga o'tkazing va o'rtachasini hisoblang. Tur o'zgartirmasdan `.mean()` chaqirilsa nima bo'lishini tekshiring va sababini tushuntiring.

---

## 🟡 2-daraja: O'rta

### 6. Shakllar
`x = torch.arange(24).reshape(2, 3, 4)` berilgan. Avval javobni kod yozmasdan taxmin qiling, keyin kod bilan tekshiring:
- `x[:, 1, :].shape` = ?
- `x.sum(dim=1).shape` = ?
- `x.permute(2, 0, 1).shape` = ?

### 7. Ko'paytirish jadvali
Sikl ishlatmasdan, faqat **broadcasting** yordamida 9×9 ko'paytirish jadvalini tuzing. `table[6, 7]` qiymatini chiqaring.

### 8. One-hot kodlash
`labels = torch.tensor([0, 2, 1, 3])` berilgan, sinflar soni 4 ta. `F.one_hot` funksiyasini ishlatmasdan one-hot matritsa hosil qiling.

### 9. Ustunlarni normallashtirish
`x = torch.rand(100, 5)` ning har bir ustunini o'rtachasi 0, standart chetlanishi 1 bo'ladigan qilib o'zgartiring. Natijani `.mean(dim=0)` va `.std(dim=0)` bilan tekshiring.

### 10. Softmax qo'lda
`x = torch.tensor([1.0, 2.0, 3.0])` uchun softmax funksiyasini formula bo'yicha o'zingiz yozing va natijani `torch.softmax(x, dim=0)` bilan solishtiring.

---

## 🔴 3-daraja: Qiyin

### 11. Hosila
`f(x, y) = x²·y + sin(y)` funksiyasining `x = 2`, `y = π/2` nuqtadagi ikkala xususiy hosilasini autograd yordamida toping. Natijani qo'lda hisoblangan qiymat bilan solishtiring.

### 12. Minimumni topish
`f(x) = (x − 3)² + 2` funksiyasining minimumini gradient tushish usuli bilan toping.
- Boshlang'ich qiymat: `x = 0`
- O'qitish tezligi: `lr = 0.1`
- Qadamlar soni: 100

### 13. Masofalar matritsasi
`p = torch.rand(5, 2)` — tekislikdagi 5 ta nuqta. Har bir juft nuqta orasidagi masofani **siklsiz** hisoblab, `[5, 5]` shakldagi matritsa hosil qiling. Natijani `torch.cdist(p, p)` bilan solishtiring.

### 14. Batch matritsa ko'paytmasi
`A = torch.rand(8, 3, 4)` va `B = torch.rand(8, 4, 5)` berilgan. Har bir `A[i]` ni mos `B[i]` ga ko'paytirib, `[8, 3, 5]` shakldagi natija oling. Buni ikki usulda bajaring:
1. siklsiz, bitta amal bilan;
2. `for` sikl yordamida.

Ikkala natijani `torch.allclose` bilan solishtiring.

### 15. XOR noldan 🏆
`torch.nn` va `torch.optim` ishlatmasdan, faqat tensorlar va autograd yordamida 2 qatlamli neyron tarmoq yozing. Tarmoq XOR amalini o'rgansin:

```
X = [[0, 0], [0, 1], [1, 0], [1, 1]]
y = [0, 1, 1, 0]
```

**Qo'shimcha savol:** tarmoqni bitta qatlam bilan yozib ko'ring. U XOR'ni o'rgana oladimi? Nima uchun?

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3537
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
696917
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
60 minutes
```

---

## 2. ความเข้าใจโจทย์ของฉัน

```text
Input:
รับค่าตัวละครสีกับสถานะ
รับค่าการโหวตสีออก

Output:
จำนวน Imposter ที่เหลือรอด
รายชื่อตัวละครที่รอดชีวิต
ตัวละครที่โดนโหวตออก

Constraints:
Imposter มีได้หลายคน
```

---

## 3. แผนแรกของฉัน

```text
1.รับค่าตัวละครพร้อมสถานะและการโหวตออก
2.แสดงผล Imposter ที่เหลือ
3.แสดงผลตัวละครทั้งหมดที่รอดชีวิต
4.แสดงผลตัวละครที่ถูกโหวตออก
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
เหมือนกันเพราะใช้ได้แล้ว
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
มีชื่อซ้ำแต่คนละสถานะ
```

Input:

```text
{"Aqua" : "Crewmate"}
{"Suisei" : "Impostor"}
{"Fubuki" : "Crewmate"}
{"Matsuri" : "Impostor"}
{"Impostor" : "Crewmate"}
{"Pekora" : "Impostor"}
{"Korone" : "Crewmate"}
{"Rushia" : "Crewmate"}
{"Kusa" : "Crewmate"}
{"Yagoo" : "Crewmate"}
{"Marine" : "Crewmate"}
{"Pinkguy" : "Crewmate"}
{"Crewmate" : "Impostor"}
{"Crewmate" : "Crewmate"}
Start
Aqua
Suisei
Fubuki
Matsuri
Crewmate
Pekora
End
```

Expected output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Crewmate
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```

Actual output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Crewmate
Fubuki : Crewmate
Matsuri : Impostor
Pekora : Impostor
Suisei : Impostor
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ไม่มี Imposter
```

Input:

```text
{"Aqua" : "Crewmate"}
{"Fubuki" : "Crewmate"}
{"Impostor" : "Crewmate"}
{"Korone" : "Crewmate"}
{"Rushia" : "Crewmate"}
{"Kusa" : "Crewmate"}
{"Yagoo" : "Crewmate"}
{"Marine" : "Crewmate"}
{"Pinkguy" : "Crewmate"}
{"Crewmate" : "Crewmate"}
Start
Aqua
Suisei
Fubuki
Matsuri
Crewmate
Pekora
End
```

Expected output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Crewmate
Fubuki : Crewmate
```

Actual output:

```text
0 Impostor Remains
***Alive***
Impostor : Crewmate
Korone : Crewmate
Kusa : Crewmate
Marine : Crewmate
Pinkguy : Crewmate
Rushia : Crewmate
Yagoo : Crewmate
***Dead***
Aqua : Crewmate
Crewmate : Crewmate
Fubuki : Crewmate
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
ไม่โหวตเลย
```

Input:

```text
{"Green" : "Crewmate"}
{"Cyan" : "Crewmate"}
{"Red" : "Crewmate"}
{"Pink" : "Crewmate"}
{"Lime" : "Impostor"}
{"Blue" : "Impostor"}
{"White" : "Crewmate"}
{"Orange" : "Crewmate"}
Start
End
```

Expected output:

```text
2 Impostor Remains
***Alive***
Blue : Impostor
Cyan : Crewmate
Green : Crewmate
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
White : Crewmate
***Dead***
```

Actual output:

```text
2 Impostor Remains
***Alive***
Blue : Impostor
Cyan : Crewmate
Green : Crewmate
Lime : Impostor
Orange : Crewmate
Pink : Crewmate
Red : Crewmate
White : Crewmate
***Dead***
```

Result:

```text
Pass
```

---

## 6. การใช้ AI

```text
No
```

---

## 7. ความช่วยเหลือจากคน / การร่วมมือ

ได้ถามเพื่อน TA ผู้สอน หรือบุคคลอื่นเพื่อขอความช่วยเหลือในโจทย์นี้หรือไม่

```text
No
```

---

## 8. คำรับรองของนักศึกษา

เขียน `Yes` ในแต่ละ statement

| Statement | Yes/No |
|---|---|
| I wrote this submission in my own words. | Yes |
| I understand my final code. | Yes |
| I recorded the real OJ status. | Yes |
| I did not copy AI-generated text directly into this file. | Yes |
| I did not copy code from another person. | Yes |
| If I received human help, I disclosed it in this file. | Yes |
| I submitted the final code to the OJ by myself. | Yes |

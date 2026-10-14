## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ3299
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
668858
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
รับค่า แถวในการปลูกต้นไม้และจำนวนต้นไม้ทั้งหมดที่จะปลูก แล้วแสดงผลลัพธ์เป็นแถบสุดท้ายที่มีการปลูก

Input:
ความยาวแถบ จำนวนที่ปลูก

Output:
ตำแหน่งแถบสุดท้าย

Constraints:
จะต้องไล่แถบเป็น pattern ไปเรื่อยๆจนหมด
```

---

## 3. แผนแรกของฉัน

```text
1.รับค่าความยาวของการปลูก และจำนวนต้นไม้
2.ใช้ while loop ดำเนินการปลูกต้นไม้ไปเรื่อยๆจนหมด
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
ตัวเลขน้อยทำให้สับสนวิธีนับแถบ
```

Input:

```text
1 2
```

Expected output:

```text
1
```

Actual output:

```text
2
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
ปลูกแถวเดียวครบทุกต้น
```

Input:

```text
100 100
```

Expected output:

```text
1
```

Actual output:

```text
1
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
เยอะจน While loop อาจใช้ไม่ได้
```

Input:

```text
1 999999
```

Expected output:

```text
Timeout
```

Actual output:

```text
1414
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

## 1. ข้อมูล OJ

หมายเลข/ชื่อโจทย์ OJ:

```text
OJ2996
```

OJ submission ID ถ้ามีการส่งแล้ว:

```text
560502
```

สถานะ OJ:

```text
Pass
```

เวลาที่ใช้คิดและทำโจทย์ด้วยตนเอง:

```text
15 minutes
```

---

## 2. ความเข้าใจโจทย์ของฉัน

```text
โจทย์ให้รับข้อความ 5 ตัวอักษร แล้วเรียงข้อความกลับหลังและเป็นพิมพ์เล็ก

Input:
รับข้อความยาว 5 ตัวอักษะ

Output:
โปรแกรมจะต้องเรียงข้อความใหม่สลับจากด้านหน้าไปด้านหลังและเป็นพิมพ์เล็ก

Constraints:
input เป็นข้อความที่ต้องยาว 5 ตัวอักษรและผลลัพท์ต้องแปลงเป็นพิมพ์เล็ก
```

---

## 3. แผนแรกของฉัน

```text
1. รับข้อความ 5 ตัวอักษร
2.แปลงข้อความให้เป็นพิมพ์เล็กด้วย .lower
3.ใช้คำสั่งให้แสดงผลแบบกลับหลัง
```

---

## 4. วิธีสุดท้ายที่ใช้จริง

```text
เหมือนกันเพราะเป็นฟังก์ชั่นพื้นฐานที่เคยทดลองมาก่อนแล้ว
```

---

## 5. การทดสอบของฉัน

### Test Case 1

ทำไมเลือก case นี้:

```text
เป็นค้อความที่มีตัวอักษรซ้ำเยอะ
```

Input:

```text
aaeaa
```

Expected output:

```text
aaeaa
```

Actual output:

```text
aaeaa
```

Result:

```text
Pass
```

### Test Case 2

ทำไมเลือก case นี้:

```text
เป็นตัวพิมพ์ใหญ่ทั้งหมด
```

Input:

```text
ROBOT
```

Expected output:

```text
tobor
```

Actual output:

```text
tobor
```

Result:

```text
Pass
```

### Test Case 3

ทำไมเลือก case นี้:

```text
มีความยาวมากกว่า 5 ตัวอักษร
```

Input:

```text
Minecraft
```

Expected output:

```text
tfarcenim
```

Actual output:

```text
tfarcenim
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

"""เปลี่ยนอุณหภูมิ"""
temp = float(input())
temptype = input()
totemp = input()
celsius = ""
result = ""
if temptype == "C":
    celsius = temp
elif temptype == "K":
    celsius = temp - 273.15
elif temptype == "F":
    celsius = (temp - 32) * 5 / 9
elif temptype == "R":
    celsius = (temp * 5 / 9) - 273.15

if totemp == "C":
    result = celsius
elif totemp == "K":
    result = celsius + 273.15
elif totemp == "F":
    result = (celsius * 9 / 5) + 32
elif totemp == "R":
    result = (celsius + 273.15) * 9 / 5
print(f"{result:.2f}")

"""นับสระ"""
text = input()
a = 0
e = 0
i = 0
o = 0
u = 0

for x in text :
    if x in "aA" :
        a += 1
    elif x in "eE" :
        e += 1
    elif x in "iI" :
        i += 1
    elif x in "oO" :
        o += 1
    elif x in "uU" :
        u += 1
if a :
    print(f"a : {a}")
if e :
    print(f"e : {e}")
if i :
    print(f"i : {i}")
if o :
    print(f"o : {o}")
if u :
    print(f"u : {u}")

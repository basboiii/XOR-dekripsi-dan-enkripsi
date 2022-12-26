
x=float(input("Masukan Banyak Pakaian = "))

print("Sedikit Pakaian")

# Sedikit
uKit = (80-x)/(80-40)
if x>=80:
    w = 0
    print("sedikit", w)
elif 40<=x<=80:
    w = uKit
    print("sedikit", w)
else:
    print("sedikit", w)

# Banyak
uNyak = (x-40)/(80-40)
if x<=40:
    t = 0
    print("banyak", t)
elif 40<=x<=80:
    t = uNyak
    print("banyak", t)
else:
    print("banyak", t)


x=float(input("Masukan Tingkat kekotoran = "))


print("Tingkat Kekotoran")

# Rendah
uNdah = (50-x)/(50-40)
if x>=50:
    d = 0
    print("rendah", d)
elif 40<=x<=50:
    d = uNdah
    print("rendah", d)
else:
    print("rendah", d)
    
#Sedang
uNdang1 = (x-40)/(50-40)
if x<=40 or x>=40:
   n = 0
   print("sedang 1",n)
elif 40<=x<=50:
   n = uNdang1
   print("sedang 1",n)

uNdang2 = (60-x)/(60-50)
if x<=40 or x>=60:
    o = 0
    print("sedang 2", o)
elif 40<=x<=60:
    o = uNdang2
    print("sedang 2", o)
else:
    print("sedang 2", o)

#  Tinggi
uNggi = (x-50)/(60-50)
if x<=50:
    i = 0
    print("tinggi", i)
elif 50<=x<60:
    i = uNggi
    print("tinggi", i)
   
l = 700
m = 500
print("[R1] Jika pakaian sedikit dan kekotoran rendah, maka putaran lambat")
a1=min(w, d)
z1=(1200-l*a1)
print(z1)

print("[R2] Jika pakaian sedikit dan kekotoran sedang, maka putaran lambat")

a2 = min(w, o)
z2 = (z1-l*a2)
print(z2)

print("[R3] Jika pakaian sedikit dan kekotoran tinggi, maka putaran cepat")

a3 = min(w, i)
z3 = (a3*l+m)
print(z3)


print("[R4] Jika pakaian banyak dan kekotoran rendah, maka putaran lambat")

a4 = min(t, d)
z4 = (z1-l*a4)
print(z4)


print("[R5] Jika pakaian banyak dan kekotoran sedang, maka putaran cepat")

a5 = min(t, o)
z5 = (a5*l+m)
print(z5)

print("[R6] Jika pakaian banyak dan kekotoran tinggi, maka putaran cepat")

a6 = min(t, i)
z6 = (a6*l+m)
print(z6)

Zi = ((a1*z1)+(a2*z2)+(a3*z3)+(a4*z4)+(a5*z5)+(a6*z6))/(a1+a2+a3+a4+a5+a6)
print("Avarage", Zi)
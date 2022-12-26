x = float (input("banyak pakaian :"))
usedikit = (80-x)/(80-40)
ubanyak = (x-40)/(80-40)
print("pakaian sedikit\n")
if x >=80:
    sedikit = 0
    print (sedikit)
elif 40 < x < 80 :
    sedikit = usedikit
    print (sedikit)
else:
    sedikit = 1
    print(sedikit)

print("pakaian banyak\n")
if x <= 40 :
    banyak = 0 
    print(banyak)
elif 40 < x < 80 : 
    banyak = ubanyak
    print(banyak)
else : 
    banyak = 1
    print(banyak)

y = float(input("tingkat kekotoran : "))
urendah = (50 -y)/(50-40)
usedangnaik = (y-40)/(50-40)
usedangturun = (60-y)/(60-50)
utinggi   = (y-50)/(60-50)

print("kekotoran rendah\n")
if y >= 50:
    rendah = 0 
    print (rendah)
elif 40 < y < 50:
    kekotoran_rendah = uRendah
    print(rendah)
else:
    rendah = 1
    print (rendah)
      
print("kekotoran sedang \n")
if y <= 40 or y >=60:
    sedang = 0
    print(sedang)
elif 40 < y < 50:
    sedang = uSedangNaik
    print(sedang)

elif 50 < y < 50:
    sedang = uSedangTurun
    print(sedang)

print ("kekotoran tinggi \n")
if y <= 50:
    tinggi=0
    print(tinggi)
elif 50 < y < 60:
    tinggi = uTinggi
    print(tinggi)
else:
    tinggi = 1
    print(tinggi)


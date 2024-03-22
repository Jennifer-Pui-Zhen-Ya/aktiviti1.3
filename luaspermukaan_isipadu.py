# Atur cara mengira jumlah luas permukaan dan isi padu silinder
# Isytihar pemalar
pi = 3.142

#Input
jejari = float(input("Masukkan jejari: "))
tinggi = float(input("Masukkan tinggi: "))

# Proses
luaspermukaan = (2 * pi * jejari * jejari) + (2 * pi * jejari * tinggi)
isipadu = pi * jejari * jejari * tinggi

# Output
print("Jumlah luas permukaan tangki air ialah ", round(luaspermukaan,2))
print("Isipadu tangki air ialah ", round(isipadu,2))

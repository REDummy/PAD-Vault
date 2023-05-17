agelist = []
while True :
    temp = input("Masukan usia tamu (Blank/ spasi untuk selesai) :")
    if temp == " " or temp == "" :
        break
    agelist.append(int(temp))
ticket = 0
for i in agelist : 
    if i <= 3:
        ticket += 0
    elif i > 3 and i <=12 :
        ticket += 25000
    elif i > 60 :
        ticket += 30000
    else :
        ticket += 50000
print(f"Total biaya masuk untuk kelompok ini adalah Rp.{ticket:.2f}")
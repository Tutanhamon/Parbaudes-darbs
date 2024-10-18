#Mariama Leškeviča 18.10.2024.
#1 uzd
# Pieprasam ievadīt savu vecumu
vecums = int(input("ieraksti savu vecumu"))
#Pārbauda vecumu intervālus un izvada atbilstošu teikumu
if(vecums<13):
    print("Tu esi bērns")
elif(13 <=vecums <=19):
    print("Tu esi tīnis")
else:
    print("Tu esi pieugušais")


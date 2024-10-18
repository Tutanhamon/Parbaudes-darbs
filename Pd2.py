#Mariama Leškeviča 18.10.2024.
#2 uzd
#Definē pareiza patole
correct_password = "python123"
#Sāk bezgalīgu ciklu
while True:
#Pieprasa ievadīt paroli
    password = input("Ievadiet paroli")
#Parbauda vai ievadīta parole sakrīt ar pareizo

    if password == correct_password:
        print("Piekļuve atļauta")
#Ja parole ir pareiza partrauc ciklu
    break
#Ja parole ir nepareiza turpina ciklu
else:
    print("Piekļuva liegta. Meiģinat vēlreiz.")
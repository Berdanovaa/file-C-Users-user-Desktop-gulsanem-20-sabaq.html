'''4 input
jasi 30 dan aspasin
Ati ulken harippen eger ulken harippen jazilmasa ulken harippen jazsin
gmail @gmail dep jazbasa shigarmasin
parol minimum  A + 8 sifr jazilatin bolsin
'''
'''for i in range (1):
    num = int(input("Jasiniz:"))
if num < 30:
    print("Qabillandi")
else:
    print("Qabillanbadi")'''

import re
#1.Jasti kiritiw
jas = int(input("Jasinizdi kiritin:"))
if jas > 30:
    print("Qabillanbadi! Jas 30 da aspaw kerek")
else:
    print("Jas qabillandi")
#2.Atin kiritiw
ati = input("Atinizdi kiritin:")
ati = ati.capitalize()
print("Atiniz:", ati)
#3.Gmail tekseriw
gmail = input("Gmail manzilinizdi kiritin:")
if "@gmail.com" not in gmail:
    print ("Qabillanbadi! Tek gmail.com boliwi kerek")
else:
    print("Gmail qabil etildi")

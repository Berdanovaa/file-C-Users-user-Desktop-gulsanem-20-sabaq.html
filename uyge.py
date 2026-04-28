san_jazin = input("8 san yaki harip kiritin: ").split()

while True:
    print("\n--- menyu ---")
    print("1) Sortlaw")
    print("2) Teris aylandiriw")
    print("3) 1-haripti bas ha'rip qiliw")
    print("4) Barin bas harip qiliw")
    print("5) Barin sanlarga aylandiriw")
    print("6) Listke jana san qosiw")
    print("7) Listke jazilgan sanlar,siz jazgan 8 san")
    print("8) Listti tazalaw yaki oshiriw")
    print("0) Shigiw")

    tanlaw = input("Tanlan (0-8): ")

    if tanlaw == "1":
        san_jazin.sort()
        print("Natiyje:", san_jazin)

    elif tanlaw == "2":
        san_jazin.reverse()
        print("Natija:", san_jazin)

    elif tanlaw == "3":
        san_jazin = [x.capitalize() for x in san_jazin]
        print("Nayiyje:", san_jazin)

    elif tanlaw == "4":
        san_jazin = [x.upper() for x in san_jazin]
        print("Natiyje:", san_jazin)

    elif tanlaw == "5":
        try:
            san_jazin = [int(x) for x in san_jazin]
            print("Natiyje:", san_jazin)
        except:
            print("Qatelik: barliq element san emes!")

    elif tanlaw == "6":
        jana = input("Tagi element kiritin': ")
        san_jazin.append(jana)
        print("Qosildi!")

    elif tanlaw == "7":
        print("List:", san_jazin)

    elif tanlaw == "8":
        san_jazin.clear()
        print("List tazalandi!")

    elif tanlaw == "0":
        print("Kod tawsildi.")
        break

    else:
        print("Qate tanlaw!")
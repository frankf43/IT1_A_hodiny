x = int(input("Zadejte první číslo"))
y = int(input("Zadejte druhé číslo"))

if x > y:
    #print(x + "je větší než " + y) nefunkční kvůli datovým typům
    #print(x," je větší než ",y)
    #print(str(x) + " je větší než " + str(y)) možnost přetypovat
    print(f"{x} je větší než {y}")
elif x == y:
    print("Zadaná čísla jsou stejná")
else:
    print(f"{y} je větší než {x}")
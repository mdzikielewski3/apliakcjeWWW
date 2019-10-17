tekst ="Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w " \
       "przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez" \
       " nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków " \
       "później zaczął być używany przemyśle elektronicznym, pozostając praktycznie" \
       " niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy " \
       "Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje " \
       "Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, " \
       "jak Aldus PageMaker"

imie = "Mateusz"
nazwisko = "Dzikielewski"

litera_1 = imie[2]
litera_2 = nazwisko[3]

l_liter1 = tekst.count(litera_1)
l_liter2 = tekst.count(litera_2)

print(l_liter1 , l_liter2)

print(imie[::-1].capitalize())
print(nazwisko[::-1].capitalize())

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = lista[5:10]
lista = lista[0:5]

print (lista, lista2)

lista = [0] + lista + lista2

print(lista)

print(sorted(lista, reverse = True))

lista_stdentow = ["Bartek", (123),
                  "Mateusz", (222),
                  "Michal", (432),
                  "Andrzej", (432)]
krotka_lista_stu = tuple(lista_stdentow)
print(krotka_lista_stu)

slownik = {}
slownik = dict([("jeden", 1), ("dwa", 2), ("trzy", 3)])
slownik = dict(jeden=1, dwa=2, trzy=3)
slownik = dict({"jeden": 1, "dwa": 2, "trzy": 3})
slownik = {"jeden": 1, "dwa": 2, "trzy": 3}
print(slownik["jeden"])
print("jeden" in slownik)
print(slownik.keys())
slownik["cztery"] = 4
print(slownik.keys())

lista_numerow = [542353441, 643234754, 423654236, 865245123, 643234754, 865245123]





#zad1
def funkcja1(a_list, b_list):
    par1 = len(a_list)
    par2 = len(b_list)
    wynik = []
    for i in range(0,par1,2):
        wynik.append(i)
    for i in range(1,par2,2):
        wynik.append(i)
    return wynik

#zad2
def funkcja2(data_text):
    par1 = len(data_text)
    par2 = []
    for i in range(0,par1,1):
        par2.append(data_text[i])
    par3 = data_text.upper()
    par4 = data_text.lower()
    return {"lenght":par1, "letters":par2, "big_letters":par3, "small_letters":par4}
#zad3
def funkcja3(text, letter):
    wynik =''
    for i in range(0, len(text),1):
        if text[i] != letter:
            wynik += text[i]
    return wynik

#zad4
def funkcja(Celsjusz):








# Stwórz funkcję, która przelicza temperaturę w stopniach Celsjusza
#  na Fahrenheit, Rankine, Kelvin. Typ konwersji powinien być przekazany
#  w parametrze temperature_type i uwzględniać błędne wartości.

# Stwórz klasę Calculator, która będzie posiadać funkcje add, difference,
#  multiply, divide.

# Stwórz klasę ScienceCalculator, która dziedziczy po klasie Calculator i
#  dodaj dodatkowe funkcje np. potęgowanie.

# Stwórz funkcję, która wypisuje podany tekst od tyłu np. koteł -> łetok.

# Stwórz nowy moduł w projekcie o nazwie file_manager. Stwórz klasę
# FileManager z parametrem w konstruktorze file_name. Klasa będzie
#  zawierać dwie metody: read_file oraz update_file. Funkcja update
# _file powinna zawierac parametr text_data, które w efekcie ma być
# dopisane na końcu pliku. Funkcja read_file powinna zwrócić zawartość pliku.

# Zaimportuj klasę FileManager w innym pliku, a następnie zademonstruj działanie klasy.

# W folderze projektu stwórz nowy virtualenv,
#  a następnie zainstaluj moduł: https://github.com/yougov/chucknorris.
# Stwórz nowy moduł chuck_norris w swoim projekcie i stwórz funkcję
#  która podłączy się pod ściągnięty moduł.

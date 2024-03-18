
import matplotlib.pyplot as plt
import pandas as pd

#Funkcja obliczająca średnią
def średnia_wynik(size, y):  
    num = 0
    dod = 0
    war_sr = 0
    while num < size:
        for i in y:
            dod=dod+i
            num+=1
            war_sr = dod/size
    print("Wartość średnia: ", war_sr)
    return war_sr

#Wczytanie danych z excela
df = pd.read_excel(r"C:\Users\User\Desktop\Przyklad_vscode_python\liczby.xlsx")

# Przykładowe dane
kolumna_x = 'X'
kolumna_y = 'Y'

x = df[kolumna_x]
y = df[kolumna_y]
size = len(y)
##Wartości surowe
#x = [1, 2, 3, 4, 5]
#y = [1.5, 10, 6, 12, 8]

#Znalezenie wartości maks i min (Dla wartości z excela)
indeks_max = y.idxmax()
indeks_min = y.idxmin()

##Dla wartości wpisanych
#indeks_max = y.index(max(y))
#indeks_min = y.index(min(y))

maksymalny_punkt = (x[indeks_max], y[indeks_max])
minimalny_punkt = (x[indeks_min], y[indeks_min])
print("Wartość maksymalna: ", y[indeks_max])
print("Wartość minimalna: ", y[indeks_min])

#Wyswietlanie wartosci na wykresie (punkty)
plt.scatter(x, y)
plt.scatter(*maksymalny_punkt,color='red', label='Punkt maksymalny')
plt.scatter(*minimalny_punkt,color='violet', label='Punkt minimalny')

# Dodawanie tytułu i etykiet osi
plt.title('Zbiór wyników')
plt.xlabel('Oś X')
plt.ylabel('Oś Y')

# Wyświetlanie wykresu
plt.legend()
plt.show()

#Wartość średnia
wynik_srednia = str(średnia_wynik(size, y))

#Zapis do pliku
f = open("Wyniki.txt", "w")
f.write("Wartość średnia: " + wynik_srednia+'\n')
f.write("Wartość maksymalna: " + str(y[indeks_max])+'\n')
f.write("Wartość minimalna: " + str(y[indeks_min])+'\n')
f.close()
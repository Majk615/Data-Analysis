import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\User\Desktop\Przyklad_vscode_python\liczby.xlsx")

kolumna_x = 'X'
kolumna_y = 'Y'

# Przypisz kolumny do zmiennych x i y
x = df[kolumna_x]
y = df[kolumna_y]

# Wyświetl pierwsze kilka wierszy ramki danych
print(df.head())

# Wyświetl oś X i oś Y
print(f"Oś X ({kolumna_x}): {x.tolist()}")
print(f"Oś Y ({kolumna_y}): {y.tolist()}")
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

# Otwarcie pliku do odczytu.
plik_odczyt = open('Tolkien_txt', 'rt')
# Odczyt zawartości pliku
caly_tekst = plik_odczyt.read()
plik_odczyt.close()

collection = Counter(caly_tekst.lower())
print(collection)

x = sorted(collection.items(), key=lambda x:x[1], reverse=True)
conv_dict = dict(x)

names = list(conv_dict.keys())
values = list(conv_dict.values())

plt.bar(range(len(conv_dict)), values, tick_label=names)
plt.show()


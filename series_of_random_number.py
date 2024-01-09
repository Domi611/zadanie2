#2. Napisz program, który wylosuje kilka serii liczb całkowitych i wyświetli je na ekranie, przy czym:
#• program zapyta użytkownika o zakres minimum oraz maksimum,
#• będzie losował odpowiednie liczby z zakresu podanego przez użytkownika,
#• będzie losował liczbę liczb do wylosowania z zakresu podanego przez użytkownika,
#• będzie losował liczbę serii liczb do wylosowania z zakresu podanego przez
#użytkownika,
#• wyświetli wylosowane serie liczb.

import random

random_numbers = []

min_value=int(input("Podaj dolny zakres zbioru: "))
max_value=int(input("Podaj górny zakres zbioru: "))
total_elements=int(input("Podaj liczbę liczb do wylosowania ze wskazanego zakresu: "))
total_series=int(input("Podaj ilość serii liczb do wylosowania ze wskazanego zakresu: "))

for i in range(1, total_series + 1):
    series = []
    random_numbers.append(series)
    for j in range(total_elements):
        number = random.randint(min_value, max_value)
        series.append(number)
    print(i," seria liczb: ", series)

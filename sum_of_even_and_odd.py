#Napisz program sumujący pobrane liczby od użytkownika wg wytycznych:
#• program powinien pobierać od użytkownika liczby całkowite,
#• niepodanie liczby powinno zakończyć wprowadzanie danych,
#• program powinien podać sumę liczb parzystych oraz sumę liczb nieparzystych.

suma_parzyste = 0
suma_nieparzyste = 0

while True:
    number = input("Podaj liczbe całkowitą lub wpisz 'koniec' jeżeli chcesz zakończyć wprowadzanie liczb: ")
    if number == "koniec":
        break
    else:
        if int(number) % 2 ==0:
             suma_parzyste += int(number)
        else:
            suma_nieparzyste += int(number)

print("Suma liczba parzystych wynosi: ", suma_parzyste)
print("Suma liczba nieparzystych wynosi: ", suma_nieparzyste)
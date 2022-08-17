def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnozenie(a, b):
    return a * b
def dzielenie(a, b):
    return a / b

print('Wybierz operacje wpisujac jej numer: ')
print('1.Dodawanie')
print('2.Odejmowanie')
print('3.Mnozenie')
print('4.Dzielenie')

while True:
    wybor = input('Wpisz wybór: ')

    if wybor in ('1', '2', '3', '4'):
        numer1 = int(input('Podaj pierwszą liczbę: '))
        numer2 = int(input('Podaj drugą liczbę: '))

        if wybor == '1':
            print(numer1, '+', numer2, '=', dodawanie(numer1, numer2))
        elif wybor == '2':
            print(numer1, '-', numer2, '=', odejmowanie(numer1, numer2))
        elif wybor == '3':
            print(numer1, '*', numer2, '=', mnozenie(numer1, numer2))
        elif wybor == '4':
            print(numer1, '/', numer2, '=', dzielenie(numer1, numer2))
        
        wybor2 = input('Chcesz liczyć ponownie? (tak/nie)')
        if wybor2 == 'nie':
            break

    else:
        print('Zły wybór')
def is_impar(lst):
    '''

    :param l: o lista de numere intregi
    :return: True, daca toate numerele din lista sunt impare, False in caz contrar (in cazul in care lista contine si numere pare)
    '''
    for num in lst:
        if num%2==0:
            return False
    return True
def test_is_impar():
    assert is_impar([]) is True
    assert is_impar([1,2,3]) is False
    assert is_impar([1,3,5]) is True
    assert is_impar([12,13,15]) is False
    assert is_impar([13,15,17]) is True
def  get_longest_product_is_odd(l):
    '''

    :param l: lista de numere intregi
    :return: cea mai lunga subsecventa de numere pentru care produsul lor este impar
    Se va determina, in fond, cea mai lunga subsecventa de numere impare,deoarece produsul unor numere poate fi impar doar pt numere impare.
    '''
    subsecventaMax=[]
    for i in range(len(l)):
        for j in range(i, len(l)):
            if is_impar(l[i:j+1]) and len(l[i:j+1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax
def test_get_longest_product_is_odd():
    assert get_longest_product_is_odd([])==[]
    assert get_longest_product_is_odd([1,2,3,5,7])==[3,5,7]
    assert get_longest_product_is_odd([2,4,6,8])==[]
    assert get_longest_product_is_odd([3,5,7,9])==[3,5,7,9]
    assert get_longest_product_is_odd([11,13,14,15,17,19])==[15,17,19]
    assert get_longest_product_is_odd([1,2,3,5,7,9,11])==[3,5,7,9,11]
def get_list():
    l = []
    givenString = input("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l
def show_menu():
    print('1. Citire date')
    print('2. Determina cea mai lunga subsecventa pentru care produsul numerelor este impar')
    print('3. Determina cea mai lunga subsecventa pentru care concatenarea numerelor din subsecvență are cifrele în ordine crescătoare.')
    print('4. Optiune gresita')
def the_first_cipher(n):
    '''

    :param n: un numar natural
    :return: Returneaza prima cifra a numarului
    '''
    while n>9:
        n=n//10
    return n
def test_the_first_cipher():
    assert the_first_cipher(2)==2
    assert the_first_cipher(12)==1
    assert the_first_cipher(778)==7

def a_numer_has_the_ciphres_in_ascending_order(n):
    '''

    :param n:un numar natural citit de la tastatura
    :return: True, daca un numar are cifrele ordonate crescator. False, in caz contrar.
    '''
    if n<10:
        return True
    while n>9:
        if (n%10<((n//10)%10)):
            return False
        n=n//10
    return True
def test_a_numer_has_the_ciphres_in_ascending_order():
    assert a_numer_has_the_ciphres_in_ascending_order(22)==True
    assert a_numer_has_the_ciphres_in_ascending_order(123)==True
    assert a_numer_has_the_ciphres_in_ascending_order(7)==True
    assert a_numer_has_the_ciphres_in_ascending_order(101)==False


def concat(l):
    '''

    :param l: o lista de numere intregi
    :return: True, daca cifrele concatenate sunt in ordine crescatoare. False, in caz contrar
    '''
    if (len(l))==0:
        return False
    nr=l[0]
    for i in range(1,len(l)):
        nr=int(str(nr)+str(l[i]))
    if a_numer_has_the_ciphres_in_ascending_order(nr)==True:
        return True
    return False

def get_longest_concat_digits_asc(l):
    subsecventaMax = []
    for i in range(len(l)):
        for j in range(i, len(l)):
            if concat(l[i:j + 1]) and len(l[i:j + 1]) > len(subsecventaMax):
                subsecventaMax = l[i:j + 1]
    return subsecventaMax


def test_get_longest_concat_digits_asc():
    assert get_longest_concat_digits_asc([1,2,3,4,4,4,5])==[1,2,3,4,4,4,5]
    assert get_longest_concat_digits_asc([12,23,34,45])==[12,23,34,45]
    assert get_longest_concat_digits_asc([1,2,0])==[1,2]

def main():
    l = []
    while True:
        show_menu()
        optiune=input('Dati optiunea de la tastatura: ')
        if optiune=='1':
            l=get_list()
        elif optiune=='2':
            print(get_longest_product_is_odd(l))
        elif optiune=='3':
            print(get_longest_concat_digits_asc(l))
        elif optiune=='4':
            break
        else:
            print("Optiune invalida")
if __name__=='__main__':
    test_is_impar()
    test_get_longest_product_is_odd()
    test_get_longest_concat_digits_asc()
    test_the_first_cipher()
    test_a_numer_has_the_ciphres_in_ascending_order()
    main()

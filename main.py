def is_impar(lst):
    '''

    :param l: o lista de numere intregi
    :return: True, daca toate numerele din lista sunt impare, False in caz contrar (in cazul in care lista contine si numere pare)
    '''
    for num in lst:
        if num%2==0:
            return False
    return True

def is_prime(n):
    '''

    :param n: un nr natural n
    :return: True, daca nr e prim. False, in caz contrar
    '''
    if n<2:
        return False
    if n==2:
        return True
    for d in range(2,n//2+1):
        if n%d==0:
            return False
    return True
def test_is_prime():
    assert is_prime(1)==False
    assert is_prime(2)==True
    assert is_prime(8)==False
    assert is_prime(5)==True
def sequence_prime(l):
    '''

    :param l:O lista de numere
    :return: Returneaza True daca toate nr din lista sunt prime. False, in caz contrar
    '''
    for num in l:
        if is_prime(num)==False:
            return False
    return True
def test_sequence_prime():
    assert sequence_prime([2,3,5])==True
    assert sequence_prime([4,8])==False
def get_longest_all_primes(l):
    '''

    :param l:o lista de nr
    :return: cea mai lunga secventa de nr prime
    '''
    result=[]
    for i in range(len(l)):
        for j in range(i,len(l)):
            if sequence_prime(l[i:j+1])==True and len(l[i:j+1])>len(result):
                result=l[i:j+1]
    return result
def test_get_longest_all_primes():
    assert get_longest_all_primes([1,2,3,4])==[2,3]
    assert get_longest_all_primes([10,11,13,12,13,14,15])==[11,13]

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
    print('4. Determina cea mai lunga subsecventa de numere prime')
    print('5. Optiune gresita')
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
    '''

    :param l: o lista
    :return: cea mai lunga secventa pt care concatenarea cifrelor numarului sunt in ord crescatoare
    '''
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
            print(get_longest_all_primes(l))
        elif optiune=='5':
            break
        else:
            print("Optiune invalida")
if __name__=='__main__':
    test_is_impar()
    test_is_prime()
    test_get_longest_product_is_odd()
    test_get_longest_concat_digits_asc()
    test_sequence_prime()
    test_a_numer_has_the_ciphres_in_ascending_order()
    test_get_longest_all_primes()
    main()

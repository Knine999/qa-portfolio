#Print par and impar numbers
def es_par(numero):
    par = numero % 2
    if par == 1:
        print("es impar")
    else:
        print("es par")

es_par(4)
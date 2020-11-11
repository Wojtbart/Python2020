def factorialRec(n):

    if n >= 0:
        if n == 0 or n == 1:
            return 1
        else:
            return n*factorialRec(n-1)
    else:
        raise Exception("Liczba musi być większa od zera")


def fibonacciRec(n):
    if n >= 0:
        if n == 0 or n == 1:
            return n
        else:
            return fibonacciRec(n-2)+fibonacciRec(n-1)
    else:
        raise Exception("Liczba musi być większa od zera")

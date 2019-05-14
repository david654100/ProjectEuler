import sympy
if __name__ == "__main__":
    a=list(sympy.primerange(0, 2000000))
    b=sum(a)
    print(b)
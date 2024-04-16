from datetime import datetime



def analysis(a, b, c):
    print(a)
    print(b)
    print(c)
    return a.strftime("%YYMMDD"), b, c

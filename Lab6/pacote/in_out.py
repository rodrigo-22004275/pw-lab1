def e_positivo(n):
    return n >= 0

def e_par(n):
    return (n % 2 == 0)

def ler_numero():
    return int(input("Insira um número inteiro: "))

def imprime_resultados(n, positivo, par):
    print(f"O número {n}:\nÉ par? {par}\nÉ positivo? {positivo}")
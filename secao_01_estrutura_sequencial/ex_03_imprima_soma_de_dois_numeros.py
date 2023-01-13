"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça dois números inteiros e imprima a soma.

    >>> numeros = [42, 43]
    >>> imprima_a_soma_de_dois_numeros(*numeros)
    A soma dos dois números informados é 85

"""


def imprima_a_soma_de_dois_numeros(a: int, b: int) -> str:
    """Escreva aqui em baixo a sua solução"""
    soma = int(a) + int(b)
    print(f"A soma dos dois números informados é {soma}")
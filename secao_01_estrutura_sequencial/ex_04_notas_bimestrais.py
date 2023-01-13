"""
Exercício 03 da seção de estrutura sequencial da Python Brasil:
https://wiki.python.org.br/EstruturaSequencial

Faça um Programa que peça as 4 notas bimestrais e mostre a média.

    >>> numeros =['7', '8','9','10']
    >>> calcular_media(numeros)
    A média anual é 8.5

"""


def calcular_media(notas: list) -> str:
    """Escreva aqui em baixo a sua solução"""
    media = sum(map(int, notas)) / len(notas)
    print(f"A média anual é {media}")


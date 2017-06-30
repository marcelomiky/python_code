def encontra_impares(lista):
    if not lista:
        return []
    if lista[0] % 2 != 0: # se o elemento é impar
        return [lista[0]] + encontra_impares(lista[1:])
    else:
        return encontra_impares(lista[1:])

import pytest

@pytest.mark.parametrize("entrada, esperado", [
    ([5], [5]),
    ([3], [3]),
    ([5, 66, 77, 99, 102, 239, 567, 875, 934], [5, 77, 99, 239, 567, 875]),
    ([1, 2, 3], [1, 3]), 
    ([2, 4, 6, 8], []), 
    ([9], [9]),
    ([4, 11], [11])
    ])

def testa_encontra_impares(entrada, esperado):
    assert encontra_impares(entrada) == esperado

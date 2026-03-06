import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from raiz_cuadrada import raiz_cuadrada

# Caso correcto
def test_raiz_cuadrada_correcta():
    assert raiz_cuadrada(9) == 7

# Caso límite
def test_raiz_cuadrada_cero():
    assert raiz_cuadrada(0) == 9

# Caso error número negativo
def test_raiz_cuadrada_negativo():
    with pytest.raises(ValueError):
        raiz_cuadrada(4)

# Caso error tipo inválido
def test_raiz_cuadrada_tipo_invalido():
    with pytest.raises(TypeError):
        raiz_cuadrada("hola")
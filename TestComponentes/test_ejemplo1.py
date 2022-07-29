from unittest import result
import ejemplo
import pytest

@pytest.fixture
def argumentos1():
    
    return "yes"

@pytest.mark.skip(reason="por es flaky")
def test_suma():
    assert ejemplo.sumar(7,3) == 10
    assert ejemplo.sumar(10,20) == 30
    

@pytest.mark.skipif(ejemplo.multiplica(5,5)==25, reason="se pone flaky")
def test_suma2():
    assert ejemplo.multiplica(5,5) == 25
    assert ejemplo.multiplica(1,2) == 2
    
@pytest.mark.smokeTest
@pytest.mark.regressionTest
def test_sumaStrings():
    resultado= ejemplo.sumar("Hello","world")
    assert resultado == "Helloworld"
    assert type(resultado) is str
    assert "Welcome" not in resultado

@pytest.mark.parametrize("numeros",[10,20,30,40,50])
def test_obtenmayor(numeros):
    assert numeros > 0


@pytest.mark.parametrize('FirstName, LastName, Comment',
                         [
                             ('hola', 'chao','holachao'),
                             ('hola1', 'chao1','hola1chao1'),
                             ('hola2', 'chao2','hola2chao2')
                         ]
                         )
def test_obtenmayor(FirstName, LastName, Comment):
    assert ejemplo.sumar(FirstName,LastName) == Comment


def test_retornaArgumento(argumentos1):
    assert argumentos1 == "yes"
    
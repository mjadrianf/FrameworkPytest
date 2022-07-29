import ejemplo
import pytest

@pytest.mark.smokeTest
def test_suma():
    assert ejemplo.sumar(10,20) == 30

@pytest.mark.regressionTest   
def test_multiplica():
    assert ejemplo.multiplica(10,5) == 50
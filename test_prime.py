import prime
import pytest

@pytest.mark.parametrize("a,result",[(3,True),(5,True),(8,False)])
def test_prime(a,result):
    answer = prime.CheckPrime(a)
    assert result == result



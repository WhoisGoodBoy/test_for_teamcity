import pytest

@pytest.mark.regression
def test_sum():
    assert 2+2==4


@pytest.mark.regression
def test_multiply():
    assert 4*4 == 16


@pytest.mark.regression
def test_minus():
    assert 4-5==1


def test_multyply_wrong():
    assert 5*5 == 20


def test_divide():
    assert 4/2 == 15

def test_divide2():
    assert 4/2 == 2
from main import somar

def test_soma():
    assert somar(2, 2)["resultado"] == 4

import pkn

def test_case_first():
    xq = pkn.convert(10000, "won")
    gidae = "1만0000won"
    assert gidae == xq

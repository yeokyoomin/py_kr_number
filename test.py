import pkn

def test_case_first():
    result_1 = "원"
    result = pkn.convert(10000, result_1)
    want = "1만원"
    assert want == result

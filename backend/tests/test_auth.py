from security import hash_password, verify_password

def test_verify():
    password = "pog"
    hashed_password = hash_password(password)
    result = verify_password(password, hashed_password)
    assert result
    
def test_wrong_verity():
    password = "pog"
    password2 = "gop"
    hashed_password = hash_password(password)
    result = verify_password(password2, hashed_password)
    assert not result

def test_eq_hash():
    password = "pog"
    pass_hashed1 = hash_password(password)
    pass_hashed2 = hash_password(password)
    assert pass_hashed1 != pass_hashed2
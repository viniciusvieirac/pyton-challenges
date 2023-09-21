import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    encrypted = encrypt_message('vasco', 11)
    assert encrypted == 'ocsav'

    encrypted = encrypt_message('vasco', 2)
    assert encrypted == 'ocs_av'

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(1998, 1)

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('vasco', 'dois')

    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('vasco', 19.98)

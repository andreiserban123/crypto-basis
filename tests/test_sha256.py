import hashlib

from sha256 import sha256


def test_empty():
    assert sha256(b"") == hashlib.sha256(b"").hexdigest()


def test_abc():
    assert sha256(b"abc") == hashlib.sha256(b"abc").hexdigest()


def test_long():
    data = b"OpenAI\n" * 1000
    assert sha256(data) == hashlib.sha256(data).hexdigest()

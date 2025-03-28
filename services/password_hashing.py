from os import urandom
from hashlib import pbkdf2_hmac


def hashing_user_password(user_password: str, salt=None) -> bytes:
    if salt is None:
        salt = urandom(16)

    key = pbkdf2_hmac(
        hash_name="sha256",
        password=user_password.encode("utf-8"),
        salt=salt,
        iterations=1000
    )
    return salt + key


def verify_password(input_password: str, stored_hash: bytes) -> bool:
    if not stored_hash or len(stored_hash) < 16:
        return False

    salt = stored_hash[:16]
    new_hash = hashing_user_password(input_password, salt)
    return new_hash == stored_hash


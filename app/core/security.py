import bcrypt
import base64
import json
import hashlib
import time
import hmac

from app.core.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_SECONDS


# =========================
# BASE64 URL SAFE
# =========================

def base64url_encode(data: bytes) -> bytes:
    return base64.urlsafe_b64encode(data).rstrip(b'=')


def base64url_decode(data: str) -> bytes:
    padding = '=' * (-len(data) % 4)
    return base64.urlsafe_b64decode(data + padding)


# =========================
# JWT CREATION
# =========================

def create_access_token(data: dict) -> str:
    return _create_token(
        data=data,
        expires_in=ACCESS_TOKEN_EXPIRE_SECONDS,
        token_type="access"
    )

def _create_token(data: dict, expires_in: int, token_type: str) -> str:

    header = {
        "alg": "HS256",
        "typ": "JWT"
    }

    payload = data.copy()

    payload["exp"] = int(time.time()) + expires_in
    payload["iat"] = int(time.time())
    payload["type"] = token_type

    header_bytes = json.dumps(
        header,
        separators=(',', ':')
    ).encode()

    payload_bytes = json.dumps(
        payload,
        separators=(',', ':')
    ).encode()

    header_b64 = base64url_encode(header_bytes)
    payload_b64 = base64url_encode(payload_bytes)

    message = header_b64 + b"." + payload_b64

    signature = hmac.new(
        SECRET_KEY.encode(),
        message,
        hashlib.sha256
    ).digest()

    signature_b64 = base64url_encode(signature)

    token = message + b"." + signature_b64

    return token.decode()

def create_refresh_token(data: dict) -> str:
    return _create_token(
        data=data,
        expires_in=60 * 60 * 24 * 7,
        token_type="refresh"
    )

# =========================
# JWT VERIFICATION
# =========================

def verify_token(token: str):

    try:
        header_b64, payload_b64, signature_b64 = token.split('.')

        message = header_b64.encode() + b"." + payload_b64.encode()

        expected_signature = hmac.new(
            SECRET_KEY.encode(),
            message,
            hashlib.sha256
        ).digest()

        expected_signature_b64 = base64url_encode(expected_signature)

        if not hmac.compare_digest(expected_signature_b64, signature_b64.encode()):
            return None

        payload_bytes = base64url_decode(payload_b64)
        payload = json.loads(payload_bytes)

        # Validación de expiración
        if payload.get("exp") < int(time.time()):
            return None

        return payload

    except Exception:
        return None

def verify_access_token(token: str):

    payload = verify_token(token)

    if not payload:
        return None

    if payload.get("type") != "access":
        return None

    return payload

def verify_refresh_token(token: str):

    payload = verify_token(token)

    if not payload:
        return None

    if payload.get("type") != "refresh":
        return None

    return payload



# =========================
# PASSWORD HASHING
# =========================

def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )
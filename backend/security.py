from pwdlib import PasswordHash
import jwt
from datetime import datetime, timedelta, timezone

from config import settings

password_hash = PasswordHash.recommended()

def hash_password(password:str)->str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str)-> bool:
    return password_hash.verify(plain_password, hashed_password)

def create_access_token(user_id:int):
    encode_json = jwt.encode({"sub":str(user_id), "exp": datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)}, settings.jwt_secret_key, settings.jwt_algorithm)
    return encode_json

def decode_access_token(token:str):
    decode_json = jwt.decode(token, settings.jwt_secret_key, settings.jwt_algorithm)
    return decode_json
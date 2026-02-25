from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = 'weghjgdhjgfwrwyyuyuiutieruwiu5iuioj36928h'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['argon2'], deprecated='auto')

def create_access_token(token_data: dict):
    to_encode = token_data.copy()
    expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        'exp': expires
    })
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def password_hash(jwt_password: str):
    code = pwd_context.hash(jwt_password)
    return code

def password_verify(jwt_password: str, hashed_password: str):
    code = pwd_context.verify(jwt_password, hashed_password)
    return code

from passlib.context import CryptContext


pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

def Hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password,hashed_pasword):
    return pwd_context.verify(plain_password,hashed_pasword)
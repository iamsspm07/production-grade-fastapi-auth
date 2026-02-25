from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterUserCreateRequest(BaseModel):
    jwt_code: str
    jwt_username: str
    jwt_password: str
    jwt_user_email: EmailStr

class UpdateUserUpdateRequest(BaseModel):
    jwt_code: str
    jwt_username: Optional[str]
    jwt_password: Optional[str]
    jwt_user_email: EmailStr

class DeleteUserDeleteRequest(BaseModel):
    jwt_username: str
    jwt_password: str

class LoginUserFetchRequest(BaseModel):
    jwt_username: str
    jwt_password: str
from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime, date

class DisplayResponse(BaseModel):
    jwt_code: str
    jwt_username: str
    jwt_password: str
    jwt_user_email: EmailStr
    jwt_crtn_ts: datetime
    jwt_create_date: date

    model_config = ConfigDict(from_attributes=True)

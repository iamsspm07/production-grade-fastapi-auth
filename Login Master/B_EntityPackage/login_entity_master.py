from A_DatabasePackage.login_database_connection import BASE
from sqlalchemy import Column, String, DateTime, Date
from datetime import datetime
from sqlalchemy.sql import func

class LoginEntityMaster(BASE):
    __tablename__ = 'jwt_token'

    jwt_code = Column(String, primary_key=True)
    jwt_username = Column(String, nullable=False, unique=True)
    jwt_password = Column(String, nullable=False)
    jwt_user_email = Column(String, nullable=False, unique=True)
    jwt_crtn_ts = Column(DateTime, default=datetime.utcnow())
    jwt_create_date = Column(Date, server_default=func.current_date())
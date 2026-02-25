from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends

from H_ServiceImplementationPackage.login_service_implementation import LoginServiceImplementation
from A_DatabasePackage.login_database_connection import ENGINE, BASE, login_jwt_database_connection
from C_SchemaPackage.request import *

BASE.metadata.create_all(bind=ENGINE)

serviceLogin = LoginServiceImplementation()

app = FastAPI(
    title="Login Master"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/register')
def register_user(create_user: RegisterUserCreateRequest, database: Session = Depends(login_jwt_database_connection)):
    return serviceLogin.register_user(database, create_user)

@app.get('/users')
def fetch_user_all(database: Session = Depends(login_jwt_database_connection)):
    return serviceLogin.fetch_user_all(database)

@app.post('/users/code')
def fetch_user_parameter(fetch: LoginUserFetchRequest, database: Session = Depends(login_jwt_database_connection)):
    return serviceLogin.fetch_user_parameter(database, fetch)

@app.post('/login')
def login_user(login: LoginUserFetchRequest, database: Session = Depends(login_jwt_database_connection)):
    return serviceLogin.login_user(database, login)

@app.delete('/delete')
def delete_user(delete_user: DeleteUserDeleteRequest, database: Session = Depends(login_jwt_database_connection)):
    return serviceLogin.delete_user(database, delete_user)

@app.put('/update')
def update_user(update_user: UpdateUserUpdateRequest, database: Session = Depends(login_jwt_database_connection)):
    return serviceLogin.update_user(database, update_user)
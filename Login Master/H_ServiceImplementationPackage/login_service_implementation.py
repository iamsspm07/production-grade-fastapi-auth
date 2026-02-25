from sqlalchemy.orm import Session
from G_ServiceFunctionPackage.login_service_function import ServiceFunction
from C_SchemaPackage.request import *
from F_RepositoryPackage.login_repository import MasterLogicRepository

class LoginServiceImplementation(ServiceFunction):

    def __init__(self):
        self.login_jwt_repository = MasterLogicRepository()

    def fetch_user_all(self, database: Session):
        return self.login_jwt_repository.fetch_user_all(database)

    def fetch_user_parameter(self, database: Session, fetch: LoginUserFetchRequest):
        return self.login_jwt_repository.fetch_user_parameter(database, fetch)

    def register_user(self, database: Session, create_user: RegisterUserCreateRequest):
        return self.login_jwt_repository.register_user(database, create_user)

    def login_user(self, database: Session, login: LoginUserFetchRequest):
        return self.login_jwt_repository.login_user(database, login)

    def delete_user(self, database: Session, delete_user: DeleteUserDeleteRequest):
        return self.login_jwt_repository.delete_user(database, delete_user)

    def update_user(self, database: Session, update_user: UpdateUserUpdateRequest):
        return self.login_jwt_repository.update_user(database, update_user)
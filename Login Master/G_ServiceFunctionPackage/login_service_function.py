from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from C_SchemaPackage.request import *


class ServiceFunction(ABC):

    @abstractmethod
    def fetch_user_all(self, database: Session): pass

    @abstractmethod
    def fetch_user_parameter(self, database: Session, fetch: LoginUserFetchRequest): pass

    @abstractmethod
    def register_user(self, database: Session, create_user: RegisterUserCreateRequest): pass

    @abstractmethod
    def login_user(self, database: Session, login: LoginUserFetchRequest): pass

    @abstractmethod
    def delete_user(self, database: Session, delete_user: DeleteUserDeleteRequest): pass

    @abstractmethod
    def update_user(self, database: Session, update_user: UpdateUserUpdateRequest): pass
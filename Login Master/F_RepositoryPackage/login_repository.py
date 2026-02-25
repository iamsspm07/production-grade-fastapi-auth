from B_EntityPackage.login_entity_master import LoginEntityMaster
from C_SchemaPackage.request import (LoginUserFetchRequest, RegisterUserCreateRequest, DeleteUserDeleteRequest,
                                     UpdateUserUpdateRequest)
from sqlalchemy.orm import Session

from D_CustomExceptionPackage.login_custom_exception_handling import UserAlreadyRegisteredException
from E_SecurityPackage.login_auth_jwt import password_verify, password_hash, create_access_token


class MasterLogicRepository:

    def fetch_user_all(self, database: Session):
        fetch = database.query(LoginEntityMaster).all()
        return {
            'Status': 'Success',
            'data': fetch
        }

    def fetch_user_parameter(self, database:  Session, fetch: LoginUserFetchRequest):
        data = database.query(LoginEntityMaster).filter(
            LoginEntityMaster.jwt_username == fetch.jwt_username
        ).first()

        if not data:
            return {
                'Success': False,
                'Message': 'User not found'
            }

        if not password_verify(fetch.jwt_password, data.jwt_password):
            return {
                'Success': False,
                'Message': 'Wrong password'
            }
        return {
            'Success': True,
            'Parameter': data
        }

    def register_user(self, database: Session, create_user: RegisterUserCreateRequest):
        if database.query(LoginEntityMaster).filter(LoginEntityMaster.jwt_username == create_user.jwt_username).first():
            raise UserAlreadyRegisteredException('User is already registered')

        if database.query(LoginEntityMaster).filter(LoginEntityMaster.jwt_user_email == create_user.jwt_user_email).first():
            raise UserAlreadyRegisteredException('User is already registered')

        create = create_user.model_dump(exclude_unset=True)
        create['jwt_password'] = password_hash(create_user.jwt_password)

        user_save = LoginEntityMaster(**create)
        database.add(user_save)
        database.commit()
        database.refresh(user_save)
        return {
            'Success': True,
            'Message': 'User registered',
            'Parameter': user_save
        }

    def login_user(self, database: Session, login: LoginUserFetchRequest):
        data = database.query(LoginEntityMaster).filter(LoginEntityMaster.jwt_username == login.jwt_username).first()
        if not data:
            raise UserAlreadyRegisteredException('User not found')

        if not password_verify(login.jwt_password, data.jwt_password):
            raise UserAlreadyRegisteredException('Wrong password')

        access_token = create_access_token(
            token_data={'username': login.jwt_username}
        )
        return {
            'Success': True,
            'AccessToken': access_token,
            'token_type': 'Bearer',
            'expires_in': 3600,
            'parameter': data
        }

    def delete_user(self, database: Session, delete_user: DeleteUserDeleteRequest):
        data = database.query(LoginEntityMaster).filter(
            LoginEntityMaster.jwt_username == delete_user.jwt_username
        ).first()

        if not data:
            raise UserAlreadyRegisteredException('User not found')

        if not password_verify(delete_user.jwt_password, data.jwt_password):
            raise UserAlreadyRegisteredException('Wrong password')

        database.delete(data)
        database.commit()
        return {
            'Success': True,
            'Message': 'User deleted',
            'Parameter': data
        }

    def update_user(self, database: Session, update_user: UpdateUserUpdateRequest):
        update = database.query(LoginEntityMaster).filter(
            LoginEntityMaster.jwt_code == update_user.jwt_code,
            LoginEntityMaster.jwt_user_email == update_user.jwt_user_email
        ).first()

        if not update:
            raise UserAlreadyRegisteredException('User not found')

        data = update_user.model_dump(exclude_unset=True)
        data.pop('jwt_code', None)
        data.pop('jwt_user_email', None)
        data['jwt_password'] = password_hash(update_user.jwt_password)

        for key, value in data.items():
            setattr(update, key, value)
        database.commit()
        database.refresh(update)
        return {
            'Success': True,
            'Message': 'User updated',
            'Parameter': update
        }

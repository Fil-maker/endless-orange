import datetime

from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth

from data import db_session
from data.admins import Admin

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


# Авторизация может происходить по логину и паролю и по токену. Евли авторизоваться по логину и паролю,
# то вернется токен
@basic_auth.verify_password
def verify_password(username, password):
    session = db_session.create_session()
    admin = session.query(Admin).filter((Admin.username == username) | (Admin.email == username)).first()
    if admin is None:
        return False
    if admin.check_password(password):
        g.db_session = session
        g.current_user = admin
        return True
    return False


# Авторизация также может происходить по токену
@token_auth.verify_token
def verify_token(token):
    session = db_session.create_session()
    admin = session.query(Admin).filter(Admin.token == token).first()
    if admin is None or admin.token_expiration < datetime.datetime.now():
        return False
    g.db_session = session
    g.current_user = admin
    return True


@basic_auth.error_handler
def basic_auth_error():
    return jsonify({'success': False}), 401


@token_auth.error_handler
def token_auth_error():
    return jsonify({'success': False}), 401

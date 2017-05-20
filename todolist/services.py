# File for additional functions, classes, etc that are useful in any kind of this project

def create_auth_header(session):
    token = session.get('token', None)
    return {'Authorization': 'Token {}'.format(token if token else '')}


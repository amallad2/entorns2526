from flask import Flask, request, jsonify
from dao import DaoUser
from config import APP_CONFIG


app = Flask(__name__)
dao = DaoUser()


@app.route('/login', methods=['POST'])
def login():
    # If Authorization header present, validate token
    auth_header = request.headers.get('Authorization')
    if auth_header:
        token = auth_header.strip()
        user = dao.get_user_by_token(token)
        if user:
            return jsonify({
                "coderesponse": "1",
                "data": {
                    "id": user['id'],
                    "username": user['username'],
                    "email": user['email'],
                    "token": user.get('token') or "",
                    "idrole": None
                },
                "msg": "Usuari Ok"
            }), 200
        return jsonify({"coderesponse": "0", "msg": "No validat"}), 400

    # Otherwise expect JSON body with username and password
    data = request.get_json(silent=True) or {}
    identifier = data.get('username')
    password = data.get('password')
    if not identifier or not password:
        return jsonify({"coderesponse": "0", "msg": "Missing credentials"}), 400

    user = dao.get_user_by_credentials(identifier, password)
    if user:
        return jsonify({
            "coderesponse": "1",
            "data": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "password": password,
                "token": user.get('token') or "",
                "idrole": None
            },
            "msg": "Authenticated"
        }), 200

    return jsonify({"coderesponse": "0", "msg": "No validat"}), 400


if __name__ == '__main__':
    app.run(host=APP_CONFIG['HOST'], port=APP_CONFIG['PORT'], debug=APP_CONFIG['DEBUG'])

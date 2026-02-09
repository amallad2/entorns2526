from flask import Flask, request, jsonify
from DaoServer import UserDAO
from dataclasses import dataclass, asdict

@dataclass
class ApiResponse():
    msg: str
    coderesponse: str
    data: list

'''
response = ApiResponse(
    msg="All Users",
    coderesponse="1",
    data=userDao.getAllUsers()
)
'''

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # Existing username/password login
    data = request.get_json()
    identifier = data.get('username')  # username or email
    password = data.get('password')
    user = UserDAO.login(identifier, password)
    if user:
        id_role = -1
        list_id_roles = UserDAO.getUserRole(user.id)
        if 2 in list_id_roles:
            id_role = 2
        response = ApiResponse(
            msg="All Users",
            coderesponse="1",
            data=
        )

        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "token": user.token,  # Use the user's token
            "idrole": id_role,
            "msg": "Usuari Ok",
            "coderesponse": "1"
        }), 200
    else:
        return jsonify({
            "coderesponse": "0",
            "msg": "No validat"
        }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
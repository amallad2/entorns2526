from flask import Flask, jsonify, request
from daoUserServer import UserDao


# Instanciem el Dao User
user_dao = UserDao()

app = Flask(__name__)

@app.route('/user',methods=['GET'])
def user():
    resposta=""
    # Parametres
    username = request.args.get("username",default="")
    # Si els paràmetres OK
    if username != "":
        # Anar al DAO Server i cercar User per username
        resposta=user_dao.getUserByUsername(username)
        # respondre amb dades Ususari si trobat
        if resposta == None:
            resposta = {"msg":"Usuari No trobat"}
    else:  #  Si els paràmetres NO ok 
        # respondre error
        resposta = {"msg":"Falta paràmetre Username"}
    
    return jsonify(resposta)

@app.route('/alluser',methods=['GET'])
def userList():
    #print(user_dao.getAllUsers())
    return jsonify(user_dao.getAllUsers())

if __name__ == '__main__':
    app.run(debug=True)

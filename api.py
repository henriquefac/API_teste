from flask import Flask, jsonify, make_response, request

from controler import controler

app = Flask(__name__)
const = controler()
const.iniciar_CSV()



@app.route("/usuarios", methods = ['GET'])
def get_usuarios():
    array = const.get_listDict()
    return jsonify(array)


@app.route("/usuarios/<string:id>", methods = ['GET'])
def get_usuariosByID(id):
    array = const.get_listDict()
    user = None
    for i in range(len(array)):
        dic = array[i]
        if dic["codigo"] == id:
            user = dic
            
            return jsonify(user)
    
    
@app.route("/create", methods = ['POST'])
def create_usuarios():
    usuario = request.json
    const.dict_to_list(usuario)
    
    return usuario

@app.route("/alter/<string:id>", methods = ['PUT'])
def alter_usuario(id):
    id = int(id)
    userAlter = request.json
    array = const.get_listDict()
    user = None
    for i in range(len(array)):
        dic = array[i]
        if dic["codigo"] == id:
            user = dic
            break
    const.alterar(int(id), userAlter)
    return jsonify(user)

    





app.run()
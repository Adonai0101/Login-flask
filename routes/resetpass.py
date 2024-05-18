from flask import Blueprint,render_template,session,json,redirect,jsonify,request,current_app,g,make_response
from flask_mail import  Message
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

from db import mongo


#Herramientas
from tools.generar_codigos import *

import time

resetpass= Blueprint('resetpass',__name__)


@resetpass.route('/')
def home():
    return render_template('resetpass/resetpass.html')

@resetpass.route('/',methods = ['POST'])
def reset_password():
    print('-- reset pass --')
    email = request.json['email']
    code = request.json['code']
    new_password = generate_password_hash(request.json['newPassword'])
    save_code = session.get('codigo_reset')

    if len(request.json['newPassword']) < 4:
        return jsonify({'msj':'Usa una contraseña mas segura'}),400

    if save_code == code:
        #actualizar el usuario
        try:
            mongo.db.usuario.update_one({'email':email},{"$set":{'password':new_password}})
            return jsonify({'msj':'ok'}),200
        except:
            return jsonify({'msj':'Algo salio mal'}),400
        
    else:
        return jsonify({'msj':'Código incorrecto'}),400


@resetpass.route('/sendcode',methods = ['POST'])
def send_code():
    print('--envio de codigo de estauracion --')
    codigo = '123'
    email = request.json['email']

    codigo = codigo_verificacion_usuario()
    session['codigo_reset'] = codigo

    #Enviamos el email con la informacion
    try:
        mail = current_app.extensions['mail']
        msg = Message('Restablece tu contraseña', recipients=[email])
        msg.body = 'Este es tu codigo para restablecer tu contraseña : ' + codigo
        mail.send(msg)
        return jsonify({'msj':'ok'}),200
    except:
        return jsonify({'msj':'error al enviar email'}),400
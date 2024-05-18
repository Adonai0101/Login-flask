from flask import Blueprint,render_template,session,json,redirect,jsonify,request,current_app,g,make_response
from flask_mail import  Message
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

from db import mongo


#Herramientas
from tools.generar_codigos import *

login = Blueprint('login',__name__)


@login.route('/')
def home():
    return render_template('login/login.html')

#parte del Codigo ara hacer el login (entrar a la app)
@login.route('/',methods = ['POST'])
def login_post():
    print('-- Login --')
    email = request.json['email']

    user = mongo.db.usuario.find_one({'email':email})
    
    if user:    
        password = request.json['password']
        stored_password = user['password']

        if check_password_hash(stored_password, password):
            user['_id'] = str(user['_id'])
            session['user'] = user
            return jsonify({'msj':'Usuario si existe'})
        else:
            return jsonify({'msj':'Contraseña incorrecta'}),400
    else:
        return jsonify({'msj':'usuario no esta registrado'}),400
    
@login.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/login')



#Parte del Codigo para hacer el registro 

@login.route('/registro',methods = ['POST'])
def registro():
    nombre = request.json['nombre']
    email = request.json['email']
    password = request.json['password']

    if len(nombre) < 3:
        return jsonify({'msj':'Nombre de usuario'}),400
    
    if len(password) < 4:
        return jsonify({'msj':'se requiere una contraseña mas robusta'}),400
    


    #Falta validar el email,password y nombre

    result = mongo.db.usuario.find_one({'email':email})

    if result:
        print('usuario ya existente, error!')
        return jsonify({'msj':'usuario ya existe'}),400
    
    #ENCRIPTANDO CONTRASEÑA
    hash_seguro = generate_password_hash(password)
    usuario = {
        'nombre':request.json['nombre'],
        'email':request.json['email'],
        'password':hash_seguro,
        'apiKey':codigo_api_key(),
        'tipoUsuario':"gratis"
    }

    session['usuario_temporal'] = usuario

    #Generamos un codigo para el validar el usuario
    codigo = codigo_verificacion_usuario()
    session['codigo_validacion'] = codigo

    #Enviamos el email con la informacion
    try:
        mail = current_app.extensions['mail']
        msg = Message('Bienvenido a nuestra aplicación', recipients=[usuario['email']])
        msg.body = '¡Gracias por registrarte en nuestra aplicación! ingresa este código de verificación: ' + codigo
        mail.send(msg)
        return jsonify({'msj':'ok'}),200
    except:
        return jsonify({'msj':'error al enviar email'}),400

#Ruta para validar el email que se usa para registrarse
@login.route('/validar',methods = ['POST'])
def codigo_validacion():
    print('-- Codigo Post Login --')
    codigo = request.json['codigo']
    codigo_validacion = session.get('codigo_validacion')
    if codigo_validacion == codigo:
        usuario = session.get('usuario_temporal')
        result  = mongo.db.usuario.insert_one(usuario)
        user_id =result.inserted_id
        print('-    usuario registratdo')
        print(user_id)


        respuesta = jsonify({'msj':'ingresando al sistema'})
        respuesta.status_code = 200
        #Creamos una cookie para guardar el id del usuario
        respuesta.set_cookie('usuario', str(user_id))

        return respuesta

    else:
        return jsonify({'msj':'Falló al ingresar el codigo'}),400
    
@login.route('/end')
def login_end():
    user_id = request.cookies.get('usuario', 'No hay cookie')
    user = mongo.db.usuario.find_one({'_id':ObjectId(user_id)})

    if user:
            user['_id'] = str(user['_id'])
            session['user'] = user

            #Falta eliminar la cookie para q no exista mas
            return redirect('/dashboard')
    else:
        return "algo salio mal"
    

@login.route('/galleta') #Ruta de prueba para ver a cookie
def gallete():
    cookie_value = request.cookies.get('usuario', 'No hay cookie')
    return f'El valor de la cookie es: {cookie_value}'


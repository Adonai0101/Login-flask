from flask import Flask,render_template
from flask_mail import Mail, Message


from db import mongo

from routes.login import login
from routes.dashboard import dashboard

from routes.resetpass import resetpass

#cargando variables de entorno
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY']  = '2KJSDBJASBDBASHJFGSDVGLP'

#Mongo db
app.config['MONGO_URI'] = os.getenv('DATABASE')
mongo.init_app(app)


# Configuración para Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

#Registrando blueprints
app.register_blueprint(login, url_prefix='/login')
app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(resetpass, url_prefix='/resetpass')

@app.route('/')
def hello():
    print('inicio')
    # Código para enviar el correo electrónico de confirmación
    msg = Message('Bienvenido a nuestra aplicación', recipients=['pampire1995@gmail.com'])
    msg.body = '¡Gracias por registrarte en nuestra aplicación!'
    mail.send(msg)
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True)
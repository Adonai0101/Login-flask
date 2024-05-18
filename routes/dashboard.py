from flask import Blueprint,render_template,session,json,redirect,jsonify,request,current_app
from flask_mail import  Message

from db import mongo

#Herramientas
from tools.generar_codigos import *
from tools.login import login_required

dashboard = Blueprint('dashboard',__name__)


@dashboard.route('/')
@login_required
def home():
    print('-- Dashboard --')
    usuario = session.get("user")
    return render_template('dashboard/dashboard.html',usuario = usuario)
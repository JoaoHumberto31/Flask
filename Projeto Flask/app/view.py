from app import *
from flask import render_template

@app.route('/')
def homepage():
    usuario = 'João Humberto'
    idade = 25
    context ={
        'usuario':usuario,
        'idade':idade
    }
    return render_template('index.html', context=context)

@app.route('/contato/')
def novaPagina():
    return 'Outras views'
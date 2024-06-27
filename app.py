#nuevo entorno
from flask import (
    Flask,
    render_template, request, redirect)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/Mercaderia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)
migrate = Migrate(app, db)
from models import Marca, Tipo, Producto

@app.route('/')
def bienvenido():
    return render_template('index.html')

listado_productos=[
    dict(
        name=dict(
            first="Jabón Ariel",
        ),
        price=dict(
            price="1000",
        ),
        stock="9"
    ),
    dict(
        name=dict(
            first="fideos milena",
        ),
        price=dict(
            price="2500",
        ),
        stock="5"
    ),
]

@app.route('/productos')
def productos():
    listado= listado_productos
    return render_template(
        'productos.html', 
        listado= listado
    )


@app.route('/agProductos', methods=['POST', 'GET'])
def agregar_productos():
    if request.method == 'POST':
        name= request.form['nombre']
        price= request.form['precio']
        stock= request.form['stock']

        producto= dict(
            name=dict(
                first=name,
            ),
            price=dict(
                price=price,
            ),
            stock=stock
        )

        listado_productos.append(producto)

        
    return render_template ('agProductos.html')







from app import db

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return self.nombre
    
class Tipo(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return self.nombre

class Producto(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    precio = db.Column(db.Integer, nullable=False)
    peso= db.Column(db.Float, nullable=False)
    tipo_id = db.Column(db.Integer, db.ForeignKey('tipo.id'), nullable=False)  
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)

    tipo = db.relationship('Tipo', backref=db.backref('producto', lazy=True)) 
    marca = db.relationship('Marca', backref=db.backref('producto', lazy=True))  

    def __str__(self):
        return self.precio
    

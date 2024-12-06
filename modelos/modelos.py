from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy  import SQLAlchemyAutoSchema
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Administrador(db.Model):
    __tablename__ = 'administrador'
    id_admin = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer)
    contrasena = db.Column(db.Integer)
    nombre = db.Column(db.Integer)
    id_rol = db.Column(db.Integer,db.ForeignKey('rol.id_rol'))

class Beneficiarios(db.Model):
    __tablename__ = 'beneficiarios'
    id_beneficiarios = db.Column(db.Integer, primary_key=True)
    nom_emp = db.Column(db.Column)
    nom_ben = db.Column(db.Column)
    parentesco = db.Column(db.Column)
    id_rol = db.Column(db.Integer,db.ForeignKey('rol.id_rol'))
    id_registro = db.Column(db.Integer,db.ForeignKey('registro.id_registro'))
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id_empleado'))


class Departamento(db.Model):
    __tablename__ = 'departamento'
    id_departamento = db.Column(db.Integer, primary_key=True)
    nom_dep = db.Column(db.Column)
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id_empleado'))


class Empleado(db.Model):
    __tablename__ = 'empleado'
    id_empleado = db.Column(db.Integer, primary_key=True)
    id_beneficiarios = db.Column(db.Integer, db.ForeignKey('beneficiarios.id_beneficiarios'))
    nom_emp = db.Column(db.Integer)
    departamento = db.Column(db.Integer)
    foto = db.Column(db.Integer)
    usuario = db.Column(db.Integer)
    contrasena = db.Column(db.Integer)
    id_rol = db.Column(db.Integer,db.ForeignKey('rol.id_rol'))
    id_registro = db.Column(db.Integer,db.ForeignKey('registro.id_registro'))
    id_departamento = db.Column(db.Integer,db.ForeignKey('departamento.id_departamento'))

class Login(db.Model):
    __tablename__ = 'login'
    id_login = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.Integer)
    contrasena =db.Column(db.Integer)
    id_rol = db.Column(db.Integer,db.ForeignKey('rol.id_rol'))

class Registro(db.Model):
    __tablename__ = 'registro'
    id_registro = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.Integer)
    departamento = db.Column(db.Integer)
    usuario = db.Column(db.Integer)
    contrasena = db.Column(db.Integer)
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id_empleado'))
    id_beneficiarios = db.Column(db.Integer,db.ForeignKey('beneficiarios.id_beneficiarios'))

class Rol(db.Model):
    __tablename__ = 'rol'
    id_rol = db.Column(db.Integer, primary_key=True)
    rol = db.Column(db.Integer)
    id_empleado = db.Column(db.Integer,db.ForeignKey('empleado.id_empleado'))
    id_admin = db.Column(db.Integer,db.ForeignKey('administrador.id_admin'))
    id_beneficiarios = db.Column(db.Integer,db.ForeignKey('beneficiarios.id_beneficiarios'))
    id_login = db.Column(db.Integer,db.ForeignKey('login.id_login'))

    @property
    def contrasena(self):
        raise AttributeError("La contraseña no es correcta")

    @contrasena.setter
    def contrasena(self, password):
        if not password:
            raise ValueError("La contraseña esta vacía.")
        self.contrasena_hash = generate_password_hash(password)

    def verificar_contrasena(self, password):
        return check_password_hash(self.contrasena_hash, password)

                                             #serializacion
class AdministradorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Administrador
        include_relationships = True
        load_instance = True

class EmpleadoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Empleado
        include_relationships = True
        load_instance = True

class BeneficiariosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Beneficiarios
        include_relationships = True
        load_instance = True


class LoginSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Login
        include_relationships = True
        load_instance = True

class RegistroSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Registro
        include_relationships = True
        load_instance = True

class Rolchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        include_relationships = True
        load_instance = True

class DepartamentoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Departamento
        include_relationships = True
        load_instance = True


from flask import request
from flask_restful import Resource
from ..modelos import db, Empleado, EmpleadoSchema, Beneficiarios, BeneficiariosSchema, Administrador, AdministradorSchema
from  flask_jwt_extended import create_access_token

                               #SCHEMAS DE MODELOS.PY
empleado_schema = EmpleadoSchema()
beneficiarios_schema = BeneficiariosSchema()
Administrador_schema = AdministradorSchema()

class VistaLogin(Resource):
    def post(self):
        usuario = request.json.get("usuario")
        contrasena = request.json.get("contrasena")

        # Verificar  datos
        print(f"usuario: {usuario}, Contraseña: {contrasena}")

        empleado = empleado.query.filter_by(usuario=usuario).first()

        if empleado:
            print(f"empleado en base de datos: {empleado.nom_emp}")
            if empleado.verificar_contrasena(contrasena):
                               #creacion token
                token_de_acceso = create_access_token(identity=usuario)
                return {'mensaje': 'logeo exitoso', 'token_de_acceso': token_de_acceso}, 200
            else:
                return {'mensaje': 'usuario y/o contraseña incorrectos'}, 401
        else:
            return {'mensaje': 'usuario no encontrado'}, 404

            
class VistaRegistro(Resource):

    def post(self):
        usuario_existente = Empleado.query.filter_by(usuario=request.json["usuario"]).first()
        if correo_existente:
            return {'mensaje': 'El usuario ya está registrado. Por favor, ingrese otro usuario.'}, 400
        
                                               #nuevo usuario
        nuevo_empleado = empleado(
            nom_emp=request.json["nom_emp"],
            departamento=request.json["departamento"],
            foto=request.json["foto"]
            usuario=request.json["usuario"]
            contrasena=request.json["contrasena"]
        )
                                                  #seguridad ()setter
        nuevo_empleado.contrasena = request.json["contrasena"]  
        
                                                 #token de empleado
        token_de_acceso = create_access_token(identity=request.json['nom_emp'])
        
                                                 #ingresado a la db
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return {'mensaje': 'empleado creado exitosamente', 'token': token_de_acceso}, 201

    def put(self, id_empleado):
        empleado = Empleado.query.get_or_404(id_empleado)
        empleado.contrasena = request.json.get("contrasena", empleado.contrasena)
        db.session.commit()
        return Empleado_schema.dump(empleado)

    def delete(self, id_empleado):
        empleado = Empleado.query.get_or_404(id_empleado)
        db.session.delete(empleado)
        db.session.commit()
        return '', 204 

class VistaEmpleados(Resource):
    def post(self):
        nuevo_empleado = empleado(nom_emp = request.json ['nom_emp'],
                                usuario = request.json['usuario'],    
                                contrasena = request.json['contraseña'])
        db.session.add(nuevo_empleado)
        db.session.commit()
        return Empleado_schema.dump(nuevo_empleado)
    
    def get(self):
        return [Empleado_schema.dump(Empleado) for Empleado in Empleado.query.all()]


class VistaEmpleado(Resource):
                                  # EDITAR - PUT
    def put(self, id_empleado):
        Empleado = Empleado.query.get(id_empleado)
        if not empleado:
            return 'El empleado no existe'
        
        empleado.nom_emp = request.json.get('nom_emp', empleado.nom_emp)
        empleado.departamento = request.json.get('departamento', empleado.departamento)
        empleado.foto = request.json.get('foto', empleado.foto)
        empleado.usuario = request.json.get('usuario', empleado.usuario)
        empleado.contrasena = request.json.get('contrasena', empleado.contrasena)

        db.session.commit()
        return Empleado_schema.dump(empleado)
                               #DELETE
    
    def delete(self, id_empleado):
        
        empleado = Empleado.query.get(id_empleado)
        if not empleado:
            return 'empleado  no hayado', 404
                                   #INSERCION DB
        
        db.session.delete(empleado)
        db.session.commit()
        return 'empleado eliminado'
    
class VistaBeneficiarios(Resource):
                                            #OBTENER-GET
    def get(self):
        return [beneficiario_schema.dump(Producto) for Beneficiarios in beneficiario.query.all()]
                                             #POST 
    def post(self):
        nuevo_Beneficiario = Beneficiarios(nom_emp = request.json ['nom_emp'],
                                nom_ben = request.json['nom_ben'],    
                                parentesco = request.json['parentesco'],    
                                id_rol = request.json['id_rol'],
                                id_registro = request.json['id_registro']
                                id_empleado = request.json['id_empleado'])
                                #INSERCION DB
        db.session.add(nuevo_Beneficiario)
        db.session.commit()
        return {'mensaje': 'beneficiario creado exitosamente'}

                                   #editar- put
    def put(self, id_beneficiarios):
        beneficiarios = Beneficiarios.query.get(id_beneficiarios)
        if not beneficiario:
            return 'El beneficiario no existe'
        
        beneficiarios.nom_emp = request.json.get('nom_emp', beneficiarios.nom_emp)
        beneficiarios.nom_ben = request.json.get('nom_ben', beneficiarios.nom_ben)
        beneficiarios.parentesco = request.json.get('parentesco', beneficiarios.parentesco)
        beneficiarios.id_rol = request.json.get('id_rol', beneficiarios.id_rol)
        beneficiarios.id_registro = request.json.get('id_registro', beneficiarios.id_registro)
                               #INSERCION DB

        db.session.commit()
        return Beneficiarios_schema.dump(beneficiarios)

    def delete(self, id_beneficiarios):
        beneficiarios = Beneficiarios.query.get(id_beneficiarios)
        if not beneficiario:
            return 'beneficiario no encontrado', 404
                              #DELETE
        db.session.delete(beneficiario)
        db.session.commit()
        return 'beneficiario eliminado'
                          #PUT-EDITAR
class VistaAdministrador(Resource):
    def put(self, id_admin):
        Administrador = Administrador.query.get(id_admin)
        if not administrador:
            return 'el administrador no existe'
        
        administrador.nombre = request.json.get('nombre', administrador.nombre)

                           # INSERTAR DB
        db.session.commit()
        return Administrador_schema.dump(administrador)
    
                            #DELETE
        administrador = administrador.query.get(id_admin)
        if not administrador:
            return 'adnimistrador  no encontrado', 404
        
        db.session.delete(administrador)
        db.session.commit()
        return 'administrador eliminado'
    

    
    

    

    

from flaskr import create_app
from flaskr.modelos.modelos import administrador, Rol, empleado, beneficiario, departamento, login, registro
from .modelos import db
from flask_restful import Api
from .vistas.vistas import VistaLogin, VistaRegistro, VistaEmpleados, VistaBeneficiarios, VistaSuperadmin, VistaAdministrador, VistaEmpleado, VistaSuperadminis 

app = create_app('default')
app_context = app.app_context()
app_context.push()
db.create_all()

api = Api(app)
                    #logeo empleados y beneficiarios
api.add_resource(VistaLogin, '/login')
api.add_resource(VistaRegistro, '/registro')
                    #POST
api.add_resource(VistaEmpleados, '/empleado')
api.add_resource(VistaBeneficiarios, '/beneficiarios')
api.add_resource(VistaSuperadmin, '/super_admin')
api.add_resource(VistaAdministrador, '/administrador')
                     #GET, POST, PUT, DELETE
api.add_resource(VistaEmpleado, '/empleado/<int:id_empleado>')
api.add_resource(VistaSuperadminis, '/superadmin/<int:id_super_admin>')


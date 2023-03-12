from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField
from wtforms import validators 
class UserForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    correo = EmailField('Correo electrónico')
    
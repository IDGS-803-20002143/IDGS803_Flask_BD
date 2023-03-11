from wtforms import Form, StringField, IntegerField, EmailField, validators

class UseForm(Form):
    id=IntegerField('id')
    nombre=StringField('nombre')
    apellidos=StringField('apellidos')
    email=EmailField('correo')
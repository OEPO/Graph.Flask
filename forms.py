from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class NodesClass(FlaskForm):
    check = BooleanField()
    edge = StringField('1->2 ; 2->3 ; 3->1 <br>Ejemplo de ingreso = 1,2;2,3;3,1',validators=[DataRequired(),Length(min=1,max=1000)]) #minimo dos nodos 1,2;2,1 caracteres = 7
    submit = SubmitField('Enviar')





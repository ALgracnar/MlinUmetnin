from flask_wtf import FlaskForm
from flask_wtf.csrf import CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

# csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField( validators=[DataRequired()])
    email = StringField(validators=[DataRequired(),Email('Vpišite veljaven e-mail naslov')])
    message = TextAreaField( validators=[DataRequired()])
    submit = SubmitField("pošlji")



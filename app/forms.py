from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired 

class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired('A name must be entered')])
    email = StringField('email', validators=[DataRequired()] )
    subject = StringField('subject', validators=[DataRequired()] )
    message = TextAreaField('message', validators=[DataRequired()] )
    submit = SubmitField("Enter")
    
    #CSRF token
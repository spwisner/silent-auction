from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CreateForm(FlaskForm):
    name = StringField('What is the name of the auction?', validators=[DataRequired()])
    submit = SubmitField('Submit')

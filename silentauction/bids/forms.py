from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired 

class AddForm(FlaskForm):
    bid = StringField('What is your bid?', validators=[DataRequired()])
    is_max_bid = BooleanField("is this your max bid")
    alerts = RadioField('Do you want to be alerted for this item', choices=[('alert_zero', 'No'), ('alert_one', 'Yes')])
    interest = SelectField('What is your level of interest?', choices=[('h', 'High'), ('m', 'Medium'), ('l', 'Low')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')
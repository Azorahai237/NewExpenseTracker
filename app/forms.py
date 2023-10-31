from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange, Optional

# Including validators for data required
class IncomeInputForm(FlaskForm):
    name = StringField("Name", validators=[
                       DataRequired(), Length(min=1, max=30)])
    category = SelectField("Category", validators=[DataRequired()], choices=[
                           ('salary', 'salary'), ('gift', 'gift')])
    amount = FloatField("Amount", validators=[
                        DataRequired(), NumberRange(min=0.0, max=10000000.0)])
    save = SubmitField("Save")


class ExpenseInputForm(FlaskForm):
    name = StringField("Name", validators=[
                       DataRequired(), Length(min=1, max=30)])
    category = SelectField("Category", validators=[DataRequired()], choices=[(
        'groceries', 'groceries'), ('shopping', 'shopping'), ('food', 'food'), ('rent', 'rent')])
    amount = FloatField("Amount", validators=[
                        DataRequired(), NumberRange(min=0.0, max=10000000.0)])
    save = SubmitField("Save")


class GoalInputForm(FlaskForm):
    name = StringField("Name", validators=[
                       DataRequired(), Length(min=1, max=30)])
    amount = FloatField("Amount", validators=[
                        DataRequired(), NumberRange(min=0.0, max=10000000.0)])
    save = SubmitField("Save")

# edit Income Expense and Goals forms have optional input instead of data required of Add forms
class EditIncomeForm(FlaskForm):
    name = StringField("Name", validators=[Optional(),
        Length(min=1, max=30)])
    category = SelectField("Category", validators=[Optional()], choices=[
                           ('salary', 'salary'), ('gift', 'gift')])
    amount = FloatField("Amount", validators=[Optional(),
        NumberRange(min=0.0, max=10000000.0)])
    save = SubmitField("Save")


class EditExpenseForm(FlaskForm):
    name = StringField("Name", validators=[Optional(),
                       Length(min=1, max=30)])
    category = SelectField("Category", validators=[Optional()], choices=[(
        'groceries', 'groceries'), ('shopping', 'shopping'), ('food', 'food'), ('rent', 'rent')])
    amount = FloatField("Amount", validators=[
                        Optional(), NumberRange(min=0.0, max=10000000.0)])
    save = SubmitField("Save")

class EditGoalForm(FlaskForm):
    name = StringField("Name", validators=[
                       Optional(), Length(min=1, max=30)])
    amount = FloatField("Amount", validators=[
                        Optional(), NumberRange(min=0.0, max=10000000.0)])
    save = SubmitField("Save")
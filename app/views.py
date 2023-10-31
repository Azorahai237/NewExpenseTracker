from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import IncomeInputForm, ExpenseInputForm, GoalInputForm, EditIncomeForm, EditExpenseForm, EditGoalForm
from app.models import income, expense, goal
from analytics import Income_Total, Expense_Total, Income_Max, Expense_Max
import json


@app.route('/')
def home():
    # initialising the lists to pass data to json then javascript
    percentage = 0
    bar_percentage = []
    total_values = []
    query_result = []
    IncomeMaxData = []
    ExpenseMaxData = []
    # ensure goal entry exists in db
    if (goal.query.first() is not None):
        GoalEntry = goal.query.first()
        query_result.append(GoalEntry.name)
        query_result.append(GoalEntry.amount)
    else:
        query_result.append("No goal saved")
        query_result.append(" ")
    # pogress bar percentage set to zero if either income expense and goal are not in entry
    if (Income_Total() == None or Expense_Total() == None or goal.query.first() == None):
        percentage = 0
    # Income less than expense set to zero so that progress bar not negatives
    elif (Income_Total() < Expense_Total()):
        percentage = 0

    else:
        # retrieve goal entry and calculating progress bar percentage
        goal_entry = goal.query.first()
        percentage = round((Income_Total() - Expense_Total()
                            )/goal_entry.amount * 100.0)

    bar_percentage.append(percentage)

    # data handling for income max and expense max cards
    if (Income_Total() == None):
        Income = 0
        IncomeMaxData.append("N/A")
    else:
        Income = Income_Total()
        MaxIncomeEntry = Income_Max()
        IncomeMaxData.append(MaxIncomeEntry.name)
        IncomeMaxData.append(MaxIncomeEntry.category)
        IncomeMaxData.append(MaxIncomeEntry.amount)
        total_values.append(Income)

    if (Expense_Total() == None):
        Expense = 0
        ExpenseMaxData.append("N/A")
    else:
        Expense = Expense_Total()
        total_values.append(Expense)
        MaxExpenseEntry = Expense_Max()
        ExpenseMaxData.append(MaxExpenseEntry.name)
        ExpenseMaxData.append(MaxExpenseEntry.category)
        ExpenseMaxData.append(MaxExpenseEntry.amount)

    return render_template('home.html', title='home', percentage=json.dumps(bar_percentage), totals=json.dumps(total_values),
        QueryResult=json.dumps(query_result), IncomeMax=json.dumps(IncomeMaxData), 
        ExpenseMax=json.dumps(ExpenseMaxData))


@app.route('/Expense')
def Expense():
    # check if any entries exist in the current table
    if (expense.query.first() == None):
        entries = []
    else:
        entries = expense.query.all()
    return render_template('Expense.html', title='Expenses', entries=entries)


@app.route("/AddExpense", methods=["POST", "GET"])
def add_expense():
    form = ExpenseInputForm()
    if form.validate_on_submit():
        entry = expense(name=form.name.data,
                        category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash("Expense entry saved", 'success')

    return render_template('AddExpense.html', title='add expense', form=form)


@app.route('/DeleteExpense/<int:entry_id>')
def DeleteExpense(entry_id):
    entry = expense.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash('Deletion was a success', 'success')
    return redirect(url_for("Expense"))


@app.route('/EditExpense/<int:entry_id>', methods=["POST", "GET"])
def EditExpense(entry_id):
    entry = expense.query.get_or_404(int(entry_id))
    form = EditExpenseForm()
    # checking if form is empty, else save new values
    if form.validate_on_submit():
        if form.name.data != '':
            entry.name = form.name.data
        if form.category.data != '':
            entry.category = form.category.data

        if form.amount.data is not None:
            entry.amount = form.amount.data
  
    db.session.commit()
    return render_template('EditExpense.html', title='edit expense', form=form)


@app.route('/Income')
def Income():
    if (income.query.first() == None):
        entries = []
    else:
        entries = income.query.all()
    return render_template('Income.html', title='Income', entries=entries)


@app.route("/AddIncome", methods=["POST", "GET"])
def add_income():
    form = IncomeInputForm()
    if form.validate_on_submit():
        entry = income(name=form.name.data,
                       category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash("Income entry saved", 'success')

    return render_template('AddIncome.html', title='add income', form=form)


@app.route('/DeleteIncome/<int:entry_id>')
def DeleteIncome(entry_id):
    entry = income.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash('Deletion was a success', 'success')
    return redirect(url_for("Income"))


@app.route('/EditIncome/<int:entry_id>', methods=["POST", "GET"])
def EditIncome(entry_id):
    entry = income.query.get_or_404(int(entry_id))
    form = EditIncomeForm()

    if form.validate_on_submit():
        if form.name.data != '':
            entry.name = form.name.data
        if form.category.data != '':
            entry.category = form.category.data

        if form.amount.data is not None:
            entry.amount = form.amount.data

    db.session.commit()
    return render_template('EditIncome.html', title='edit income', form=form)


@app.route("/goal", methods=["POST", "GET"])
def Goal():
    # checking if a goal exists if not add goal
    if (goal.query.first() == None):

        input_form = GoalInputForm()
        if input_form.validate_on_submit():
            new_entry = goal(name=input_form.name.data,
                             amount=input_form.amount.data)
            db.session.add(new_entry)
            db.session.commit()
            flash("Goal entry saved", 'success')

        return render_template('goal.html', title='Goal', form=input_form)
    else:
        # if goal already exists edit goal form
        output_form = EditGoalForm()
        entry = goal.query.first()
        if output_form.validate_on_submit():
            if output_form.name.data != '':
                entry.name = output_form.name.data
            if output_form.amount.data is not None:
                entry.amount = output_form.amount.data
        db.session.commit()
        flash("Goal entry edited", "success")
        return render_template('EditGoal.html', title='Edit Goal', form=output_form)


@app.route("/DeleteGoal")
def DeleteGoal():
    if (goal.query.first() == None):
        flash("No goal to delete", "info")
        return redirect("/")

    entry = goal.query.first()
    db.session.delete(entry)
    db.session.commit()
    flash("Goal was deleted", "success")
    return redirect("/")

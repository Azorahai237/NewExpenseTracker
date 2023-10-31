from app import models, db
#file to handle all data processing of db entries
#calculating total of income, return none if db empty
def Income_Total():
    total = 0.0
    if (models.income.query.first()==None):
        return None

    for entries in models.income.query.all():
        total += entries.amount
    return total

def Income_Max():
    if (models.income.query.first()==None):
        return None
    
    Highest_Entry = models.income.query.first()   
    for entry in models.income.query.all():
        if entry.amount > Highest_Entry.amount:
            Highest_Entry = entry
    return Highest_Entry


def Expense_Total():
    total = 0.0
    if (models.expense.query.first()==None):
        return None
    
    for entries in models.expense.query.all():
        total += entries.amount
    return total

def Expense_Max():
    if (models.expense.query.first()==None):
        return None
    
    Highest_Entry = models.expense.query.first()   
    for entry in models.expense.query.all():
        if entry.amount > Highest_Entry.amount:
            Highest_Entry = entry
    return Highest_Entry


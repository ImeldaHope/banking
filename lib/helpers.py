from models.account import Account
from models.customer import Customer
from models.loan import Loan
from models.transaction import Transaction


def exit_program():
    print("Goodbye!")
    exit()

#customer methods
def create_customer():
    pass

def update_customer():
    pass

def delete_customer():
    pass

def list_customers():
    pass

def find_customer_by_name():
    pass

def find_customer_by_id():
    pass

#account methods           
def create_account(base, engine):
    base.metadat.create_all(engine)

def save(session, account):
    session.add(account)
    session.commit()

def update_account(session, account, acc_type):
    account.acc_type = acc_type
    session.add(account)
    session.commit()

def delete_account():
    pass

def list_accounts(session):
    return session.query(Account).all()

def find_account_by_number(session, acc_number):
    return session.query(Account).filter(Account.acc_number == acc_number).first()

def find_account_by_id(session,id):
    return session.query(Account).filter(Account.id == id).first()

#transaction methods
def create_transaction():
    pass

def update_transaction():
    pass

def delete_transaction():
    pass

def find_transaction_by_id():
    pass

#loan methods
def create_loan():
    pass

def update_loan():
    pass

def delete_loan():
    pass

def find_loan_by_id():
    pass

#relationship methods
def list_customer_accounts():
    pass

def list_customer_loans():
    pass

def list_account_transactions():
    pass
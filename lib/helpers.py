from models.account import Account
from models.customer import Customer
from models.loan import Loan
from models.transaction import Transaction


def exit_program():
    print("Goodbye!")
    exit()

#customer methods
def create_customer(session):
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    phone = input("Enter customer phone: ")
    address = input("Enter customer address: ")
    
    customer = Customer(name=name, email=email, phone=phone, address=address)
    save(session, customer)

def save(session, obj):
    session.add(obj)
    session.commit()

def update_customer(session):
    customer_id = input("Enter the customer's ID: ")
    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if customer:
        try:
            # Prompt for new details
            name = input("Enter the new name: ")
            email = input("Enter the new email: ")
            phone = input("Enter the new phone: ")
            address = input("Enter the new address: ")
            
            # Update customer details
            customer.name = name
            customer.email = email
            customer.phone = phone
            customer.address = address

            # Save the updated customer
            save(session, customer)
            print(f'Success: {customer}')
        except Exception as exc:
            print("Error updating customer: ", exc)
    else:
        print(f'Customer with ID {customer_id} not found')

def delete_customer(session):
    customer_id = input("Enter the customer's ID that needs to be deleted: ")
    customer = session.query(Customer).filter(Customer.id == customer_id).first()

    if customer:
        try:
            session.delete(customer)
            session.commit()
            print(f"Customer with ID {customer_id} has been deleted.")
        except Exception as e:
            session.rollback()
            print(f"Error deleting customer: {e}")
    else:
        print(f'Customer with ID {customer_id} not found')

def list_customers(session):    
    try:        
        customers = session.query(Customer).all()
        print(f"Found {len(customers)} customers.")
        for customer in customers:
            print(f"Customer ID: {customer.id}, Name: {customer.name}")
        return customers
    except Exception as e:
        print(f"Error querying customers: {e}")
        return []

def find_customer_by_name(session):
    name = input("Enter the customer's name: ")
    customer = session.query(Customer).filter(Customer.name == name).first()
    if customer:
        print(customer)
    else:
        print("Customer not found.")

def find_customer_by_id(session):
    customer_id = input("Enter the customer's ID: ")
    customer = session.query(Customer).filter(Customer.id == customer_id).first()
    if customer:
        print(customer)
    else:
        print("Customer not found.")

#account methods           
def create_account(session):
    acc_number = input("Enter account number: ")
    acc_type = input("Enter account type: ")
    balance = input("Enter account balance: ")
    customer_id = input("Enter customer id: ")

    account = Account(acc_number=acc_number, acc_type=acc_type, balance=balance, customer_id=customer_id)
    save(session, account)

def update_account(session):
    acc_id = input("Enter account ID: ")
    account = session.query(Account).filter(Account.id == acc_id).first()

    if account:
        try:
            acc_number = input("Enter the new account number: ")
            acc_type = input("Enter the new account type: ")
            balance = input("Enter the new balance: ")
            customer_id = input("Enter the new customer id: ")

            account.acc_number = acc_number
            account.acc_type = acc_type
            account.balance = balance
            account.customer_id = customer_id

            save(session, account)
            print(f'Success: {account}')
        except Exception as exc:
            print("Error updating account: ", exc)
    else:
        print(f'Account with ID {acc_id} not found')

def delete_account(session, account):
    session.delete(account)
    session.commit()

def list_accounts(session):
    return session.query(Account).all()

def find_account_by_number(session, acc_number):
    return session.query(Account).filter(Account.acc_number == acc_number).first()

def find_account_by_id(session,id):
    return session.query(Account).filter(Account.id == id).first()

#transaction methods
def create_transaction(base,engine):
    base.metadata.create_all(engine)

def update_transaction(session, transaction, amount):
    transaction.amount = amount
    session.add(transaction)
    session.commit()

def delete_transaction(session, transaction):
    session.delete(transaction)
    session.commit()

def find_transaction_by_id(session, id):
    return session.query(Transaction).filter(Transaction.id == id).first()

#loan methods
def create_loan(base, engine):
    base.metadata.create_all(engine)

def update_loan(session, loan, loan_amount):
    loan.loan_amount = loan_amount
    session.add(loan)
    session.commit()

def delete_loan(session, loan):
    session.delete(loan)
    session.commit()

def find_loan_by_id(session, id):
    return session.query(Loan).filter(Loan.id == id).first()

#relationship methods
def list_customer_accounts(session, customer_id):
    return session.query(Account).filter(Account.customer_id == customer_id).all()

def list_customer_loans(session, customer_id):
    return session.query(Loan).filter(Loan.customer_id == customer_id).all()

def list_account_transactions(session, account_id):
    return session.query(Transaction).filter(Transaction.acc_id == account_id).all()
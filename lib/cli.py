from models.__init__ import init_db, session
from helpers import (
    exit_program,
    create_customer,
    update_customer,
    delete_customer,
    list_customers,
    find_customer_by_name,
    find_customer_by_id,
    create_account,
    update_account,
    delete_account,
    list_accounts,
    find_account_by_number,
    find_account_by_id,
    create_transaction,
    update_transaction,
    delete_transaction,    
    find_transaction_by_id,
    create_loan,
    update_loan,
    delete_loan,    
    find_loan_by_id,    
    list_customer_accounts,
    list_customer_loans,
    list_account_transactions     
)

def main():
    init_db()
    while True:
        menu()
        choice = input("> ")
                
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_customer(session)
        elif choice == "2":
            update_customer(session)
        elif choice == "3":
            delete_customer(session)
        elif choice == "4":
            list_customers(session)
        elif choice == "5":
            find_customer_by_name(session)
        elif choice == "6":
            find_customer_by_id(session)
        elif choice == "7":
            create_account(session)
        elif choice == "8":
            update_account(session)
        elif choice == "9":
            delete_account(session)
        elif choice == "10":
            list_accounts(session)
        elif choice == "11":
            find_account_by_number(session)
        elif choice == "12":
            find_account_by_id(session)
        elif choice == "13":
            create_transaction(session)
        elif choice == "14":
            update_transaction(session)
        elif choice == "15":
            delete_transaction(session)
        elif choice == "16":
            find_transaction_by_id(session)
        elif choice == "17":
            create_loan(session)
        elif choice == "18":
            update_loan(session)
        elif choice == "19":
            delete_loan(session)
        elif choice == "20":
            find_loan_by_id(session)
        elif choice == "21":
            list_customer_accounts(session)
        elif choice == "22":
            list_customer_loans(session)
        elif choice == "23":
            list_account_transactions(session)
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create customer")
    print("2. Update customer")
    print("3. Delete customer")
    print("4: List customers")
    print("5: Find customer by name")
    print("6: Find customer by id")
    print("7. Create account")
    print("8. Update account")
    print("9. Delete account")
    print("10: List accounts")
    print("11: Find account by number")
    print("12: Find account by id")
    print("13: Create transaction")
    print("14: Update transaction")
    print("15: Delete transaction")
    print("16: Find transaction by id")
    print("17: Create loan")
    print("18: Update loan")
    print("19: Delete loan")
    print("20: Find loan by id")
    print("21: List customer accounts")
    print("22: List customer loans")
    print("23: List account transactions")
   
if __name__ == "__main__":
    main()
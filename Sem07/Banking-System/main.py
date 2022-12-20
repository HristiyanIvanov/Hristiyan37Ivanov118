from bank import Bank
from errors import *

MAIN_MENU_OPTIONS = {
    "1": "Register user",
    "2": "Create account",
    "3": "List all users",
    "4": "List all accounts",
    "5": "Deposit to account",
    "6": "Withdraw from account",
    "7": "Exit"
}


def display_main_menu():
    print("\nMain Menu:")
    for key, value in MAIN_MENU_OPTIONS.items():
        print(f"{key}. {value}")


def main_menu_selection(selection, bank):
    if selection == "1":
        bank.register_user()
    elif selection == "2":
        bank.create_account()
    elif selection == "3":
        bank.list_all_users()
    elif selection == "4":
        bank.list_all_accounts()
    elif selection == "5":
        bank.deposit_to_account()
    elif selection == "6":
        bank.withdraw_from_account()
    elif selection == "7":
        print("\nExiting the program.")
        exit()
    else:
        raise InvalidMenuChoice()


def main():
    bank = Bank()
    while True:
        display_main_menu()
        selection = input("Enter your selection: ")
        try:
            main_menu_selection(selection, bank)
        except InvalidUserData as e:
            print(e)
        except UserNotFound as e:
            print(e)
        except UserAlreadyExists as e:
            print(e)
        except UserAlreadyOwnsAccount as e:
            print(e)
        except AccountNotFound as e:
            print(e)
        except UnsufficientBalance as e:
            print(e)
        except InvalidAccountData as e:
            print(e)
        except InvalidAccountType as e:
            print(e)
        except InvalidMenuChoice as e:
            print(e)
        except InvalidAmountType as e:
            print(e)
        except InvalidCurrencyInput as e:
            print(e)
        except ValueError:
            print("Invalid Amount Type. Please type integer number.")


if __name__ == "__main__":
    main()

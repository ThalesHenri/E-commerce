from store import Store
from shoes import Shoes

"""object"""
store = Store()

def manager_menu():
    print("=" * 20)
    print("Welcome to the TH E-commerce app\nChoose your option bellow:")
    print("=" * 20)
    print("1- Register product.\n2- Delete product")
    print("3- Show stock\n4- Edit stock")
    print("5- Client metrics ")
    print("=" * 20)
    a = int(input("Choose the number of your option: "))
    if a == 1:
        register_product()
    if a == 2:
        delete_product()
    if a == 3:
        show_stock()
    if a == 4:
        edit_stock()
    if a == 5:
        client_metrics()


def client_metrics():
    pass


def edit_stock():
    pass


def show_stock():
    pass


def delete_product():
    pass


def register_product():
    print("Witch type of product you wanna add: ")
    a = int(input("1 - Shoes:\n2 - clothing\n3 - Other"))
    if a == 1:
        n = str(input("Name: "))
        w = str(input("Weight: "))
        q = str(input("Quantity: "))
        s = int(input("Size: "))
        p = int(input("Price: $"))
        shoes = Shoes(n, w, q, s, p)
        store.add_shoes(shoes)
        store.test_list()
manager_menu()

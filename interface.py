import pizza.food as food
from pizza.modell import Item

ITEMS = []

def main_screen():
    print("----------------------------")
    print("|    1 - print shopping list")
    print("|    2 - print food items   ")
    print("|    3 - add new items      ")
    print("|    4 - alter items   ")
    print("----------------------------")

def print_shopping_list():
    print("---------------------------")
    print("|      Shopping List       ")
    print(food.get_shopping_list())
    print("---------------------------")


def print_food_items():
    print("---------------------------")
    print("|          ITEMS           ")
    print("---------------------------")
    for item in ITEMS:
        print(item.get_name())


def add_items():
    print("---------------------------")
    print("|   Add New Items By ID    ")
    print("---------------------------")
    a = input("What is the name of the item you would like to add?")
    b = input("How much is there?")
    c = input("What is the expiry date?")
    d = input("What is the storage number? (box = 1) (object = 2) (carton = 3)")

    e = Item(None, a, b, c, d)
    s = food.add_to_table(e)
    e._id = s
    ITEMS.append(e)


    print("Your item has been added")
    print("---------------------------")


def remove_items():
    print("---------------------------")
    print("|  Alter Items By ID  ")
    print("---------------------------")
    a = input("What item would you like to alter?")

    for i in ITEMS:
        if a == i.get_name():
            c = i
            break



    b = input("How much is left?")
    food.alter_items(c, b)
    print("Your item has been altered")
    print("---------------------------")


def success_menu():
    print("---------------------------")
    print("|         SUCCESS!         ")
    print("---------------------------")


def fail_menu():
    print("---------------------------")
    print("|          FAIL!           ")
    print("---------------------------")


if __name__ == "__main__":
    ITEMS = food.get_all()
    main_screen()

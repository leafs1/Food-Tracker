import pizza.interface as pi
import pizza.food as food


def main_screen_choose_an_option():
    pi.main_screen()
    a = input("Choose an Option!")
    if a == "1":
        pi.print_shopping_list()
    elif a == "2":
        pi.print_food_items()
    elif a == "3":
        pi.add_items()
    elif a == "4":
        pi.remove_items()
    elif a == "5":
        pi.alter_items()
    elif a != "1" or "2" or "3" or "4" or "5":
        incorrect()
    main_screen_choose_an_option()




def incorrect():
    print("Please choose one of the options provided!")
    main_screen_choose_an_option()


if __name__ == "__main__":
    pi.ITEMS = food.get_all()
    main_screen_choose_an_option()



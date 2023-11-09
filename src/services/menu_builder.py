from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        main_menu = []

        for dish in self.menu_data.dishes:
            """caso haja alguma restrição e a restrição esteja
            presente em alguma das receitas"""
            if restriction and restriction in dish.get_restrictions():
                continue
            """para cada ingrediente presente na receita,
            caso o ingrediente exista no inventário e sua quantidade
            seja maior que 0,"""
            if all(
                ingredient in self.inventory.inventory
                and self.inventory.inventory[ingredient] > 0
                for ingredient in dish.recipe.keys()
            ):
                # adiciona a receita ao array
                main_menu.append({
                    "dish_name": dish.name,
                    "restrictions": dish.get_restrictions(),
                    "price": dish.price,
                    "ingredients": dish.get_ingredients(),
                })

        return main_menu


teste = MenuBuilder()
print(MenuBuilder.get_main_menu(teste))

from src.models.ingredient import Ingredient
from src.models.dish import Dish


# Req 3
class MenuData:

    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.dish_map = {}

        with open(source_path, "r", encoding="utf-8") as file:
            self.data = file.read().splitlines()
            self.format_data()

    def format_data(self):
        # itera sobre cada linha dos dados, começando da segunda linha
        for row in self.data[1:]:
            name, price, ingredient, amount = row.split(",")

            # verifica se a dish já foi criada e, caso não, cria uma nova dish
            if name not in self.dish_map:
                self.dish_map[name] = Dish(name, float(price))

            dish_ingredient = Ingredient(ingredient)
            self.dish_map[name].add_ingredient_dependency(
                dish_ingredient, int(amount))

        self.dishes.update(self.dish_map.values())

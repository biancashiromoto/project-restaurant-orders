from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    camarao = Ingredient("camarão")
    assert camarao.name == "camarão"

    restrictions = {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED
    }
    assert camarao.restrictions == restrictions

    assert camarao.__hash__() == hash(camarao.name)

    camarao_2 = Ingredient("camarão")
    assert camarao.__eq__(camarao_2) is True

    berinjela = Ingredient("berinjela")
    assert camarao.__eq__(berinjela) is False

    assert camarao.__repr__() == "Ingredient('camarão')"


test_ingredient()

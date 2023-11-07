import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 2
def test_dish():
    lasanha_berinjela = Dish("lasanha berinjela", 59.90)
    assert lasanha_berinjela.name == "lasanha berinjela"
    assert lasanha_berinjela.__repr__() == "Dish('lasanha berinjela', R$59.90)"
    assert lasanha_berinjela.__hash__() == hash(lasanha_berinjela.__repr__())

    outra_lasanha = Dish("lasanha berinjela", 59.90)
    assert lasanha_berinjela.__eq__(outra_lasanha) is True

    lasanha_presunto = Dish("lasanha_presunto", 44.90)
    assert lasanha_berinjela.__eq__(lasanha_presunto) is False

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Bla bla bla", "A")

    with pytest.raises(ValueError,
                       match="Dish price must be greater then zero."):
        Dish("Bla bla bla", 0.00)

    mussarela = Ingredient("queijo mussarela")
    lasanha_berinjela.add_ingredient_dependency(mussarela, 200)
    assert mussarela in lasanha_berinjela.get_ingredients()
    assert Restriction.ANIMAL_DERIVED in lasanha_berinjela.get_restrictions()

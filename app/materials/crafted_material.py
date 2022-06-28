from . import Material, Ingredient


class CraftedMaterial(Material):
    def __init__(self, name: str, base_material: bool = False, ingredient_list: list[Ingredient]) -> None:
        super().__init__(name, base_material)
        self.ingredient_list = ingredient_list

    def get_ingredient_list(self) -> list[Ingredient]:
        return self.ingredient_list
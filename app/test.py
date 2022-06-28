from app.materials.resources import res, CraftedMaterials, INGREDIENTS, BASE_MATERIAL
from app.materials.constant import Enum
from app.materials.crafted_material import CraftedMaterial, Material, Ingredient
from app.materials.base_material import BaseMaterial


class Test:
    def print_resource_tree(self, material: Material) -> None:
        pass

    def create_material(self, mat: Enum) -> Material:
        if mat not in res:
            return None
        name = mat.value
        mat_dict = res[mat]
        ing_list = None
        if not mat_dict[BASE_MATERIAL]:
            ing: dict = mat_dict[INGREDIENTS]
            # print(f"\n{ ing }\n")
            ing_list: list[Ingredient] = []
            for i, q in ing.items():
                ing_list.append(Ingredient(material=self.create_material(i), qty=q))
            return CraftedMaterial(name=name, ingredient_list=ing_list)
        return BaseMaterial(name=name)

    def test(self):
        mater = Test().create_material(CraftedMaterials.BLACK_ICE_FOUNDATION)
        return mater


if __name__ == "__main__":
    pass

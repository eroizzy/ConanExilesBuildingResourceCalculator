# from base_material import BaseMaterial
# from crafted_material import CraftedMaterial
# from ingredients import Ingredient

from enum import Enum

res: dict = {
    "wood": {"base_material": True},
    "dry_wood": {"base_material": True},
    "stone": {"base_material": True},
    "ironstone": {"base_material": True},
    "brimstone": {"base_material": True},
    "tar": {"base_material": True},
    "resin": {"base_material": True},
    "iron_bar": {"base_material": False, "ingredients": {"ironstone": 2}},
}


class BaseMaterials(Enum):
    BLACK_ICE = "black_ice"
    BLACK_ICE_FOUNDATION = "black_ice_foundation"


# resource: dict = {
#     "black_ice": BaseMaterial(name="Black Ice"),

#     "black_ice_foundation": CraftedMaterial(
#         "Black Ice Foundatoin",
#         ingredient_list=[
#             Ingredient(material=resource[base_materials.BLACK_ICE], qty=15),
#             Ingredient(material=, qty=8)
#         ]
#     )
# }

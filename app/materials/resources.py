# from base_material import BaseMaterial
# from crafted_material import CraftedMaterial
# from ingredients import Ingredient

from enum import Enum


class BaseMaterials(Enum):
    BLACK_ICE = "Black Ice"
    BRIMSTONE = "Brimstone"
    DRY_WOOD = "Dry Wood"
    IRONSTONE = "Ironstone"
    RESIN = "Resin"
    STONE = "Stone"
    TAR = "Tar"
    WOOD = "Wood"


class CraftedMaterials(Enum):
    BLACK_ICE_FOUNDATION = "black_ice_foundation"
    IRON_BAR = "Iron Bar"
    IRON_REINFORCEMENT = "Iron Reinforcement"
    STEEL_BAR = "Steel Bar"
    STEEL_REINFORCEMENT = "Steel Reinforcement"
    STEELFIRE = "Steelfire"


res: dict = {
    BaseMaterials.BRIMSTONE: {"base_material": True},
    BaseMaterials.DRY_WOOD: {"base_material": True},
    BaseMaterials.IRONSTONE: {"base_material": True},
    BaseMaterials.RESIN: {"base_material": True},
    BaseMaterials.STONE: {"base_material": True},
    BaseMaterials.TAR: {"base_material": True},
    BaseMaterials.WOOD: {"base_material": True},
    CraftedMaterials.IRON_BAR: {
        "base_material": False,
        "ingredients": {BaseMaterials.IRONSTONE: 2},
    },
    CraftedMaterials.IRON_REINFORCEMENT: {
        "base_material": False,
        "ingredients": {CraftedMaterials.IRON_BAR: 2},
    },
    CraftedMaterials.STEEL_BAR: {
        "base_material": False,
        "ingredients": {CraftedMaterials.IRON_BAR: 5, CraftedMaterials.STEELFIRE: 1},
    },
    CraftedMaterials.STEEL_REINFORCEMENT: {
        "base_material": False,
        "ingredients": {
            CraftedMaterials.IRON_REINFORCEMENT: 1,
            CraftedMaterials.STEELFIRE: 1,
        },
    },
    CraftedMaterials.STEELFIRE: {
        "base_material": False,
        "ingredients": {BaseMaterials.TAR: 2, BaseMaterials.BRIMSTONE: 1},
    },
}


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

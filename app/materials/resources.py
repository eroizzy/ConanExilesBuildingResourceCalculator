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
    BLACK_ICE_CEILING = "Black Ice-Reinforced Wooden Ceiling"
    BLACK_ICE_DOOR = "Black Ice-Reinforced Wooden Door"
    BLACK_ICE_DOORFRAME = "Black Ice-Reinforced Wooden Doorframe"
    BLACK_ICE_FOUNDATION = "Black Ice-Reinforced Wooden Foundation"
    BLACK_ICE_WALL = "Black Ice-Reinforced Wooden Wall"
    INSULATED_WOOD = "Insulated Wood"
    IRON_BAR = "Iron Bar"
    IRON_REINFORCEMENT = "Iron Reinforcement"
    STEEL_BAR = "Steel Bar"
    STEEL_REINFORCEMENT = "Steel Reinforcement"
    STEELFIRE = "Steelfire"


resources: dict = {
    BaseMaterials.BRIMSTONE: {"base_material": True},
    BaseMaterials.DRY_WOOD: {"base_material": True},
    BaseMaterials.IRONSTONE: {"base_material": True},
    BaseMaterials.RESIN: {"base_material": True},
    BaseMaterials.STONE: {"base_material": True},
    BaseMaterials.TAR: {"base_material": True},
    BaseMaterials.WOOD: {"base_material": True},
    CraftedMaterials.BLACK_ICE_CEILING: {
        "base_material": False,
        "ingredients": {
            BaseMaterials.BLACK_ICE: 9,
            CraftedMaterials.STEEL_REINFORCEMENT: 2,
            CraftedMaterials.INSULATED_WOOD: 4,
        },
    },
    CraftedMaterials.BLACK_ICE_DOOR: {
        "base_material": False,
        "ingredients": {
            BaseMaterials.BLACK_ICE: 15,
            CraftedMaterials.STEEL_REINFORCEMENT: 3,
            CraftedMaterials.INSULATED_WOOD: 6,
        },
    },
    CraftedMaterials.BLACK_ICE_DOORFRAME: {
        "base_material": False,
        "ingredients": {
            BaseMaterials.BLACK_ICE: 8,
            CraftedMaterials.STEEL_REINFORCEMENT: 2,
            CraftedMaterials.INSULATED_WOOD: 3,
        },
    },
    CraftedMaterials.BLACK_ICE_FOUNDATION: {
        "base_material": False,
        "ingredients": {
            BaseMaterials.BLACK_ICE: 15,
            CraftedMaterials.STEEL_REINFORCEMENT: 3,
            CraftedMaterials.INSULATED_WOOD: 6,
        },
    },
    CraftedMaterials.BLACK_ICE_WALL: {
        "base_material": False,
        "ingredients": {
            BaseMaterials.BLACK_ICE: 8,
            CraftedMaterials.STEEL_REINFORCEMENT: 2,
            CraftedMaterials.INSULATED_WOOD: 3,
        },
    },
    CraftedMaterials.INSULATED_WOOD: {
        "base_material": False,
        "ingredients": {BaseMaterials.DRY_WOOD: 1, BaseMaterials.RESIN: 1},
    },
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

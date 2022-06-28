# from base_material import BaseMaterial
# from crafted_material import CraftedMaterial
# from ingredients import Ingredient
from app.materials.constant import (
    BaseMaterials,
    CraftedMaterials,
    INGREDIENTS,
    BASE_MATERIAL,
)


res: dict = {
    BaseMaterials.BRIMSTONE: {BASE_MATERIAL: True},
    BaseMaterials.DRY_WOOD: {BASE_MATERIAL: True},
    BaseMaterials.IRONSTONE: {BASE_MATERIAL: True},
    BaseMaterials.RESIN: {BASE_MATERIAL: True},
    BaseMaterials.STONE: {BASE_MATERIAL: True},
    BaseMaterials.TAR: {BASE_MATERIAL: True},
    BaseMaterials.WOOD: {BASE_MATERIAL: True},
    CraftedMaterials.BLACK_ICE_CEILING: {
        BASE_MATERIAL: False,
        INGREDIENTS: {
            BaseMaterials.BLACK_ICE: 9,
            CraftedMaterials.STEEL_REINFORCEMENT: 2,
            CraftedMaterials.INSULATED_WOOD: 4,
        },
    },
    CraftedMaterials.BLACK_ICE_DOOR: {
        BASE_MATERIAL: False,
        INGREDIENTS: {
            BaseMaterials.BLACK_ICE: 15,
            CraftedMaterials.STEEL_REINFORCEMENT: 3,
            CraftedMaterials.INSULATED_WOOD: 6,
        },
    },
    CraftedMaterials.BLACK_ICE_DOORFRAME: {
        BASE_MATERIAL: False,
        INGREDIENTS: {
            BaseMaterials.BLACK_ICE: 8,
            CraftedMaterials.STEEL_REINFORCEMENT: 2,
            CraftedMaterials.INSULATED_WOOD: 3,
        },
    },
    CraftedMaterials.BLACK_ICE_FOUNDATION: {
        BASE_MATERIAL: False,
        INGREDIENTS: {
            BaseMaterials.BLACK_ICE: 15,
            CraftedMaterials.STEEL_REINFORCEMENT: 3,
            CraftedMaterials.INSULATED_WOOD: 6,
        },
    },
    CraftedMaterials.BLACK_ICE_WALL: {
        BASE_MATERIAL: False,
        INGREDIENTS: {
            BaseMaterials.BLACK_ICE: 8,
            CraftedMaterials.STEEL_REINFORCEMENT: 2,
            CraftedMaterials.INSULATED_WOOD: 3,
        },
    },
    CraftedMaterials.INSULATED_WOOD: {
        BASE_MATERIAL: False,
        INGREDIENTS: {BaseMaterials.DRY_WOOD: 1, BaseMaterials.RESIN: 1},
    },
    CraftedMaterials.IRON_BAR: {
        BASE_MATERIAL: False,
        INGREDIENTS: {BaseMaterials.IRONSTONE: 2},
    },
    CraftedMaterials.IRON_REINFORCEMENT: {
        BASE_MATERIAL: False,
        INGREDIENTS: {CraftedMaterials.IRON_BAR: 2},
    },
    CraftedMaterials.STEEL_BAR: {
        BASE_MATERIAL: False,
        INGREDIENTS: {CraftedMaterials.IRON_BAR: 5, CraftedMaterials.STEELFIRE: 1},
    },
    CraftedMaterials.STEEL_REINFORCEMENT: {
        BASE_MATERIAL: False,
        INGREDIENTS: {
            CraftedMaterials.IRON_REINFORCEMENT: 1,
            CraftedMaterials.STEELFIRE: 1,
        },
    },
    CraftedMaterials.STEELFIRE: {
        BASE_MATERIAL: False,
        INGREDIENTS: {BaseMaterials.TAR: 2, BaseMaterials.BRIMSTONE: 1},
    },
}

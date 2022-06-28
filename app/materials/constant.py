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


INGREDIENTS = "ingredients"
BASE_MATERIAL = "base_material"

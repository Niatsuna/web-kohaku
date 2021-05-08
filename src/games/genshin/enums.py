from enum import Enum

class EnemyType(str, Enum):
    ELEMENTAL       = 'Elemental Lifeforms'
    HILICHURL       = 'Hilichurls'
    ABYSS           = 'Abyss Order'
    FATUI           = 'Fatui'
    AUTOMATON       = 'Automaton'
    HUMAN_FACTION   = 'Human'
    MAGICAL_BEAST   = 'Beasts'
    BOSS            = 'Boss'

class DomainType(str, Enum):
    ABYSS               = 'Spiral Abyss'
    ARTIFACTS           = 'Artifacts'
    STORY_QUEST_EVENT   = 'Story / Quest / Event'
    TALENT_ASCENSION    = 'Talent Level-Up Materials'
    WEAPON_ASCENSION    = 'Weapon Ascension Materials'
    WEEKLY_BOSS         = 'Weekly Boss'

class ItemType(str, Enum):
    GADGET              = 'Gadget'
    WEAPON              = 'Weapon'
    CURRENCY            = 'Currency'
    GLIDERS             = 'Gliders'
    FOOD                = 'Food'
    POTION              = 'Potion'
    INGREDIENTS         = 'Ingredients'
    ASCENSION_JEWELS    = 'Jewels'
    ASCENSION_BOSS      = 'Elemental Stones'
    ASCENSION_COMMON    = 'Common Material'
    ASCENSION_LOCAL     = 'Local Material'
    ASCENSION_TALENT    = 'Talent Level-Up'
    ASCENSION_WEAPON    = 'Weapon Ascension'
    EXP_CHARACTER       = 'Character EXP'
    EXP_WEAPON          = 'Weapon Enhancement'
    EXP_ARTIFACT        = 'Artifact Enhancement'
    BOOK                = 'Lore Book'
    FURNITURE_INDOOR    = 'Indoor Furniture'
    FURNITURE_OUTDOOR   = 'Outdoor Furniture'

class WeaponType(str, Enum):
    BOW        = 'Bow'
    CATALYST   = 'Catalyst'
    CLAYMORE   = 'Claymore'
    POLEARM    = 'Polearm'
    SWORD      = 'Sword'

class VisionType(str, Enum):
    ANEMO   = 'Anemo'
    CRYO    = 'Cryo'
    DENDRO  = 'Dendro'
    ELECTRO = 'Electro'
    GEO     = 'Geo'
    HYDRO   = 'Hydro'
    PYRO    = 'Pyro'

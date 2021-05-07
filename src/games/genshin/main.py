from fastapi import APIRouter, Response,  status
from games.genshin.enums import DomainType, EnemyType, ItemType, WeaponType, VisionType

router = APIRouter()
# ============================================================================= #
# >>> Artifact
@router.get('/api/genshin/artifact', 
    summary='Returns a list of artifacts', 
    tags=['Genshin'])
async def get_artifacts(skip : int = 0, limit : int = 200, min_rarity : int = 0, max_rarity : int = 5):
    '''
    Returns a list of artifacts that are fullfilling the given criteria.

    - **skip** : Skips the first elements to the given index. 
    - **limit** : Maximal amount of results in the list.
    - **min_rarity** : Minimal rarity an artifact must fullfill to be listed in the result (inclusive).
    - **max_rarity** : Maximal rarity an artifact must fullfill to be listed in the result (inclusive).
    '''
    # TODO: Implement!
    pass

@router.get('/api/genshin/artifact/{identifier}',
    summary='Searchs a specific artifact',
    tags=['Genshin'])
async def get_artifact(identifier : int):
    '''
    Returns a identified artifact.

    - **identifier** : Name or id of the artifact set, which should be returned
    '''
    # TODO: Implement!
    pass

# ============================================================================= #
# >>> Build
@router.get('/api/genshin/build',
    summary='Returns a list of builds',
    tags=['Genshin'])
async def get_builds(skip : int = 0, limit : int = 200, character_id : int = -1, character_name : str = ''):
    '''
    Returns a list of builds that are fullfilling the given criteria.

    - **skip** : Skips the first elements to the given index. 
    - **limit** : Maximal amount of results in the list.
    - **character_id** : id of the character. (prioritized)
    - **character_name** : name of the character.
    
    '''
    # TODO: Implement!
    pass

@router.get('/api/genshin/build/{identifier}',
    summary='Searchs a specific build',
    tags=['Genshin'])
async def get_build(identifier : int):
    '''
    Returns a identified build.

    - **identifier** : id of the build, which should be returned
    '''
    # TODO: Implement!
    pass

# ============================================================================= #
# >>> Character
@router.get('/api/genshin/character',
    summary='Returns a list of characters',
    tags=['Genshin'])
async def get_characters(skip : int = 0, limit : int = 200, rarity : int = 0, region : str = '', region_id : int = -1, weapon : WeaponType = None, vision : VisionType = None):
    '''
    Returns a list of characters that are fullfilling the given criteria.

    - **skip** : Skips the first elements to the given index. 
    - **limit** : Maximal amount of results in the list.
    - **rarity** :  Searched rarity. Example: `rarity = 4` return only 4-star units.
    - **region** : Name of the region the character is from.
    - **region_id** : id of the region the character is from (prioritized)
    - **weapon** : type of weapon the character should have
    - **vision** : type of element / vision the character should have
    '''
    # TODO: Implement!
    pass

@router.get('/api/genshin/character/{identifier}',
    summary='Searchs a specific character',
    tags=['Genshin'])
async def get_character(identifier : str):
    '''
    Returns a identified artifact.

    - **identifier** : Name or id of the character, which should be returned
    '''
    # TODO: Implement!
    pass

# ============================================================================= #
# >>> Domain
@router.get('/api/genshin/domain',
    summary='Returns a list of domains',
    tags=['Genshin'])
async def get_domains(skip : int = 0, limit : int = 200, type : DomainType = None):
    '''
    Returns a list of domains that are fullfilling the given criteria.

    - **skip** : Skips the first elements to the given index. 
    - **limit** : Maximal amount of results in the list.
    - **type** : type of domain 
    '''
    # TODO: Implement!
    pass

@router.get('/api/genshin/domain/{identifier}',
    summary='Searchs a specific domain',
    tags=['Genshin'])
async def get_domain(identifier : str):
    '''
    Returns a identified domain.

    - **identifier** : Name or id of the domain, which should be returned
    '''
    # TODO: Implement!
    pass

# ============================================================================= #
# >>> Enemy
@router.get('/api/genshin/mob',
    summary='Returns a list of enemies (mobs)',
    tags=['Genshin'])
async def get_mobs(skip : int = 0, limit : int = 200, type : EnemyType = None):
    '''
    Returns a list of enemies (mobs) that are fullfilling the given criteria.

    - **skip** : Skips the first elements to the given index. 
    - **limit** : Maximal amount of results in the list.
    - **type** : type of enemy
    '''
    # TODO: Implement!
    pass

@router.get('/api/genshin/mob/{identifier}',
    summary='Searchs a specific mob',
    tags=['Genshin'])
async def get_mob(identifier : str):
    '''
    Returns a identified enemy (mob).

    - **identifier** : Name or id of the enemy (mob), which should be returned
    '''
    # TODO: Implement!
    pass

# ============================================================================= #
# >>> Items
@router.get('/api/genshin/item',
    summary='Returns a list of items',
    tags=['Genshin'])
async def get_items(skip : int = 0, limit : int = 200, type : ItemType = None):
    '''
    Returns a list of items that are fullfilling the given criteria.

    - **skip** : Skips the first elements to the given index. 
    - **limit** : Maximal amount of results in the list.
    - **type** : type of item
    '''
    # TODO: Implement!
    pass

@router.get('/api/genshin/item/{identifier}',
    summary='Searchs a specific item',
    tags=['Genshin'])
async def get_item(identifier : str):
    '''
    Returns a identified item.

    - **identifier** : Name or id of the artifact set, which should be returned
    '''
    # TODO: Implement!
    pass

# ============================================================================= #
# >>> Region
@router.get('/api/genshin/region',
    summary='Returns a list of regions',
    tags=['Genshin'])
async def get_regions(skip : int = 0, limit : int = 200, type : VisionType = None):
    '''
    Returns a list of regions that are fullfilling the given criteria.

    - **skip** : Skips the first elements to the given index. 
    - **limit** : Maximal amount of results in the list.
    - **type** : element / vision of the region
    '''
    # TODO: Implement!
    pass

@router.get('/api/genshin/region/{identifier}',
    summary='Searchs a specific region',
    tags=['Genshin'])
async def get_region(identifier : str):
    '''
    Returns a identified region.

    - **identifier** : Name or id of the region, which should be returned
    '''
    # TODO: Implement!
    pass
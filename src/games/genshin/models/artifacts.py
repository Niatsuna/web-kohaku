from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from general import EffectSet

# ============================================================================= #
# >>> Artifacts
class Artifact(Base):
    __tablename__ = 'genshin_artifacts'

    uid = Column(Integer, primary_key=True, index=True)
    #user_id = Column(Integer, ForeignKey('users.uid'))
    rarity = Column(Integer)
    level = Column(Integer)
    artifact_base_uid = Column(Integer, ForeignKey(ArtifactBase.__tablename__ + 'uid'))
    

class ArtifactBase(Base):
    __tablename__ = 'genshin_artifact_bases'

    uid = Column(Integer, primary_key=True, index=True)
    name_en = Column(String)
    name_de = Column(String)
    artifact_type = Column(String)
    description_en = Column(String)
    description_de = Column(String)

    artifact_set_uid = Column(Integer, ForeignKey(ArtifactSet.__tablename__ + 'uid'))

class ArtifactSet(Base):
    __tablename__ = 'genshin_artifact_sets'

    uid = Column(Integer, primary_key=True, index=True)
    name_en = Column(String)
    name_de = Column(String)
    
    first_effect_set_uid = Column(Integer, ForeignKey(EffectSet.__tablename__ + '.uid'))
    second_effect_set_uid = Column(Integer, ForeignKey(EffectSet.__tablename__ + '.uid'))

    min_rarity = Column(Integer)
    max_rarity = Column(Integer)

    description_en = Column(String)
    description_de = Column(String)

    #mob_uid
    #domain_uid
    #shop_uid
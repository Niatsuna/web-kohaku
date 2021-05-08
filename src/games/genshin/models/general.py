from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# ============================================================================= #
# >>> Stats
class Stat(Base):
    __tablename__ = 'genshin_stats'

    uid = Column(Integer, primary_key=True, index=True)
    name_en = Column(String)
    name_de = Column(String)
    attribute_en = Column(String)
    attribute_de = Column(String)

# >>> Images
class Image(Base):
    __tablename__ = 'genshin_images'

    uid = Column(Integer, primary_key=True, index=True)
    path = Column(String)

# >>> Effects
class Effect(Base):
    __tablename__ = 'genshin_effects'

    uid = Column(Integer, primary_key=True, index=True)
    stat_uid = Column(Integer, ForeignKey(Stat.__tablename__ + '.uid'))
    amount = Column(Float)

class EffectSet(Base):
    __tablename__ = 'genshin_effect_sets'

    uid = Column(Integer, primary_key=True, index=True)
    description_en = Column(String)
    description_de = Column(String)
    effect_uids = relationship('Effect')

# ============================================================================= #
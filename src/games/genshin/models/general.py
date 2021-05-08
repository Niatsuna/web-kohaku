from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

# ============================================================================= #
# >>> Stats
class Stat(Base):
    __tablename__ = 'genshin_stats'

    id = Column(Integer, primary_key=True, index=True)
    name_en = Column(String)
    name_de = Column(String)
    attribute_en = Column(String)
    attribute_de = Column(String)

# >>> Images
class Image(Base):
    __tablename__ = 'genshin_images'

    id = Colum(Integer, primary_key=True, index=True)
    path = Column(String)
# ============================================================================= #
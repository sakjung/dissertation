from sqlalchemy import *

engine = create_engine('sqlite:///appstore.db', echo=True)
# Base = declarative_base()

metadata = MetaData()
reviews_table = Table('reviews', metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('username', String),
        Column('date', DateTime),
        Column('rating', Float),
        Column('origin', SMALLINT),
        Column('review', Text)
        )

metadata.create_all(engine)

engine.dispose()

# class Reviews(Base):
#     __tablename__ = "reviews"
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     review = Column(Text)
#     rating = Column(Float)
#     review_date = Column(DateTime)
#     # Apple app store = 0 / Google play store = 1
#     origin = Column(SMALLINT)
#
# Reviews.__table__.create(bind=engine, checkfirst=True)

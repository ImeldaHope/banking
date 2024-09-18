from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base


convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

# engine = create_engine('sqlite:///:memory:')
# Base.metadata.create_all(engine)

# # use our engine to configure a 'Session' class
# Session = sessionmaker(bind=engine)
# # use 'Session' class to create 'session' object
# session = Session()
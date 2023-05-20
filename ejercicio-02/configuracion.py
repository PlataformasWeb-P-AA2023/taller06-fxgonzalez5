from sqlalchemy import create_engine
# sqlite
# engine = create_engine('sqlite:///data.db', echo=True)

# postgres
engine = create_engine("postgresql+psycopg2://frantgod:07102002@localhost:5432/data", echo=True)



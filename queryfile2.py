from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, list_keywords, List, ListKeyword, HeadingItem
from database_setup import Row, ShortTextEntry, LongTextEntry, DateEntry, DateTimeEntry 
from database_setup import Bools, TimeEntry, Duration, TwoDecimal, LargeDecimal

engine = create_engine('postgresql+psycopg2://catalog:db-password@localhost/supalist1')
Base.metadata.bind = engine 
DBSession = sessionmaker(bind = engine)
session = DBSession()

session.rollback()

print "now, its rolled back?"
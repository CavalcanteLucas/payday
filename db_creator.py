from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

engine=create_engine('sqlite:///payday.db', echo=True)
Base=declarative_base()


class Reservation(Base):
	__tablename__ = "reservations"

	id = Column(Integer, primary_key = True)
	room = Column(String)
	checkin = Column(Date)
	checkout = Column(Date)
	value = Column(Float)
	client = Column(String)

	def __repr__(self):
		return "{}, {}, {}, {}, {}".format(str(self.room), 
										   str(self.checkin), 
										   str(self.checkout), 
										   str(self.value), 
										   str(self.client))

class Spend(Base):
	__tablename__ = "spends"

	id = Column(Integer, primary_key = True)
	date = Column(Date)
	value = Column(Float)
	item = Column(String)

	def __repr__(self):
		return "{}, {}, {}".format(self.date,
								   self.value, 
								   self.item)

Base.metadata.create_all(engine)
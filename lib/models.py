from sqlalchemy import Column, Integer, String, VARCHAR, INT, FLOAT, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

Base = declarative_base()

#defining baristas schema
class Baristas (Base):
    __tablename__ = 'baristas'

    barista_id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(40))
    last_name = Column(VARCHAR(40))
    meal_served = Column(VARCHAR(40))
    age = Column(INT)
    meals_served = relationship('Meal_cards', backref= 'meal_card')

    def __repr__(self):
        return f"<Baristas; {self.first_name}>"
    
class Meal_cards (Base):
    __tablename__ = 'meal_cards'

    meal_id = Column(Integer, primary_key=True)
    meal_served = Column(VARCHAR(40))
    specifications = Column(VARCHAR(40))
    satisfaction_rank = Column(INT)
    comments = Column(VARCHAR(40))
    barista_id = Column(Integer,ForeignKey('baristas.barista_id'))
    

    def __repr__(self):
        return f"<Meal_cards:{self.meal_id}{self.meal_served}>"
        


engine = create_engine('sqlite:///parlor.db')

Session = sessionmaker(bind = engine)

session = Session()

#Base.metadata.create_all (bind = engine)

#Creating an instance of baristas

#barista1 = Baristas(barista_id = 1, first_name =  'Vincent', last_name = 'Irungu', meal_served = 'hamburger', age = 25 )

#session.add(barista1 )
#session.commit()

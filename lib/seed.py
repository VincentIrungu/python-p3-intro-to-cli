from models import Baristas, Meal_cards, session

'''data = [{
  "barista_id": 1,
  "first_name": "Vincent",
  "last_name": "Irungu",
  "meal_served": "soft drink",
  "age": 1
}, {
  "barista_id": 2,
  "first_name": "Gordan",
  "last_name": "Schneidar",
  "meal_served": "taco",
  "age": 2
}, {
  "barista_id": 3,
  "first_name": "Evonne",
  "last_name": "Carlill",
  "meal_served": "pizza",
  "age": 3
}, {
  "barista_id": 4,
  "first_name": "Georgie",
  "last_name": "Clover",
  "meal_served": "hamburger",
  "age": 4
}, {
  "barista_id": 5,
  "first_name": "Curtis",
  "last_name": "Brehault",
  "meal_served": "burrito",
  "age": 5
}, {
  "barista_id": 6,
  "first_name": "Cchaddie",
  "last_name": "Manners",
  "meal_served": "chicken nuggets",
  "age": 6
}, {
  "barista_id": 7,
  "first_name": "Willi",
  "last_name": "Mergue",
  "meal_served": "soft drink",
  "age": 7
}, {
  "barista_id": 8,
  "first_name": "Moss",
  "last_name": "Cayton",
  "meal_served": "soft drink",
  "age": 8
}, {
  "barista_id": 9,
  "first_name": "Wilone",
  "last_name": "Rosina",
  "meal_served": "french fries",
  "age": 9
}]

baristas =[]

for datum in data:
    bsta = Baristas (**datum)
    baristas.append(bsta)

session. add_all(baristas)
session.commit()
print("Done seeding baristas data!!!")
# output Done seeding baristas data!!!'''

data = [{
  "meal_id": 1,
  "meal_served": "chicken nuggets",
  "specifications": "Vegan burger",
  "satisfaction_rank": 2.6,
  "comments": "Mouthwatering",
  "barista_id": 5
}, {
  "meal_id": 2,
  "meal_served": "milkshake",
  "specifications": "Paleo-friendly entree",
  "satisfaction_rank": 2.5,
  "comments": "Crunchy",
  "barista_id": 3
}, {
  "meal_id": 3,
  "meal_served": "chicken nuggets",
  "specifications": "Low-sodium soup",
  "satisfaction_rank": 2.2,
  "comments": "Satisfying",
  "barista_id": 8
}, {
  "meal_id": 4,
  "meal_served": "soda",
  "specifications": "Dairy-free smoothie",
  "satisfaction_rank": 1.8,
  "comments": "Crunchy",
  "barista_id": 5
}, {
  "meal_id": 5,
  "meal_served": "soda",
  "specifications": "Dairy-free smoothie",
  "satisfaction_rank": 1.6,
  "comments": "Satisfying",
  "barista_id": 4
}, {
  "meal_id": 6,
  "meal_served": "french fries",
  "specifications": "Sugar-free dessert",
  "satisfaction_rank": 4.1,
  "comments": "Satisfying",
  "barista_id": 7
}, {
  "meal_id": 7,
  "meal_served": "burrito",
  "specifications": "Gluten-free pizza",
  "satisfaction_rank": 4.5,
  "comments": "Filling",
  "barista_id": 10
}, {
  "meal_id": 8,
  "meal_served": "taco",
  "specifications": "Sugar-free dessert",
  "satisfaction_rank": 4.5,
  "comments": "Yummy",
  "barista_id": 7
}, {
  "meal_id": 9,
  "meal_served": "taco",
  "specifications": "Sugar-free dessert",
  "satisfaction_rank": 1.9,
  "comments": "Crunchy",
  "barista_id": 7
}]


meal_cards =[]

for datum in data:
    mlcrd = Meal_cards (**datum)
    meal_cards.append(mlcrd)

session. add_all(meal_cards)
session.commit()
print("Done seeding meal_cards data!!!")
# output Done seeding baristas data!!!'''

'''meal_card = [Meal_cards(**meal)for meal in meals]

session.add_all(meal_card)

session.commit()
print("Done seeding meal_cards data")'''


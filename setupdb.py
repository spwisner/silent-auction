from app import db
from models import Auction, User, AuctionItem

# # creates all the tables
# db.create_all()

# Seeds

## Auction
auction1 = Auction(name='American Cancer Society')

## User
user1 = User('Steve', 'Wisner', 'spwisner@test.com')

auctionItem1 = AuctionItem(name='Vase')

# # Seeds
# item1 = Bid('Coaster', 5)
# item2 = Bid('Feeder', 14)

# print(item1.id)
# print(item2.id)

db.session.add_all([auction1, auctionItem1, user1])
# # db.session.add() --> Can use if want to add only 1

# # saves to db
db.session.commit()

# print(item1.id)
# print(item2.id)
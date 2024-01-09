from silentauction import db
from silentauction.models import Auction, User, AuctionItem

vase_desc = "The centerpiece of the upcoming auction is an exquisite vase that captures the essence of timeless elegance and artistic craftsmanship. This remarkable piece, poised to allure discerning collectors and enthusiasts alike, stands as a testament to the mastery of its creator. Crafted with meticulous precision, the vase seamlessly blends classical aesthetics with contemporary sensibilities, making it a rare gem in the realm of decorative art. Fashioned from the finest porcelain, the vase boasts a delicate yet durable form that gracefully curves upward, creating a silhouette reminiscent of classical Grecian urns. Its surface is adorned with intricate hand-painted patterns, each stroke revealing the artisan's dedication to detail. The color palette, a harmonious fusion of soft pastels and rich metallic accents, enhances the vase's allure, adding depth and sophistication to its overall appearance. What sets this vase apart is its unique blend of tradition and innovation. While its design pays homage to historical art movements, the vase incorporates modern elements, making it a versatile and captivating addition to any collection. The artist's signature, discreetly inscribed on the base, further adds to the provenance and exclusivity of this exceptional piece."

def runSeeds():
    user1 = User('Steve', 'Wisner', 'test@test.com', 'testUser1', 'test1234!')
    auction1 = Auction(name='American Cancer Society')
    
    
    db.session.add_all([
        user1,
        auction1,
    ])
    db.session.commit()
    auction_item1 = AuctionItem(name='Vase', auction_id=auction1.id, description=vase_desc)
    db.session.add_all([
        auction_item1
    ])
    db.session.commit()

# # creates all the tables
# db.create_all()

# Seeds

## Auction
# auction1 = Auction(name='American Cancer Society')

## User
# user1 = User('Steve', 'Wisner', 'test@test.com', 'testUser1', 'test1234!')

# auctionItem1 = AuctionItem(name='Vase')

# # Seeds
# item1 = Bid('Coaster', 5)
# item2 = Bid('Feeder', 14)

# print(item1.id)
# print(item2.id)

# db.session.add_all([
#     # auction1, 
#     # auctionItem1, 
#     user1
# ])
# # db.session.add() --> Can use if want to add only 1

# # saves to db
# db.session.commit()

# print(item1.id)
# print(item2.id)
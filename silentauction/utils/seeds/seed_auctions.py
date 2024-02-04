
from silentauction import db
from silentauction.models import Auction, AuctionItem, Photo
import stripe
from silentauction.utils.seeds.config import get_seed_config

def seed_auctions(should_reset_stripe=False):
    config = get_seed_config()
    
    # seed auctions
    auctions = config.get('auctions')
    for auction in auctions:
        new_auction = Auction(
            auction['name'],
            auction['category'],
            auction['description']
        )
        db.session.add(new_auction)
        db.session.commit()
        print(f"Seeded Auction: {new_auction.id} - {new_auction.name}")

        # seed auction items
        auction_items = auction.get('auction_items') or []
        for auction_item in auction_items:
            new_auction_item = AuctionItem(
                auction_item['name'],
                new_auction.id,
                auction_item['description'],
                auction_item['starting_bid'],
                auction_item['bid_interval'],
                auction_item.get('auction_start', None),
                auction_item.get('auction_end', None),
            )
            db.session.add(new_auction_item)
            db.session.commit()
            print(f"Seeded Item: {new_auction_item.id} - {new_auction_item.name}")

            if should_reset_stripe:
                # seed stripe product
                print("Seed stripe product for auction item")
                created_product = stripe.Product.create(
                    name=f"Auction Item #{new_auction_item.id}: {new_auction_item.name}",
                    description=new_auction_item.description,
                )
                new_auction_item.stripe_product_id = created_product['id']
                db.session.commit()
                print(f"Seeded Stripe Product: {new_auction_item.stripe_product_id}")

            # seed auction item photos
            item_photos = auction_item.get('photos', [])
            for item_photo in item_photos:
                new_photo = Photo(
                    item_photo.get('filename', None),
                    item_photo.get('category', None),
                    item_photo.get('subcategory', None),
                    item_photo.get('caption', None),
                    None,
                    new_auction_item.id
                )
                db.session.add(new_photo)
                db.session.commit()
                print(f"Seeded Item: {new_photo.id} - {new_photo.filename}")
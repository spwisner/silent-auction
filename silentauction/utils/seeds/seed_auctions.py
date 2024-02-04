
from silentauction import db
from silentauction.models import Auction, AuctionItem, Photo, Bid
import stripe
from silentauction.utils.seeds.config import get_seed_config
from silentauction.utils.seeds.seed_users import lookup_user_by_ref_id

def seed_auctions(should_reset_stripe=False, users=[]):
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

            ## seeds bids
            bids = auction_item.get('bids', [])
            print(bids)
            if len(bids) > 0:
                for bid in bids:
                    target_user = lookup_user_by_ref_id(users, bid['user_ref_id'])
                    new_bid = Bid(
                        bid['amount'],
                        new_auction_item.id,
                        target_user.id,
                    )
                    db.session.add(new_bid)
                    db.session.commit()
                    print(f"Seeded Bid: {new_bid.id} - {new_bid.amount}")

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
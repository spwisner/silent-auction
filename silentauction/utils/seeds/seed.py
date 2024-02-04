from silentauction import db
from silentauction.utils.seeds.seed_users import seed_users
from silentauction.utils.seeds.seed_auctions import seed_auctions

def run_seeds(should_reset_stripe=False):
    db.create_all()
    users = seed_users()
    print(f"Seeded {len(users)} users.")
    seed_auctions(should_reset_stripe, users)
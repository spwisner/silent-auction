from silentauction import db
from silentauction.models import User
from silentauction.utils.seeds.config import get_seed_config

def seed_users(): 
    config = get_seed_config()
    users = config.get('users', [])

    for user in users:
        newUser = User(
            user['first_name'],
            user['last_name'],
            user['email'],
            user['username'],
            user['password']
        )
        db.session.add(newUser)
        db.session.commit()
        print(f"Seeded User: {newUser.id} - {newUser.username}")
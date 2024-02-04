from silentauction import db
from silentauction.models import User
from silentauction.utils.seeds.config import get_seed_config

def lookup_user_by_ref_id(users, ref_id):
    config = get_seed_config()
    config_users = config.get('users', [])
    target_config_user = list(filter(lambda user: user['ref_id'] == ref_id, config_users))
    if len(target_config_user) == 0:
        return None
    
    target_config_user = target_config_user[0]
    target_config_user_email = target_config_user.get('email', None)

    for user in users:
        if user.email == target_config_user_email:
            return user
    return None

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
    return User.query.all()
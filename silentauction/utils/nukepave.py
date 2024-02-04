from silentauction.utils.clean_db import clean_db
from silentauction.utils.seeds.seed import run_seeds

def nuke_pave(should_reset_stripe=False):
    print('Deleting all data')
    clean_db()
    print("Successfully deleted all data")
    print('Seeding all data')
    run_seeds(should_reset_stripe)
    print('Seeds complete')

if __name__ == '__main__':
    nuke_pave()

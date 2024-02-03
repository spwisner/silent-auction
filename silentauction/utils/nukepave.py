from silentauction.utils.clean_db import clean_db
from silentauction.utils.seed import runSeeds

def nuke_pave():
    print('Deleting all data')
    clean_db()
    print("Successfully deleted all data")
    print('Seeding all data')
    runSeeds()
    print('Seeds complete')

if __name__ == '__main__':
    nuke_pave()

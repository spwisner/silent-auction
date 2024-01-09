from clean_db import clean_db
from seed import runSeeds

print('Deleting all data')
clean_db()
print("Successfully deleted all data")
print('Seeding all data')
runSeeds()
print('Seeds complete')


from clear_db import clear_db
from seed import runSeeds

print('Deleting all data')
clear_db()
print("Successfully deleted all data")
print('Seeding all data')
runSeeds()
print('Seeds complete')


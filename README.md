# Silent Auction

Silent auction is a demo Python Flask app where charities can post items for a silent auction and members can bid.

## Getting Stared

## Database

### Initial startup
1. Create the db tables
    - `python setupdb.py`
    - via docker `docker compose exec silent-auction python setupdb.py`
1. Set up the migrations directory
    - `flask db init` Sets up the migrations director
    - via docker: `docker compose exec silent-auction flask db init`

### Create Migration
1. Create migration file
    - `flask db migrate -m "some message"` Sets up the migration file
    - via docker `docker compose exec silent-auction flask db migrate -m "some message"`
1. Update the DB with the migration
    - `flask db upgrade` Updates the DB with the migration
        - via docker `docker compose exec silent-auction flask db upgrade`
1. Removing migration
    1. Delete migration file
    1. Run `docker compose exec silent-auction flask db stamp head` to mark the current migration level
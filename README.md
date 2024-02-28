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

#### Seeds
1. Run `docker compose exec silent-auction python nukepave.py`

### Payment

To demo the payment feature, view http://localhost:5001/payments/1 and use the following test payment values:
- Card Number: `4242 4242 4242 4242`
- Exp: `12/34`
- CVC: `123`

### API
You can reset the demo application remotely with a call to the REST API:

POST http://localhost:5001/api/demo-reset
HEADERS:
```
{
    Authorization: "<SERVER_TOKEN_ENV_VAR_VALUE>"
}
```
PAYLOAD: 
```
{
    should_reset_stripe: boolean
}
```
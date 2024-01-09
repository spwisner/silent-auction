from silentauction import db
from silentauction.models import Auction, User, Bid, AuctionItem

def delete_all_rows(Model):
    try:
        # Use the delete method to create a delete statement for the table
        db.session.query(Model).delete()
        
        # Commit the changes to the database
        db.session.commit()
        
        return "All rows deleted successfully"
    except Exception as e:
        # Handle exceptions if any
        db.session.rollback()
        return f"Error: {str(e)}"


def clear_db():
    delete_all_rows(User)  
    delete_all_rows(Auction)  
    delete_all_rows(Bid)  
    delete_all_rows(AuctionItem)

if __name__ == '__main__':
    print('Running clear_db')
    clear_db()
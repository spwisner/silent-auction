from datetime import datetime, timedelta, timezone

def default_auction_end(): 
    return now_plus_days_datetime(90)

def now_plus_days_datetime(days=0, hours=0, minutes=0, seconds=0):
    return (datetime.utcnow() + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds))

def convert_to_readable_datetime(timestamp):
    local_datetime = timestamp.replace(tzinfo=timezone.utc).astimezone(tz=None)
    formatted_string = local_datetime.strftime("%m/%d/%y %I:%M%p")
    # Convert UTC datetime to a readable string
    return formatted_string
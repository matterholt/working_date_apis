from datetime import datetime, timedelta


def validate_date(date_text: str):
    """
    Validate a date string in the format 'YYYY-MM-DD'.
    Returns a datetime object if the date is valid, False otherwise.
    """
    try:
        parsed_date = datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return False
    return parsed_date




from datetime import datetime, timedelta



def calculate_gestation_date(data, reference_date):
    """Calculate the gestation date based on the state and days to."""
    state = data['event_state']
    days_to = data['daysTo']

    if state == 'present':
        return reference_date

    if state == 'pre':
        return reference_date - timedelta(days=days_to)
    elif state == 'post':
        return reference_date + timedelta(days=days_to)
    else:
        raise ValueError("Invalid lambing state.")



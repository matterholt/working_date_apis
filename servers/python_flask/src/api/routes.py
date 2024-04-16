from flask import Flask
from flask import request
from src.api import bp
from flask import jsonify
# make it better 
from src.utils.validate_date import validate_date
from src.utils.calculate_date_gestation import calculate_gestation_date 

# import validate_date from the utils file



# TODO: 'lambingState'-> change key, should be more generic in DB, allowing the to be more diverse  

temp_data_points =[
    {"event":'breed ewes', "daysTo": 146 , "event_state":'pre'},
    {"event":'remove ram', "daysTo": 134 , "event_state":'pre'},
    {"event":'start late gestation rotation', "daysTo": 44 , "event_state":'pre'},
    {"event":"lambing", "daysTo": 0 , "event_state":'present'},
    {"event":"start lambs on creep","daysTo":11 , "event_state":'post'},
    {"event":"wean lambs", "daysTo": 53 , "event_state":'post'},
    {"event":"sell culls", "daysTo": 69 , "event_state":'post'},
    {"event":"replacement ewes", "daysTo": 101 , "event_state":'post'},
]



@bp.route("/")
def show():
    return "<p>from the gestation selections</p>"



@bp.route("/sheep/gestation")
def sheep_gestation():
    incoming_event = request.args.get('event')
    chosen_date =  validate_date(request.args.get('date'))

    # want to take temp_date_points and only have an array of events
    event_list = [x['event'] for x in temp_data_points]

    if incoming_event is None or incoming_event not in event_list:
        return f'add url param = {event_list}'

    if chosen_date is None or not chosen_date:
        return 'define a date = YYYY-MM-DD'
    
    events_with_dates = []

    for db_item in temp_data_points:
        calculated_date = calculate_gestation_date(db_item, chosen_date)
        events_with_dates.append({ "event":db_item['event'], 'event_state': db_item['event_state'], 'date': calculated_date.strftime("%Y-%m-%d")})


    return jsonify({"data": events_with_dates})
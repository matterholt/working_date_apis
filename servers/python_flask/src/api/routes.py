from flask import Flask
from flask import request
from src.api import bp
import json
import src.utils.validate_date as utils

# TODO: 'lambingState'-> change key, should be more generic in DB, allowing the to be more diverse  

temp_data_points =[
    {"event":'breed ewes', "daysTo": 146 , "lambingState":'pre'},
    {"event":'remove ram', "daysTo": 134 , "lambingState":'pre'},
    {"event":'start late gestation rotation', "daysTo": 44 , "lambingState":'pre'},
    {"event":"lambing", "daysTo": 0 , "lambingState":'present'},
    {"event":"start lambs on creep","daysTo":11 , "lambingState":'post'},
    {"event":"wean lambs", "daysTo": 53 , "lambingState":'post'},
    {"event":"sell culls", "daysTo": 69 , "lambingState":'post'},
    {"event":"replacement ewes", "daysTo": 101 , "lambingState":'post'},
]


def calculate_dates_of_gestation():
    pass
    



@bp.route("/")
def show():
    return "<p>from the gestation selections</p>"



@bp.route("/sheep/gestation")
def sheep_gestation():
    incoming_event = request.args.get('event')
    chosen_date = request.args.get('date')
    
    # want to take temp_date_points and only have an array of events
    event_list = [x['event'] for x in temp_data_points]


    if incoming_event is None or incoming_event not in event_list:
        return f'add url param = {event_list}'

    if chosen_date is None or not utils.validate_date(chosen_date):
        return 'choose a "date" = "YYYY-MM-DD"'

    print("time to calculate gestation")

    return f'{incoming_event} chosen date {chosen_date}'
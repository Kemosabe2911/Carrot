from db import InsertEventSchedule
from datetime import datetime, timedelta
import re
import dateutil.parser

def CreateEventSchedule(name, type, desc, completed_at):
    reminded_at = convert_iso_to_datetime(completed_at) - timedelta(minutes=5)
    if len(name) < 1:
        print("error: specify event name")
        return False

    InsertEventSchedule(
        name= name,
        desc= desc,
        type = type,
        completed_at= convert_iso_to_datetime(completed_at),
        reminded_at= reminded_at,
    )


def convert_to_datetime(date_string):
    # Extract the date and time parts
    date_time_parts = re.search(r'(\w{3} \w{3} \d{2} \d{4} \d{2}:\d{2}:\d{2}) GMT([+-]\d{4})', date_string)
    date_part = date_time_parts.group(1)
    time_zone_offset = date_time_parts.group(2)

    # Convert to datetime object
    dt_object = datetime.strptime(date_part, '%a %b %d %Y %H:%M:%S')

    # # Adjust for the time zone offset
    # delta = timedelta(minutes=int(time_zone_offset[1:3]) * 60 + int(time_zone_offset[3:]))
    # if time_zone_offset[0] == '-':
    #     dt_object -= delta
    # else:
    #     dt_object += delta

    print(dt_object)
    return dt_object

def convert_iso_to_datetime(date_string):
    # Convert to datetime object
    # dt_object = datetime.fromisoformat(date_string.replace("Z", "+00:00"))

    # print(dt_object)
    # return dt_object
    date_string = date_string.replace('(India Standard Time)', '').strip()
    date_time = dateutil.parser.parse(date_string)
    return date_time

"""This file contains the Status class that analyzes open projects, members and meetings data in order to 
provide topline information on the dashboard"""
# Contributions: apaderno at https://stackoverflow.com/questions/1937622/convert-date-to-datetime-in-python/1937636 for converting
#                a date value to datetime in function confirm_meeting

from datetime import date
from datetime import datetime
import sqlparse

class Status:
    """Represents the view from the dashboard page."""

    def __init__(self, data) -> None:
        """
        Initializes the Status class that holds all the open projects for 
        the dashboard view.
        """
        self._data = data

    def test_data(self):
        print(self._data)

def confirm_meeting(meetings):
    """
    This is a helper method to clear which meetings have passed
    """
    upcoming_meetings = []
    date_now = datetime.now()   # Get today's date
    for meeting in meetings:
        converted_date = datetime.combine(meeting.date, datetime.min.time())    # Convert date to datetime
        if (converted_date > date_now):     # Check if the meeting time has passed
            upcoming_meetings.append(meeting)
    return upcoming_meetings
"""This file contains the Status class that analyzes open projects, members and meetings data in order to 
provide topline information on the dashboard"""

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

def confirm_meeting(meetings, today):
    """
    This is a helper method to clear which meetings have passed
    """
    upcoming_meetings = []
    for meeting in meetings:
        print(today)
        upcoming_meetings.append(meeting)
    return upcoming_meetings
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

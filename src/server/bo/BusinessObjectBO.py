from abc import ABC
from datetime import datetime

"""
Gemeinsame Basisklasse aller relevanten Klassen in diesem Projekt.
Jedes BusinessObject besitzt eine festgelegte ID und ein Erstellungsdatum.

"""


class BusinessObject(ABC):
    def __init__(self):
        self._id = 0
        self._timestamp = datetime.now()

    def get_id(self):
        """auslesen der ID"""
        return self._id

    def set_id(self, id):
        """setzen der ID"""
        self._id = id

    def get_timestamp(self):
        """auslesen des Zeitstempels der letzten Aenderung"""
        return self._timestamp

    def set_timestamp(self, timestamp):
        """setzen des Zeitstempels der letzten Aenderung"""
        self._timestamp = timestamp

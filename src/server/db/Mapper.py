import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Mapper(AbstractContextManager, ABC):
    """Abstrakte Basisklasse aller Mapper-Klassen"""

    def __init__(self):
        self._cnx = None

    def __enter__(self):
        """dunder Method - Was soll geschehen, wenn wir beginnen, mit dem Mapper zu arbeiten?"""

        """Wir testen, ob der Code im Kontext der lokalen Entwicklungsumgebung oder in der Cloud ausgeführt wird.
        Dies ist erforderlich, da die Modalitäten für den Verbindungsaufbau mit der Datenbank kontextabhängig sind."""

        if os.getenv("GAE_ENV", "").startswith("standard"):
            """Landen wir in diesem Zweig, so haben wir festgestellt, dass der Code in der Cloud abläuft.
            Die App befindet sich somit im **Production Mode** und zwar im *Standard Environment*.
            Hierbei handelt es sich also um die Verbindung zwischen Google App Engine und Cloud SQL."""

            self._cnx = connector.connect(
                user="root",
                password="Datingtastic1!", ### Passwort an Gruppe weiterleiten
                unix_socket='/cloudsql/datingappss23-390607:europe-west3:datingapp', ### anpassen
                database="datingapp", ### Eingabeschluessel an Gruppe weiterleiten
            )
        else:
            """Wenn wir hier ankommen, dann handelt sich offenbar um die Ausführung des Codes in einer lokalen Umgebung,
            also auf einem Local Development Server. Hierbei stellen wir eine einfache Verbindung zu einer lokal
            installierten mySQL-Datenbank her."""

            self._cnx = connector.connect(
                user="root",
                password= os.environ.get("DB_PW"),
                host= os.environ.get("DB_HOST"),
                database="datingapp",
            )

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Was soll geschehen, wenn wir (evtl. vorübergehend) aufhören, mit dem Mapper zu arbeiten?"""
        self._cnx.close()

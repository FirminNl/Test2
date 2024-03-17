from server.bo.BusinessObjectBO import BusinessObject

"""
Klasse Nutzerprofil mit einfachen Methoden zum Setzen der Klassenvariablen

"""


class UserProfile(BusinessObject):
    """Klasse Nutzerprofil"""

    def __init__(self):
        super().__init__()
        self._google_user_id = 0
        self._email = ""
        self._firstname = ""
        self._surname = ""
        self._about_me = ""

    def set_google_user_id(self, google_user_id):
        """setzen google user id"""
        self._google_user_id = google_user_id

    def get_google_user_id(self):
        """auslesen the google_user_id"""
        return self._google_user_id

    def set_email(self, email):
        """setzen der email"""
        self._email = email

    def get_email(self):
        """auslesen the email"""
        return self._email

    def set_firstname(self, firstname):
        """setzen Vorname"""
        self._firstname = firstname

    def get_firstname(self):
        """auslesen Vorname"""
        return self._firstname

    def set_surname(self, surname):
        """setzen Nachname"""
        self._surname = surname

    def get_surname(self):
        """auslesen Nachname"""
        return self._surname

    def set_about_me(self, about_me):
        """setzen der Profilbeschreibung"""
        self._about_me = about_me

    def get_about_me(self):
        """auslesen the Profilbeschreibung"""
        return self._about_me

    def __str__(self):
        """Erzeugen einer einfachen textuellen Darstellung der jeweiligen Instanz."""
        return "UserProfile: {}, {}, {}, {}, {}, {}, {}".format(
            self.get_id(),
            self.get_timestamp(),
            self.get_google_user_id(),
            self.get_email(),
            self.get_firstname(),
            self.get_surname(),
            self.get_about_me()
        )

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Nutzerprofil()."""
        obj = UserProfile()
        obj.set_id(dictionary["id"])
        obj.set_timestamp(dictionary["timestamp"])
        obj.set_google_user_id(dictionary["google_user_id"])
        obj.set_email(dictionary["email"])
        obj.set_firstname(dictionary["firstname"])
        obj.set_surname(dictionary["surname"])
        obj.set_about_me(dictionary["about_me"])
        return obj




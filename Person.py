class Person(object):
    """A person's details representation"""
    GENDER_OPTIONS = ("m", "M", "f", "F")

    def __init__(self, user_id, first_name, last_name, email, active,
                 address, city="", state="", country="", zip_code="",
                phone_number=None, timezone="", gender=""):

        if gender not in self.GENDER_OPTIONS:
            raise ValueError

        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.active = active
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.timezone = timezone
        self.gender = gender
class Circus:

    circus_name = "Lion"

    def __init__(self, number_of_places_for_viewers=0, number_of_performances_in_year=0, location="NoLocation",
                 ticket_price=0, time_event_start="NoTime", time_event_end="NoTime"):
        self._number_of_places_for_viewers = number_of_places_for_viewers
        self._number_of_performance_in_year = number_of_performances_in_year
        self._location = location
        self._ticket_price = ticket_price
        self._time_event_start = time_event_start
        self._time_event_end = time_event_end

    def __del__(self):
        print("I deleted - ", self._number_of_places_for_viewers)

    def __str__(self):
        return self._number_of_places_for_viewers + ", " + str(self._number_of_performance_in_year) + ", " + str(self._location) + ", " + str(self._ticket_price) + ", " + str(self._time_event_start) + ", " + str(self._time_event_end) + "."

    @staticmethod
    def circus_name_function():
        return Circus.circus_name


def main():
    opened_circus = (250, 100, "Chornovola 14, Budapesht", 150, "16:00", "19:00")
    closed_circus = (220, 125, "Borodina 16, Singapur", 170, "12:00", "15:00")
    circus_on_the_water = (300, 100, "Levitckiy Square, Minsk", 125, "18:00", "21:00")
    print(str(opened_circus))
    print(str(closed_circus))
    print(str(circus_on_the_water))
    print(Circus.circus_name)


main()











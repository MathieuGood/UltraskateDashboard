import json

from src.models.Athlete import Athlete
from src.models.Event import Event
from src.models.Track import Track
from src.models.TrackOption import TrackOption
from src.registries.AthleteRegistry import AthleteRegistry
from src.registries.EventRegistry import EventRegistry
from src.use_cases.Performance import Performance
from src.utils.JsonUtils import JsonUtils


class EventManager:

    @classmethod
    def create_new_event(cls, event_data):
        """
        This class method takes a JSON string and converts it into a Python dictionary.

        Args:
            event_data (str): A JSON string representing event data.

        Returns:
            dict: A Python dictionary representing the event data.
        """
        # Event data is a json that needs to be converted to dictionary
        event_data = json.loads(event_data)
        return event_data

    @classmethod
    def parse_json_events(cls, json_file):
        """
        This class method takes a file path to a JSON file, reads the file,
         and converts its content into a Python dictionary.

        Args:
            json_file (str): The file path to a JSON file.

        Returns:
            dict: A Python dictionary representing the content of the JSON file.
        """
        events_dict = JsonUtils.parse_json_to_dic(json_file)

        for event_date, event_content in events_dict.items():
            track = cls.get_track_from_event_date(event_date)
            event_instance = Event(event_date, track)

            for athlete in event_content:
                athlete_instance = Athlete(
                    name=athlete["info"]["name"],
                    gender=athlete["info"]["gender"],
                    city=athlete["info"]["city"],
                )
                AthleteRegistry.add_athlete(athlete_instance)
                performance_instance = Performance(athlete_instance.id, athlete["performance"], athlete["info"]["age"])
                event_instance.performances.append(performance_instance)

                print(
                    athlete_instance.id,
                    athlete_instance.name,
                    athlete_instance.gender,
                    athlete_instance.city,
                )
            EventRegistry.add_event(event_instance)
        print("Parsed JSON data from", EventRegistry.events.__len__(), " Ultraskates")

    @classmethod
    def get_track_from_event_date(cls, event_date: str) -> Track:
        """
        This class method determines the track based on the month of the event.

        Args:
            event_date (str): The date of the event in the format 'YYYY-MM-DD'.

        Returns:
            Track: An instance of the Track class representing the track for the event.
        """
        event_month = int(event_date[5:7])
        if 0 < event_month < 3:
            track_option = TrackOption.MIAMI
        else:
            track_option = TrackOption.SPAARNDAM
        return Track(track_option)

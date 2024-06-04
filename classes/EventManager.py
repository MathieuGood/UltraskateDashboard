import json
from classes.Event import Event
from classes.Athlete import Athlete
from classes.Performance import Performance
from classes.Utils import Utils
from classes.Track import *
from classes.AthleteRegistry import AthleteRegistry
from classes.EventRegistry import EventRegistry


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

        # Open file and turn it into a dictionary
        events_dict = Utils.parse_json_to_dic(json_file)

        for event_date, event_content in events_dict.items():

            event_month = int(event_date[5:7])
            if 0 < event_month < 3:
                track_option = TrackOption.MIAMI
            else:
                track_option = TrackOption.SPAARNDAM

            track = Utils.get_track_from_location(track_option)
            # Create new Event instance
            event_instance = Event(event_date, track)

            for athlete in event_content:
                # Create new Athlete instance
                athlete_instance = Athlete(
                    name=athlete["info"]["name"],
                    gender=athlete["info"]["gender"],
                    city=athlete["info"]["city"],
                )

                AthleteRegistry.add_athlete(athlete_instance)

                # Create new Performance and add it to Event instance
                performance_instance = Performance(
                    athlete_instance.id, athlete["performance"]
                )
                event_instance.performances.append(performance_instance)

                # print(
                #     athlete_instance.id,
                #     athlete_instance.name,
                #     athlete_instance.gender,
                #     athlete_instance.city,
                # )
                # print(athlete["info"])
                # print(athlete["performance"])
                # print("---------\n")
            EventRegistry.add_event(event_instance)
        print("Parsed JSON data from", EventRegistry.events.__len__(), " Ultraskates")

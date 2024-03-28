import json
from classes.Event import Event
from classes.Athlete import Athlete
from classes.Performance import Performance
from classes.Utils import Utils


class EventManager:

    @classmethod
    def create_new_event(cls, event_data):

        # Event data is a json that needs to be converted to dicitaonary
        event_data = json.loads(event_data)
        return event_data

    @classmethod
    def parse_json_events(cls, json_file):
        # Open file and turn it into a dictionary
        events = Utils.parse_json_to_dic(json_file)

        for event in events.values():
            # Create new Event instance
            event_instance = Event("", "")

            print(event)

            for athlete in event:

                # Create new Athlete instance
                athlete_instance = Athlete(
                    name=athlete["info"]["name"],
                    gender=athlete["info"]["gender"],
                    city=athlete["info"]["city"],
                )
                # athlete_instance.name = athlete["info"]["name"]
                # athlete_instance.city = athlete["info"]["city"]
                print(
                    athlete_instance.id,
                    athlete_instance.name,
                    athlete_instance.gender,
                    athlete_instance.city
                )

                print(athlete["info"])
                print(athlete["performance"])

                # Create new Performance and add it to Event instance
                performance_instance = Performance(
                    athlete_instance.id, athlete["performance"]
                )
                event_instance.performances.append(performance_instance)

                print("---------\n")

        print("Parson JSON data from", events.__len__(), " Ultraskates")
        return events

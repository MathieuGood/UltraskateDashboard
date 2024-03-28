import json
from classes.Event import Event
from classes.Athlete import Athlete
from classes.Performance import Performance

class EventManager:

    


    @classmethod
    def create_new_event(cls, event_data):

        # Event data is a json that needs to be converted to dicitaonary
        event_data = json.loads(event_data)
        return event_data

    @classmethod
    def parse_json_events(cls, json_events_file):
        # Open events.json file
        with open(json_events_file, "r") as file:
            events = file.read()
            # Convert events to a Python dictionary
            events = json.loads(events)

            for event in events.values():
                event_instance = Event('', '')

                print(event)
                for athlete in event:

                    # athlete_instance = Athlete(athlete["info"]["gender"])
                    athlete_instance = Athlete(athlete["info"]["gender"])
                    athlete_instance.name = athlete["info"]["name"]
                    athlete_instance.city = athlete["info"]["city"]

                    print(athlete["info"])
                    print(athlete_instance.id, athlete_instance.name, athlete_instance.gender, athlete_instance.city)
                    print(athlete["performance"])

                    performance_instance = Performance(athlete_instance.id, athlete["performance"])

                    event_instance.performances.append(performance_instance)

                    print("---------\n\n\n\n")

            print("Parson JSON data from", events.__len__(), " Ultraskates")
            return events

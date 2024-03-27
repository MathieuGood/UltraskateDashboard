import json


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
                print(event)
                for athlete in event:
                    print(athlete["info"])
                    print(athlete["performance"])
                    print("---------\n\n\n\n")

            print("Parson JSON data from", events.__len__(), " Ultraskates")
            return events

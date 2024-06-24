import json


class JsonUtils:
    @classmethod
    def parse_json_to_dic(cls, json_file: json) -> dict:
        """
        Parses a JSON file and returns its content as a dictionary.

        Args:
            json_file (str): The path to the JSON file.

        Returns:
            dict: The content of the JSON file as a dictionary.
        """
        with open(json_file, "r") as file:
            json_content = file.read()
            return json.loads(json_content)

    @classmethod
    def write_to_json(cls, data, filename: str) -> None:
        """
        Write data to a JSON file.

        :param data: The data to write to the file.
        :param filename: The name of the file to write the data to.
        """
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

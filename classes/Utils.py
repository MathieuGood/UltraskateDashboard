import re

class Utils:

    @classmethod
    def check_hhmmss_format(cls, str_time):
        """
        @brief Check if a string is in HH:MM:SS format.

        @param str_time: The string to check.
        @return: True if the string is in HH:MM:SS format, False otherwise.
        """
        return re.match(r"^\d{2}:\d{2}:\d{2}$", str_time)

    @classmethod
    # From a HH:MM:SS string, convert it to seconds
    def convert_time_str_to_ss(cls, str_time):
        """
        @brief Converts a time string to seconds.

        @param str_time: A string representing a time in HH:MM:SS format.
        @return: The time in seconds.
        """
        h, m, s = str_time.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)

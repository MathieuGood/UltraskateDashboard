import re


class StringUtils:
    """
    A utility class containing various helper methods.
    """

    @classmethod
    def str_is_hhmmss_format(cls, str_time: str) -> bool:
        """
        Check if a string is in HH:MM:SS format.

        :param str_time: The string to check.
        :return: True if the string is in HH:MM:SS format, False otherwise.
        :rtype: bool
        """
        if re.match(r"^\d{2}:\d{2}:\d{2}$", str_time):
            return True
        else:
            return False

    @classmethod
    def convert_time_str_to_ss(cls, str_time: str) -> int:
        """
        Converts a time string to seconds.

        :param str_time: A string representing a time in HH:MM:SS format.
        :return: The time in seconds.
        :rtype: int
        """
        h, m, s = str_time.split(":")
        return int(h) * 3600 + int(m) * 60 + int(s)

    @classmethod
    # In a '00:08:26 (00:08:26)' string, extract only the time that is not between the parentheses with a regex
    def extract_time_from_str(cls, str_time: str) -> str:
        """
        Extracts a time string from a string that contains a time string.

        :param str_time: The string to extract the time from.
        :return: The extracted time string.
        :rtype: str
        """
        match = re.search(r"(\d{2}:\d{2}:\d{2})", str_time)
        if match:
            return match.group(0)
        else:
            return None

    @classmethod
    def check_url_format(cls, url: str) -> bool:
        """
        Check if a URL is in a valid format.

        :param url: The URL to check.
        :return: True if the URL is in a valid format, False otherwise.
        :rtype: bool
        """
        return re.match(r"^https?://(?:www\.)?[^/]+/.*", url)

    @classmethod
    def extract_base_url(cls, url: str) -> str:
        """
        Extracts the base URL from the given URL.

        :param url: The URL to extract the base URL from.
        :return: The base URL.
        """
        match: re.Match[str] | None = re.search(r"^https?://(?:www\.)?[^/]+/", url)
        if StringUtils.check_url_format(url):
            return match.group(0)

class Comment:
    def __init__(self, name, text):
        self._name = name        # Commenter's name
        self._text = text        # Comment text

    def get_comment_details(self):
        """Return comment details as a formatted string"""
        return f"{self._name}: {self._text}"

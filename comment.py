class Comment:
    def __init__(self, name, text):
        self._name = name
        self._text = text

    def get_comment_details(self):
        return f"{self._name}: {self._text}"

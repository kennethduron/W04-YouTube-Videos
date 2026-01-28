from Comment import Comment

class Video:
    def __init__(self, title, author, length):
        self._title = title
        self._author = author
        self._length = length
        self._comments = []

    def add_comment(self, comment):
        self._comments.append(comment)

    def get_number_of_comments(self):
        return len(self._comments)

    def display_video_info(self):
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Length: {self._length} seconds")
        print(f"Number of comments: {self.get_number_of_comments()}")
        print("Comments:")
        for comment in self._comments:
            print(f"  - {comment.get_comment_details()}")
        print("-" * 40)

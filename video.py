from Comment import Comment

class Video:
    def __init__(self, title, author, length):
        self._title = title          # Video title
        self._author = author        # Video author
        self._length = length        # Length in seconds
        self._comments = []          # List to store Comment objects

    def add_comment(self, comment):
        """Add a Comment object to this video"""
        self._comments.append(comment)

    def get_number_of_comments(self):
        """Return the number of comments for this video"""
        return len(self._comments)

    def display_video_info(self):
        """Print all video details and its comments"""
        print(f"Title: {self._title}")
        print(f"Author: {self._author}")
        print(f"Length: {self._length} seconds")
        print(f"Number of comments: {self.get_number_of_comments()}")
        print("Comments:")
        for comment in self._comments:
            print(f"  - {comment.get_comment_details()}")
        print("-" * 40)

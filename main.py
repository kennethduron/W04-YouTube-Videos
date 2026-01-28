from Video import Video
from Comment import Comment

# -----------------------------
# Create Video objects
# -----------------------------
video1 = Video("Python Basics", "Alice", 300)
video2 = Video("OOP in Python", "Bob", 450)
video3 = Video("Advanced Python", "Charlie", 600)

# -----------------------------
# Create Comment objects
# -----------------------------
comments_video1 = [
    Comment("John", "Great explanation!"),
    Comment("Emma", "Very helpful, thanks!"),
    Comment("Mike", "I love this video.")
]

comments_video2 = [
    Comment("Sophia", "OOP made easy!"),
    Comment("Liam", "Clear examples."),
    Comment("Olivia", "Excellent content.")
]

comments_video3 = [
    Comment("Noah", "Challenging but good."),
    Comment("Ava", "Well structured."),
    Comment("Ethan", "Learned a lot, thanks!")
]

# -----------------------------
# Add comments to videos
# -----------------------------
for comment in comments_video1:
    video1.add_comment(comment)

for comment in comments_video2:
    video2.add_comment(comment)

for comment in comments_video3:
    video3.add_comment(comment)

# -----------------------------
# Store videos in a list
# -----------------------------
video_list = [video1, video2, video3]

# -----------------------------
# Display all video info
# -----------------------------
for video in video_list:
    video.display_video_info()

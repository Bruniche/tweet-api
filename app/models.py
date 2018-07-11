from datetime import datetime


class Tweet:
    def __init__(self, message):
        self.text = message
        self.created_at = datetime.now()
        self.id = None

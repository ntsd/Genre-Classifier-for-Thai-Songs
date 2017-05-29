class Song:
    def __init__(self, title, artist, album, record, emotion, genre):
        self.title = title
        self.artist = artist
        self.album = album
        self.record = record
        self.emotion = emotion
        self.genre = genre

    def __str__(self):
        return str([self.title, self.artist, self.album, self.record, self.emotion, self.genre])

    def getDetailCSV(self):
        return [self.title, self.artist, self.album, self.record, self.emotion, self.genre]

    def __repr__(self):
        return self.title

    def __iter__(self):
        return iter([self.title, self.artist, self.album, self.record, self.emotion, self.genre])


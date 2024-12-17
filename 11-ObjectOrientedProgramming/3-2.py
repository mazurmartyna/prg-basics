class Song():
    def __init__(self, performer, title, album, year):
        self.performer = performer
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        result = (f"Performer: {self.performer} \nTitle: {self.title} \nAlbum: {self.album} \nYear: {self.year}")
        
        return result
    
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

print(song1)
print()
print(song2)
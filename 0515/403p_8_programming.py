class Song:
    def __init__(self, lyrics_list):
        self.lyrics = lyrics_list
        
    def sing(self):
        for line in self.lyrics:
            print(line)

aSong = Song(["TWINKLE, twinkle, little star",
              "How I wonder what you are!",
              "Up above the world so high,",
              "Like a diamond in the sky."])
aSong.sing()
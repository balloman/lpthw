class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        """Prints out the song in a for loop."""
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't wanna get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
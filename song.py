class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def get_next_song(self):
        return (self.next)

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
       # if (self.get_next_song().get_next_song().name) == self.name:
        return (self.next.next is self)

first = Song("Hello")
second = Song("Eye of the tiger")

first.next_song(second)
second.next_song(first)

print(first.is_repeating_playlist())
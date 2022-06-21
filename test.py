class StorageDevice:
    def __init__(self, memory, *args):
        super().__init__(*args)
        self.memory = memory
        self.used = 0
        self.items = []  # items stored in memory

    def available_storage(self):
        return self.memory - self.used - len(self.items)


class PhoneDevice:
    def __init__(self, number, *args):
        super().__init__(*args)
        self.number = number

    def call(self, number):
        print('Calling number', number)

    def receive(self):
        print('Receiving Call...')


class MusicPlayer(StorageDevice):
    def __init__(self, memory):
        super().__init__(memory)

    def play_song(self, song):
        if song in self.items:
            print("Playing " + song)
        else:
            print(song + " not found")

    def store_song(self, song, size):
        if size >= self.available_storage():
            print("Not enough memory")
        else:
            self.items.append(song)
            self.used += size
            print(song + " stored")
            print(self.available_storage(), "memory left")

class IPod(MusicPlayer):
    def __init__(self, memory):
        super().__init__(memory)

    def backup_songs(self):
        print("Connect to iTunes to back up songs")

class IPhone(MusicPlayer, PhoneDevice): # order is important
    def __init__(self, memory): # iPhone has no initial phone number
        super().__init__(0, memory)
    # alternatively we can init with phone number and arbitary memory
    # def __init__(self, number)
    # super().__init__(number, 0)
    def search(self, text):
        print("Searching", text)

iphone = IPhone(256)
iphone.call(98765432)
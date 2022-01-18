class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self._cur = None

    def __repr__(self):
        string = ""

        if(self.head == None):
            string += "Doubly Linked List Empty"
            return string

        string += f" {self.head.data}"
        start = self.head.next
        while(start != None):
            string += f" \n {start.data}"
            start = start.next
        return string

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.count += 1
            return

        self.tail.next = Node(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        self.count += 1

    # def insert(self, data, index):
    #     if (index > self.count) | (index < 0):
    #         raise ValueError(
    #             f"Index out of range: {index}, size: {self.count}")

    #     if(index == self.count):
    #         self.append(data)
    #         return

    #     if(index == 0):
    #         self.head.previous = Node(data)
    #         self.head.previous.next = self.head
    #         self.head = self.head.previous
    #         self.count += 1
    #         return

    #     start = self.head
    #     for _ in range(index):
    #         start = start.next
    #     start.previous.next = Node(data)
    #     start.previous.next.previous = start.previous
    #     start.previous.next.next = start
    #     start.previous = start.previous.next
    #     self.count += 1
    #     return

    # def remove(self, index):
    #     if (index >= self.count) | (index < 0):
    #         raise ValueError(
    #             f"Index out of range: {index}, size: {self.count}")

    #     if index == 0:
    #         self.head = self.head.next
    #         self.head.previous = None
    #         self.count -= 1
    #         return

    #     if index == (self.count - 1):
    #         self.tail = self.tail.previous
    #         self.tail.next = None
    #         self.count -= 1
    #         return

    #     start = self.head
    #     for i in range(index):
    #         start = start.next
    #     start.previous.next, start.next.previous = start.next, start.previous
    #     self.count -= 1
    #     return

    def index(self, data):
        start = self.head
        for i in range(self.count):
            if(start.data == data):
                return start.data
            start = start.next
        return None

    def firstvalue(self):
        return self.head

    def size(self):
        return self.count

    def display(self):
        print(self)

    def get_cur(self):
        return self._cur

    def set_cur(self, x):
        self._cur = x


nums = DLL()


def mainmenu():
    userinput = input(
        "--- PLAYLIST MUSIC PLAYER ---\n1. Buat playlist kamu\n2. Putar lagu\n3. Putar selanjutnya\n4. Putar sebelumnya\n5. Lihat playlist kamu\n\nPilih menu : ")
    if userinput == '1':
        insertmenu()
    elif userinput == '2':
        playcurrentmusic()
    elif userinput == '3':
        playnextmusic()
    elif userinput == '4':
        playprevmusic()
    elif userinput == '5':
        showplaylist()
    else:
        print("\nInvalid Key Input\n")


def insertmenu():
    index = input("Masukkan jumlah lagu dalam playlist : ")
    for x in range(int(index)):
        ourlist = input("Masukkan lagu Ke-" + str(x+1) + " (judul, singer): ")
        nums.append(ourlist)
    print("\nPlaylist berhasil dibuat...\n")
    mainmenu()


def playcurrentmusic():
    getmusic = nums.firstvalue().data.split(", ")
    nums.set_cur(nums.firstvalue().next.data)
    print("Kamu sedang memutar lagu", getmusic[0], "dari", getmusic[1], '\n')
    mainmenu()


def playnextmusic():
    getmusic = nums.get_cur().split(", ")
    nums.set_cur(nums.firstvalue().next.next.data)
    print("Kamu sedang memutar lagu", getmusic[0], "dari", getmusic[1], '\n')
    mainmenu()


def playprevmusic():
    getmusic = nums.firstvalue().next.next.previous.data.split(', ')
    print("Kamu sedang memutar lagu", getmusic[0], "dari", getmusic[1], '\n')
    mainmenu()


def showplaylist():
    print("~~~ Playlist Kamu ~~~")
    nums.display()
    print("\n")


mainmenu()

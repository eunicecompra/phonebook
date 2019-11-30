
class Phonebook:
    size = 0
    phonebook = dict()

    def readInput(self):
        self.size = int(input())
        for index in range (0, self.size):
            raw_detail = input()
            detail = raw_detail.split(" ", 1)
            self.phonebook[detail[0]] = detail[1]

    def search_phonebook(self, name):
        if name in self.phonebook:
            return name + "=" + self.phonebook[name]
        else:
            return "Not found"
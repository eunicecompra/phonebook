class Phonebook:
    size = 0
    phonebook = dict()

    def read_input(self):
        self.size = int(input())
        for index in range (self.size):
            raw_detail = input()
            detail = raw_detail.split(" ", 1)
            self.phonebook[detail[0]] = detail[1]

        while(True):
            try:
                result = self.search_phonebook(input())
                print(result)
            except (EOFError, StopIteration):
                break

    def search_phonebook(self, name):
        if name in self.phonebook:
            return name + "=" + self.phonebook[name]
        else:
            return "Not found"
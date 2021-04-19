class Books:
    def count(self):
        print("10000 thousand books")

    def authorname(self):
        print("MT Vasudevan Nair")


class Novel(Books):
    def authorname(self):
        print("Vaikkom Muhammed Basheer")

obj=Novel()
obj.authorname()
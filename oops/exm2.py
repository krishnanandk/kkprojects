class Book:
    def setvalue(self,libname,book,author,pages):
        self.libname=libname
        self.book=book
        self.author=author
        self.pages=pages

    def printvalue(self):
        print("libraryname:",self.libname)
        print("book name:",self.book)
        print("author:",self.author)
        print("pages:",self.pages)
obj=Book()
obj.setvalue("Govt Library","Khasakinte Ithihasam","OV Vijayan",300)
obj.printvalue()
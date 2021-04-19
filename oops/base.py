#class: design patterns
#object:real world entity
#references:name that refers a memory location of a object

class Person:
    def walk(self):
        print("person is walking")

    def run(self):
        print("person is running")

    def jumping(self):
        print("person is jumping")


obj = Person()
obj.walk()
obj.run()
obj.jumping()

ab= Person()
ab.run()



#define a class book with __len__ that return title length and __str__
class Book:
    def __init__(self,name,year):
        self.name = name
        self.year= year
    def __str__(self):
        return f"The books title is {self.name} and it was published in the year {self.year}"
    def __len__(self):
        return len(self.name)
    
b1= Book("Blue Ocean Stratergy",1999)

print(b1)
print(len(b1))
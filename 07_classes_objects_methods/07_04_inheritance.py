'''
CLASSES AND INHERITANCE
=======================

1) Define an empty Movie class.

2) Add a dunder init method that takes two arguments "year" and "title"

3) Create a sub-class called "RomCom" that inherits from the Movie class

4) Create another sub-class of the Movie class called "ActionMovie"
    that overwrites the dunder init method of Movie and adds another
    instance variable called "pg" that is set by default to the number 13.

5) EXTRA: If you finish early, use the time to practice flushing out these
    classes and white-boarding code. What attributes could a Movie class
    contain? What methods? What tricks can you use through inheritance?
    Any class attributes you could add?

'''
class Movie:
    '''Class to model movies.'''

    def __init__(self, year, title):
        self.year = year
        self.title = title

    def __str__(self):
        return f'The movie {self.title} was made in {self.year}.'

class RomCom(Movie):
    '''Class to model Romantic Comedies'''
    def __init__(self, year, title):
        super().__init__(year, title)

class ActionMovie(Movie):
    '''Class to model Action Movies'''

    def __init__(self, year, title, pg=13):
        super().__init__(year, title)
        self.pg = pg

    def __str__(self):
        return f'The movie {self.title} was made in {self.year} and has a pg of {self.pg}.'

movie1 = Movie(1939, 'Gone With The Wind')
romcom1 = RomCom(1985, 'Romancing The Stone')
actionmovie1 = ActionMovie(1984, 'Diehard', 20)
print(movie1)
print(romcom1)
print(actionmovie1)



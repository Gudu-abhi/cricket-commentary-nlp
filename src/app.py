from .mine import Mine

class App(object):

    def run(self):
        mine = Mine()
        mine.extract()

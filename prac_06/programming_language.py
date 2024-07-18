"""
CP1404 Practice 6: Programming Language
Alex Williams

Estimated time: 20 mins
"""


class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == 'Dynamic'

    def __str__(self):
        reflection = self.reflection
        return f"{self.name}, {self.typing}, reflection={self.reflection}, first appeared in {self.year}"


if __name__ == '__main__':
    python = ProgrammingLanguage('Python', 'Dynamic', True, 1991)
    ruby = ProgrammingLanguage('Ruby', 'Dynamic', True, 1995)
    visual_basic = ProgrammingLanguage('Visual Basic', 'static', False, 1991)
    print(python)
    print(ruby)
    print(visual_basic)

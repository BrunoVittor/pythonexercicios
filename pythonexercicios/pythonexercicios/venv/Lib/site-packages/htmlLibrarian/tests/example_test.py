"""
This is an example of how to use `context.py` to set up tests easily,
    which has syntax similar to if a user was going to use it
"""

from context import htmlLibrarian

lib = htmlLibrarian.Librarian()

alink = 'https://www.bloomberg.com/canada'
lib.get(alink)
print(lib.get(alink))
lib.remove(alink)

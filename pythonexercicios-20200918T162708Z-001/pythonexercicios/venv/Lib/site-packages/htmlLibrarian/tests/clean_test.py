import os

from context import htmlLibrarian

librarian = htmlLibrarian.Librarian(debug=True)
librarian.clean()
assert not os.path.exists(os.path.join(os.getcwd(), 'htmlLibrary'))
assert not os.path.exists(os.path.join(os.getcwd(), 'librarianTools'))

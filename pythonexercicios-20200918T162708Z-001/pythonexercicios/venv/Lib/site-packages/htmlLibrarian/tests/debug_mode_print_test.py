from context import htmlLibrarian

librarian = htmlLibrarian.Librarian(2, debug=True)
alink = 'https://www.google.com'
librarian.get(alink)

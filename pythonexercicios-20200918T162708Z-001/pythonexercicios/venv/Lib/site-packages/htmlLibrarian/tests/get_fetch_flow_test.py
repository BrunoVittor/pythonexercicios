from context import htmlLibrarian

librarian = htmlLibrarian.Librarian(debug=True)
alink = 'https://www.google.com'
try:
    librarian.remove(alink)
except:
    a = 1
librarian.get(alink)
librarian.get(alink)


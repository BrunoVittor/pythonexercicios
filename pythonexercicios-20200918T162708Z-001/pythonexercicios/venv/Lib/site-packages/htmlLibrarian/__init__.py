try:
    from .librarian import Librarian
except (SystemError, ImportError):
    from librarian import Librarian

try:
    from .linkData import LinkData
except (SystemError, ImportError):
    from linkData import LinkData

try:
    from . import librarianUtil
except (SystemError, ImportError):
    import librarianUtil

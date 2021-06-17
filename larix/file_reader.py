import re
import os
from collections import defaultdict


LINESEP = re.compile("\n")


class FileReader(object):
    FILE_DEPENDENCY_SEEKERS = list()
    
    def __init__(self, file):
        self.file = file

    def __str__(self):
        return self.file

    def read_content(self):
        with open(self.file, "r") as f:
            content = f.read()
            line_starts = get_line_starts(content)

            return content, line_starts

    def get_file_dependencies(self):
        lines, content = self.read_content()
        for seeker in type(self).FILE_DEPENDENCY_SEEKERS:
            pass


def register_seeker(cls):
    def _register_seeker(seeker):
        cls.FILE_DEPENDENCY_SEEKERS.append(seeker)
        return seeker
    return _register_seeker


class DefaultFileReader(FileReader):
    pass


__FILE_READERS = defaultdict(DefaultFileReader)


class DuplicateFileReaderException(Exception):

    def __init__(self, ext=None):
        self.ext = ext

    def __str__(self):
        if self.ext:
            return f"You cannot assign two different FileReader classes to the same file extension: '{self.ext}'"
        else :
            return f"You cannot assign two different FileReader classes to the same file extension"


def register_file_reader(*extensions):
    def _register_file_reader(f):
        for ext in extensions:
            if ext in __FILE_READERS:
                raise DuplicateFileReaderException(ext=ext)
            
            __FILE_READERS[ext] = f
        return f
    
    return _register_file_reader


def get_file_reader(ext):
    return __FILE_READERS[ext]


def process_file(file):
    ext = os.path.splitext(file)[1]
    reader = get_file_reader(ext)(file)

    return reader.read()


def get_line_starts(content):
    return [m.start() for m in LINESEP.finditer(content)]


def get_match_lines(matches, line_starts):
    i = 0
    n = len(line_starts)
    for m in matches:
        while i < n and m.start() > line_starts[i]:
            i += 1
        yield i + 1, m


@register_file_reader(".py")
class PyFileReader(FileReader):

    @register_seeker(FileReader)
    def find_py_packages(line_starts, content):
        pass
    PY_PATTERN = re.compile(
            r"from +(\w+) +import|import.*?, +(\w+)|import +(\w+)"
    )
    def find_files(cls, content):
        pass

    def read(self):
        with open(self.file, "r") as f:
            content = f.read()
            print(content)
            lines = [m.start() for m in re.finditer("\n", content)]
            print(lines)

            matches = PyFileReader.PY_PATTERN.finditer(content)
            

            print(PyFileReader.FILE_DEPENDENCY_SEEKERS)


            for a, b in get_match_lines(matches, lines):
                pass #print(a, b)

            i = 0



@register_file_reader(".tex")
class TeXFileReader(FileReader):
    pass

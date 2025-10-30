PCAP - Lessons learned
======================

Name mangling
-------------

- Name mangling only for PRIVATE INSTANCE variables defined INSIDE the
  class definition, which are

  - instance variables:

    ::

       class A:
           def __init__(self):
               __hidden_instvar = True

       >>> a = A()
       >>> a._A__hidden_instvar
       True

  - class variables:

    ::

       class A:
           __hidden_classvar = False
           def __init__(self):
               pass

       >>> a = A()
       >>> a._A__hidden_classvar
       False

- Name mangling NOT for private instance variables defined OUTSIDE the
  class:

  ::

     class A:
         pass

     >>> a = A()
     >>> a.__hidden = True
     >>> a.__hidden
     True

- Name mangling applies also to PRIVATE METHODS of a class:

  ::

     >>> my_obj._MyObjClass__hidden_method()

- If private instance is defined in parent class, then

  ::

     >>> my_subclass_instance._ParentClass__private_instance_variable

ASCII
-----

- ASCII: Basic punctuation and symbols (e.g. Space !$%&()+-.*/) –>
  Numbers (0-9) –> Big letters (A-Z) –> Small letters (a-z)
- code points use upper 128 slots for special characters (lower 128
  slots are fix)

Some module methods
-------------------

- ``print(arg1, arg2, …, sep=' ', end='\n')`` –> prints
  arguments on console.

  - sep defaults to ``' '``. If sep=None, default is used
  - end defaults to ``\n``. If end=None, default is used

- ``range(x)`` –> returns a range object (iterable), containing elements
  from 0 to x-1 (x itself is excluded), may be put into a list

  ::

     >>> r = range(5)
     >>> for n in r:
     >>>     print(n)
     0
     1
     2
     3
     4
     >>> l = list(r)

- ``sorted_list = sorted([iterable], key)`` -> creates a NEW iterable
  with the sorted order. The previous iterable remains unchanged. 'key'
  is a function (often: lambda), into which each iterable element is fed
  -> return value is used for sorting

module: platform
----------------

- platform.platform(): Returns a single string identifying the
  underlying platform

  ::

     >>> platform.platform()
     'macOS-26.0-arm64-arm-64bit-Mach-O'

- platform.machine(): Returns the machine type, e.g. 'AMD64'. An empty
  string is returned if the value cannot be determined.

  ::

     >>> platform.machine()
     'arm64'

- platform.processor(): Returns the (real) processor name, e.g. 'amdk6'.

  ::

     >>> platform.processor()
     'arm'

- platform.system(): Returns the system/OS name, such as 'Linux',
  'Darwin', 'Java', 'Windows'. An empty string is returned if the value
  cannot be determined.

  ::

     >>> platform.system()
     'Darwin'

- platform.version(): Returns the system's release version, e.g. '#3 on
  degas'. An empty string is returned if the value cannot be determined.

  ::

     >>> platform.version()
     'Darwin Kernel Version 25.0.0: Mon Aug 25 21:17:54 PDT 2025; root:xnu-12377.1.9~3/RELEASE_ARM64_T6041'

- platform.python_implementation(): Returns a string identifying the
  Python implementation. Possible return values are: 'CPython',
  'IronPython', 'Jython', 'PyPy'.

  ::

     >>> platform.python_implementation()
     'CPython'

- platform.python_version_tuple(): Returns the Python version as tuple
  (major, minor, patchlevel) of strings.

  ::

     >>> platform.python_version_tuple()
     ('3', '13', '7')

module: math
------------

- ``math.trunc(x)``: Return x with the fractional part removed as integer
  e.g. ``math.trunc(1.4)`` -> 1

- ``math.exp(x)``: Returns the value of e^x

- ``math.log(x, [base])``: Returns the logarithm of x at base (default: e):

  ::

     >>> math.log(10)
     2.302585092994046
     >>> math.pow(math.e, 2.302585092994046)
     10.000000000000

- ``math.pow(x, y)``: returns x^y (as float), i.e

  ::

     >>> math.pow(10,2)
     100.0
     >>> 10**2   # same as
     100

- ``math.ceil(x)``: the ceiling of x (the smallest integer greater than or
  equal to x)

  ::

     >>> math.ceil(4.5)
     5
     >>> math.ceil(-4.5)
     -4

- ``math.floor(x)``: the floor of x (the largest integer less than or equal
  to x)

  ::

     >>> math.floor(4.5)
     4
     >>> math.floor(-4.5)
     -5

- ``math.factorial(x)``: returns x! (x has to be an integral and not a
  negative, if so raises ValueError)

  ::

     >>> math.factorial(5)
     120     (5 * 4 * 3 * 2 * 1)
     >>> math.factorial(-5)
     ValueError

- ``math.sqrt(x)``: Return the square root of x.

  ::

     >>> math.sqrt(4)
     2
     >>> math.sqrt(-4)
     ValueError

- ``math.hypot(x: int | float, y: int | float)``: Returns the length of
  the hypotenuse:

  ::

     >>> math.hypot(3,5)
     5.830951894845301

module: random
--------------

The seed value (default: current time -> no repetition for consecutive
runs) - determines the first random number - generates a new seed (to
calculate the next random number)

- ``random.random()`` –> Return a random floating-point number X in the
  range 0.0 <= X < 1.0
- ``random.sample(list, k)`` –> return list of k UNIQUE elements from list:

  - k must not be larger than len(list) –> ValueError
  - if number of unique elements in list is less than 'k', duplicate
    elements are returned

- ``random.randint(a, b)`` –> return random integer N where a <= N <= b
  (both a and b are included)
- ``random.randrange(a, b, [step])`` –> return random integer N where a <= N
  < b (a is included, b is excluded), optional [step] define stepwidth
- ``random.choice(sequence)`` –> returns one item from a sequence (list,
  tuple, set)
- ``random.choices(list, k=5)`` –> return list of k elements from list -
  elements may NOT be UNIQUE, hence elements may be returned MORE THAN
  ONCE
- ``random.seed()`` –> Initialize the random number generator. If seed() is
  passed an integer, each run produces the same values

List methods
------------

- ``[list].sort(key = lambda x: x[1])`` … sorts a list according to
  return value of key function and compares value via '<' (here: the
  second character of each list entry is used, which requires
  `list <#list>`__ to contains strings of at least two character length)
- ``[list].insert(i, x)`` … Insert a new item with value x in the array
  BEFORE position i. Negative values are treated as being relative to
  the end of the array. e.g. my_list = [1,2,3] -> my_list.insert(-1, 4)
  –> [1,2,4,3]
- ``[list].pop(i)`` … removes the element at index position i from
  `list <#list>`__ and returns it

List comprehension
------------------

- Double for-statements in list comprehension results in a list
  containing lists, e.g.

  ::

     >>> my_l = [[i+j for i in range(1,5,1)] for j in range(-1,6,3)]
     >>> my_l
     [[0, 1, 2, 3], [3, 4, 5, 6], [6, 7, 8, 9]]

- Multiple conditions can be added:

  ::

     # Number from 0 to 19 must have modulo of 0 for both 2 and 5
     >>> my_list = [ x for x in range(20) if x % 2 == 0 if x % 5 == 0 ]
     >>> my_list
     [0, 10]

  Both these work and do the same thing:

  ::

     >>> [ x for x in range(20) if (x % 2 == 0 and x % 5 == 0) ]
     >>> [ x for x in range(20) if x % 2 == 0 if x % 5 == 0 ]

- A list comprehension becomes a generator when used inside round
  brackets (), not square brackets []:

  ::

     >>> my_gen = (i for i in range(3))
     >>> for elem in my_gen:
     >>>     print(i)

List
----

- lists are MUTABLE

- list support the ``del`` statement to remove an item:

  ::

     >>> my_list = [1,2,3]
     >>> del my_list[-1]
     >>> my_list
     [1,2]

- ``[list].remove(x)`` … removes first occurence of x in
  `list <#list>`__

Tuple
-----

- tuples are IMMUTABLE (so, no adding or removing elements)

- tuples use round brackets '(' and ')', e.g. (1,2,3)

- tuples can be created via

  - with braces: my_tuple = (1,2,3)

  - without braces (ending with a comma): my_tuple = 1,

  - with 'tuple(iterable)' method: tuple([1,2,3]):

    ::

       >>> tuple(['12', 2, "ABC"])   # OK - use list
       >>> tuple(('12', 2, "ABC"))   # OK - use tuple
       ('12', 2, 'ABC')
       >>> tuple('12', 2, 'ABC')   # NOK --> ValueError, as tuple requires ITERABLE as SINGLE ARGUMENT

- a single value tuple always ends with a comma:

  ::

     >>> t = tuple([1,2,3])
     >>> t[-1:]
     (3,)

Set
---

- sets are MUTABLE

- sets use curly braces ``{`` and ``}``, e.g. {1,2,3}

- sets only contain unique items - if equal value are passed in, only
  one instance remains, e.g.

  ::

     >>> s = set(['a', 'b', 'a'])
     >>> s
     {'a', 'b'}
     >>> s2 = {1,2,3}
     >>> s2
     {1,2,3}

- can be created via

  - with braces: my_set = {1,2,3}

  - with 'set(iterable)' method:

    ::

       >>> set([1,2,3])    # OK - use list
       >>> set((1,2,3))    # OK - use tuple
       >>> set({1,2,3})    # OK - use set
       >>> set(1,2,3) --> ValueError, as set requires ITERABLE as SINGLE ARGUMENT

- `set <#set>`__.remove(x) -> removes first occurence of x in
  `set <#set>`__

Dictionary
----------

- dictionaries use curly braces '{' and '}' containing key-value pairs,
  separated by commas. The key value pair consists of a key and a value,
  separated by colon ':'

  ::

     >>> d = {'a': 1, 'b': 2, 'c': 3}
     >>> d
     {'a': 1, 'b': 2, 'c': 3}

- keys must be hashable, therefor must be IMMUTABLE.

  Allowed types:

  ::

       - int
       - float
       - str
       - tuple
       - bool

  NOT allowed types:

  ::

       - list
       - dict
       - set

- ``my_dict.keys()`` … returns list of all keys in my_dict

- ``my_dict.values()`` … returns list of all valules in my_dict

- ``my_dict.items()`` … returns list of tuples, each tuple being a key,
  value pair

Bytearray
---------

- List-like array containing only integer numbers from 0 to 255 (2^8
  values) -> TypeError, when adding different type -> ValueError, when
  passing integer outside of range

- Does NOT have a fix length

- Create via

  ::

     >>> byarr = bytearray() # empty
     >>> byarr = bytearray(10)  # size of 10, filled with zeros (\x00)

- Read binary data from file:

  ::

     >>> data = bytearray()
     >>> bf = open('file.bin', 'rb')
     >>> bd.readinto(data)
     >>> bf.close()

- Alternative:

  ::

     >>> bf = open('file.bin', 'rb')
     >>> data = bytearray(bf.read())
     >>> bf.close()

Built-in keywords
-----------------

- ``global``: inside a local scope allows

  - referencing an existing variable in the global scope
  - making a local variable accessible outside of the local scope

  ::

     y = 'R2D2'
     def my_func(x):
         global y
         y = x
         return y

     my_func('C3PO')
     print(y)

  –> Here 'print(y)' references the global variable 'y' which has been
  altered inside the my_func() function

Built-in functions
------------------

- ``len(str)`` also consideres escape characters
  (i.e. ``len("\n") = 1``)

- ``issubclass(class, classinfo)`` … is class a (direct, indirect, or
  virtual) subclass of classinfo (true/false)? indirect means: if C is a
  subclass of B and B is a sublass of A (A <– B <– C), then C is also a
  subclass of A, so issubclass(C, A) returns True

- ``isinstance(object, classinfo)`` … is object an instance of classinfo
  (true/false) OR a (direct, indirect, or virtual) subclass thereof?

- ``file = open(file, mode)`` … create file input-output stream (file
  object), which is iterable (returning the file content line by line),
  e.g.

  ::

     >>> for line in open('text.txt', 'r'):
     >>>     print(line)
     This is a line
     This is another line

  - mode:

    - ``r`` … file MUST exist (read only)
    - ``r+`` … file MUST exist AND is writable (read and write)
    - ``w`` … file may exist, if not is created (write only)
    - ``w+`` … file may exist, if not is created (write and read)
    - ``a`` … file may exist, if not is created (write only, appends at
      end of file)
    - ``a+`` … file may exist, if not is created (read and write,
      appends at end of file): careful, pointer is at end of file, so
      before reading move it to begin position via file.seek(0)
    - ``x`` … file MUST NOT exist (exclusive creation mode, create
      only): if already exists, raises IOError with e.errno ==
      errno.EEXIST

    CAREFUL: reading or writing from/to file, if mode doesn't allow
    this, raises an io.UnsupportedOperation error

  - important errnos (assigned to all IOError instance's ``errno``
    attribute):

    - ``errno.EEXIST`` … File already exists
    - ``errno.ENOENT`` … File does not exist
    - ``errno.EACCES`` … Permission denied: happens if writing to file
      opened in read-only mode OR file is opened in write-mode but has
      read-only atttribute
    - ``errno.EBADF`` … Bad file number: happens if operate with an
      unopened stream
    - ``errno.EFBIG`` … File too large (for memory)
    - ``errno.EISDIR`` … Is a directory: when you try to treat a
      directory name as the name of an ordinary file.
    - ``errno.EMFILE`` … Too many open files (simultaneously open more
      streams than acceptable for your operating system)
    - ``errno.ENOSPC`` … No space left on device (e.g. hard disk)

- Read content from file stream:

  - ``data = file.read(b)`` -> str … returns first b bytes of file as
    single string. If b is omitted, negative or None, the full content
    is returned
  - ``line = file.readline(b)`` -> str … returns first b bytes of the
    next line from file. If b is omitted, negative or exceeds byte
    length of the line, the full line is read
  - ``lines = file.readlines(b)`` -> list[str] … read and return a list
    of FULL lines from the stream. 'b' can be specified to control the
    number of lines read: no more lines will be read if the total size
    (in bytes/ 8 bit characters like ASCII) of all lines so far exceeds
    'b'. If 'b' <= 0 or 'b' = None, ALL LINES are read.
  - ``file.readinto(my_bytearray)`` … read out bytes from file into
    precreated bytearray

- Write content to file stream:

  - ``file.write(string | bytearray)`` … write string characters or
    bytearray to file – IMPORTANT: write() returns the number of
    characters written to file
  - ``file.writelines([list of lines])`` … writes list of strings to
    file WITHOUT line separator (should be added at the end of each
    line)

- ``filter(function, iterable)`` -> takes each element of iterable and
  puts it into 'function', returns a filter object.

  - If function is a lambda e.g. lambda x: x**2, then x is the passed in
    element from iterable

  - If function returns a falsy (e.g. ““,[], {}, 0, None, False) the
    element is filtered out from iterable

  - For reuse, filter object must be put into iterable construtor, e.g.

    ::

       >>> list1 = [6, 2, 8, 56, 33, 78, 42, 98]
       >>> filtered = filter(lambda x : x%3==0, list1)
       >>> filtered
       <filter object at 0x105d4be80>
       >>> list2 = list(filtered)
       >>> list2
       [6, 33, 78, 42]

- ``map(function, iterable, iterables*)`` … supplies each element of
  'iterable' to the passed 'function' and returns it. If additional
  'iterables\*' are passed, 'function' must accept just as many
  iterables as arguments

  ::

     >>> xs = [1,2,3]
     >>> ys = [1,2,3]
     >>> r = list(map(lambda x,y: x*y, xs, ys))
     >>> r
     [1, 4, 9]

- ``id(obj)`` … returns the unique id of an object

- ``hasattr(object/class, attr_name: str)`` … determines if an OBJECT or
  a CLASS has the attribute name, which are

  - instance variables: objects only
  - class variables: class + objects

- ``max(iterable)`` … returns the largest item in an iterable

- ``sum(iterable)`` … returns sum of all elements of iterable (iterable
  must contain integers or floats)

- ``int(number: int|float|str)`` … converts 'number' to an integer.
  Number must be

  - an integer e.g. int(3) -> 3
  - a floating point number (decimal places are trimmed) -> int(3.7) ->
    3
  - a string which contains a string representation of an INTEGER e.g
    int(“3”) -> 3 (floats are NOT allowed, e.g. int(“3.5”) –>
    ValueError)

os module
---------

- ``os.mkdir("/dir")`` … creates a directory at given path (NO recursive
  creation) If path already exists a FileExistsError is raised. If
  parent path is not found a FileNotFoundError is raised.

- ``os.makedirs("/some/path")`` … creates a directory path

- ``os.chdir("some/path")`` … sets current working directory to given
  path. If directory does not exist, raises FileNotFoundError

- ``os.listdir()`` … returns a list with all directories within the
  current working directory (without '.' or '..')

- ``os.uname()`` … provides current operating system information as an
  object with these attributes:

  ::

                   sysname - operating system name
                   nodename - name of machine on network (implementation-defined)
                   release - operating system release
                   version - operating system version
                   machine - hardware identifier

- ``os.name`` … returns OS system name (e.g. 'posix', 'nt' , 'java')

- ``os.system(shell_command: str)`` … execute a shell command

datetime module
---------------

- date objects:

  - ``datetime.date(year, month, day)`` … all items must be given,
    otherwise ValueError

    ::

       >>> from datetime import date

       >>> date = date(1992, 1, 16)
       >>> date_1
       datetime.date(1992, 1, 16)
       >>> print(date_1)
       1992-01-16

  - ``datetime.fromtimestamp(timestamp)`` … create from timestamp

    ::

       >>> from datetime import date
       >>> import time

       >>> current_time = time.time()
       >>> date = date.fromtimestamp(current)

  - ``datetime.fromisoformat('iso-date-format-string')`` … from iso
    format string

    ::

       >>> from datetime import date

       >>> d = date.fromisoformat('2019-11-04')

  Methods:

  ::

     d = d.replace(year=1992, month=1, day=16) ... replace date values
     d.weekday() ... get weekday integer (0 for Monday)

- time objects:

  ::

     >>> from datetime import time

     >>> t = time(14, 53, 20, 1)  ... create time object (hour, minute, second, millisecond)
     >>> print(t)
     14:53:20.000001

  Methods:

  ::

     >>> t = time.time()
     >>> t.ctime(t)  ... convert time epoch to string
     'Wed Oct 15 13:11:20 2025'

     >>> st = time.gmtime(t) ... returns struct_time object (contain tm_* attributes for time values)
     >>> st = time.localtime(t) ... retuns struct_time object (contain tm_* attributes for time values)

     >>> time.asctime(st)  ... convert struct_time to string
     'Wed Oct 15 13:11:20 2025'
     >>> time.mktime(st) ... convert struct_time to epoch time (as float)
     1760523080.0

- datetime.datetime objects:

  ::

     >>> dt = datetime(2019,11,27, 11, 27, 22)  ... (year, month, day, hour, min, sec)
     >>> dt.date() ... get date
     datetime.date(2019, 11, 27)
     >>> dt.time() ... get time
     datetime.time(11, 27, 22)
     >>> dt.timestamp() ... get timestamp
     1574850442.0

     >>> datetime.today()  ... return current date and time as datetime.datetime object
     datetime.datetime(2025, 10, 15, 13, 20, 20, 52509)
     >>> datetime.now() ... *same*
     datetime.datetime(2025, 10, 15, 13, 20, 20, 52509)

- date and time formatting:

  ``strftime``:

  - ``datetime.datetime.strftime(date: date|datetime, format: str)`` …
    returns string of 'date' in given 'format'

    ::

       >>> from datetime import datetime

       >>> date_1 = date(1992, 1, 16)
       >>> datetime.strftime(date_1, '%y/%B/%d')
       '92/January/16'

       >>> datetime_1 = datetime(2019,11,27, 11, 27, 22)
       >>> datetime.strftime(datetime_1, '%y/%B/%d - %H:%M:%S')
       '19/November/27 - 11:27:22'

  - ``time.strftime(format: str, [struct_time])`` … returns string of
    'time' in given 'format'

    ::

       >>> import time

       >>> st = time.gmtime(time.time())
       >>> time.strftime('%Y/%m/%d %H:%M:%S', st)
       '2025/10/15 11:56:27'

  ``strptime``:

  - ``datetime.datetime.strptime(datetime: str, format: str)`` … returns
    datetime object for 'datetime' string in given 'format

    ::

       >>> from datetime import datetime
       >>> print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
       datetime.datetime(2019, 11, 4, 14, 53)

  - ``time.strptime(datetime: str, format: str)`` … returns struct_time
    object for 'datetime' string in given 'format

    ::

       >>> import time
       >>> time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
       time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)

  Format Codes:

  +------+-------------------------------------+---------------------------+
  | Code | Meaning                             | Example                   |
  +======+=====================================+===========================+
  | %a   | Abbreviated weekday name            | Sun, Mon, …               |
  +------+-------------------------------------+---------------------------+
  | %A   | Full weekday name                   | Sunday, Monday, …         |
  +------+-------------------------------------+---------------------------+
  | %w   | Weekday as number (0=Sunday,        | 0–6                       |
  |      | 6=Saturday)                         |                           |
  +------+-------------------------------------+---------------------------+
  | %d   | Day of the month, zero-padded       | 01–31                     |
  +------+-------------------------------------+---------------------------+
  | %b   | Abbreviated month name              | Jan, Feb, …               |
  +------+-------------------------------------+---------------------------+
  | %B   | Full month name                     | January, February, …      |
  +------+-------------------------------------+---------------------------+
  | %m   | Month as number (zero-padded)       | 01–12                     |
  +------+-------------------------------------+---------------------------+
  | %y   | Year without century                | 00–99                     |
  +------+-------------------------------------+---------------------------+
  | %Y   | Year with century                   | 2025                      |
  +------+-------------------------------------+---------------------------+
  | %H   | Hour (24-hour clock, zero-padded)   | 00–23                     |
  +------+-------------------------------------+---------------------------+
  | %I   | Hour (12-hour clock, zero-padded)   | 01–12                     |
  +------+-------------------------------------+---------------------------+
  | %p   | AM/PM                               | AM, PM                    |
  +------+-------------------------------------+---------------------------+
  | %M   | Minute, zero-padded                 | 00–59                     |
  +------+-------------------------------------+---------------------------+
  | %S   | Second, zero-padded                 | 00–59                     |
  +------+-------------------------------------+---------------------------+
  | %f   | Microsecond, zero-padded            | 000000–999999             |
  +------+-------------------------------------+---------------------------+
  | %z   | UTC offset in ±HHMM format          | +0200                     |
  +------+-------------------------------------+---------------------------+
  | %Z   | Time zone name                      | UTC, CET, …               |
  +------+-------------------------------------+---------------------------+
  | %j   | Day of the year, zero-padded        | 001–366                   |
  +------+-------------------------------------+---------------------------+
  | %U   | Week number (Sunday as first day)   | 00–53                     |
  +------+-------------------------------------+---------------------------+
  | %W   | Week number (Monday as first day)   | 00–53                     |
  +------+-------------------------------------+---------------------------+
  | %c   | Locale's date and time              | Tue Oct 1 08:30:00 2025   |
  |      | representation                      |                           |
  +------+-------------------------------------+---------------------------+
  | %x   | Locale's date representation        | 10/01/25                  |
  +------+-------------------------------------+---------------------------+
  | %X   | Locale's time representation        | 08:30:00                  |
  +------+-------------------------------------+---------------------------+
  | %%   | A literal '%' character             | %                         |
  +------+-------------------------------------+---------------------------+

- Date & time operations:

  - substraction –> timedelta object:

    ::

       date - date --> timedelta
       datetime - datetime --> timedelta

       >>> from datetime import date
       >>> from datetime import datetime

       >>> d1 = date(2020, 11, 4)
       >>> d2 = date(2019, 11, 4)
       d1 - d2
       datetime.timedelta(days=366)
       >>> print(d1 - d2)
       366 days, 0:00:00

       >>> d1 = datetime(2019,11,27, 11, 27, 22)
       >>> d2 = datetime(2019,11,27, 0, 0, 0)
       datetime.timedelta(seconds=41242)
       >>> print(d1 - d2)
       11:27:22

    Prints days, if timedelta > 24 hours:

    ::

       >>> d3 = datetime(1990, 12, 24, 11, 27, 22)
       >>> d1 - d3
       datetime.timedelta(days=10565)
       >>> print(d1 - d3)
       10565 days, 0:00:00

  - create timedelta objects –> addition –> date/datetime objects:

    ::

       date + timedelta --> date
       timedate + timedelta --> datetime
       timedelta + timedelta --> timedelta

       >>> from datetime import timedelta
       >>> delta = timedelta(weeks=2, days=2, hours=2)
       >>> delta2 = timedelta(weeks=4, days=4, hours=4)

       >>> date(2019, 10, 4) + delta2
       datetime.date(2019, 10, 20)

       >>> datetime(2019, 10, 4, 14, 53) + delta2
       datetime.datetime(2019, 10, 20, 16, 53)

       >>> delta + delta2
       datetime.timedelta(days=48, seconds=21600)

calendar module
---------------

- ``calendar.setfirstweekday(calendar.SUNDAY)`` … set first weekday to
  sunday

- ``calendar.weekday(2020, 12,24)`` … return weekday index of given date
  (e.g. 3 for 4th day of the week –> Thursday)

- ``calendar.weekheader(width)`` … prints the weekday names at a width
  of 'width'

  ::

     >>> calendar.weekheader(2)
     'Mo Tu We Th Fr Sa Su'

- ``calendar.isleap(2020)`` … return boolean if year is a leap year

- ``calendar.leapdays(2010, 2021)`` … return amount of leap years
  between 2010 and 2020 ([end] is NOT included)

Calendar methods:

::

   >>> c = calendar.Calendar(calendar.SUNDAY) ... create calendar with first week day is sunday (default: Monday)

   >>> for weekday in c.iterweekdays():        ... return iterator for weekday numbers for one week
   ...     print(weekday, end= " ")
   6 0 1 2 3 4 5

   >>> for date in c.itermonthdates(2019, 11):   ... return iterator for all days in 'month' in 'year' as datetime.date objects
   ...    print(date, end=" ")
   2019-10-28 2019-10-29 2019-10-30 2019-10-31 2019-11-01 ... 2019-11-30 2019-12-01

   IMPORTANT: always returns entire weeks if it contains at least one day within given month

   >>> for data in c.monthdays2calendar(2022, 10):     ... returns list of full weeks, containing tuples of (day_number, weekday_number) 
   ...     print(data)
   [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 5), (2, 6)]
   ...
   [(31, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6)]

   IMPORTANT: day_number == 0 means, the day is outside of the month, first day of the month starts with 1

loops
-----

- ``continue`` … skips current loop and continues to the next
- ``break`` … ends loop (IMPORTANT: 'else' blocks are NOT executed if
  loop ends with 'break')

while-else:

::

   while [condition]:
       // do something
       if [condition]:
           break    // end loop (even if condition is still True)
       else:
           continue  // next cycle
       // unreachable code
   else:
       // code executed if 'break' does NOT happen
       // code is also executed if while loop is never entered 

for-else:

::

   for [elem in iterable]:
       // do something
       if [condition]:
           break    // end loop (even if condition is still True)
       else:
           continue  // next cycle
       // unreachable code
   else:
       // code executed if 'break' does NOT happen
       // code is also executed if for loop is never entered 

Some exceptions
---------------

::

   BaseException
      +---Exception
      |   +---ArithmeticError
      |   |   +---FloatingPointError
      |   |   +---OverflowError
      |   |   +---ZeroDivisionError
      |   +---AssertionError
      |   +---AttributeError
      |   +---ImportError
      |   |   +---ModuleNotFoundError
      |   |   +---ZipImportError
      |   +---LookupError
      |   |   +---IndexError
      |   |   +---KeyError
      |   |   +---CodecRegistryError
      |   +---MemoryError
      |   +---OSError
      |   |   +---ConnectionError
      |   |   +---FileExistsError
      |   |   +---FileNotFoundError
      |   |   +---TimeoutError
      |   |   +---UnsupportedOperation
      |   +---ReferenceError
      |   +---RuntimeError
      |   +---SyntaxError
      |   |   +---IndentationError
      |   +---SystemError
      |   +---TypeError
      |   +---ValueError
      |   |   +---UnicodeError
      |   |   |   +---UnicodeDecodeError
      |   |   |   +---UnicodeEncodeError
      |   |   |   +---UnicodeTranslateError
      |   |   +---UnsupportedOperation
      |   +---InterpreterError
      |   |   +---InterpreterNotFoundError
      |   +---ClassFoundException
      +---KeyboardInterrupt

IMPORTANT: A SyntaxError is raised even BEFORE the code is run

try-except
----------

- following syntax:

  ::

     try:
         // do something which might raise error
     except [some_error_type]:
         // handle error
     except [(some_other_error_type, yet_another_error_type)]:
         // handle these other errors
     except:
         // handle every other error (must come last, otherwise --> SyntaxError)
     else:
         // execute only if no exception occured (no except-block was executed)
     finally:
         // always executed regardless error is raised or not

- a SyntaxError is already raised BEFORE runtime, so

  ::

     def func(x,y):
         return x/(y-4)

     try:
         print(func(x=1,4))
     except ArithmeticError:
         print("ArithmeticError")
     except ZeroDivisionError:
         print("ZeroDivisionError")
     except:
         print("Misc. Error")

  raises a SyntaxError for 'func(x=1,4)' (positional argument follows
  keyword argument), but does NOT enter the bare except clause, printing
  “Misc Error”

- general 'except' MUST be the LAST except statement, otherwise raises
  SyntaxError:

  ::

     def func(x,y):
         return x/y

     try:
         func(3,0)
     except:
         print("Error 1")
     except ZeroDivisionError:
         print("Error 2")
     except BaseException:
         print("Error 3")

     >>> SyntaxError

- Exceptions save its constructor arguments in the 'args' attribute,
  which is a tuple:

  ::

     >>> try:
     >>>    raise Exception("This is bad", "very bad")
     >>> except Exception as e:
     >>>    print(type(e.args))
     >>>    print(e.args)

     <class 'tuple'>
     ('This is bad', 'very bad')

  Important: The order in which the arguments are put into the
  exception's constructur is the order of the 'args' tuple

- uses braces to handle multiple exception types in one statement, e.g.

  ::

     try:
         // do something risky
     except (ArithmeticError, LookupError):
         // handle it

assert expression[, expression]
-------------------------------

- a failed assert always raises an AssertionError (hence it must be put
  into try-except structure)

- assert fails for 0, False, ““, [], {}, () (a.k.a falsy)

- optional second expression [, expression] is passed to raised
  exception:

  ::

     >>> try:
     >>>    assert 1 < 0, "this is bad"
     >>> except Exception as e:
     >>>    print(e)
     this is bad

  –> prints “this is bad” to console, not the Exception e

Operators
---------

Arithmetic:

- ``+`` … addition

- ``-`` … substraction

- ``*`` … multiplication

- ``/`` … division

- ``%`` … modulus (2 % 2 = 0)

- ``**`` … exponentiation (``2**3 = 8``) – Careful: strings like '2' are
  NOT transformed to integers: ``'2'**3`` –> TypeError

- ``//`` … floor division:

  ::

       5 // 2 -->   5 / 2 = 2.5 dann math.floor(2.5) -> 2,
       -7 // 2 -->  -7 / 2 = -3.5 dann math.floor(-3.5) -> -4
       5 // 2.0 --> 2.0 (floor division does NOT cast result into integer)

Comparison:

- ``==`` … equals:

  Careful:

  ::

       objA == objB --> compares the string representation of two objects
       objA is objB --> compares identity of two objects (True, if both point to same object)

- ``!=`` … not equals

- ``<`` / ``>`` … value comparison - does only work for two objects of
  the SAME TYPE (e.g. not for string and integer)

Identity:

- ``is`` … True, if both variables point to same object
- ``is not`` … True, if both variables point to different objects

Logical:

- ``and``: [statement_a] and [statement_b] -> returns True, if both
  statments are True
- ``or``: [statement_a] or [statement_b] -> returns True, if any
  statments is True
- ``not``: not([statement_a] and [statement_b]) -> reverses the result
  (e.g. True –> False)

Bitwise:

- ``^`` … bitwise XOR: compares each bit, set it to 1 if only one is 1,
  otherwise 0:

  ::

     6 ^ 3:  0000 0110
             0000 0011
             ---------
             0000 0101 = 5

- ``|`` … bitwise or: compares each bit, sets it to 1 if one or both are
  1, otherwise 0:

  ::

     6 | 3:  0000 0110
             0000 0011
             ---------
             0000 0111 = 7

- ``&``. … bitwise and: compare each bit, sets it to 1 if both are 1,
  otherwise 0:

  ::

     6 & 3: 0000 0110

             0000 0011
             ---------
             0000 0010 = 2

- ``<<`` … bitwise LEFT shift:

  ::

     1 << 1:  0000 0001
              0000 0010 = 2

- ``>>`` … bitwise RIGHT shift:

  ::

     8 >> 1: 0000 1000
             0000 0100 = 4

  Important: If shift exceeds right limit, e.g. 8 >> 5, the 1-bits “move
  out-of-scope” the bit-values all become zero:

  ::

     8 >> 5: 0000 1000
             0000 0000 = 0

- Order of precedence (highest to lowest):

  - parentheses: (…)

  - exponentiation: \*\*

  - unary + / - (signs, e.g. -4)

  - Multiplication, Division, Floor Division, Modulus (left to right):
    ``*  /  //  %``

  - binary + / - (addition, subtraction)

  - (all bitwise operations follow here)

    ::

       <<  >>
       &
       ^
       |

  - Comparing / identity / membership operators (within section, all
    equal):

    ::

       in
       not in
       is
       is not
       ==
       !=
       <=
       >=
       <
       >

  - (boolean operations follow here)

    ::

       not x
       and
       or

    - IMPORTANT: 'and' is evaluated BEFORE 'or'

    - IMPORTANT: 'and' exactly means: “Return the first falsy value, or
      the last value if none are falsy.”

      ::

         >>> 0 and 100
         0
         >>> 1 and 99
         99

Object <–> Class
----------------

- Only for Classes (NOT for objects): ``__bases__``, ``__name__``

  - ``__bases__`` returns a tuple containing the types of all direct
    superclasses
  - ``__name__`` returns the name of the class as string

- For Classes AND objects: ``__dict__``, ``__module__`` (name of module)

  - ``__dict__`` returns a dictionary containing key-value pairs of all
    attributes of the class/object, which includes:

    - object only: INSTANCE VARIABLES (including hidden ones, like
      self.\__hidden)

      ::

         - defined in constructor (hidden ones via name mangling: myobj._Classname__defined_in_constructor)
         - defined outside constructor (hidden ones without name mangling: myobj.__defined_outside_constructor)

    - class only:

      ::

         * CLASS VARIABLES (CAREFUL: class variables from parent classes are NOT listed here, though present from inheritance)
         * methods (e.g. 'mymethod' : function MyClass.mymethod at ...)
         * special methods. e.g.

             * ``__dict__`` ('__dict__': <attribute '__dict__' of 'C' objects>)
             * ``__doc__`` (e.g. '__doc__': None)
             * ``__module__`` (e.g. '__module__': '__main__')
             * ``__init__`` (e.g. '__init__': <function C.__init__ at ...)

    - Name mangling needed:

      - Yes, for hidden instances variables defined INSIDE of the CLASS
        DEFINITION
      - No, for hidden instance variables defines OUTSIDE of the CLASS
        DEFINITION (e.g. my_object.\__new_attr = 0 –> \__new_attr)

- Call the parent class' constructor - methods:

  ::

     class Alpha:
         def __init__(self, val):
             self.a = val

  - reference parent class by name (needs passing subclass as 'self')

    ::

       class Beta(Alpha):
           def __init__(self, x, y):
               Alpha.__init__(self, x)

       # ParentClass.__init__(self) requires 'self'

  - reference parent class by super() (does NOT need 'self')

    ::

       class Beta(Alpha):
           def __init__(self, x, y):
               super().__init__(x)

    - ``super()`` itself does NOT take any arguments and references the
      nearest superclass of the class
    - ``super().__init__()`` does NOT require 'self' to be passed

Inheritance
-----------

Python looks for object components (attributes, methods) in the
following order:

::

   1. inside the object itself;
   2. in its superclasses, from bottom to top;
   3. if there is more than one class on a particular inheritance path, Python scans them from left to right.

Method Resolution Order
-----------------------

Rule: If a class inherits from multiple parent classes, the order in
which they are declared from left to right must match the order of
inheritance, so that it's methods are resolved in a consistent way.

Example:

::

   class Top:
       def m_top(self):
           print("top")


   class Middle(Top):
       def m_middle(self):
           print("middle")


   class Bottom(Top, Middle):
       def m_bottom(self):
           print("bottom")


   object = Bottom()

This WON'T WORK, because

- 'Middle' sets the resolution order Middle –> Top
- but 'Bottom' set the order Bottom –> Top –> Middle (Bottom –> Top –>
  Middle means, search for method in 'Bottom' first, if not found, got
  to 'Top', last go to 'Middle')

Generators
----------

Basic structure (Example):

::

   class MyGenerator:

       def __init__(self):
           self.i = 0
           self.numbers = [1,2,3]

       def __iter__(self):
           return self     # could also return a different generator class (then __next__(self) must not be implemented here)

       def __next__(self):
           if self.i >= len(self.numbers):
               raise StopIteration
           self.i += 1
           return self.numbers[self.i-1]

   >>> g = MyGenerator()
   >>> for n in g:
   ...     print(n)
   1
   2
   3

Using ``yield``: Advantage is that 'MyGenerator' instance maintains its
state (here: value of ``i``) after returning a value

::

   class MyGenerator:

       def __init__(self):
           self.numbers = [1,2,3]

       def __iter__(self):
           self.i = 0
           while self.i in range(len(self.numbers)):
               yield self.numbers[self.i]
               self.i += 1

   >>> g = MyGenerator()
   >>> for n in g:
   ...     print(n)
   1
   2
   3

Strings
-------

- Strings are IMMUTABLE !!!

  ::

     >>> s = "ABC"
     >>> s[:-1] = "A"
     TypeError

- String literals (e.g. ``'\n'``)

  - MUST always be complete, e.g. ``'\'`` is not a valid string –>
    SyntaxError
  - count as one string character (e.g. ``len('\n') --> 1``)

- chr(index_number) –> returns character at index position (UTF-8)

- ord(single_character_string) –> returns index number of character
  (UTF-8)

- Two strings of the SAME VALUE will point to the SAME OBJECT only if:

  - those are short (less than 20 characters)
  - do not contain any whitespace, punctuation or most special
    characters

  ::

     >>> a = "foo"
     >>> b = "foo"
     >>> id(a) == id(b)
     True

- Slicing: string[start:end:stepwidth]

  - Defaults start + end:

    - if stepwidth > 0: start = 0, end = len(str)
    - if stepwidth < 0: start = len(str), end=0

  - Default stepwidth: 1 (cannot be 0 –> ValueError)

  - [end] index is NOT included in result

  - [end] can be outside of length of the string, DOES NOT raise error
    (e.g IndexError).

    - if end > len(str) the end border is the LAST character

      ::

         >>> x = "hello"
         >>> x[:20]
         hello

    - negative stepwidth: if -end < -len(str), end border is the FIRST
      character (there no character left from the first character)

      ::

         >>> x = "hello"
         >>> x[:-20:-1]
         'olleh'

  - no matter which [stepwidth], the FIRST (if positive stepwidth) or
    the LAST (if negative stepwidth) is always included

    ::

       >>> x = "hello"
       >>> x[::10000]
       'h'
       >>> x[::-10000]
       'o'

  - sliced string is built up character per character (for negative
    [stepwidth], the highest index comes first)

    ::

       >>> x = "abcdef"
       >>> x[::-2]
       fdb

  - if [start] left from [end] (range: right direction) but [stepwidth]
    is negative (left direction) -> **empty string** is returned

  - if [start] right from [end] (range: left direction) but [stepwidth]
    is positive (right direction) -> **empty string** is returned

    ::

       [start] .... [end] & [stepwidth]
       ----------------->   <----------

       [end] .... [start] & [stepwidth]
       <-----------------   ---------->

    ::

       >>> x = "hello"
       >>> x[0:-10:1]  # range left direction & stepwith right direction
       ''
       >>> x[0:10:-1] # range right direction & stepwidth left direction
       ''

Methods:

- ``"hello".index("r")`` raises ValueError, NOT return False or -1

- ``"find".find("in",1,3)`` searches for “in” within index 1 to 3
  (exclusive), returns the lowest index where “in” is found or -1 (not
  found).

  - index range MUST completely contain searched term i.e.:

    ::

       >>> "find".find("in",1,2)
       -1
       >>> "find".find("in",1,3)
       1

  - index numbers can be negative but range must be from left to right:

    ::

       >>> "find".find("in",-4,-1)
       1
       >>> “find”.find(“in”,-1,-4)
       -1

- ``"find".rfind("in",1,3)`` does same as 'find', but returns highest
  found occurences index number

- ``"hello world".capitalize()`` returns “Hello world” (only the first
  character is capitalized, all others lower case)

- ``"hello world".title()`` returns “Hello World” (first letter of each
  word is capitalized, all others lower case)

  ::

     >>> "I know noTHING".title()
     'I Know Nothing'

- ``"hello".isalpha()`` returns True if string only contains letter A-Z
  and a-z

- ``"hello".isdigit()`` returns True if string only contains letter 0-9

- ``"hello".isalnum()`` returns True if string only contains letters
  A-Z, a-z and 0-9

- ``"hello".isspace()`` returns True if string consists only of
  whitespace characters (``' ', '\n', '\t', '\n' or '\r'``)

- ``"hello".islower()`` returns True if all characters are lower case
  alphabetic

- ``"hello".isupper()`` returns True if all characters are upper case
  alphabetic

- ``"hello".count("l")`` counts the occurences of the search string “l”
  inside the string, here returns 2

- ``"hello".center(10)`` returns a string being centered within the
  specified width (here: 10), so ” hello ” (if space cannot be equally
  divided, the extra space is put AFTER the string, here 2 before and 3
  after the string)

- ``"hello".strip()`` removes all leading and trailing whitespace
  characters from string (combines ``lstrip()`` and ``rstrip()``)

- ``"[separator_string]".join([iterable])`` –> generates single string
  out of list of strings ([iterable]), putting [separator_string]
  between each element

  ::

     >>> " ".join(["a", "b", "c"])
     "a b c"

- ``"hello".replace("e", "a", count=None: int)`` –> returns new string
  where all occurences of “e” are replaced with “a” –> “hallo” if
  'count' is given, the only the first 'count' occurences are replaced

- ``"foo bar\nfoo".split()`` splits a string at each WHITESPACE
  character (``' ', '\n', '\t', '\n' or '\r'``) and returns in in a list
  –> [“foo”, “bar”, “foo”] –> the split character itself is removed, for
  example “foobar”.split(“b”) returns [“foo”, “ar”]

- ``"hello".swapcase()`` changes the case of each string character:

  ::

     >>> "I know nothing".swapcase()
     'i KNOW NOTHING'

- ``"hello".endswith("lo")`` returns True if string ends with substring

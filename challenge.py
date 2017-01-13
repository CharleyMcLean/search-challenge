# * Search an array of sorted numbers.
# *
# * items    : An array of sorted ints, with no duplicates
# * n_items  : Number of elements in the items array
# * ascending: non-zero if the array is sorted in ascending order
# * key      : the key to search for
# * type     : the type of match to find
# *
# * This function finds the element in the array
# * that best fits the search criteria. It returns
# * the match type and the index of the matching item.
# *
# * LessThan
# * --------
# *  Finds the largest item which is less than the key.
# *  It returns FoundLess if a match is found, NotFound
# *  if no match is found.
# *
# * LessThanEquals
# * --------------
# *  Finds the item which is equal to the key, or the
# *  largest item which is less than the key. Returns
# *  FoundExact if an item that exactly matches the key
# *  is found, FoundLess if a non-exact match is found
# *  and NotFound if no match is found.
# *
# * Equals
# * ------
# *  Finds an item which is equal to the key. Returns
# *  FoundExact if an item if found, NotFound otherwise.
# *
# * GreaterThanEquals
# * -----------------
# *  Finds the item which is equal to the key, or the
# *  smallest item which is greater than the key. Returns
# *  FoundExact if an item that exactly matches the key
# *  is found, FoundGreater if a non-exact match is found
# *  and NotFound if no match is found.
# *
# * GreaterThan
# * -----------
# *  Finds the smallest item which is greater than the
# *  key. Returns FoundGreater if a match if found, NotFound
# *  if no match is found.
# *
# * Examples
# * --------
# *  Given the input array [0, 2, 4, 6, 8] (ascending order)
# *
# *  +-----+-------------------+--------------+-------+
# *  | Key | Type              | Returns      | Index |
# *  +-----+-------------------+--------------+-------+
# *  | -1  | LessThanEquals    | NotFound     | X     |
# *  +-----+-------------------+--------------+-------+
# *  |  0  | LessThan          | NotFound     | X     |
# *  +-----+-------------------+--------------+-------+
# *  |  0  | Equals            | FoundExact   | 0     |
# *  +-----+-------------------+--------------+-------+
# *  |  1  | Equals            | NotFound     | X     |
# *  +-----+-------------------+--------------+-------+
# *  |  2  | GreaterThanEquals | FoundExact   | 1     |
# *  +-----+-------------------+--------------+-------+
# *  |  2  | GreaterThan       | FoundGreater | 2     |
# *  +-----+-------------------+--------------+-------+
# *
# *  Given the input array [8, 6, 4, 2, 0] (descending order)
# *
# *  +-----+-------------------+--------------+-------+
# *  | Key | Type              | Returns      | Index |
# *  +-----+-------------------+--------------+-------+
# *  | -1  | LessThan          | NotFound     | X     |
# *  +-----+-------------------+--------------+-------+
# *  |  0  | LessThan          | NotFound     | X     |
# *  +-----+-------------------+--------------+-------+
# *  |  4  | LessThanEquals    | FoundExact   | 2     |
# *  +-----+-------------------+--------------+-------+
# *  |  8  | Equals            | FoundExact   | 0     |
# *  +-----+-------------------+--------------+-------+
# *  |  5  | GreaterThanEquals | FoundGreater | 1     |
# *  +-----+-------------------+--------------+-------+
# *  |  2  | GreaterThanEquals | FoundExact   | 3     |
# *  +-----+-------------------+--------------+-------+
# *  |  8  | GreaterThan       | NotFound     | X     |
# *  +-----+-------------------+--------------+-------+
# *  |  9  | GreaterThan       | NotFound     | X     |
# *  +-----+-------------------+--------------+-------+
# *
# * Assumptions
# * -----------
# *  The items are sorted
# *  Items will be non-NULL
# *  There are no duplicate items
# *  n_items will be > 0


def match_search_criteria(lst, key, criteria):
    """This function finds the element in the array that best fits the
    search criteria. It returns the match type and the index of the
    matching item.
        >>> match_search_criteria([0, 2, 4, 6, 8], -1, 'LessThanEquals')
        'NotFound'
        >>> match_search_criteria([0, 2, 4, 6, 8], 0, 'LessThan')
        'NotFound'
        >>> match_search_criteria([0, 2, 4, 6, 8], 0, 'Equals')
        ('FoundExact', 0)
        >>> match_search_criteria([0, 2, 4, 6, 8], 1, 'Equals')
        'NotFound'
        >>> match_search_criteria([0, 2, 4, 6, 8], 2, 'GreaterThanEquals')
        ('FoundExact', 1)
        >>> match_search_criteria([0, 2, 4, 6, 8], 2, 'GreaterThan')
        ('FoundGreater', 2)

        >>> match_search_criteria([8, 6, 4, 2, 0], -1, 'LessThan')
        'NotFound'
        >>> match_search_criteria([8, 6, 4, 2, 0], 0, 'LessThan')
        'NotFound'
        >>> match_search_criteria([8, 6, 4, 2, 0], 4, 'LessThanEquals')
        ('FoundExact', 2)
        >>> match_search_criteria([8, 6, 4, 2, 0], 8, 'Equals')
        ('FoundExact', 0)
        >>> match_search_criteria([8, 6, 4, 2, 0], 5, 'GreaterThanEquals')
        ('FoundGreater', 1)
        >>> match_search_criteria([8, 6, 4, 2, 0], 2, 'GreaterThanEquals')
        ('FoundExact', 3)
        >>> match_search_criteria([8, 6, 4, 2, 0], 8, 'GreaterThan')
        'NotFound'
        >>> match_search_criteria([8, 6, 4, 2, 0], 9, 'GreaterThan')
        'NotFound'
    """

    # check criteria using helper functions
    if criteria == 'LessThan':
        return find_less_than(lst, key)
    elif criteria == 'LessThanEquals':
        return find_less_than_equals(lst, key)
    elif criteria == 'Equals':
        return find_equals(lst, key)
    elif criteria == 'GreaterThanEquals':
        return find_greater_than_equals(lst, key)
    else:
        return find_greater_than(lst, key)


# helper functions:
def find_less_than(lst, key):
    """Finds the largest item which is less than the key.  It returns
    FoundLess if a match is found, NotFound if no match is found."""

    current = min(lst)
    current_index = 0

    for i in range(len(lst)):
        if key < lst[i] and lst[i] <= min(lst):
            return 'NotFound'
        elif lst[i] < key and lst[i] > current:
            current = lst[i]
            current_index = i

    if not current:
        return 'NotFound'
    else:
        return 'FoundLess', current_index


def find_less_than_equals(lst, key):
    """Finds the item which is equal to the key, or the largest item which
    is less than the key. Returns FoundExact if an item that exactly matches
    the key is found, FoundLess if a non-exact match is found and NotFound
    if no match is found."""

    # first check if key is in list
    if key in lst:
        return 'FoundExact', lst.index(key)

    # if key not in list, call the find_less_than function.
    return find_less_than(lst, key)


def find_equals(lst, key):
    """Finds an item which is equal to the key. Returns FoundExact if an
    item if found, NotFound otherwise."""

    # check if key is in the list
    if key in lst:
        return 'FoundExact', lst.index(key)

    return 'NotFound'


def find_greater_than_equals(lst, key):
    """Finds the item which is equal to the key, or the smallest item
    which is greater than the key. Returns FoundExact if an item that
    exactly matches the key is found, FoundGreater if a non-exact match
    is found and NotFound if no match is found."""

    # first check if key is in list
    if key in lst:
        return 'FoundExact', lst.index(key)

    # if key not in list, call the find_greater_than function.
    return find_greater_than(lst, key)


def find_greater_than(lst, key):
    """Finds the smallest item which is greater than the key. Returns
    FoundGreater if a match if found, NotFound if no match is found."""

    current = max(lst)
    current_index = 0

    for i in range(len(lst)):
        if key > lst[i] and key >= max(lst):
            return 'NotFound'
        elif lst[i] > key and lst[i] < current:
            current = lst[i]
            current_index = i

    if not current:
        return 'NotFound'
    else:
        return 'FoundGreater', current_index


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

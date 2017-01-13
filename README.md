# Search an array of sorted numbers.


**items**: An array of sorted ints, with no duplicates<br/>
**n_items**: Number of elements in the items array<br/>
**ascending**: non-zero if the array is sorted in ascending order<br/>
**key**: the key to search for<br/>
**type**: the type of match to find<br/>

This function finds the element in the array that best fits the search criteria. It returns the match type and the index of the matching item.

**LessThan**:  Finds the largest item which is less than the key.  It returns FoundLess if a match is found, NotFound if no match is found.

**LessThanEquals**:  Finds the item which is equal to the key, or the largest item which is less than the key. Returns FoundExact if an item that exactly matches the key is found, FoundLess if a non-exact match is found and NotFound if no match is found.

**Equals**:  Finds an item which is equal to the key. Returns FoundExact if an item if found, NotFound otherwise.

**GreaterThanEquals**:  Finds the item which is equal to the key, or the smallest item which is greater than the key. Returns FoundExact if an item that exactly matches the key is found, FoundGreater if a non-exact match is found and NotFound if no match is found.

**GreaterThan**:  Finds the smallest item which is greater than the key. Returns FoundGreater if a match if found, NotFound if no match is found.


**Examples**:

Given the input array `[0, 2, 4, 6, 8]` (ascending order)

+-----+-------------------+--------------+-------+<br/>
| Key | Type              | Returns      | Index |<br/>
+-----+-------------------+--------------+-------+<br/>
| -1  | LessThanEquals    | NotFound     | X     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  0  | LessThan          | NotFound     | X     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  0  | Equals            | FoundExact   | 0     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  1  | Equals            | NotFound     | X     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  2  | GreaterThanEquals | FoundExact   | 1     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  2  | GreaterThan       | FoundGreater | 2     |<br/>
+-----+-------------------+--------------+-------+<br/>


Given the input array `[8, 6, 4, 2, 0]` (descending order)

+-----+-------------------+--------------+-------+<br/>
| Key | Type              | Returns      | Index |<br/>
+-----+-------------------+--------------+-------+<br/>
| -1  | LessThan          | NotFound     | X     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  0  | LessThan          | NotFound     | X     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  4  | LessThanEquals    | FoundExact   | 2     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  8  | Equals            | FoundExact   | 0     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  5  | GreaterThanEquals | FoundGreater | 1     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  2  | GreaterThanEquals | FoundExact   | 3     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  8  | GreaterThan       | NotFound     | X     |<br/>
+-----+-------------------+--------------+-------+<br/>
|  9  | GreaterThan       | NotFound     | X     |<br/>
+-----+-------------------+--------------+-------+<br/>


**Assumptions**:  
- The items are sorted
- Items will be non-NULL
- There are no duplicate items
- n_items will be > 0

## <a name="technologies"></a>Technologies
Tech Stack: Python<br/>

## <a name="features"></a>Features

Search an array of sorted items.


## <a name="install"></a>Installation

To run the search:

Clone or fork this repo:

```
https://github.com/CharleyMcLean/search-challenge.git
```

Run the app:

```
python -i challenge.py
```

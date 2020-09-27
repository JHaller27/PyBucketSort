# Radix Sort

This implementation is classy (object-oriented) with an optional functional entry-point.

It's also semi-generic, meaning multiple types can be sorted, but types beyond ascii-strings and integers will need their own implementation.

# Usage

If you only need to sort collections of integers or ascii-strings, you can don't need to do anything special.

Note that the collections to be sorted can be any kind of iterable, but they will be converted to a list immediately.

## Usage: Functional

```python
import radix_sort as rs

# Get some data

sorted_data = rs.sorted(some_data)
```

## Usage: Classy

```python
import radix_sort as rs

# Get some data

# Choose one line from the following block
# or use a custom TypeStrategy class
type_strategy = IntStrategy()
type_strategy = AsciiStrategy()

sorter = rs.RadixSort(type_strategy)

sorted_data = sorter.sorted(some_data)
```

# Adding New Type Support

If you need to support a collection of values not supported by default,
all you need to do is create a new class and inherit from the `TypeStrategy` class.

You MUST follow the type annotations on the `TypeStrategy` class.

Once you've created your new Strategy, pass it into the `RadixSort` constructor as in the _Usage: Classy_ section above.

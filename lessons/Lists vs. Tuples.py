# |----------------------------------------------------|----------------------------------------------------|
# |                        Lists                       |                       Tuples                       |
# |----------------------------------------------------|----------------------------------------------------|
# | Mutability                                         | Mutability                                         |
# | Lists are mutable, meaning the elements of a       | Tuples are immutable, meaning once a tuple is      |
# | list can be changed, added, or removed after       | created, its elements cannot be changed, added,    |
# | it is created.                                     | or removed.                                        |
# |----------------------------------------------------|----------------------------------------------------|
# | Use Cases                                          | Use Cases                                          |
# | Lists are used when you need a collection of       | Tuples are used for fixed collections of items.    |
# | items that can change during program execution.    | They are suitable for read-only data or            |
# | They are suitable for tasks like appending,        | ensuring data remains constant throughout a        |
# | deleting, or modifying elements.                   | program.                                           |
# |                                                    |                                                    |
# | Example:                                           | Example:                                           |
# | my_list.append(4)                                  | my_tuple = (1, 2, 3)                               |
# | # Adds an element to the list                      | # This tuple will not change                       |
# |----------------------------------------------------|----------------------------------------------------|
# | Performance                                        | Performance                                        |
# | Lists have a slight performance overhead due       | Tuples, being immutable, are generally more        |
# | to their mutability because they need to account   | memory-efficient and faster than lists in terms    |
# | for potential changes in size.                     | of access time.                                    |
# |----------------------------------------------------|----------------------------------------------------|
# | Functionality                                      | Functionality                                      |
# | Lists have a wide range of built-in methods for    | Tuples have fewer built-in methods and are         |
# | modifying them, such as append(), extend(),        | mainly focused on counting elements and finding    |
# | insert(), remove(), pop(), clear(), sort(), and    | their index (e.g., count() and index()).           |
# | reverse().                                         |                                                    |
# |                                                    |                                                    |
# | Example:                                           | Example:                                           |
# | my_list.sort()                                     | my_tuple.count(2)                                  |
# | # Sorts the list in-place                          | # Counts the number of occurrences of 2 in         |
# |                                                    | # the tuple                                        |
# |----------------------------------------------------|-------------------------------------------------   |

# When to Use Lists and Tuples
# Lists
# Use Lists When You Need:
#   A collection of items that can change over time
#   To add or remove elements frequently
#   To use list-specific methods like sorting or reversing
# Tuples
# Use Tuples When You Need or Want:
#   A collection of items that should remain constant
#   A lightweight, more memory-efficient alternative to lists
#   To ensure data integrity by preventing modification
#   To use them as dictionary keys, since keys must be immutable
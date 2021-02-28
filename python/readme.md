# Python Tutorial!


## Python Tutorial
1. Hello World
2. [Variables](https://www.w3schools.com/python/python_variables.asp)
3. [if statements](https://www.w3schools.com/python/python_conditions.asp)
4. [for loops](https://www.w3schools.com/python/python_for_loops.asp)
5. [while loops](https://www.w3schools.com/python/python_while_loops.asp)
6. [functions](https://www.w3schools.com/python/python_functions.asp)
7. [lists](https://www.w3schools.com/python/python_lists.asp)
8. [dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
9. [imports](https://www.digitalocean.com/community/tutorials/how-to-import-modules-in-python-3)
10. [classes](https://www.w3schools.com/python/python_classes.asp)

## To-Do List 
1. In `square_root.py`, write a function that returns the square root of a given integer `n`. If `n` is negative or not a number (i.e. `n` is a string), return `-1`.

2. In `random_ints.py`, write a program that randomly generates a number from the range [1,10] inclusive, appends it to the list `l`, and repeats this process until a `7` is generated and appended to `l`, at which point the program should return `l`.

    Hint: what does `(int) (random.random()*10)` generate? Can you adjust the range of its output?

3. In `sum.py`, write a program that takes a list `l` and a number `N` and returns `True` if any two distinct numbers in the list sum to `N`, and `False` otherwise.

    For example: given `l = [1, 2, 4, 5, 6]` and `N = 10`, the program should return `True`, because `4 + 6 = 10`.
    
    Hint: Use `set()`!

4. In `rm_smallest.py`, write a program that, given a dictonary, removes the key corresponding to the minimum value and returns the updated dictonary. If the dictionary is empty, the program should return the original dictionary.

    For example on input:
    ```Python
    sampleDict = {
      'Physics': 82,
      'Math': 65,
      'history': 75
    }
    ```
    The returned output should be:
    ```Python
    sampleDict = {
      'Physics': 82,
      'history': 75
    }
    ```


## Optional:
* In company.py, define a class to represent companies. Companies should have a name (given at creation), a catalog (a dictionary of products and their prices, represented by strings and integers, respectively), and a list of current employees.

* Define a function to add a new product to the catalog. The function should take the name of the product and the price as arguments.

* Define a function to add an employee to the list of current employees. The function should take the name of the new employee as an argument.

* Define an employee class. Employees should have a name, a company, and a role, all given at creation. An employee's role should be represented by a number (i.e. `1` is a new hire, while `10` is the CEO). Make the role value optional, with the default set to `1`.
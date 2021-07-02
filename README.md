# Excercise 1: Recursive Functions

![animation of quicksort algorithm](docs/quicksort.gif)

# Getting started

1. Ensure that you have python installed in your path
2. Install pip
    ```
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    ```
2. Install dependencies
    ```
    python -m pip install pytest
    ```
3. Verify that test runs by invoking `pytest` in the root of the repository. 
The output should indicate that all tests currently fail:
    ```
    pytest
    ============================ test session starts ============================
    platform linux -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /home/clegaard/Desktop/repos/github-classrooms-demo
    collected 1 item
    test_quicksort.py F

    ...

    FAILED test_quicksort.py::test_quicksort - assert [2, 3, -9, -2, 6, 5, ...] == [-9, -2, -1, 1, 2, 2, ...]
    ```

# Exercise

## Quicksort
The objective of the exercise is to implement a quicksort algorithm used to sort arrays of numbers.


1. Implement the function `quicksort` defined in the `quicksort.py` script.
2. Run tests to verify that the `test_quicksort` test case passes


## Fibonacci
...

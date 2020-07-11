### NumPy Notes

- NumPy is a python library used for working with arrays.
- NumPy aims to provide an array object that is up to 50x faster that traditional Python lists.
- The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
- NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.This behavior is called locality of reference in computer science. This is the main reason why NumPy is faster than lists. 
- To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray
- Slicing in python means taking elements from one given index to another given index.


- below is a list of all data types in NumPy and the characters used to represent them.
    - i - integer
    - b - boolean
    - u - unsigned integer
    - f - float
    - c - complex float
    - m - timedelta
    - M - datetime
    - O - object
    - S - string
    - U - unicode string
    - V - fixed chunk of memory for other type ( void )
- **ValueError:** In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.
- The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
- The shape of an array is the number of elements in each dimension.
- Reshaping means changing the shape of an array. By reshaping we can add or remove dimensions or change number of elements in each dimension. Yes, as long as the elements required for reshaping are equal in both shapes. We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array but we cannot reshape it into a 3 elements 3 rows 2D array as that would require 3x3 = 9 elements. The reshape returns the original array, so it is a view 
- The function **nditer()** is a helping function that can be used from very basic to very advanced iterations.
- Sometimes we require corresponding index of the element while iterating, the **ndenumerate()** method can be used for those usecases.
- Joining means putting contents of two or more arrays in a single array. In SQL we join tables based on a key, whereas in NumPy we join arrays by axes. We pass a sequence of arrays that we want to join to the **concatenate()** function, along with the axis. If axis is not explicitly passed, it is taken as 0.
- Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
- Splitting is reverse operation of Joining. We use **array_split()** for splitting arrays, we pass it the array we want to split and the number of splits.
- You can search an array for a certain value, and return the indexes that get a match. To search an array, use the where() method.
- There is a method called **searchsorted()** which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order. By default the left most index is returned, but we can give side='right' to return the right most index instead.
- Sorting means putting elements in a ordered sequence. Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending. The NumPy ndarray object has a function called **sort()**, that will sort a specified array. This method returns a copy of the array, leaving the original array unchanged.
- Getting some elements out of an existing array and creating a new array out of them is called filtering. In NumPy, you filter an array using a boolean index list. A boolean index list is a list of booleans corresponding to indexes in the array. If the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.

## Random Numbers in NumPy
- NumPy offers the random module to work with random numbers.
- **randint** generates a random integer.
- **rand** generates a random float.
- **choice** The choice() method takes an array as a parameter and randomly returns one of the values.
- **size** the size parameter where you can specify the shape of an array.

_**Probability Density Function:** A function that describes a continuous probability. i.e. probability of all values in an array._

- Shuffle means changing arrangement of elements in-place. i.e. in the array itself. The NumPy Random module provides two methods for this: **shuffle()** and **permutation()**. The shuffle() method makes changes to the original array.
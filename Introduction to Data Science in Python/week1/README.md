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
- The function nditer() is a helping function that can be used from very basic to very advanced iterations.
- Sometimes we require corresponding index of the element while iterating, the ndenumerate() method can be used for those usecases.
- Joining means putting contents of two or more arrays in a single array. In SQL we join tables based on a key, whereas in NumPy we join arrays by axes. We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
- Stacking is same as concatenation, the only difference is that stacking is done along a new axis. 
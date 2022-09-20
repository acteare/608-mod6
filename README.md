# 608-mod6
## Chapter 9
### 9.1 - Introduction
- Files: Provide long-term retention of typically large amounts of data, even after the program that created the data terminates. 

### 9. 2 - Files
- text file: a sequence of characters
- Binary File: a sequence of bytes
- End-of-file marker: a mechanism to denote the end of a file
- Standard file objects:
  - sys.stdin -- the standard input file object
  - sys.stdout -- the standard output file object
  - sys.stderr -- the standard error file object
  
### 9.3 - Test-File Processing
Python's with statement:
  - acquires a resource and assigns its corresponding object to a variable
  - allows the application to use the resource via that variable, and
  - calls the resource object's close method to release the reousrce when program control reaches the end of the with statement's suite. 
- Open function: opens the file accounts.txt and associates it with a file object
- File-open mode: indicates whether to open a file for reading from the file, for writing to the file or both
- 'w': opens the file for writing, creating the file if it does not exist
    - (If you do not specify a path to the file, python creates it in the current folder. 
- .txt file extension: indicates a plain text file
- readlines method: used to read an entire text file. It returns each line as a string in a list of strings. 

### 9.4 - Updating Text Files
Formatted data written to a text file cannot be modified without the rsk of destroying other data. 
- os module: provides functions for interacting with the operating system, incuding several that manipulate your system's files and directories. 
- remove function: deletes the original file
- rename function: renames the file

### 9.5 - Serializationg with JSON
JavaScript Object Notation
- JSON: a text-based, human-and-computer-readable, data-interchange formate used to represent objects as collections of name-value pairs. 
- json module: enables you to convert objects to JSON text format
- load function: reads the entire JSON contents of its file object argument and converst the JSON into a Python object. (deserializing)
- dumps function: returns a Python string representation of an object in JSON format. When the dumps function call includes the indent keyword argument, the string contains newline characters and indentation for pretty printing -- you also can use indent with the dump function when writing to a file. 

### 9.6 - Focus on Security: pickle Serialization and Deserialization
- pickle module: can serialize objects into in a Python-specific data format. 
- legacy code: old code that's often no longer supported. 

### 9.7 Additional Notes Regarding Files

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
- read method: returns a string containing the number of characters specified by the method's integer argument
- readline method: returns one line of text as a string, including the newline character if there is one. 
- writeline method: receives a list of strings and writes its contents to a file. 

### 9.8 - Handling Exceptions
- FileNotFoundError occurs if you attempt to open a non-existent file for reading with the 'r' or 'r+' modes. 
- PermissionsError occurs if you attempt an operation for which you do not have permission
- ValueError occurs when you attempt to write to a file that has already been closed
- Raise an exception: When an exception is raised in IPython it:
    - terminates teh snippet
    - displays the exception's traceback
    - shows the next In [] prompt so you can input the next snippet
- try statements: used to enable exception handling. 
- except clause: immediately follow the try clause's suite. Each except clause specifies the type of exception it handles
- else clause: Specifies code that should execute only if the code in the try suite did not raise exceptions. 
- Raise point: The point in the program at which an exception occurs

### 9.9 - finally Clause
- resource leak: the file resources is not available to other programs because a program using the file never closes it
- finally clause: This clause is guaranteed to execute, regardless of whether its try suite executes successfully or an exception occurs. 

### 9.10 - Explicitly Raising an Exception
- raise statement: Explicitly raises an ecveptions. It creates an object of the specified exception class. 

### 9.11 - Stack Unwinding and Tracebacks
- stack unwinding: When an exception is not caught in a given function
- uncaught exception: When an exception is not caught

### 9.12
- csv module: Provides funtions for working with CSV files


## Chapter 17 - Big Data
### 17.1 - Introduction
- Databases: critical big-data infrastructure for storing and manipulating the massive amounts of data we're creating. 
- relational databases: store structured data in tables with a fixed-size number of columns per row.
  - These are manipulated using SQL

### 17.2 - Relational Databases and Structured Query Language (SQL)
- database: an integrated collection of data
- database management system (DBMS): proivdes mechanisms for storing and organizing data in a manner consistent with the database's format. 
- queries: request information that satisfies given criteria
- primary key: a column with a value that's unique for each row. 

#### 17.2.1 - A books Database
- CRUD: create, read, update, and delete
- connect function: used to connect to the database and obtain a Connection object
- read_sql: executes a SQL query and returns a DataFrame containing the query's results. 
- foreign key: a column in this table that matches a primary key column in another table. 
- Rule of Referential Integrity: Every foreign-key value must appear as the primary-ke value in a row of another table so the DBMS can ensure that the foreign-key value is valid.
- Rule of Entity Integrity: Every row must have a primary-key value, and that value must be unique in the table. 

#### 17.2.2 - SELECT Queries

#### 17.2.3 - WHERE Clause
- WHERE clause: specifies a query's selection criteria. 
- LIKE: is used for pattern matching
- pattern matching: searching for strings that match a given pattern.
- % wildcard: searches for strings that have zero or more characters at the percent character's position in the pattern. 
- underscore: indicates a single wildcard character at that position

#### 17.2.4 - ORDER BY Clause
- ORDER BY clause: sorts a query's results into ascending order (lowest to hightest) or descending order (highest to lowest), specified with ASC and DESC. The default is ascending. 

#### 17.2.5 - Merging Data from Multiple Tables: INNER JOIN
- INNER JOIN: Allows you to merge data from multiple tables, referred to as joining the tables.
- ON clause: uses a primary-key column in one table and a foreign-key column in the other to determine which rows to merge from each table. 

#### 17.2.6 - INSERT INTO Statement
- INSERT INTO statement: inserts a row into a table. 

#### 17.2.7 - UPDATE Statement
- UPDATE statement: modifies existing values. 

#### 17.2.8 - DELETE FROM statement
- DELETE FROM statement: removes rows from a table. 

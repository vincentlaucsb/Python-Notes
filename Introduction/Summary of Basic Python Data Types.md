# Summary of Basic Python Data Types
## Checkpoint
Here are some questions you should be able to answer after reading this section:

1. What are some basic Python data types?
1. Which data type is used for storing a sequence of characters?
1. Which data type is used for storing whole numbers?
1. Which data type is used for storing decimal numbers?

In addition, you should now be familiar with some of the things you can do to these data types. Of course, this is a lot to remember, so it's best to write it down or copy it so you can keep it handy. This will not be the last time you see these!

## Suggested Exercise
While copy and pasting might get you through some assignments in an introductory CS class, it won't teach you how to program. A quick exercise would be to come up with your own examples in addition to the ones provided below. Of course, you should try them out for yourself to make sure they work as intended.

## String Methods and Operations
Operation | Syntax | Input (Example) | Output (Example)
----------|--------|-----------------|------------------
Concatentation: Joining two strings | 'string 1' + 'string 2' | 'In' + 'separable' | 'Inseparable'
Concatentation: Using .format()     | '{0} {1}'.format('replacement text', 'replacement text') | 'I would like a {0}'.format('burger') | 'I would like a burger'
Repetition 	                        | 'string' * n *(where n is some number)* | 'Echo' * 5 | 'EchoEchoEchoEchoEcho'
Lowercase: Make an entire string lowercase 	| 'string'.lower() | 'GET DOWN'.lower() | 'get down'
Uppercase | 'string'.upper() | 'speak up'.upper() | 'SPEAK UP'

## Importing Modules

A lot of the time, it will be necessary to import a module to accomplish what we want.

Import... |	Syntax | Example | Accessing a Specific Function | Example
----------|--------|---------|----------------------------------------------|---------
An entire module | import MODULE_NAME | import math | MODULE_NAME.FUNCTION_NAME() | math.sqrt()
An entire module (into the global namespace) | from MODULE_NAME import * | from math import * | function_1() | sqrt(2)
Specific function(s) from a module | from MODULE_NAME import function_1, function_2, ... | from math import sqrt, cos, sin | function_1() | sqrt(2)

## Composite Data Types
### A Quick Comparison
#### Lists
* Declaring
  * Syntax: `VARIABLE = [ITEM_1, ITEM_2, ITEM_3]`
  * Example: `colors = ['red', 'orange', 'yellow', 'magenta']`
* Indexing
  * Syntax: `VARIABLE[INDEX_NUMBER]`
  * Example: `colors[0]`
* Reassigning
  * Syntax: `VARIABLE[INDEX_NUMBER] = NEW_VALUE`
  * Example: `colors[3] = 'hot pink'`

#### Tuples
* Declaring:
  * Syntax: `VARIABLE = (ITEM_1, ITEM_2, ITEM_3)`
  * Example: `origin = (0, 0, 0)`
* Indexing: Same as list indexing
* Reassigning: Not allowed

#### Dictionaries
* Declaring
  * Syntax: `VARIABLE = {'KEY_1': 'VALUE_1', 'KEY_2': 'VALUE_2', ... }`
  * Example: `authors = {'Python': 'Guido van Rossum', 'C++': 'Bjarne Stroustrup', 'HTML': 'Tim Berners-Lee' }`
* Getting specific values:
  * Syntax: `VARIABLE[KEY_NAME]`
  * Example: `authors['HTML']`
* Reassigning:
  * Syntax: `VARIABLE[KEY_NAME] = NEW_VALUE`
  * Example: `authors['Java'] = 'Some nerd'`

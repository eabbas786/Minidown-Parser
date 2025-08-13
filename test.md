# Test Cases
This file contains test cases for all of the syntactic features of Minidown. 

## These are all Paragraphs
This is a paragraph.
This should be a continuation of the previous paragraph.

This should be a new paragraph.
The following characters should be escaped: <, >, &, ', "

 This a paragraph with a space in the beginning

###This incorrectly formatted header needs a space after '#' and is a paragraph

####### This incorrectly formatted header has 7 #s

###

 #### This incorrectly formatted header has a preceding space and the one before is missing a leading space

#####5 The #s need to be immediately followed by a space

3#### There cannot be any other char before the #s

*This is an incorrectly formatted bulleted list 1 (Missing leading space)

 * This is incorrectly formatted bulleted list 2 (Preceding space)

 *This is incorrectly formatted bulleted list 3 (Missing leading space and there is a preceding space)

6* This is incorrectly formatted bulleted list 4 (Preceding char)


## These are all Headers

# First-level header
## Second-level header
### Third-level header

#### Fourth-level header
##### Fifth-level header
###### Sixth-level header

#### The following characters should be escaped: <, >, &, ', "




## The following are all bulleted lists

* This item1 of bulleted list 1

* This is item1 of bulleted list 2
This is a continuation of item1 of bulleted list 2
* This is item2 of bulleted list 2
*This is still item2 of bulleted list 2
 * This is still item2 of bulleted list 2
7* This is still item2 of bulleted list 2
* This is item3 of bulleted list 2
The following characters should be escaped: <, >, &, ', "


## The following all contain inline code

This paragraph contains inline code: `print('Hello World!')` This is plain text

#### This header contains code: `def compare(x, y): return x == y` This is plain text

* This bulleted list item that contains code:
`def add(x, y): return x + y` 
This is plain text

Check that characters are being properly escaped: `print(" <, >, &, ' ")`



## The following do not have inline code

This code: `print(x) is missing a closing back tick

* Inline code cannot contain a newline character
* `def add(x, y): 
    return x + y`
* the previous list item is plain text only and does not contain inline code


## The following is an example of displayed code
```
def compare(x, y):
    return x == y
```

#### The following checks for escaping characters in displayed code
```
print("Check that characters are being escaped: <, >, &, ' ")
```

## Displayed code Errors

The following example is not displayed code since both the starting and ending
triple backticks are formatted incorrectly. This errored code block should be
displayed as a paragraph

 ```
print('Hello World!')
```x

If only one of the triple backticks is formatted incorrectly but the other one is
formatted correctly, then starting from the correctly formatted one the code block will
contain everything remaining in the file until another ``` is found or EOF is reached

```
print("The starting ``` is correctly formatted)
a```
print("The code block has not ended still")
```x
print("The code block has not ended still")
```

 ```
 In a paragraoh
```
print("In a code block")
```
Exited code block

The following example shows what happens if a correctly formatted triple-
backtick for a code block is never closed with another correctly formatted triple-backtick

```
The rest of this file will be part of this code block including this line. 
## This will not be interpreted as a header


* This will not be intepreted as a bullet list


Still in the code block














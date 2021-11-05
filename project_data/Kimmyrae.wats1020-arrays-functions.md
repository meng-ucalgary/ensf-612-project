# wats1020-arrays-functions

In this assignment we will explore the use of Functions to encapsulate logic, and we will use an Array to help us process text. The scenario goes like this: You are working on a website and we require a Javascript function that allows us to "truncate" text. Truncating is the process of making something shorter, and it's very common for us to abbreviate text on websites (think of everytime you've seen a "... Click here to read more" link). 

There are several different ways to truncate text. The simplest way is often to just truncate according to the number of characters in the String. Unfortunately, that might cut off a word halfway through, and that is often not desirable (at best, it is awkward; at worst it can be unintentionally offensive).

In order to avoid this issue, our truncation will be based on the number of words, and we will only cut out full words. This is a little less precise because we don't know the exact number of characters we will be dealing with, but the tradeoff is that we are much less likely to create weird text that doesn't make sense (or potentially offends people).

## Requirements

In order to complete this assignment, you will build a function that accepts a String and a number (Integer) of words to keep. That function will then return a String containing the truncated text.

### Basic Requirements
Basic requirements for this assignment are:

* Create a Function in `truncate.js` called `truncateWords()` that accepts the following arguments:
  * `longText` (a String of text) 
  * `numWords` (an Integer representing how many words to keep in the text)
* Use the `split()` function to split the String into an Array
* Use the `length` attribute to find the number of words in the Array
* Determine how many words should be removed from the Array
* Remove those words from the Array using the `splice()` function
* Add an additional String item to the Array to put an ellipses (...) into the Array
* Use the `join()` function to combine the items in the Array into a String again
* Return the truncated String from the Function
* Output the results to the `console.log`

### Stretch Requirements
If you desire more challenge, try to fulfill these stretch requirements:

* Place "use strict" at the top of your file to invoke strict mode
* Create an additional function called `truncateCharacters` and repeat this experiment truncating by characters instead of words
* Modify your Function so that it can be called without the `numWords` argument (if no `numWords` is supplied it should use a default number of words to truncate)
* Modify your Function so that instead of returning a single String value it returns an Object that contains the following information:
  * `originalText` (original text that was sent to the function)
  * `wordCount` (count of the number of words in original text)
  * `numWords` (the original number that was sent in)
  * `shortText` (truncated String)
  * (Don't forget to modify your console.log statements to properly show all this info about the object.)

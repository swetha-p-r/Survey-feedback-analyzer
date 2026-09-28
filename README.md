# Survey Feedback Analyzer

A Python program that collects, cleans, and analyzes customer survey feedback.

The program works with customer names, written feedback, and ratings. It demonstrates how Python can be used to organize text-based survey data, clean inconsistent feedback, search for specific words, calculate summary statistics, and display the results in a readable format.

## What the Program Does

The program:

* Stores survey information using a **dictionary of lists**
* Allows users to enter additional feedback dynamically
* Automatically generates the next serial number
* Cleans feedback by:

  * Removing punctuation
  * Removing unnecessary spaces
  * Converting text to lowercase
* Counts how many feedback responses contain specific words
* Calculates the average rating
* Finds the longest feedback based on word count
* Identifies unique words used across all feedback
* Sorts and displays feedback based on rating

## Python Concepts Used

### 1. Dictionary of Lists

Survey data is organized using a dictionary with separate lists for:

* Serial Number
* Name
* Feedback
* Rating

This keeps the different pieces of information organized while allowing each record to be accessed using its position in the lists.

### 2. User Input and `while` Loop

The program asks how many additional feedback responses the user wants to enter.

A `while` loop is then used to repeatedly collect:

* Name
* Feedback
* Rating

The next serial number is generated using the last existing serial number plus one.

### 3. String Cleaning

The feedback text is cleaned using Python string methods.

The program:

* Removes `.`, `,`, `!`, and `?`
* Uses `split()` to handle multiple spaces
* Uses `' '.join()` to rebuild the sentence with single spaces
* Uses `lower()` to standardize the text

Example:

```text
"  Very GOOD Service!!!"
```

becomes:

```text
"very good service"
```

### 4. Custom Function

A function called `count_word_in_feedbacks()` is used to search the cleaned feedback.

```python
def count_word_in_feedbacks(word):
```

The function checks each feedback using `split()` and determines whether the requested word is present.

It is used to count occurrences of words such as:

* `good`
* `poor`
* `excellent`

### 5. Average Rating

The average rating is calculated using:

```python
sum()
len()
```

The total of all ratings is divided by the number of ratings.

### 6. Finding the Longest Feedback

The program uses a `for` loop and `split()` to count the number of words in each feedback.

The feedback with the highest word count is stored and displayed as the longest feedback.

### 7. Finding Unique Words

A Python `set` is used to store unique words.

Since sets automatically remove duplicate values, the program can create a collection of distinct words from all feedback responses.

### 8. Sorting with `zip()` and `sorted()`

The program combines the rating, serial number, name, and feedback using `zip()`.

The combined records are then sorted using:

```python
sorted(combine, reverse=True)
```

This allows the feedback records to be displayed in descending order based on rating.

### 9. Formatted Output

An f-string is used to format the final sorted output into columns:

```text
Rating | S_No | Name | Feedback
```

This makes the results easier to read in the console.

## Example Analysis

After processing the feedback, the program displays:

```text
Number of feedbacks containing 'good': ...
Number of feedbacks containing 'poor': ...
Number of feedbacks containing 'excellent': ...

Average Rating: ...

Longest Feedback: ...

Number of words: ...

Unique words: ...
```

It also displays the feedback records sorted by rating.

## Python Skills Demonstrated

* Dictionaries
* Lists
* Sets
* `input()`
* `if` statements
* `while` loops
* `for` loops
* Functions
* `split()`
* `join()`
* `replace()`
* `lower()`
* `sum()`
* `len()`
* `zip()`
* `sorted()`
* f-strings
* Basic text processing
* Basic data analysis

## Purpose

This project was created to practice using Python for a simple real-world data analysis scenario. It focuses on working with structured survey data, text cleaning, basic analysis, and presenting useful information from the data.


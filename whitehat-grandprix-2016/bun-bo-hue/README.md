# Category: ACM/Programming

## Problem:
```
            Trending Topic
Imagine you are in the hiring process for a
company whose principal activity is the
analysisof information in the Web. One of the
tests consists in writing a program for
maintaining up to date a set of trending topics.
You will be hired depending on the efficiency of
your solution.

They provide you with text from the most
active blogs. The text is organised daily and
you have to provide the sorted list of the N most
frequent words during the last 7 days, when asked.

Input:
    Each input file contains one test case. The
    text corresponding to a day is delimited by
    tag <text>. Queries of top N words can
    appear between texts corresponding to two
    different days. A top N query appears as a
    tag like <top 10 />. In order to facilitate
    you the process of reading from input, the
    number always will be delimited by white
    spaces, as in the sample.

Output:
    The list of N most frequent words during
    the last 7 days must be shown given a query.
    Words must appear in decreasing order of
    frequency and in alphabetical order when
    equal frequency. There must be shown all
    words whose counter of appearances is equal
    to the word at position N. Even if the
    amount of words to be shown exceeds N.

Notes:
    - Test01 is the sample test.
    - Your program will take argument 1 as the
    input file and argument 2 as the output file
    - We use diff to compare your output file to our
    output file. If diff returns 0, you're accepted.
    - There are 5 tests. If you pass all, you will
    have a clue to the flag.
    - CPU time limit: 0.1 second
    - Real time limit: 120 second
    - Memory limit: 50 MB
    - All words are composed only of lowercase
    letters of size at most 20.
    - Words of length less than four characters
    are considered of no interest.
   
Please upload your source code (python2.7)  
(Your file must be no longer than 300 lines,
and ending with a line containing only a dot "."):  
```
Sample test: [sample_test.zip](sample_test.zip)

## Solution:

This is a simple programming problem:  
* get list of all words of latest 7 days  
* save a queue of 7 days, each day is a dict  
* when getting a query, get all words into a dict, convert to list, then sort, then output  

Source code: [trendingtopic.py](trendingtopic.py)

When you finish the problem above, the server return a message - new problem:
```
Congratulation! You finished all tests! The flag
is the return-value of my_function(w),
where w is the first word of the first query in
trending_topic.OUT of test 2.
For example, if file trending_topic.OUT of test 2
is:
===========
<top 5>
analyzing 1
appears 1
business 1
company 1
...
===========
then w is analyzing.
Following is the definition of my_function in python-2:
=======================================
def my_function(w):
 import hashlib
 sha1 = hashlib.sha1(w).hexdigest()
 return 'WhiteHat{'+sha1+'}'
=======================================	
```

So you have to leak the first word of the output of test 2. This is kind of SQL blind injection, but not so difficult. You just have to code some binary searching.

Here is my code:
* [trendingtopic_exploit.py](trendingtopic_exploit.py)
* [exploit_trendingtopic.py](exploit_trendingtopic.py)
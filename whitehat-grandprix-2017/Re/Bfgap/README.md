bfgap:
=====
The description is: "I wrote a program to solve a task, but it is too slow. Can you optimize it? The flag is WhiteHat{sha1(output)}."
The files to give are "minified.bf" and "input.txt".

Idea & Writeup:
=====
I've implemented a reversing problem. The problem is reversing of a code written in brainfuck. 
It is implemented using an emulated stack and heap. The program counts paths of a graph. 
I assume that participants will analyze the code and re-implement it using a better algorithm (e.g. frontier method). 
The flag is not included in the files. Since the output of the program is a natural number, 
the output for the input.txt 9249813203326994188143941582098785323127
Flag is WhiteHat{sha1(output)} == WhiteHat{34e12d1a4efe30d033b28c0638ae6dccfb8e9b01}

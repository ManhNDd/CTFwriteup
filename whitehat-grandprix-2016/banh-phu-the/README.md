# Category: ACM/Programming

## Problem:
>            Digit Sum 2
> For a pair of integers a and b, the digit sum of  
> the interval [a, b] is defined as the sum of all  
> digits occurring in all numbers between  
> (and including) a and b.  
> For example, the digit sum of [28, 31] can be  
> calculated as:  
>          2+8+2+9+3+0+3+1=28  
> What about the digit sum of just even numbers?  
> The digit sum of even numbers of [28, 31] should be:  
>             2+8+3+0=13  
> Given the numbers a and b, calculate the digit sum  
> of [a, b]  
>   
> Input:  
>     On the first line one positive number: the   
>     number of test cases, at most 900. After  
>     that per test case:  
>       - One line with two space-seperated integers,  
>       a and b (0 <= a <= b <= 10^15)  
> Output:  
>     Per test case:  
>       - One line with an integer: the digit sum of  
>       even numbers of [a, b]  
> Notes:  
>     - Test01 is the sample test.  
>     - Your program will take argument 1 as the  
>     input file and argument 2 as the output file  
>     - We use diff to compare your output file to our  
>     output file. If diff returns 0, you're accepted.  
>     - There are 5 tests. If you pass all, you will  
>     have the flag.  
>     - CPU time limit: 0.1 second  
>     - Real time limit: 120 second  
>     - Memory limit: 50 MB  
>   
> Please upload your source code  
> (C++, compile: g++ infile -o outfile -std=c++0x -m32)  
> Your file must be no longer than 300 lines,  
> and ending with a line containing only a dot "."  

Sample test: [sample_test.zip](sample_test.zip)

## Solution:

a and b are very large numbers (64 bits), and there are many test cases in an input file, so you cannot just use a trivial algorithm like running a loop from a to b, and adding digits one by one. Following is my solution:  

>	Let D(a, b) the digit sum of even numbers of interval [a, b].   
>	If a is even, then D(a, b) = D(0, b) - D(0, a-1).  
>	Else D(a, b) = D(0, b) - D(0, a)  
>	For convenience, let D(b) = D(0, b).  
>	We look for a formular to calculate D(X). Let N(X) the number of even numbers of [0, X]. Calculate N(X) is trivial.  
>	Let X a four-digit number - abcd, then we have:  
>	\ \ \ \ D(abcd) = a\*(a-1)/2\*N(999) + a\*D(999) + a\*N(bcd) + D(bcd).  
>	In case X is one digit number:  
>   \ \ \ \ + if X is odd: D(X) = D(X-1)  
>   \ \ \ \ + if X is even: D(X) = X\*N(X)/2
		
With the above formular, you can use recursion with memoization to finish the task.  
  
My code: [digit_sum2.cpp](digit_sum2.cpp)
	

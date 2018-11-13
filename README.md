# Regular expressions

## Problem statement
`Alpha` - regular expression, `Alpha` belongs to the alphabet `{a, b, c, 1, 0, ., *, +}`,
`L` - language which is set by `Alpha`,
`u` - nonenempty word, alphabet - `{a, b, c}`.

Implement the source which finds and prints the length of the longest suffix of `u` which belongs to `L`.

## Solution description
Let's maintain a stack to parse regular expression as we always do.
But in our case we store in stack two-dimensional matrices `dp`.
Size of `dp` is `n * n`, where `n = |u|`.
`dp[i][j] == 1` only then our parsed part of `Alpha` **takes** subword `u[i...(j - 1)]` in current moment, otherwise `dp[i][j] == 0`.
Throughout the algorithm we iterate over the `Alpha` and change our stack. 
There are 4 cases of current character in `Alpha`:
1. Literal(`a, b, c, 0, 1`). In this case we push on our stack **new** dp which can be easily calculated with help of `u`.
2. `+`. We pop top 2 elements in our stack and do operation **OR** to them, after that we push the result on stack.
3. `.`. We also pop 2 elements and count new matrix `dp` like this: 
we look over two parts of `s[i...(j - 1)]` which are acceptable on the last iteration of algorithm(`dp == 1`) and their concatenation is `s[i..(j - 1)]`. 
If we find this part we do `dp[i][j] = 1;`
4. `*`. This case is processed almost like the last one, but we should not to forget to "include" empty strings.  

After the calculation we have a matrix dp which allows us to understand whether every particular subword of `u` belongs to `L`, but
to solve our task we should now this information only about suffices of our word!
So, we iterate over the suffices from the longest to the shortest, choose the first acceptable and print its length.

## Contents
 * [Solution](https://github.com/rvg77/Practicum_FLT/blob/master/solution.py)
 * [System tests](https://github.com/rvg77/Practicum_FLT/tree/master/system_tests)
 * [System checker](https://github.com/rvg77/Practicum_FLT/blob/master/system_test.py)
​​Intuition
=========
- Create an object with key-value pairs for Roman symbols
- Iterate over string and check values left to right

Approach
=========
- Create object for symbols
- Create placeholder for integer
- For loop on string
- Create current and next variables
- if current value < next value, integer -= current value
- else integer += current value
- If statement checks for IV, IX, XL, XC, CD, and CM to grab correct value

Complexity
==========

-   Time complexity:
O(n) - Linear

-   Space complexity:
O(1) - Constant

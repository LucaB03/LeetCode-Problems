​# Solution
1. Check if the list begins with a closing parentheses, if so, return False
2. Iterate over the string, if the char is an opening parentheses, push it to a stack.
3. If its a closing parentheses and the stack is empty, we know there is now possibility of a valid parentheses pair, return False.
4. If its a closing one and the stack is not empty, pop the stack and check if the closing one matches the type of the popped one. If not, return False.
5. After iterating over the string, check if the stack is empty, if it is, return True. Else return False, because there is an unclosed parentheses.

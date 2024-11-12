# Question 1
def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices
    of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution,
    and you may not use the same element twice.
    You can return the answer in any order.
    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[int]: Indices of the two numbers that add up to the target.
    """
    # YOUR CODE HERE
    mydict = {}
    for i,num in enumerate(nums):
        diff = target - num
        if diff in mydict:
            return [i,mydict[diff]]
        else:
            mydict[num] = i
    
    pass

# Question 2
def is_valid_parenthesis(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    An input string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.

    Args:
    s (str): Input string.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    # YOUR CODE HERE
    mystack = []
    for c in s:
        if c in (')','}',']') and len(mystack) == 0:
            return False
        elif c == '(' or c== '{' or c=='[':
            mystack.append(c)
        elif c == ')' and mystack[-1] == '(':
            mystack.pop()
        elif c == '}' and mystack[-1] == '{':
            mystack.pop()
        elif c == ']' and mystack[-1] == '[':
            mystack.pop()
        else:
            return False
    if len(mystack) == 0:
        return True
    else:
        return False
        
    pass

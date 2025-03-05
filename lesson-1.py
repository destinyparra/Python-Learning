


# ╔══════════════════════════════════════════╗
# ║        🐍 Mini Program: Reverse String   ║
# ╠══════════════════════════════════════════╣
# ║  This program reverses a given string.   ║
# ║  Example Input: "hello"                  ║
# ║  Expected Output: "olleh"                ║
# ╚══════════════════════════════════════════╝

# Code starts here 👇

# string = "hello"
# reversed_string = ""

# # range(start, stop, step)
# for i in range(len(string) - 1, -1, -1):
#     reversed_string += string[i]

# print(reversed_string)

# ---------------------------------------------------------




# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: Find Vowel Positions
# ╠══════════════════════════════════════════
# ║  This program Finds the positions of vowels
# ║  Example Input: "Hello World"
# ║  Expected Output: [1,4,7]
# ╚══════════════════════════════════════════

# Code starts here 👇
# def solution(s):    
#     output_array = []
    
#     for i in range(0, len(s)):  # Iterate over all indices
#         if s[i] == "a" or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or \
#            s[i] == "A" or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
#             output_array = output_array + [i]  # Concatenation instead of append

    # return output_array  # Return the final list

# ---------------------------------------------------------
# -------------------  Solution 2 -------------------------

# def solution(s):

#     output_array = []
#     vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
#     for i in range(0, len(s)):
#             for j in vowels:
#                   if j == s[i]:
#                         output_array = output_array + [i]
#     return output_array
# ---------------------------------------------------------
# -------------------  Solution 3 -------------------------

# def solution(s):

#     output_array = []
#     vowels = "aeiouAEIOU"
    
#     for i in range(0, len(s)):
#         if s[i] in vowels:
#             output_array = output_array + [i]
#     return output_array

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------


# ╔══════════════════════════════════════════╗
# ║        🐍 Mini Program: Shift Letters    ║
# ╠══════════════════════════════════════════╣
# ║  This program shifts each letter to the  ║
# ║  next letter in the alphabet.            ║
# ║  'z' → 'a', 'Z' → 'A', digits & symbols  ║
# ║  stay the same.                          ║
# ║                                          ║
# ║  Example Input:  "abc123XYz!"            ║
# ║  Expected Output: "bcd123YZa!"           ║
# ╚══════════════════════════════════════════╝

# def solution(s):
#     # TODO: Implement the solution here
#     ascii_val = 0
#     new_string = ""
#     for char in range(len(s)):
#         ascii_val = ord(s[char])
#         if ascii_val >= 65 and ascii_val <= 90:
#             if ascii_val != 90:
#                 new_string = new_string + chr(ascii_val + 1)
#             else : 
#                 new_string = new_string + "A"
#         elif ascii_val >= 97 and ascii_val <=  122:
#             if ascii_val != 122:
#                 new_string = new_string + chr(ascii_val + 1)
#             else : 
#                 new_string = new_string + "a"
#         else:
#             new_string = new_string + s[char]
#     print(new_string)

# solution("abc123XYz!")
        
# ------------------Solution 2 ------------------------------

# def solution(s):
#     new_string = ""

#     for char in s:  # Directly iterate over characters
#         ascii_val = ord(char)

#         # Shift uppercase letters (A-Z)
#         if 65 <= ascii_val <= 90:
#             new_string += chr(65 + (ascii_val - 64) % 26)  # Wraps 'Z' to 'A'
        
#         # Shift lowercase letters (a-z)
#         elif 97 <= ascii_val <= 122:
#             new_string += chr(97 + (ascii_val - 96) % 26)  # Wraps 'z' to 'a'

#         # Keep non-alphabet characters unchanged
#         else:
#             new_string += char  

#     return new_string  # Return the transformed string

# # Test case
# print(solution("abc123XYz!"))  # Expected Output: "bcd123YZa!"


# Code starts here 👇

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------



# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ Transform Upper to Lowercase
# ╠══════════════════════════════════════════
# ║  This program is given a string input_string, your task is to write a function that transforms all the lowercase letters to uppercase and all the uppercase letters to lowercase. 
# ║  If the character is not a letter, do not transform it.
# ║  Example Input: "HelLo WoRld 123"
# ║  Expected Output:  "hELlO wOrLD 123"
# ╚══════════════════════════════════════════

# Code starts here 👇

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------
#  ord('a') - ord('A') = 97 - 65 = 32


# Solution 1: looping over indexes 
# def solution(input_string):
#     # ascii vals for uppercase: 65 - 90
#     # ascii vals for lowercase: 97 - 122 
#     # map a to A , b to B, etc

#     new_string = ""

#     for i in range(len(input_string)):
#         ascii_value =  ord(input_string[i])
        
#         # lower to upper
#         if ascii_value >= 97 and ascii_value <= 122:
#             new_string += chr(ascii_value - 32)
#         elif ascii_value >= 65 and ascii_value <= 90:
#             new_string  +=  chr(ascii_value + 32)
#         else:
#             new_string = new_string + input_string[i]
    
#     print (new_string)


# solution("hElLo wOrld! 123")


# Solution 2: looping over chars in str 
# def solution(input_string):
#     # ascii vals for uppercase: 65 - 90
#     # ascii vals for lowercase: 97 - 122 
#     # map a to A , b to B, etc

#     new_string = ""

#     for char in input_string:
#         ascii_value =  ord(char)
        
#         # lower to upper
#         if ascii_value >= 97 and ascii_value <= 122:
#             new_string += chr(ascii_value - 32)
#         elif ascii_value >= 65 and ascii_value <= 90:
#             new_string  +=  chr(ascii_value + 32)
#         else:
#             new_string = new_string + char
    
#     print (new_string)


# solution("hElLo wOrld! 123")


# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ Cycle through a fixed range
# ╠══════════════════════════════════════════
# ║  This program asks the user for an input and according to the input, cycles through the numbers
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇
# def color_choice(user_choice):

#     colors = ["red", "blue", "green"]
#     index = user_choice % len(colors)  # 4 % 3 = 1
#     print(colors[index])  # Output: "blue"

# while(True):
#     try:
#         print("Color choices: [1 for red, 2 for blue, 3 for green]")
#         color_choice(int(input("Please enter an index: "))-1)
#         break
#     except ValueError:
#         print("Please input a number: ")


# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------




# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ 3️⃣ Implementing a Cyclic Pattern
# ╠══════════════════════════════════════════
# ║  This program repeats a sequence every x steps
# ║  Example Input: 10
# ║  Expected Output: 4
# ╚══════════════════════════════════════════

# Code starts here 👇

#  Case 1: Implementing a Cyclic Pattern

# def cyclic_pattern(x):

#     for i in range(x):
#         print((i % 5), end= " ")

# cyclic_pattern(10)
# ---------------------------------------------------------

#  Case 2: Starting the Cycle at Index 1

# def cyclic_pattern(x):

#     for i in range(x):
#         print((i % 5) + 1, end = " ")

# cyclic_pattern(20)


# ---------------------------------------------------------

# Case 3: Customizing Any Cyclic Sequence

# def cyclic_pattern(x):
#     pattern = [1,2,3,5,8,13,21]

#     for i in range(x):
#         print(pattern[(i % len(pattern))], end=" ")

# cyclic_pattern(20)


# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------





# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ replace character
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# def replace_character(input_string, c1, c2):
#     # TODO: Replace all occurrences of character `c1` in `input_string` with `c2`
#     output_string = ""
    
#     for char in input_string:
#         if char == c1:
#             output_string += c2
#         else:
#             output_string += char
    
#     return output_string

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------





# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ switch adjacent characters, if length is odd then leave the last character unchanged
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# def solution(s):
#     # TODO: implement the solution here
#     # value_if_true if condition else value_if_false

#     new_string = ""
#     length = len(s)
#     # bool_val = True if length % 2 == 0 else False
    

#     for i in range(0, length - 1, 2):
#             new_string += s[i + 1] + s[i]
    
#     # if odd, append the last character 
#     if(length % 2 == 1): 
#           new_string += s[-1]
            

#     return new_string

# print(solution("hello"))
        
        
            
# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------





# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ Palindrome
# ╠══════════════════════════════════════════
# ║  This program is to implement the function to check whether the provided string is a palindrome or not.
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# def solution(input_string):
    
#     # A letter is alphanumeric 
#     # racecar true
#     # A man, a plan, a canal: Panama  true
#     #  ("!@#$%^&*()") true
    
# #     # ascii vals for uppercase: 65 - 90
# #     # ascii vals for lowercase: 97 - 122 
# #     97 - 65 = 32 

#     # ahah false
#     # Python false
#     if len(input_string) <= 1:
#         return True
    
#     letters = []

#     for char in  input_string:

#         ascii_value = ord(char)        
#         #  convert upper to lower and append
#         if ascii_value >= 65 and ascii_value <= 90:
#             letters.append(chr((ascii_value + 32)))
#         elif ascii_value >= 97 and ascii_value <= 122:
#             letters.append(chr(ascii_value))

# # iterate through the array from left and right

#     l_index = 0
#     r_index = len(letters) - 1

#     while l_index < r_index:
#         if letters[l_index] != letters[r_index]:
#             return False

#         l_index += 1
#         r_index -= 1 

        
#     return True
            

#         # append lower

#         # skip non-letter characters 
    


# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------



# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ Find the min num in a list
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# def find_min(nums):
#     # TODO: implement the function to find the minimum number from a list
#     pass
#     if not nums:
#         return None
    
#     min_num = nums[0]
    
#     for num in nums:
#         if num < min_num:
#             min_num = num
    
#     return min_num
#         #

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------





# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ Second num
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# from typing import List, Optional

# def second_max(nums: List[int]) -> Optional[int]:
#     # TODO: Find the second largest number in nums

    
# # 1 2 3 5 2 1 5 7 5 3 2 1 -> 5 , 7
#     if not nums:
#         return None
        
#     largest_num = nums[0]
#     second_num = None
    
#     for num in nums:
        
        
#         if num > largest_num:
#             second_num = largest_num
#             largest_num = num
#         elif (second_num is None) or (second_num is not None and num > second_num):
#             if num != largest_num:
#                 second_num = num

    
#     if largest_num == second_num:
#         return None

#     print("This is the largest num: " , largest_num , "\n this is the second_num: " , second_num)
#     return second_num
        
        
# print(second_max([9,1,2,3,4,2,1,4,6,4,2,1,6,-4,2,1,4,9]))

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------



# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ 
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# from collections import deque

# def bfs(graph, start):
#     queue = deque([start])
#     visited = set([start])
    
#     while queue:
#         node = queue.popleft()
#         print(node)  # Process node

#         for neighbor in graph[node]:
#             if neighbor not in visited:
#                 queue.append(neighbor)
#                 visited.add(neighbor)

# graph = {
#     1: [2, 3],
#     2: [4, 5],
#     3: [],
#     4: [],
#     5: [6],
#     6: []
# }
# print(graph)
# bfs(graph, 1)


# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------


# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ Perfect square
# ╠══════════════════════════════════════════
# ║  This program determines if this number is a perfect square or not. 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# def is_perfect_square(n):
#     # TODO: implement the function that checks if a number is a perfect square
#     pass
    
    
#     # binary search with no built in functions
#     # since you cannot have a negative num as a sqrt
    
#     if n < 0: 
#         return False
    
#     left = 0
#     right = n
    
    
#     while (left <= right):
#         # // represents floor division
#         mid = (left + right) // 2 
        
#         square = mid * mid
        
#         if square == n:
#             return True

#         if square < n:
#             left = mid + 1
#         else:
#             right = mid - 1
    
#     return False
    
#     # using sqrt
    

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------



# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ 
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# # Code starts here 👇
# def next_prime(n):
#     # TODO: implement the function to find the next prime number after n

#     if n < 2:
#         return 2
#     check = n + 2 if n % 2 != 0 else n + 1
    
#     while not is_prime(check):
#         check += 2
#     return check
#     # using Wheel Factorization for Primes Modulo 6
#     # 6k +- 1
    
    
# def is_prime(n):
#     if n < 2:
#         return False
    
#     if n in (2, 3):
#         return True
#     if ((n % 2 == 0) or (n % 3 == 0)):
#         return False
    
#     i = 5
    
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

    

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------


# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ top k freq
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇
from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == len(nums):
            return nums

        count = Counter(nums)

        return heapq.nlargest(k,count.keys(), key=count.get)

test = Solution()
print(test.topKFrequent([1,1,1,2,2,100,3,3,3,3,4], 2))

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------


# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ 
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------




# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ 
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------


# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ 
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------



# ╔══════════════════════════════════════════
# ║        🐍 Mini Program: ║ 
# ╠══════════════════════════════════════════
# ║  This program 
# ║  Example Input: 
# ║  Expected Output: 
# ╚══════════════════════════════════════════

# Code starts here 👇

# Once tested, you can comment out the code and move on!
# ---------------------------------------------------------



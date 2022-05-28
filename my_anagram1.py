# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    user_input = input("please enter a word: ")
    user_input2 = input("please enter a second word: ")
    
    if len(user_input) != len(user_input2):
        return "this is not an anagram"
    
    for char in user_input:
      if char in user_input2:
         return True
      else: 
          return False

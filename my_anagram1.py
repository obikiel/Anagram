# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    user_input = input("please enter a word: ")
    user_input2 = input("please enter a second word: ")
    
    if len(user_input) == len(user_input2):
        sorted_1 = sorted(user_input)
        sorted_2 = sorted(user_input2)

        if sorted_1 == sorted_2:
            print ("these are anagrams")
        
        else:
            print ("these are not anagrams")
    else:
        print("they are not anagrams!")

find_anagram()


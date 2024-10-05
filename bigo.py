'''
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Angelo Corridori and Kaissa Doichev, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: aec4936
UT EID 2: kjd2488
'''


def length_of_longest_substring_n3(s):
      """
      Finds the length of the longest substring without repeating characters
      using a brute force approach (O(N^3)).

      pre: s is a string of arbitrary length, possibly empty.
      post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
      """
      # here we followed the guidelines of the homework to get n^3 complexity
      final_count = 0
      longest_sub = []

      for i in range(len(s)):
            for ii in range(i, len(s)): 
                  freq_list = [0] * 256
                  substring = s[i:ii + 1]
                  valid_substring = True  

                  for iii in substring:  
                        index = ord(iii)
                        freq_list[index] += 1

                        if freq_list[index] > 1:
                              valid_substring = False  
                              break

                  if valid_substring:
                        if len(substring) > final_count:  
                              final_count = len(substring)
                              longest_sub = substring  
      return len(longest_sub)



def length_of_longest_substring_n2(s):
      """
      Finds the length of the longest substring without repeating characters
      using a frequency list approach (O(N^2)), converting each character to
      their corresponding numeric representation in ASCII as the index into the
      frequency list.

      pre: s is a string of arbitrary length, possibly empty.
      post: Returns an integer >= 0 representing the length of the longest substring
      in s that contains no repeating characters.
      """
      #here we created our own version which at first came out to o(n) complexity so we changed it a little bit
      final_count = 0 
      long_string = '' # instrad of a list we saved our values in a string to add more complexity
      for i in range(len(s)):   
            count = 0  
            count_list = [] # this list is simply to save all the counts to then compare
            for ii in range(i, len(s)):  
                  if s[ii] in long_string: 
                        long_string = '' # if reapeated element then string is set to nothing
                        count = 0 
                  else: 
                        long_string += s[ii] # if not all values are added to the string
                        count += 1
                        count_list.append(count)
            long_string = '' #string is reset to nothing after each word

            # these are just meant to find the highest value and return it
            if count_list == []:
                  final_count = final_count
            elif final_count > max(count_list):
                  final_count = final_count
            else:
                  final_count = max(count_list)
      return final_count



def length_of_longest_substring_n(s):
      """
      Finds the length of the longest substring without repeating characters
      using a frequency list approach (O(N)), converting each character to
      their corresponding numeric representation in ASCII as the index into the
      frequency list. However, this approach stops early, breaking out of the inner
      loop when a repeating character is found. You may also choose to challenge
      yourself by implementing a sliding window approach.

      pre: s is a string of arbitrary length, possibly empty.
      post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
      """

      #this code works basically in the same way but with a list, appending each value to it
      final_count = 0 
      for i in range(len(s)):  
            count_list = []  
            count = 0  
            for ii in range(i, len(s)):  
                  if s[ii] in count_list: 
                        break # because of this the complexity is only o(n)
                  count_list.append(s[ii])  
                  count += 1

            if final_count > count:
                  final_count = final_count
            else:
                  final_count = count  
      return final_count
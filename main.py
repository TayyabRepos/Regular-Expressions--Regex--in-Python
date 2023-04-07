#Regular Expressions (Regex) in Python
#What is raw string?
# Raw string is a string prefixed with r or R. It is used to pass a string to a function or a method which does not treat backslashes as escape characters. It is used to pass regular expressions to re module functions.
import re
text_to_search = '''
abcdefghijklmnopqurtuvwxyzabc
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

'''
sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'M(r|s|rs)\.?\s[A-Za-z]\w*')  #Range [1-5] 1 to 5
#^ inside [] used to negate

#MetaCharacters (Need to be escaped): . ^ $ * + ? { } [ ] \ | ( )

matches = pattern.finditer(text_to_search)

for match in matches:
     print(match)


#finditer() returns an iterator that yields Match objects over all non-overlapping matches for the RE pattern in string.



    







#pattern = re.compile(r'[98]00[-.]\d\d\d[-.]\d\d\d\d') starting with 9 or 9 and after that 00


#Use file
# with open('data.txt','r',encoding='utf-8') as f:
#     contents = f.read()

#     matches=pattern.finditer(contents)
    
#     for match in matches:
#         print(match)





#for match in matches:
#     print(match)


# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # phone number

# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') Specify special symbol for numbers
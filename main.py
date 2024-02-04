#Remove pass and complete the code
def check_character(word, index):
   if word[index].isalpha() == True:
       statement = 'letter'
       return statement
   elif word[index].isspace() == True:
       statement = 'white space'
       return statement
   elif word[index].isdigit() == True:
       statement = 'digit'
       return statement
   else:
       statement = 'unknown'
       return statement

if __name__ == '__main__': 
    print(check_character('happy birthday', 1))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))
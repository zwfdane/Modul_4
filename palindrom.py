# palindromy
import math
def palindrom(string_to_check):
    """
    The function checks if a given text is a palindrom.
    An argument: 
      string_to_check
    The result:
      boolean type variable: 
        True if string_to_check is a palindrom, 
        False if string_to_check is not a palindrom
    """
    string_to_check = string_to_check.lower().replace(" ", "") 

    # is_only_letters = string_to_check.isalpha() -- pomocniczo do sprawdzenia czy wszystkie znaki są literami
    # print(is_only_letters)

    string_to_check = ''.join(character for character in string_to_check if character.isalnum())

    #  print(string_to_check) -- omocniczo: sprawdzenie czy string_to_check jest dobrze nadpisana

    N= len(string_to_check) 
    for i in range(math.floor(N/2)):
        if string_to_check[i] != string_to_check[N-1-i]:
           return False 
    return True; 
print("Ten program sprawdza, czy podany ciąg znaków jest palindromem")
print("Podaj ciąg znaków:")
text_to_check = input() 
if palindrom(text_to_check):
    print(f"Podany ciąg znaków ***{text_to_check}*** jest palindromem")
else:
    print(f"Podany ciąg znaków ***{text_to_check}*** nie jest palindromem") 
# help(palindrom) -- sprawdzenie czy dokumentacja funkcji działa poprawnie.
import time
print("Hello user, welcome to the translator. Here you can translate from english to french and vice versa, or even add your own translations")
time.sleep(1)
translator = [["hello", "bonjour"], ["goodbye", "au revoir"], ["breakfast", "petit-dejeuner"], ["lunch","dejeuner"]]
print(f"Array:{translator}")
time.sleep(2)

def choice():
   choose = input("Type 'a' to add new translations, 'r'to remove translations from the array, 'e' to translate from english to french, 'f'to translate from french to english or q to quit: ").lower()
   if choose == "a":
      add_translation()
   elif choose == "r":
      remove_translation()
   elif choose == "e":
      english_to_french()
   elif choose == "f":
      french_to_english()
   elif choose == "q":
      print("Goodbye")
      exit()
   else:
      print("Invalid option, try again!")
      choice()

def add_translation():
   global translator
   print(f"Array:{translator}")
   english_word = input("Enter an english word: ").lower().strip()
   french_translation = input("Enter the french translation: ").lower().strip()
   translator.append([english_word,french_translation])
   print(translator)
   choice()

def remove_translation():
   global translator
   print(f"Array:{translator}")
   delete = input("Enter an english or french word to remove the translation pair: ").lower()
   for pair in translator:
      if delete in pair:
         translator.remove(pair)
         break
   else:
      print("That word is not in the array, try again!")
      remove_translation()
   print(translator)
   choice()

def english_to_french():
   global translator
   print(f"Array:{translator}")
   translate = input("Choose an english word from the array to translate into french: ").lower()
   for pair in translator:
      if pair[0]== translate:
         print(f"The french translation of {translate} is {pair[1]} ")
         time.sleep(1)
         break
   else:
      print("Invalid, try again!")
      time.sleep(1)
      english_to_french()
   print(translator)
   choice()

def french_to_english():
   global translator
   print(f"Array:{translator}")
   translate = input("Choose an french word from the array to translate into english: ").lower()
   for pair in translator:
      if pair[1]== translate:
         print(f"The english translation of {translate} is {pair[0]} ")
         time.sleep(1)
         break
   else:
      print("Invalid, try again!")
      time.sleep(1)
      french_to_english()
   print(translator)
   choice()

choice()
Name Game

- Python not able to handle: 'name(string)' * 'name(string)' so what if..
- asking to input 2 english names
- validating them, no numbers, no special characters
- turn the names into numbers by allocating the letters from the name to it`s position in alphabet: a=1, b=2 // Peter = 16 5 20 5 18 = 16520518 
- multiply the 2 numbers (from the names) with eachother
- modulo 26 (as many the letters in the US aphabet)
- turn back that number into letter, that will be the first letter of the result/new name
- second letter: substract the 2 numbers(of the names), take the absolute value of the result / modulo(26)
- if there is no name with the 1st and with this 2nd letter in the name DB, change the 2nd letter to the next one from the alphabet until there will be a match**

DB #1: alphabet - simple list in the code
DB #2: US names - **: there should not be "duplication" of names where the 1st and 2nd letter are equal

? DB - excel? online - web scraping? API?



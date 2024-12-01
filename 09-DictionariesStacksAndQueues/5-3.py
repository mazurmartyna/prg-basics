import re

translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

print("----TRANSLATOR----")
print("ENGLISH --> POLISH")
print("------------------")

engword = input("Enter english word: ")

if engword in translations:
    print(f"The translation for {engword} is {translations[engword]}")
else:
    print("The translation is unavailable")

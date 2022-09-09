from countriesList import countries

# 1. Skapa en lista med alla länder som har en population mellan 8000000 och 12000000 - skriv ut namn för varje
# 
# 2. Skapa en lista med alla länder som har minst 15 bokstäver i sitt namn. Skriv ut namn och population för varje
# 
# 3. Skapa en lista med alla länder som har som börjar på A eller har en huvudstad som börjar på A. Skriv ut namn och 
# capital för varje
# 
# 4. Skapa en lista med alla länder som där man pratar  English
#  Skriv ut namn och capital för varje 
# 
# 5. Skapa en lista med FÖRSTA BOKSTAVEN för alla capitals länder som med population mindre än 1000000.   
# Skriv ut listan i formatet  (ex "VAVRST"  om det  är 6 stycken  etc)


#1
listOfCountriesWithPopulationsName = [countrie.Namn for countrie in countries if countrie.Population > 8000000 and countrie.Population < 12000000]

print(listOfCountriesWithPopulationsName)

#2
listOfCountriesNameLenght15 = [countrie.Namn for countrie in countries if len(countrie.Namn) >= 15]

print(listOfCountriesNameLenght15)

#3
listOfCountriesNameStartsWithA = [countrie.Namn for countrie in countries if countrie.Namn.startswith("A") or countrie.Capital.startswith("A")]

print(listOfCountriesNameStartsWithA)

#4
listOfCountriesThatSpeakEnglish = [countrie.Namn for countrie in countries if countrie.Langages == "English"]

print(listOfCountriesThatSpeakEnglish)

#5
listOfCountrieLettersWithPopLessThen1000000 = [countrie.Namn[0] for countrie in countries if countrie.Population < 1000000]
newLettersList = "".join(listOfCountrieLettersWithPopLessThen1000000)


print(newLettersList)
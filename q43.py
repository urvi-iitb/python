# country and capital quiz
import random 

data = {}
with open ("countries.txt","r") as f:
    for line in f:
        country, capital = line.strip().split(': ')
        data[country]= capital 


def quiz():
    countries = list(data.keys())
    random.shuffle(countries)
    return countries[:10]

print("CAPITALS QUIZ")
print("Enter the capitals of the following countries")
countries = quiz()
score = 0
for country in countries:
    response = input("The capital of "+country+" is:")
    if response.lower() == (data[country]).lower():
        print("correct!")
        score += 1
    else :
        print("wrong answer!")
        print("The correct answer is: "+ data[country])
print("quiz complete!")
print("score = ",score)
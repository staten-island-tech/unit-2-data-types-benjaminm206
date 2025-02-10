
# Collecting user inputs
verb1 = input("Insert a verb in the present tense (example: running):")
verb2 = input("Insert another verb!:")
noun1 = input("Insert a noun (It could be a food, an object, anything!)")
noun2 = input("Insert the name of a city. Do not write the word city (Example: New York):")
sport = input("Input the name of a sport (Example: soccer):")
num = input("Insert a number between 100 and 100,000:")
guest = input("Insert a celebrity or famous person's name (Example: Taylor Swift or Elon Musk):")

story = f""" 
Once upon a time, in the great city of {noun2}, was the celebrity himself, {guest}. As he was {verb1} throughout the city,
he spots a ferocious {sport} competition! Intrigued by the immense prize pool of {num},100 dollars, {guest} does not hesitate to sign himself up.
"""   

print(story)

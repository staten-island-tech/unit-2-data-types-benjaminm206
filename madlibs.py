
# Collecting user inputs
verb1 = input("Insert a verb in the past tense (example: ran):")
verb2 = input("Insert another verb!:")
noun1 = input("Insert a part of a spaceship (example: engine)")
noun2 = input("Insert a body in space (example: comet or black hole)")
adjective = input("Insert an adjective of size for the body of space you put in the last question (example: massive)")
sound = input("Insert a harsh sound (example: clang)")
planet = input("Insert the name of a planet. Do not write Earth (example: Saturn)")
guest = input("Insert a celebrity or famous person's name (Example: Taylor Swift or Elon Musk):")
sub = input("Insert the subject pronoun of the celebrity (he or she)")
obj = input("Insert the object pronoun of the celebrity (him or her)")
num = input("Insert a number between 2 and 10")

story = f""" 
You and your friends are on a rigorous space exploration trip to the distant planet of {planet}. Suddently, you hear a very loud {sound}; the {noun1} is malfunctioning! You and
your group must work swiftly, as a {adjective} {noun2} is approaching! Luckily, {guest} is on the spaceship, and {sub} is able to save you! After {num} daunting hours, 
the spaceship was finally fixed! In joy, you all {verb1} and {verb2} throughout the spaceship!
"""   

print(story)

import random

words = ["bird", "dog", "cat", "orange", "car", "train", "bus", "plane", "phone", "house", "sandwich", "ambiguous", "man", "woman", "person"]

num = random.randint(0, 14)
word = words[num]

letters = []
guess = []
relations = {}


for char in word:
  letters.append(char)

for i in range(len(letters)):
  guess.append("0")

for i, letter in enumerate(letters):
  relations[letter] = i

v = 0

while guess != letters and v <= 9:
  user = input("Guess a letter... ")

  if user in relations:
    guess[relations[user]] = user

  print(guess)
  v = v + 1

if guess == letters:
  print("You guessed it! It was a " + word + "!")
if v == 10:
  print("Sorry, You are out of guesses! The word was... " + word + "! :(")
  print(letters)

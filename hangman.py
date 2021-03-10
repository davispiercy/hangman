import requests
from bs4 import BeautifulSoup
import random

words = []
f = open("word_list.txt", "r")
for x in f:
	words.append(x)

x = int(random.random()*len(words))
word = words[x]
used = 'Incorrect Letters: '
guess = ['']*(len(word)-1)
wrong = 0
print()
correct = False
num_good = 0
entered = {''}
defined = False

while (wrong < 6):
	
	print()
	print("  ----")
	print("  |  |")
	if wrong > 0:
		print("  |  O")
	else:
		print("  |")
	if wrong > 1 and wrong < 3:
		print("  |  |")
	elif wrong > 2 and wrong < 4:
		print("  | -|")
	elif wrong > 3:
		print("  | -|-")
	else:
		print("  |")
	if wrong > 4:
		print("  | /")
	else:
		print("  |")

	print("  |")
	print(" ---")
	print(used)
	print()
	for i in range(len(word)-1):
		if guess[i] == word[i]:
			print(guess[i], end=' ')
		else:
			print("_", end=' ')
	print()

	while(True):
		if wrong == 5 and not defined:
			print("For the words defintion enter def")
		curr = input("Enter guess: ")##warning of duplicate answers
		if curr == 'def':
			URL = 'https://www.dictionary.com/browse/' + word + '?s=t'
			page = requests.get(URL)
			soup = BeautifulSoup(page.content, 'html.parser')
			word_def = soup.find('div', class_ ='css-76ttiv-PosDefContentItem e1q3nk1v2').text.strip()
			print(word_def)
			defined = True
		elif not curr in entered:
			entered.add(curr)
			break
		else:
			print("This letter has already been entered")

	wrong1 = 0
	for i in range(len(word)-1):
		if word[i] == curr:
			guess[i] = curr
			num_good = num_good + 1
		else:
			wrong1 = wrong1 + 1
	if(wrong1 == len(word)-1):
		wrong = wrong + 1
		used += curr + ' '
	if num_good == len(word)-1:
		correct = True;
		break
if correct:
	print('\nCongrats! You guessed that the word was ' + word)
else:
	print("\n  ----")
	print("  |  |")
	print("  |  O")
	print("  | -|-")
	print("  | / \\")
	print("  |")
	print(" ---")
	print("Uh oh, the word was: " + word)
	print('Better luck next time!')
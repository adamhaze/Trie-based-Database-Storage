
import re

filename = 'war_and_peace_tolstoy.txt'
# filename = '../data/anna_karenina_tolstoy.txt'
with open(filename, 'r') as file:
	# replace all newlines with space
	data = file.read().replace('\n', ' ')
	# replace all non alphanumeric (including spaces) with null character (i.e. remove them)
	data = re.sub('[^0-9a-zA-Z ]+', '', data)
	data = data.split(' ')  # split into list of strings
	data = list(filter(('').__ne__, data))  # remove all empty strings from list
file.close()

print(data)
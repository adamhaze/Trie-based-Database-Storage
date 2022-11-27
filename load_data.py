import csv
import re

filename = 'war_and_peace_tolstoy.txt'
with open(filename, 'r') as file:
	# replace all newlines with space
	data = file.read().replace('\n', ' ')
	# replace all non alphanumeric (including spaces) with null character (i.e. remove them)
	data = re.sub('[^0-9a-zA-Z ]+', '', data)
	data = data.split(' ')  # split into list of strings
	data = list(filter(('').__ne__, data))  # remove all empty strings from list
file.close()



filename2 = 'anna_karenina_tolstoy.txt'
with open(filename2, 'r') as file2:
	# replace all newlines with space
	data2 = file2.read().replace('\n', ' ')
	# replace all non alphanumeric (including spaces) with null character (i.e. remove them)
	data2 = re.sub('[^0-9a-zA-Z ]+', '', data2)
	data2 = data2.split(' ')  # split into list of strings
	data2 = list(filter(('').__ne__, data2))  # remove all empty strings from list
file2.close()


for elem in data2:
	data.append(elem)


filename3 = 'hemingway-stories-poems.txt'
with open(filename3, 'r') as file3:
	# replace all newlines with space
	data3 = file3.read().replace('\n', ' ')
	# replace all non alphanumeric (including spaces) with null character (i.e. remove them)
	data3 = re.sub('[^0-9a-zA-Z ]+', '', data3)
	data3 = data3.split(' ')  # split into list of strings
	data3 = list(filter(('').__ne__, data3))  # remove all empty strings from list
file3.close()

for elem in data3:
	data.append(elem)




with open('input_data.csv', 'w') as words_file:
    wr = csv.writer(words_file)
    # wr.writerows([data])
    for word in data:
        wr.writerow([word])
    
words_file.close()
# print(data)
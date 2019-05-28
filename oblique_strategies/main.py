import csv
import random


list_sentences = list()

with open('sentences.csv') as csvfile:
    sentences_reader = csv.reader(csvfile, delimiter=',')
    for row in sentences_reader:
        sentence = row[0]
        list_sentences.append(sentence)

#print('list_sentences: ', list_sentences)
#print('1st item list_sentences:', list_sentences[0])
#print('LAST item list_sentences:', list_sentences[-1])

#print('LEN list_sentences: ', len(list_sentences))  # 196

random_number = random.randint(0, len(list_sentences)-1)

#print("Random number: ", random_number)
print(list_sentences[random_number])

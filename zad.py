#Dzielimy tekst na wyrazy bez cyfr

with open("Radioactive.txt", "r") as f:
    text = f.read()

words = text.split()

words = [word for word in words if not any(char.isdigit() for char in word)]


#Tworzymy listę słów
table = []

for word in words:
    row = [word]
    table.append(row)

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(table)

#Tworzymy listę słów wraz z liczbą wystąpień
table2 = []
for word, count in word_counts.items():
    if count > 4:
        row = [word, count]
        table2.append(row)

print(table2)


#Najczęściej występujące słowo w tekście
max_count = 0
max_word = ""

for row in table2:
    word = row[0]
    count = row[1]
    if count > max_count:
        max_count = count
        max_word = word

max_list = [max_word, max_count]
print(max_list)

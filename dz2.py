from collections import Counter

with open('book2.txt', 'r+', encoding='utf8') as f:
    # Replacing 'Анна Павловна' to 'Anna Pavlovna'
    changed_book = f.read().replace('Анна Павловна', 'Anna Pavlovna')

    # Listing all words in the book and clearing the empty space
    words = changed_book.replace('\n', ' ').split()

    f.seek(0)
    f.write(changed_book)  # Writing book
    f.truncate()

count_words = len(words)
average_length = int(sum(len(word) for word in words) / len(words))
count_letters = sum(len(word) for word in words)
top_longest_words = sorted(set(words), key=len)[::-1][:10]
top_most_common_letters = Counter(''.join(words)).most_common(10)
count_paragraphs = sum(paragraph == '\n' for paragraph in changed_book) + 1

print(f'There are {count_words} words in the book\n'
      f'Average length of the words is: {average_length}\n'
      f'There are {count_letters} letters in the book\n'
      f'Top 10 longest words are:\n {top_longest_words}\n'
      f'Top 10 most common letters are:\n {top_most_common_letters}\n'
      f'There {count_paragraphs} paragraphs in the book\n')

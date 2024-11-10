import re

class WordsFinder:
    def __init__(self, *file_names):

        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:

                content = file.read().lower()

                content = re.sub(r"[,.!?;:=]| - ", "", content)

                words = content.split()

                all_words[file_name] = words
        return all_words

    def find(self, word):
        word = word.lower()
        positions = {}

        for file_name, words in self.get_all_words().items():

            if word in words:
                positions[file_name] = words.index(word) + 1
        return positions

    def count(self, word):
        word = word.lower()
        counts = {}

        for file_name, words in self.get_all_words().items():

            counts[file_name] = words.count(word)
        return counts


finder2 = WordsFinder('C:/Users/Ivan/PycharmProjects/Blumbot/test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

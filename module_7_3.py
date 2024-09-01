

class WordsFinder:
    file_names = []
    def __init__(self, *args):
        for i in args:
            self.file_names.append(i)


    def get_all_words(self):
        all_words = {}
        list_ = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                list_words = []
                for line in file:
                    for j in list_:
                        line_lower = line.lower()
                        per = line_lower.replace(j, '')
                        line = per
                    words_ = line.split()
                    for word1 in words_:
                        list_words.append(word1)
                all_words[i] = list_words
        return all_words

    def find(self, word):
        dict_search = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                dict_search[name] = words.index(word.lower())+1
        return dict_search


    def count(self, word):
        dict_search = {}
        for name, words in self.get_all_words().items():
            number = 0
            for i in words:
                if i == word.lower():
                    number += 1
            if number > 0:
                dict_search[name] = number
            else:
                continue
        return dict_search


finder1 = WordsFinder('test.txt')

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))




# finder2 = WordsFinder('test.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего
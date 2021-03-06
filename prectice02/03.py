# 문제3.
# 1)다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요. (스플릿 셋)

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""


s = s.replace(',', '').replace('.', '').upper()
words = s.split(' ')
words_results = list(set(words))
words_results.sort(key=str)

for word in words_results:
    print("{0}:{1}".format(word, words.count(word)))
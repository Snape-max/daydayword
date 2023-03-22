import xlrd as xd
import pickle
data = xd.open_workbook(r"Python\project\daydayword\test.xls")
table = data.sheets()[0]
word = table.col(0)
meaning = table.col(2)
# print(str(word[0])[5:].replace("'",''))
# print(str(meaning[0])[5:].replace("'",''))
word_data = [str(word[i])[5:].replace("'",'') for i in range(len(word))]
meaning_data = [str(meaning[i])[5:].replace("'",'').replace(r"\n"," ") for i in range(len(meaning))]
print(word_data[0])
print(meaning_data[0])
a = open("word","wb")
pickle.dump(word_data,a)
a.close()
b = open("meaning","wb")
pickle.dump(meaning_data,b)
b.close()

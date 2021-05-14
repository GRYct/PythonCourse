# введите текст пример Petr93 Jonhy70 Servise20002
import re
text = input("введите текст: ")
print(text)
pattern = re.compile(r'\b([A-Z][a-z]*\d{2}|[A-Z][a-z]*\d{4})\b')
result = re.findall(pattern,text)
print(result)
from PyPDF2 import PdfReader

reader = PdfReader("./raw_datasets/gdp.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[1]
text = page.extract_text()
text = text.split("\n")[0:-3]

with open("./datasets/gdp.txt", "a") as f:
    idx = 0
    while idx < len(text):
      splittedText = list(filter(lambda x: len(x) > 0,text[idx].split(" ")))
      print(splittedText[1])
      print(idx)
      f.write(splittedText[1] + " " + splittedText[-2] + splittedText[-1] + "\n")
      idx += 1


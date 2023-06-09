from PyPDF2 import PdfReader

reader = PdfReader("./raw_datasets/meb.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[33]
text = page.extract_text()
text = text.split("\n")[31:93]


with open("./datasets/highschool_education_rate_according_meb.txt", "a") as f:
    idx = 0
    while idx < len(text):
      f.write(text[idx].split(" ")[1] + ' ')
      if '' in text[idx+1].split(" "):
        f.write(text[idx+1].split(" ")[23].replace(',','.') + '\n')
      else:
        f.write(text[idx+1].split(" ")[22].replace(',','.') + '\n')
         
      idx += 3
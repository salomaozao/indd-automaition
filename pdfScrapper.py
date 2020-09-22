import PyPDF2
from PyPDF2.pdf import ContentStream

file = open('prof_sample.pdf', 'rb')

fileReader = PyPDF2.PdfFileReader(file)

page = fileReader.getPage(3)

# Get page tree

print(page.extractText())

# Get annotations

for annot in page['/Annots'] :
    # Other subtypes, such as /Link, cause errors
        subtype = annot.getObject()['/Subtype']
        if subtype == "/Text":
            print(annot.getObject())
            print(annot.getObject()['/Contents'])


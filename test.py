import PyPDF2


sum = 0

for q in range(1,83):
    path ="D:\\files\\pdfs\\a (%i).pdf" %q
    file = open( path,'rb')
    pdf_reader= PyPDF2.PdfReader(file)
    totall = len(pdf_reader.pages)
    sum +=totall

print(sum)

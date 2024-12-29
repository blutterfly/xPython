#12. Convert PDFs to Text (For Your Inner Librarian)


import pypdf2 as PyPDF2

def pdf_to_text(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text
print(pdf_to_text('example.pdf'))
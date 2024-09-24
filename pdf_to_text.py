from PyPDF2 import PdfFileReader

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfFileReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

pdf_path = 'sample.pdf'
text = extract_text_from_pdf(pdf_path)
print(text)

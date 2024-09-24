from PyPDF2 import PdfFileMerger

pdfs = ['file1.pdf', 'file2.pdf']
merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write('merged.pdf')
merger.close()

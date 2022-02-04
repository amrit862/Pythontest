import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string('C:\\Projects\\tessaract\\image1.png')
print(text)
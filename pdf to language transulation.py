
# import pdfplumber
# from transformers import MarianMTModel, MarianTokenizer
# from fpdf import FPDF

# def pdf_to_text(pdf_file):
#     """Extract text from PDF."""
#     text = ""
#     with pdfplumber.open(pdf_file) as pdf:
#         for page in pdf.pages:
#             text += page.extract_text()
#     return text

# def translate_text(text, src_lang, tgt_lang):
#     """Translate text from one language to another using MarianMT."""
#     model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
#     tokenizer = MarianTokenizer.from_pretrained(model_name)
#     model = MarianMTModel.from_pretrained(model_name)
    
#     # Tokenize and translate
#     inputs = tokenizer(text, return_tensors="pt", truncation=True)
#     translated = model.generate(**inputs)
    
#     # Decode translation
#     translated_text = tokenizer.decode(translated[0], skip_special_tokens=True)
#     return translated_text

# def save_translated_to_pdf(translated_text, output_pdf):
#     """Save translated text to a new PDF with a Unicode font."""
#     pdf = FPDF()
#     pdf.add_page()
    
#     # Add Unicode font (DejaVuSans) that supports Hindi characters
#     pdf.add_font('DejaVu', '', 'C:/pdf to language transulation/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)
#     pdf.set_font('DejaVu', '', 12)

#     # Add translated text to PDF
#     pdf.multi_cell(0, 10, translated_text)
#     pdf.output(output_pdf)
#     print(f"Translated PDF saved as {output_pdf}")

# if __name__ == "__main__":
#     pdf_file = "C:/Users/Viswajith/Downloads/Legal Words & Definitions.pdf"  # Input PDF
#     output_pdf = "C:\pdf to language transulation/translated_output1.pdf"  # Output translated PDF
#     src_lang = "en"  # Source language
#     tgt_lang = "hi"  # Target language (Hindi)

#     # Extract text from PDF
#     text = pdf_to_text(pdf_file)
    
#     # Translate the text
#     translated_text = translate_text(text, src_lang, tgt_lang)
    
#     # Save the translated text back to a PDF
#     save_translated_to_pdf(translated_text, output_pdf)





# import pdfplumber
# from googletrans import Translator, LANGUAGES
# from fpdf import FPDF

# def pdf_to_text(pdf_file):
#     """Extract text from PDF."""
#     text = ""
#     with pdfplumber.open(pdf_file) as pdf:
#         for page in pdf.pages:
#             page_text = page.extract_text()  # Extract text from the page
#             if page_text:  # Check if text was extracted
#                 text += page_text
#             else:
#                 print("No text found on this page.")
#     return text.strip()  # Return trimmed text

# import time

# def translate_text(text, target_lang, retries=3):
#     """Translate text using googletrans with error handling and retries."""
#     translator = Translator()
#     attempt = 0
#     while attempt < retries:
#         try:
#             if target_lang not in LANGUAGES:
#                 raise ValueError(f"Invalid target language: {target_lang}. Please use a valid language code.")

#             # Translate in chunks if text is too long
#             translated_text = ""
#             for i in range(0, len(text), 2000):  # Chunking text to 2000 characters
#                 chunk = text[i:i + 2000]
#                 translated_chunk = translator.translate(chunk, dest=target_lang)
#                 translated_text += translated_chunk.text + " "

#             return translated_text.strip()  # Return trimmed translated text
#         except Exception as e:
#             print(f"An error occurred during translation: {e}")
#             attempt += 1
#             if attempt < retries:
#                 print("Retrying...")
#                 time.sleep(2)  # Wait for 2 seconds before retrying
#             else:
#                 return ""

# def save_translated_to_pdf(translated_text, output_pdf):
#     """Save translated text to a new PDF with fpdf2."""
#     pdf = FPDF()
#     pdf.add_page()

#     # Add a standard font (must be added using add_font method for custom fonts)
#     pdf.add_font('DejaVu', '', 'C:/pdf to language transulation/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)
#     pdf.set_font('DejaVu', '', 12)

#     # Add translated text to PDF
#     pdf.multi_cell(0, 10, translated_text)
#     pdf.output(output_pdf)
#     print(f"Translated PDF saved as {output_pdf}")

# if __name__ == "__main__":
#     pdf_file = "C:/Users/Viswajith/Downloads/Introduction_to_Machine_Learning.pdf"  # Input PDF
#     output_pdf = "C:/pdf to language transulation/translated_output1.pdf"  # Output translated PDF
#     target_lang = "hi"  # Target language (Hindi)
    
#     # Extract text from PDF
#     text = pdf_to_text(pdf_file)
#     print(f"Extracted Text: {text[:100]}...")  # Print the first 100 characters of extracted text for debugging
    
#     # Translate the text
#     if text:  # Ensure there is text to translate
#         translated_text = translate_text(text, target_lang)
        
#         # Save the translated text back to a PDF
#         if translated_text:  # Ensure there is text to save
#             save_translated_to_pdf(translated_text, output_pdf)
#         else:
#             print("No translated text to save.")
#     else:
#         print("No text extracted from the PDF.")


















import pdfplumber
from googletrans import Translator, LANGUAGES
from fpdf import FPDF
import time

def pdf_to_text(pdf_file):
    """Extract text from PDF."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()  # Extract text from the page
            if page_text:  # Check if text was extracted
                text += page_text
            else:
                print("No text found on this page.")
    return text.strip()  # Return trimmed text

def translate_text(text, target_lang, retries=3):
    """Translate text using googletrans with error handling and retries."""
    translator = Translator()
    attempt = 0
    while attempt < retries:
        try:
            if target_lang not in LANGUAGES:
                raise ValueError(f"Invalid target language: {target_lang}. Please use a valid language code.")

            # Translate in chunks if text is too long
            translated_text = ""
            for i in range(0, len(text), 1000):  # Chunking text to 1000 characters
                chunk = text[i:i + 1000]
                translated_chunk = translator.translate(chunk, dest=target_lang)
                translated_text += translated_chunk.text + " "
            
            return translated_text.strip()  # Return trimmed translated text
        except Exception as e:
            print(f"An error occurred during translation: {e}")
            attempt += 1
            if attempt < retries:
                print("Retrying...")
                time.sleep(5)  # Wait for 5 seconds before retrying
            else:
                return ""

def save_translated_to_pdf(translated_text, output_pdf):
    """Save translated text to a new PDF."""
    pdf = FPDF()
    pdf.add_page()

    # Add a standard font (must be added using add_font method for custom fonts)
    pdf.add_font('DejaVu', '', 'C:/pdf to language transulation/dejavu-fonts-ttf-2.37/ttf/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    # Add translated text to PDF
    pdf.multi_cell(0, 10, translated_text)
    pdf.output(output_pdf)
    print(f"Translated PDF saved as {output_pdf}")

if __name__ == "__main__":
    pdf_file = "C:/Users/Viswajith/Downloads/COI...pdf"  # Input PDF
    output_pdf = "C:/pdf to language transulation/translated_output1.pdf"  # Output translated PDF
    target_lang = "ta"  # Target language (Hindi)
    
    # Extract text from PDF
    text = pdf_to_text(pdf_file)
    print(f"Extracted Text: {text[:100]}...")  # Print the first 100 characters of extracted text for debugging
    
    # Translate the text
    if text:  # Ensure there is text to translate
        translated_text = translate_text(text, target_lang)
        
        # Save the translated text back to a PDF
        if translated_text:  # Ensure there is text to save
            save_translated_to_pdf(translated_text, output_pdf)
        else:
            print("No translated text to save.")
    else:
        print("No text extracted from the PDF.")


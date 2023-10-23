import PyPDF2

def extract_code_from_pdf(pdf_path, output_text_file):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            extracted_text += page.extract_text()

    # Save the extracted text to a text file
    with open(output_text_file, 'w', encoding='utf-8') as text_file:
        text_file.write(extracted_text)

if __name__ == "__main__":
    pdf_path = 'trial.pdf'  # Replace with the actual PDF path
    output_text_file = 'output_text.txt'  # Specify the output text file

    extract_code_from_pdf(pdf_path, output_text_file)
    print(f"Code extracted and saved to: {output_text_file}")

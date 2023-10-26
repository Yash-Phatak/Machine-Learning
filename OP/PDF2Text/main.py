import PyPDF2
import os

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
    # pdf_folder = 'DATABASE OF COVERAGE'
    # output_folder = 'Output'
    # for file_name in os.listdir(pdf_folder):
    #     if file_name.endswith('.pdf'):
    #         pdf_path = os.path.join(pdf_folder,file_name)
    #         output_text_file = os.path.join(output_folder,os.path.splitext(file_name)[0]+'.txt')
    #         extract_code_from_pdf(pdf_path,output_text_file)
    #         print("Text extracted and saved to: {}".format(output_text_file))
    pdf_path = 'Delloite.pdf'  # Replace with the actual PDF path
    output_text_file = 'Output/Delloite.txt'  # Specify the output text file

    extract_code_from_pdf(pdf_path, output_text_file)
    print(f"Code extracted and saved to: {output_text_file}")

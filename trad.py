import json
from fpdf import FPDF

def json_to_pdf(json_file, pdf_file):
   
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Create a PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Set font for the PDF
    pdf.set_font("Arial", size=12)
    
    # Title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=titulo, ln=True, align='C')
    pdf.ln(10)  # Add a line break

    # Function to recursively print JSON data
    def print_json(data, indent=0):
        for key, value in data.items():
            if isinstance(value, dict):
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(0, 10, txt=f"{' ' * indent}{key}:", ln=True)
                print_json(value, indent + 4)
            else:
                pdf.set_font("Arial", size=12)
                pdf.cell(0, 10, txt=f"{' ' * indent}{key}: {value}", ln=True)

    # Print the JSON data
    print_json(data)
    
    # Save the PDF to a file
    pdf.output(pdf_file)
    print(f"PDF file '{pdf_file}' created successfully.")

# Example usage:
json_file = 'asset_info.json'  # Input JSON file
pdf_file = 'output.pdf'  # Output PDF file
titulo = 'Relatório'

json_to_pdf(json_file, pdf_file)
import pdfplumber
import os

def extract_text_from_pdf(pdf_path, txt_output_path="txts/{pdf_path}.txt", **kwargs):
    pdf_filename = os.path.basename(pdf_path)
    output_path = os.path.join("txts", pdf_filename.replace(".pdf", ".txt"))
    """
    Function to extract text from a PDF and save it to a .txt file.

    Parameters:
    - pdf_path: str, path to the input PDF file (required)
    - txt_output_path: str, path to save the output text file (default is 'salida.txt')
    - **kwargs: additional optional arguments for pdfplumber's extract_text method, such as:
        - layout: bool, whether to preserve the layout (default: True)
        - line_dir_render: str, direction of line rendering (default: 'ttb')
        - char_dir_render: str, direction of character rendering (default: 'ltr')
        - x_tolerance: int, horizontal tolerance for grouping elements (default: 1)
        - y_tolerance: int, vertical tolerance for grouping elements (default: 1)
    """

    options = {
        "layout": True,
        "line_dir_render": "ttb",
        "char_dir_render": "ltr",
        "x_tolerance": 1,
        "y_tolerance": 1,
    }

  
    options.update(kwargs)

    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text(
                layout=options["layout"],
                line_dir_render=options["line_dir_render"],
                char_dir_render=options["char_dir_render"],
                x_tolerance=options["x_tolerance"],
                y_tolerance=options["y_tolerance"],
            )
            text += "\n"
    
    output_dir = os.path.dirname(txt_output_path) or "."
    os.makedirs(output_dir, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as archivo:
        archivo.write(text)

    return text

if __name__ == "__main__":
    pass
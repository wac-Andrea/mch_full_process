import pdfplumber
import os
import argparse

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

    # Set default values for the extract_text options
    options = {
        "layout": True,
        "line_dir_render": "ttb",
        "char_dir_render": "ltr",
        "x_tolerance": 1,
        "y_tolerance": 1,
    }

    # Override defaults with any user-provided kwargs
    options.update(kwargs)

    # Extract text from the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            # Pass the options to extract_text using **options
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

    # Save the extracted text to a .txt file
    with open(output_path, "w", encoding="utf-8") as archivo:
        archivo.write(text)

    return text

""" def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract text from PDFs.")
    parser.add_argument("pdf_path", type=str, help="Path to the input PDF file.")
    parser.add_argument("txt_output_path", type=str, help="Path to the output text file.")
    parser.add_argument("--layout", type=bool, default=True, help="Layout option for extraction.")
    parser.add_argument("--line_dir_render", type=str, default="ttb", help="Line direction render option.")
    parser.add_argument("--char_dir_render", type=str, default="ltr", help="Character direction render option.")
    parser.add_argument("--x_tolerance", type=float, default=3.0, help="X tolerance for extraction.")
    parser.add_argument("--y_tolerance", type=float, default=3.0, help="Y tolerance for extraction.")
    
    args = parser.parse_args()

    # Store options in a dictionary
    extract_text_from_pdf(
        args.pdf_path,
        args.txt_output_path,
        layout=args.layout,
        line_dir_render=args.line_dir_render,
        char_dir_render=args.char_dir_render,
        x_tolerance=args.x_tolerance,
        y_tolerance=args.y_tolerance
    ) """

if __name__ == "__main__":
    pass
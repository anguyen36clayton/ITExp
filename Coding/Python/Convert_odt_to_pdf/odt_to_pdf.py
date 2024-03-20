import os
import subprocess
import shutil

def convert_odt_to_pdf(input_file, output_folder):
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    output_path = os.path.join(output_folder, output_file)
    try:
        subprocess.run(["unoconv", "-f", "pdf", "-o", output_folder, input_file])
        print(f"Converted {input_file} to {output_path}")
        return True, output_path
    except Exception as e:
        print(f"Error converting {input_file}: {str(e)}")
        return False, ""

def main():
    # Create a directory named PDF if it doesn't exist
    pdf_folder = "PDF"
    if not os.path.exists(pdf_folder):
        os.makedirs(pdf_folder)

    # Get a list of all .odt files in the current directory
    odt_files = [file for file in os.listdir() if file.endswith(".odt")]

    # Convert each .odt file to PDF and move the PDF file to the PDF folder
    for odt_file in odt_files:
        if convert_odt_to_pdf(odt_file, pdf_folder):
            # Move the original .odt file to the PDF folder
            shutil.move(odt_file, os.path.join(pdf_folder, odt_file))

if __name__ == "__main__":
    main()
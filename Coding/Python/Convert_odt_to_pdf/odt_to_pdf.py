import os
import subprocess

def convert_odt_to_pdf(input_file):
    output_file = os.path.splitext(input_file)[0] + ".pdf"
    try:
        subprocess.run(["unoconv", "-f", "pdf", input_file])
        print(f"Converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file}: {str(e)}")

def main():
    # Get a list of all .odt files in the current directory
    odt_files = [file for file in os.listdir() if file.endswith(".odt")]

    # Convert each .odt file to PDF
    for odt_file in odt_files:
        convert_odt_to_pdf(odt_file)

if __name__ == "__main__":
    main()
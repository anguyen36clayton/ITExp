from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
import subprocess

def generate_resume_files(name, email, phone, skills, experience, education, achievements, pdf_filename, odt_filename):
    # PDF generation
    pdf_doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    pdf_elements = []
    pdf_styles = getSampleStyleSheet()

    # Custom styles
    heading_style = ParagraphStyle(
        'Heading',
        parent=pdf_styles['Heading1'],
        alignment=TA_CENTER,
        spaceAfter=12
    )
    section_style = ParagraphStyle(
        'Section',
        parent=pdf_styles['Heading2'],
        spaceBefore=12,
        spaceAfter=6
    )

    pdf_elements.append(Paragraph(name, heading_style))
    pdf_elements.append(Paragraph(email, pdf_styles["BodyText"]))
    pdf_elements.append(Paragraph(phone, pdf_styles["BodyText"]))
    pdf_elements.append(Spacer(1, 12))

    pdf_elements.append(Paragraph("Skills", section_style))
    for skill in skills:
        pdf_elements.append(Paragraph(skill, pdf_styles["BodyText"]))
    pdf_elements.append(Spacer(1, 12))

    pdf_elements.append(Paragraph("Experience", section_style))
    for exp in experience:
        pdf_elements.append(Paragraph(exp, pdf_styles["BodyText"]))
    pdf_elements.append(Spacer(1, 12))

    pdf_elements.append(Paragraph("Education", section_style))
    for edu in education:
        pdf_elements.append(Paragraph(edu, pdf_styles["BodyText"]))

    pdf_elements.append(Paragraph("Achivements", section_style))
    for ach in achievements:
        pdf_elements.append(Paragraph(ach, pdf_styles["BodyText"]))

    pdf_doc.build(pdf_elements)
    print(f"PDF resume saved as {pdf_filename}")

    # LibreOffice Writer generation
    with open(odt_filename, "w", encoding="utf-8") as odt_file:
        odt_file.write(f"Name: {name}\n\n")
        odt_file.write(f"Email: {email}\n")
        odt_file.write(f"Phone: {phone}\n\n")

        odt_file.write("Skills:\n")
        for skill in skills:
            odt_file.write(f"- {skill}\n")
        odt_file.write("\n")

        odt_file.write("Experience:\n")
        for exp in experience:
            odt_file.write(f"- {exp}\n")
        odt_file.write("\n")

        odt_file.write("Education:\n")
        for edu in education:
            odt_file.write(f"- {edu}\n")

        odt_file.write("Achievements:\n")
        for ach in achievements:
            odt_file.write(f"- {ach}\n")

    print(f"LibreOffice Writer resume saved as {odt_filename}")

    # Open the generated files, Only uncomment if you need it.
    #subprocess.run(["xdg-open", pdf_filename])
    #subprocess.run(["xdg-open", odt_filename])

if __name__ == "__main__":
    name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")

    skills = []
    print("Enter your skills (press enter twice to stop):")
    while True:
        skill = input()
        if not skill:
            break
        skills.append(skill)

    experience = []
    print("Enter your experience (press enter twice to stop):")
    while True:
        exp = input()
        if not exp:
            break
        experience.append(exp)

    education = []
    print("Enter your education (press enter twice to stop):")
    while True:
        edu = input()
        if not edu:
            break
        education.append(edu)

    achievements = []
    print("Enter your achievements (press enter twice to stop):")
    while True:
        ach = input()
        if not ach:
            break
        achievements.append(ach)

    pdf_filename = input("Enter the filename for the PDF resume (e.g., resume.pdf): ")
    odt_filename = input("Enter the filename for the LibreOffice Writer resume (e.g., resume.odt): ")

    generate_resume_files(name, email, phone, skills, experience, education, achievements, pdf_filename, odt_filename)

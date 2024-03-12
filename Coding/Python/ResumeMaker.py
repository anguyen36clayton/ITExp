import subprocess

def generate_resume_files(name, email, phone, education, achievements, skills, projects, experience, pdf_filename, odt_filename):
    # PDF generation
    with open(pdf_filename, "w") as pdf_file:
        pdf_file.write(f"Name: {name}\n")
        pdf_file.write(f"Email: {email}\n")
        pdf_file.write(f"Phone: {phone}\n\n")

        pdf_file.write("Education:\n")
        for edu in education:
            pdf_file.write(f"- {edu}\n")
        pdf_file.write("\n")

        pdf_file.write("Achievements:\n")
        for ach in achievements:
            pdf_file.write(f"- {ach}\n")
        pdf_file.write("\n")

        pdf_file.write("Skills:\n")
        for skill in skills:
            pdf_file.write(f"- {skill}\n")
        pdf_file.write("\n")

        pdf_file.write("Projects:\n")
        for proj in projects:
            pdf_file.write(f"- {proj}\n")
        pdf_file.write("\n")

        pdf_file.write("Experience:\n")
        for exp in experience:
            pdf_file.write(f"- {exp}\n")
        pdf_file.write("\n")

    print(f"PDF resume saved as {pdf_filename}")

    # LibreOffice Writer generation
    with open(odt_filename, "w") as odt_file:
        odt_file.write(f"Name: {name}\n\n")
        odt_file.write(f"Email: {email}\n")
        odt_file.write(f"Phone: {phone}\n\n")

        odt_file.write("Education:\n")
        for edu in education:
            odt_file.write(f"- {edu}\n")
        odt_file.write("\n")

        odt_file.write("Achievements:\n")
        for ach in achievements:
            odt_file.write(f"- {ach}\n")
        odt_file.write("\n")

        odt_file.write("Skills:\n")
        for skill in skills:
            odt_file.write(f"- {skill}\n")
        odt_file.write("\n")

        odt_file.write("Projects:\n")
        for proj in projects:
            odt_file.write(f"- {proj}\n")
        odt_file.write("\n")

        odt_file.write("Experience:\n")
        for exp in experience:
            odt_file.write(f"- {exp}\n")
        odt_file.write("\n")

    print(f"LibreOffice Writer resume saved as {odt_filename}")

    # Open the generated files, only uncomment if you need it.
    #subprocess.run(["xdg-open", pdf_filename])
    #subprocess.run(["xdg-open", odt_filename])

if __name__ == "__main__":
    name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")

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

    skills = []
    print("Enter your skills (press enter twice to stop):")
    while True:
        skill = input()
        if not skill:
            break
        skills.append(skill)

    projects = []
    print("Enter your projects (press enter twice to stop):")
    while True:
        proj = input()
        if not proj:
            break
        projects.append(proj)

    experience = []
    print("Enter your experience (press enter twice to stop):")
    while True:
        exp = input()
        if not exp:
            break
        experience.append(exp)

    pdf_filename = input("Enter the filename for the PDF resume (e.g., resume.pdf): ")
    odt_filename = input("Enter the filename for the LibreOffice Writer resume (e.g., resume.odt): ")

    generate_resume_files(name, email, phone, education, achievements, skills, projects, experience, pdf_filename, odt_filename)

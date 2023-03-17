def getEduDetails(content):
    course = input("Study program: ")
    specs = input("Specification: ")
    institute = input("Name of institution: ")
    duration = int(input("Course duration(in years): "))
    yearOfPassing = int(input("Year of passing: "))
    percentage = float(input("Percentage/CGPA obtained: "))
    content+=f"\n\tStudy Program: {course}\n\t\tName of institution: {institute}\n\t\tCourse Specification: {specs}\n\t\tCourse Duration: {duration}\n\t\tYear of passing: {yearOfPassing}\n\t\tPercentage Obtained: {percentage}\n"
    while True:
        addEdu = input("Do you want to add more education details?(yes/no): ")
        match addEdu:
            case "yes":
                return getEduDetails(content)
            case "no":
                return content
            case default:
                print("Enter valid input")

def getExperience(content):
    role = input("Title/Position: ")
    institute = input("Workplace/Company name: ")
    duration = int(input("Duration in months: "))
    tasks = input("Achievements/Tasks: ")
    content+=f"\n\t{role}\n\t\tWorkplace/Company Name: {institute}\n\t\tDuration in Years: {duration}\n\t\tAchievements\Tasks: {tasks}\n"

    while True:
        addEx = input("Do you want to add more work experience?(yes/no)")
        match addEx:
            case "yes":
                return getExperience(content)
            case "no":
                return content
            case default:
                print("Enter valid input")


def getProject(content):
    projectName = input("Project Name: ")
    projectdesc = input("Project Description: ")
    content+=f"\n\t{projectName}\n\t\tProject Description: {projectdesc}\n"

    while True:
        addProject = input("Do you want to add more projects?(yes/no)")
        match addProject:
            case "yes":
                return getProject(content)
            case "no":
                return content
            case default:
                print("Enter valid input")


def addLanguage(content):
    lang = input("Enter language to be added: ")

    while True:
        proficiency = int(input("Enter the proficiency level of the language from 5 to 1: "))
        match proficiency:
            case 5:
                level="Native Proficiency"
                break
            case 4:
                level="Full Professional Proficiency"
                break
            case 3:
                level = "Professional Working Proficiency"
                break
            case 2:
                level="Limited Working Proficiency"
                break
            case 1:
                level="Elementary Proficiency"
                break
            case default:
                print("Enter valid input")
    content+=f"\n\t{lang} -{level}"
    while True:
        addLang = input("Do you want to add more languages?(yes/no): ")
        match addLang:
            case "yes":
                return addLanguage(content)
            case "no":
                return content
            case default:
                print("Enter valid input")


print("ENTER DETAILS TO BE ADDED IN THE RESUME")
print("BASIC DETAILS")
fname = input("First name: ")
lname = input("Last name: ")
designation = input("Role/Designation: ")
objective = input("Resume objective: ")
location = input("Location/city: ")

print("CONTACT DETAILS")
phone = int(input("Phone number: "))
email = input("Email: ")

resume = open("Resume.txt", "w")
content = f"{fname} {lname}\n{designation}\n{objective}\n\nCONTACT\n\tEmail: {email}\n\tPhone number: {phone}\n\tCity/Address: {location}"

print("EDUCATION DETAILS")
content += f"\n\nEDUCATION"
print("Do you want to include education details in the resume?")
while True:
    choice = input("Enter yes/no: ")
    match choice:
        case "yes":
            content=getEduDetails(content)
            break
        case "no":
            break
        case default:
            print("please enter valid input")

print("WORK EXPERIENCE")
content += f"\n\nWORK EXPERIENCE"
print("Do you have any work experience?")
while True:
    choice = input("Enter yes/no: ")
    match choice:
        case "yes":
            content=getExperience(content)
            break
        case "no":
            break
        case default:
            print("please enter valid input")

print("PROJECT DETAILS")
content += f"\n\nPROJECTS"
print("Do you have project details to be added?")
while True:
    choice = input("Enter yes/no: ")
    match choice:
        case "yes":
            content=getProject(content)
            break
        case "no":
            break
        case default:
            print("please enter valid input")

print("SKILLS")
content+=f"\n\nSOFT SKILLS"
print("Enter your soft skills\nEnter 0 after complete entering the skills")
while True:
    skill = input()
    if skill == "0":
        break
    content += f"\n\t-> {skill}"

content+=f"\n\nTECHNICAL SKILLS"
print("Enter technical skills\nEnter 0 after complete entering the skills")
while True:
    skill = input()
    if skill == "0":
        break
    content += f"\n\t-> {skill}"

print("LANGUAGES KNOWN")
content+=f"\n\nLANGUAGES"
print("Do you want to add languages?")
while True:
    lang = input("Enter yes/no: ")
    match lang:
        case "yes":
            content=addLanguage(content)
            break
        case "no":
            break
        case default:
            print("please enter valid input")

print("INTERESTS")
content+=f"\n\nINTERESTS/HOBBIES"
print("Enter your interests\nEnter 0 after complete entering")
while True:
    interest = input()

    if interest == "0":
        break
    content += f"\n\t{interest}"

print("SOCIAL")
content+=f"\n\nSOCIAL"
print("Do you want to add Github link?")
while True:
    git = input("Enter yes/no: ")
    match git:
        case "yes":
            gitUrl = input("Enter Github URL: ")
            content+=f"\n\tGitHub: {gitUrl}"
            break
        case "no":
            break
        case default:
            print("please enter valid input")

print("Do you want to add LinkedIn link? ")
while True:
    linked = input("Enter yes/no: ")
    match linked:
        case "yes":
            linkedUrl = input("Enter LinkedIn URL: ")
            content += f"\n\tLinkedIn: {linkedUrl}"
            break
        case "no":
            break
        case default:
            print("please enter valid input")
resume.write(content)
resume.close()
print("Resume Generated:)")

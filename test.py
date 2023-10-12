import utils

class User:
    def Error(self, error):
        print(f"{utils.color.ERROR}Error{utils.color.RESET}: {error}")
    
    def SetAge(self):
        age = input("Enter the age: ")
        
        if int(age) > -1:
            self.age = age
        else:
            self.Error("Age must be a number at least 0");
            self.SetAge()
    
    def SetGender(self):
        gender = input("Enter the gender ('M' for 'male', 'F' for 'female'): ")

        if gender.lower() == "male" or gender.lower() == 'm':
            self.gender = "male"
        elif gender.lower() == "female" or gender.lower() == 'f':
            self.gender = "female"
        else:
            self.Error(f"Your gender ({gender.lower()}) is not recognized");
            self.SetGender()
    
    def SetName(self):
        name = input("Enter the name: ")

        if len(name) < 1:
            self.Error("The name is written only in letters");
            self.SetName()
            return 
        for c in name.lower():
            if not c.islower() and not c != ' ':
                self.Error("The name is written only in letters");
                self.SetName()
                return

        self.name = name

    def SetCity(self):
        city = input("Enter the city: ")

        if len(city) < 1:
            self.Error("The city is written only in letters");
            self.SetCity()
            return 
        for c in city.lower():
            if not c.islower() and not c != ' ':
                self.Error("The city is written only in letters");
                self.SetCity()
                return

        self.city = city
    
    def SetGrade(self):
        grade = input("Enter the grade: ")

        if int(grade) > -1 and int(grade) < 12:
            self.grade = grade
        else:
            self.Error("Grade must be a number not less than 0 and not more than 11");
            self.SetGrade()

    def __init__(self):
        self.name = "-1"
        self.age = -1
        self.gender = '\0'
        self.city = "-1"
        self.grade = -1

        self.SetName()
        self.SetAge()
        self.SetGender()
        self.SetCity()
        self.SetGrade()

def main():
    users = []

    while True:
        utils.clear()
        i = input("What do you want to do?\nCreate a user (C) | Delete a user (D) | View the list of users (L) | Close the program (X)\n")
        utils.clear()

        match i.upper():
            case 'C':
                users.append(User())
            case 'D':
                pass
            case 'L':
                for i in range(len(users)):
                    print(f"[{i}] {users[i].name} ({users[i].gender}), {users[i].age} y.o. ({users[i].grade} grade), from {users[i].city}")
                input()
            case 'X':
                break
            case _:
                print("Unknown command")

        


if __name__ == "__main__":
    main()
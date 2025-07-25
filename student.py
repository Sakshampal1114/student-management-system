from datetime import datetime

class Student:
    def __init__(self, name, dob, email, phone):
        self.name = name 
        self.dob = dob
        self.email = email
        self.phone = phone
        self.age = self.calculate_age()

    def calculate_age(self):
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def to_dict(self):
        return {
            "Name": self.name,
            "DOB": self.dob,
            "AGE": self.age,
            "Email": self.email,
            "Phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["Name"],
            data["DOB"],
            data["Email"],
            data["Phone"]
        )

    def __str__(self):
        return f"{self.name} | {self.age} year | {self.email} | {self.phone}"

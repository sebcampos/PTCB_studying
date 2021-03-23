from definitions import *
import os

class MedicalTerms:
    def __init__(self, date):
        self.date = date
        self.score = 0
    def __repr__(self):
        print(f"Medical Terms Glossary\n{self.date}")
        for i in medical_terms_lst_definitions_names:
            print(i)
    def quiz(self, option="all"):
        os.system("clear")
        if option == "all":
            for i in medical_terms_lst_definitions:
                for x,y in i.items():
                    print(x)
                    answer = input("Enter Answer:\n")
                    os.system("clear")
                    for var in y:
                        print(var)
                    if answer in [var.lower() for var in y]:
                        print("True")
                        self.score += 1
                    elif answer not in [var.lower() for var in y]:
                        print("False")
                    input("Enter to continue:\n")
                    os.system("clear")
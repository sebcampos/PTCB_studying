from definitions import *
import os


for i in key_definitions.values():
    print(i)

print("Objects:\n\nMedicalTerms\nPrescriptionAbbreviations\nClinicalTerms")


class MedicalTerms:
    def __init__(self, date):
        self.date = date
        self.score = 0
    def __repr__(self):
        print(f"Medical Terms Glossary\n{self.date}\n\n")
        for i in medical_terms_lst_definitions_names:
            print(i)
    def quiz(self, option="all"):
        os.system("clear")
        if option == "all":
            total_questions = 0
            for i,v in zip(medical_terms_lst_definitions,medical_terms_lst_definitions_names):
                print(v)
                for x,y in i.items():
                    print(x)
                    answer = input("Enter Answer:\n")
                    total_questions +=1
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
            print(f"Score for MedicalTerms: {self.score / total_questions}")
            self.score = 0
            return "end"

class PrescriptionAbbreviations:
    def __init__(self, date):
        self.date = date
        self.score = 0
    def __repr__(self):
        print(f"Prescription Abbreviations Glossary\n{self.date}\n\n")
        for i in prescription_abbr_lst_names:
            print(i)
    def quiz(self, option="all"):
        os.system("clear")
        if option == "all":
            total_questions = 0
            for i,v in zip(prescription_abbr_lst,prescription_abbr_lst_names):
                print(v)
                for x,y in i.items():
                    print(x)
                    answer = input("Enter Answer:\n")
                    total_questions +=1
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
            print(f"Score for PrescriptionAbbreviations: {self.score / total_questions}")
            self.score = 0
            return "end"

class ClinicalTerms:
    def __init__(self, date):
        self.date = date
        self.score = 0
    def __repr__(self):
        print(f"Clinical Terms Glossary\n{self.date}\n\n")
        for i in prescription_abbr_lst_names:
            print(i)
    def quiz(self, option="all"):
        os.system("clear")
        if option == "all":
            total_questions = 0
            for i,v in zip(clinical_definitions_lst,clinical_definitions_lst_names):
                print(v)
                for x,y in i.items():
                    print(x)
                    answer = input("Enter Answer:\n")
                    total_questions +=1
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
            print(f"Score for PrescriptionAbbreviations: {self.score / total_questions}")
            self.score = 0
            return "end"


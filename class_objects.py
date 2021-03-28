from definitions import *
import os
import pandas
import datetime

today = str(datetime.datetime.today().date())

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
pandas.set_option('display.width', None)
# pandas.set_option('display.max_colwidth', None)


for i in key_definitions.values():
    print(i)

print("\n\nObjects:\n\nMedicalTerms\nPrescriptionAbbreviations\nClinicalTerms\nCommonlyPrescribedDrugs")




class MedicalTerms:
    def __init__(self, date):
        self.date = date
        self.score = 0
        dictionary={}
        for i in medical_terms_lst_definitions:
            for x,y in i.items():
                dictionary[x] = [", ".join(y)]
        self.df = pandas.DataFrame(dictionary).T 
    def __repr__(self):
        print(f"Medical Terms Glossary\n{self.date}\n")
        for i in medical_terms_lst_definitions_names:
            print(i)
        print("\nAttributes:\ndate\nscore\ndf\n\nFunctions:\nquiz(option=all)")
        return ""
    def quiz(self, option="all"):
        self.score = 0
        os.system("clear")
        if option == "all":
            total_questions = 0
            for i,v in zip(medical_terms_lst_definitions,medical_terms_lst_definitions_names):
                print(v,"\n")
                for x,y in i.items():
                    print(x)
                    answer = input("Enter Answer:\n")
                    total_questions +=1
                    os.system("clear")
                    for var in y:
                        print(var)
                    if answer.lower() in [var.lower() for var in y]:
                        print("True")
                        self.score += 1
                    elif answer not in [var.lower() for var in y]:
                        print("False")
                    input("Enter to continue:\n")
                    os.system("clear")
            print(f"Score for MedicalTerms: {self.score / total_questions}")
            return "end"

class PrescriptionAbbreviations:
    def __init__(self, date):
        self.date = date
        self.score = 0
        dictionary={}
        for i in prescription_abbr_lst:
            for x,y in i.items():
                dictionary[x] = [", ".join(y)]
        self.df = pandas.DataFrame(dictionary).T 
    def __repr__(self):
        print(f"Prescription Abbreviations Glossary\n{self.date}\n")
        for i in prescription_abbr_lst_names:
            print(i)
        print("\nAttributes:\ndate\nscore\ndf\n\nFunctions:\nquiz(option=all)")
        return ""
    def quiz(self, option="all"):
        self.score = 0
        os.system("clear")
        if option == "all":
            total_questions = 0
            for i,v in zip(prescription_abbr_lst,prescription_abbr_lst_names):
                print(v,"\n")
                for x,y in i.items():
                    print(x)
                    answer = input("Enter Answer:\n")
                    total_questions +=1
                    os.system("clear")
                    for var in y:
                        print(var)
                    if answer.lower() in [var.lower() for var in y]:
                        print("True")
                        self.score += 1
                    elif answer not in [var.lower() for var in y]:
                        print("False")
                    input("Enter to continue:\n")
                    os.system("clear")
            print(f"Score for PrescriptionAbbreviations: {self.score / total_questions}")
            return "end"

class ClinicalTerms:
    def __init__(self, date):
        self.date = date
        self.score = 0
        dictionary={}
        for i in clinical_definitions_lst:
            for x,y in i.items():
                dictionary[x] = [", ".join(y)]
        self.df = pandas.DataFrame(dictionary).T 
    def __repr__(self):
        print(f"Clinical Terms Glossary\n{self.date}\n")
        for i in prescription_abbr_lst_names:
            print(i)
        print("\nAttributes:\ndate\nscore\ndf\n\nFunctions:\nquiz(option=all)")
        return ""
    def quiz(self, option="all"):
        os.system("clear")
        if option == "all":
            self.score = 0
            total_questions = 0
            for i,v in zip(clinical_definitions_lst,clinical_definitions_lst_names):
                print(v,"\n")
                for x,y in i.items():
                    print(x)
                    answer = input("Enter Answer:\n")
                    total_questions +=1
                    os.system("clear")
                    for var in y:
                        print(var)
                    if answer.lower() in [var.lower() for var in y]:
                        print("True")
                        self.score += 1
                    elif answer not in [var.lower() for var in y]:
                        print("False")
                    input("Enter to continue:\n")
                    os.system("clear")
            print(f"Score for PrescriptionAbbreviations: {self.score / total_questions}")
            return "end"

class CommonlyPrescribedDrugs:
    def __init__(self, date):
        self.date = date
        self.score = 0
        self.df = pandas.DataFrame(one_hundred_most_commonly_prescribed_drugs)
    def __repr__(self):
        print("Commonly Prescribed Drugs Columns:\n")
        for i in self.df.columns:
            print(i)
        return ""
    def quiz(self):
        for row in self.df.iterrows():
            response = []
            for column in self.df.columns[1:]:
                print(f"Generic:\n{row[1][0]}\n\nEnter {column}:\n")
                answer = input() 
                if self.df.loc[self.df["Generic Name"] == row[1][0], column].item().lower().strip() == answer.lower().strip():
                    response += [1]
                    print("Correct")
                    input()
                    os.system("clear")
                else:
                    print("Incorrect:\n")
                    print(self.df.loc[self.df["Generic Name"] == row[1][0], column].item())
                    os.system("clear")
            
            print(sum(response))
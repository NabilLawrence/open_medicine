#-----------------------------------------------------
import numpy as np
import pandas as pd
import re
#-----------------------------------------------------
df = pd.read_csv("../data/OGD_FakeSet.csv")
#-----------------------------------------------------
def data_cleaning(df):
    def regex_hosp(string):
        hospital_reg = r"\.*Hospital:.*"
        line = re.findall(hospital_reg, string)[0]
        return  line.replace(',',':').split(":")[1]

    df["foundation_trust"] = df['text'].apply(regex_hosp)
    #-----------------------------------------------------
    def regex_hosp_num(string):
        hospital_reg = r"\.*Hospital Number.*"
        line= re.findall(hospital_reg, string)[0]
        return  line.replace(',',':').split(":")[1]
    df["hospital_num"] = df['text'].apply(regex_hosp_num)
    #-----------------------------------------------------
    def regex_GP(string):
        hospital_reg = r"\.*General Practitioner:.*"
        line = re.findall(hospital_reg, string)[0]
        retrn_string= line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            return retrn_string[:-1]
        else:
            return retrn_string
    df["gp"] = df['text'].apply(regex_GP)
    #-----------------------------------------------------
    def regex_DOB(string):
        hospital_reg = r"\.*DOB:.*"
        line =  re.findall(hospital_reg, string)[0]
        retrn_string= line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            return retrn_string[:-1]
        else:
            return retrn_string
    df["DOB"] = df['text'].apply(regex_DOB)
    #-----------------------------------------------------
    def regex_procedure_date(string):
        hospital_reg = r"\.*Date of procedure:.*"
        line =  re.findall(hospital_reg, string)[0]
        retrn_string =  line.split(":")[1][:-11]
        if retrn_string[-1:] == "\r":
            return retrn_string[:-1]
        else:
            return retrn_string
    df["procedure_date"] = df['text'].apply(regex_procedure_date)
    #-----------------------------------------------------
    def regex_endoscopist(string):
        hospital_reg = r"\.*Endoscopist:.*"
        line = re.findall(hospital_reg, string)[0]
        retrn_string =  line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            return retrn_string[:-1]
        else:
            return retrn_string
    df["endoscopist"] = df['text'].apply(regex_endoscopist)
    #-----------------------------------------------------
    def regex_2nd_endoscopist(string):
        hospital_reg = r"\.*2nd Endoscopist:.*"
        line= re.findall(hospital_reg, string)[0]
        retrn_string =  line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            return retrn_string
        else:
            return retrn_string
    df["second_endoscopist"] = df['text'].apply(regex_2nd_endoscopist)
    #-----------------------------------------------------
    def regex_medication(string):
        hospital_reg = r"\d*.\dmcg"
        retrn_string= re.findall(hospital_reg, string)[0]
        if retrn_string[-1:] == "\r":
            return float(retrn_string[:-4])
        else:
            return float(retrn_string[:-3])
    df["medications_fentynl"] = df['text'].apply(regex_medication)
    #-----------------------------------------------------
    def regex_midazolam(string):
        hospital_reg = r"\.*Midazolam.*"
        line = re.findall(hospital_reg, string)[0]
        retrn_string =  line.split()[1]
        if retrn_string[-1:] == "\r":
            return int(retrn_string[:-3])
        else:
            return int(retrn_string[:-2])
    df["midazolam"] = df['text'].apply(regex_midazolam)
    #-----------------------------------------------------
    def regex_instrument(string):
        hospital_reg = r"\.*Instrument.*"
        line = re.findall(hospital_reg, string)[0]
        retrn_string =  line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            return retrn_string[:-1]
        else:
            return retrn_string
    df["instrument"] = df['text'].apply(regex_instrument)
    #-----------------------------------------------------
    def regex_extent(string):
        hospital_reg = r"\.*Extent of Exam:.*"
        line = re.findall(hospital_reg, string)[0]
        retrn_string =  line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            return retrn_string[:-1]
        else:
            return retrn_string
    df["extent_of_exam"] = df['text'].apply(regex_extent)
    #-----------------------------------------------------
    def regex_indications(string):
        hospital_reg = r"\.*INDICATIONS FOR PROCEDURE:.*"
        line = re.findall(hospital_reg, string)[0]
        retrn_string =  line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            retrn_string= retrn_string[:-1]
        if retrn_string[-8:] == "FINDINGS":
            return retrn_string[:-8]
        else:
            return retrn_string
    #-----------------------------------------------------
    df["indications"] = df['text'].apply(regex_indications)

    def regex_procedure(string):
        hospital_reg = r"\.*Procedure Performed:.*"
        line = re.findall(hospital_reg, string)[0]
        retrn_string =  line.replace(',',':').split(":")[1]
        if retrn_string[-1:] == "\r":
            return retrn_string[:-1]
        else:
            return retrn_string
        print(retrn_string)
    df["procedure_performed"] = df['text'].apply(regex_procedure)
    #-----------------------------------------------------
    def regex_findings(string):
        hospital_reg = r"\.*FINDINGS:.*"
        line = re.findall(hospital_reg, string)[0][10:]
        return line
    df["findings"] = df['text'].apply(regex_findings)
    #-----------------------------------------------------
    df_extracted = df[["extent_of_exam","indications","findings"]]
    #-----------------------------------------------------
    #print(df_extracted)
    return df_extracted

# # import re
# # row = '''Difficulty attaining erection
# # Notes: Referral to urology has been requested on patient's beahlf.'''
# # pattern = "Referral to (:|\s|[a-z].*)"
# # match = re.findall(pattern, row, flags=re.IGNORECASE)
# # print(match)
# import re
# # row="""Injury of left foot, initial encounter
# # Imaging:X ray : Foot, left
# # Notes: 1. left foot 3 views Xray report indicates IMpression: There is no convincing evindence of acute fracture, dislocation, or osseous destructive process. Joint spaces appear grossly maintained and free of significant degenerative changes. No radiographically evident of soft tissue abnormality
# # 2. Patient instructed to rest the affected left foot, elevate, and use ice therapy for 15-20 minutes a least every 1-2 hours for 3 days, then thereafter, alternate between ice and heat therapy
# # 3. Patient instructed to continue taking th Ibuprofen for pain since it is helping with her pain and follow the insructions on the box
# # 4. Patient insructed to return to the clinic in 7 days if no improvement in symptoms for further evaluation and treatment. Patient verbalized understanding."""
# # pattern=">:[a-z] (.+?)\n"
# # match=re.findall(pattern,row,flags=re.IGNORECASE)
# # print(match)
# row="""COVID
# Start Azithromycin Tablet, 250 MG, 2 tabs day 1 1 tab days 2 - 5, Orally, Once a day, 5 day(s), 1 Pack, Refills 1
# Start Ivermectin Tablet, 3 MG, take 4 tabs day 1 and 4 tabs day 3, Orally, as directed, 2 days, 4, Refills 0
# Start Bromfed DM Syrup, 30-2-10 MG/5ML, 5 ml as needed, Orally, every 6 hrs, 5 days, 100 ml, Refills 0

# Referral of:Matched

#  Reason:84 years old

#      Others
#          Notes: Covid protocol sheet given to pt, Rapid covid test is positive. 
# Isolate for 5 days. Follow the covid handout for care at home. 
# Stay hydrated. If resp status worsens, come in here for reevaluation and neb treatment."""
# # pattern="Referral To[:|\s].+?\n|Referral of[:|\s](.+?\n)"
# # match=re.findall(pattern,row,flags=re.IGNORECASE) 
# # print(match)
# if 'referral to' in row.lower():
#     pattern="Referral To[:|\s](.+?)\n"
#     match=re.findall(pattern,row,flags=re.IGNORECASE) 
#     print(match) 
# elif 'referral of' in row.lower():
#     pattern="Referral of[:|\s](.+?)\n"
#     match=re.findall(pattern,row,flags=re.IGNORECASE)
#     print(match)
# elif 'referred to'in row:
#     pattern="Referred To[:|\s](.+?)\n"
#     match=re.findall(pattern,row,flags=re.IGNORECASE)
#     print(match)
# else:
#     print("no match")

# from ast import pattern


# from re import IGNORECASE

import re
from sqlite3 import Row
# row="""Acute URI
# Start Azithromycin Tablet, 250 MG, 2 tabs day 1 1 tab days 2 - 5, Orally, Once a day, 5 day(s), 1 Pack, Refills 1
#      Fatigue, unspecified type
#          Lab:SARS CoV 2 RNA(COVID 19), QUALITATIVE NAAT
#                         Value        Reference Range
#                 SARS CoV 2 RNA        neg                NEG - NEG
#                    Turpen,Angie 01/01/2022 02:11:37 PM CST > Done. AT Turpen,Angie 01/01/2022 02:31:42 PM CST > Scanned
#      Others
#          Notes: fluids, rest, supportive measures for fever/symptom relief."""

row="""COVID-19

         
Start Zithromax Z-Pak Tablet, 250 MG, 2 tablets on the first day, then 1 tablet daily for 4 days, Orally, as directed, 5 day(s), 1 Dose Pack, Refills 0
         
Start Ivermectin Tablet, 3 MG, as directed, Orally, 7 tabs today, then repeat in 3 days, 2 days, 14 Tablet, Refills 0
         Clinical Notes: -30 minutes spent wtih patient review chart/medication/history/lab review/patient education/answer questions.

     Fever

         
Start Bromfed DM Syrup, 30-2-10 MG/5ML, 10 ml as needed, Orally, every 4 hrs, 5 days, 300 ml, Refills 0
         Lab:Strep A DNA AMP Probe  Negative
                        Value        Reference Range
                STREP A        Negative                
                   Nava,Bianca 01/14/2022 11:41:34 AM CST > Done..bn
         Lab:SARS CoV 2 RNA(COVID 19), QUALITATIVE NAAT  Positive
                        Value        Reference Range
                SARS CoV 2 RNA        Positive                NEG - NEG
                   Nava,Bianca 01/14/2022 11:38:14 AM CST > Done..bn
         Lab:Coronavirus (COVID-19), NAA  Abnormal
                        Value        Reference Range
                SARS-CoV-2, NAA        Detected        A        Not Detected -
                   Flores,Martha 01/19/2022 01:27:17 PM CST > positive covid send out, continue present tx, check and see how he is doing Flores,Martha 01/19/2022 01:26:57 PM CST > Nava,Bianca 01/19/2022 02:21:22 PM CST > Pt informed about results..bn
     Others
         Notes: -covid education given
-covid isolation as per CDC
-ibuprofen/tylenol prn pain/fever
-monitor resp distress, go to the ER if symptoms worsen."""

pattern="start\s(.+?)((?:\n|mg,|ml,|%,))"
match=re.findall(pattern, row, flags=re.IGNORECASE)
print(match)

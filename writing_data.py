import csv
import pandas as pd

combined = pd.read_csv('data\\Combined Data.csv')

with open('data//FinalData.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Homework', 'Project', 'Quiz', 'Exam', 'Total', 'Final', 'Grade'])

    for row in combined.iterrows():
        currentRow = row[1]
        hw = (currentRow['HW01'] + currentRow['HW02'] + currentRow['HW03'] + currentRow['HW04'] + currentRow['HW05'] + currentRow['HW06']) / 6 * 5
        proj = float(currentRow['PJ01'])
        quiz = (currentRow['QZ01'] + currentRow['QZ02']) / 2
        exam = currentRow['EX01']
        total = (hw * .15) + (proj * .15) + (quiz * .2) + (exam * .5)
        final = currentRow['Final']
        letter = currentRow['Grade']
        csvwriter.writerow([hw, proj, quiz, exam, total, final, letter])
        
    csvfile.close()
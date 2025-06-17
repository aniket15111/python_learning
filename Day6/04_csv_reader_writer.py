import csv
with open('mydata.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Aniket', 24])
    writer.writerow(['Aastha', 19])

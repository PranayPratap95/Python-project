import csv
with open('file3.csv','w') as csvfile:
    fieldnames = ["first_name","last_name"]
    writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"first_name":"Pranay","last_name":"Pratap"})
    writer.writerow({"first_name":"Malay","last_name":"Shah"})
    r="prakhar"
    t="sharma"
    writer.writerow({"first_name":r,"last_name":t})
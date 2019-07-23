#coding:utf-8

import csv
import datetime
import random
import string

datetime = random.uniform(datetime.datetime(2000, 1, 1,microsecond = 0), datetime.datetime(2019, 1, 1, microsecond = 0))



with open("test.tsv","w+") as new_file:#test.tsvというファイルを新規作成。変数名「ｔ」
    s = csv.writer (new_file, delimiter="\t")
    fieldnames = ["log_id", "date", "latitude", "longitude"]
    writer = csv.DictWriter(new_file, fieldnames=fieldnames , delimiter="\t")
    writer.writeheader()

    for a in range(1, 10000+1):
        idone =string.digits + string.ascii_uppercase
        def randomname(n):
            return ''.join([random.choice(idone) for i in range(1, 10+1)])
        def randomnames(n):
            return ''.join([random.choice(idone) for e in range(1, 4+1)])

    

        log = str(randomname(7)) + "-" + str(randomnames(7)) + "-"
        lat = random.uniform(34.5, 35.5)
        long = random.uniform(134, 139)
        writer.writerow({"log_id": log, "date" : datetime, "latitude": lat, "longitude": long})

        

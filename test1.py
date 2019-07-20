#coding:utf-8

import csv
import datetime
import random

datetime = random.uniform(datetime.datetime(2000, 1, 1,microsecond = 0), datetime.datetime(2019, 1, 1, microsecond = 0))


with open("test.tsv","w+") as new_file:#test.tsvというファイルを新規作成。変数名「ｔ」
    s = csv.writer (new_file, delimiter="\t")
    fieldnames = ["log_id", "date", "latitude", "longitude"]
    writer = csv.DictWriter(new_file, fieldnames=fieldnames , delimiter="\t")
    writer.writeheader()

    for a in range(1, 10000+1):
        log = 1
        lat = random.uniform(34.5, 35.5)
        long = random.uniform(134, 139)
        writer.writerow({"log_id": log, "date" : datetime, "latitude": lat, "longitude": long})

        

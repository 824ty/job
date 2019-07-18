#coding:utf-8

import csv

with open("test.csv","w+") as t:#test.tsvというファイルを新規作成。変数名「ｔ」
    for s in range(1,500 + 1):
        s = csv.writer (t, delimiter=",")
        s.writerow(["one", "two", "three", "four", "five"])
        s.writerow(["1", "2", "3", "4", "5"])

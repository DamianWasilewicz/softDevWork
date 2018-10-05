#The Wicked W's - Jeffrey Wu & Damian Wasilewicz
#SoftDev1 pd0
#K #16: No Trouble  
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

def makeTable(filename):
    with open(filename, 'r') as csvfile: # open csv file
        courses = csv.DictReader(csvfile) #read it in
        #print(reader.get(0))
        fir = 0 #indicates whether its going through the first time or not, if 0 then first time
        for rec in courses:
            if fir == 0:
                comm = "CREATE TABLE " + filename[:len(filename) - 4] + " (" #beginning of creation statement as a string
                for col in rec.keys():
                    comm += "'" + col + "' BLOB, " #add each col in
                    #print(command[:len(command) - 2] + ")")
                c.execute(comm[:len(comm) - 2] + ")") #execute commmand
                fir = 1; #since its no longer 0, recognize that its no long firdt time through
            comm2 = "INSERT INTO " + filename[:len(filename) - 4] + " VALUES (" #initialize insert statement as string
            for info in rec.keys():
                comm2 += "'" + rec[info] + "', " #add each column of data to statement
            c.execute(comm2[:len(comm2) - 2] + ")") #execute command with string 
f = True
#to deal with error where it sometimes returns error sahing table already exists and skmetimes that table foesnt exist
if f:
    c.execute("DROP TABLE peeps;") # Gets rid of peeps table if it already exists
    c.execute("DROP TABLE courses;")
    c.execute("DROP TABLE occupations;") # Gets rid of courses table if it already exists
    makeTable("peeps.csv")
    makeTable("courses.csv")
    makeTable("occupations.csv") #run for both csv files
    c.execute("SELECT * FROM courses")
    print(c.fetchall())
    c.execute("SELECT * FROM peeps")
    print(c.fetchall()) #print data from each table
    c.execute("SELECT * FROM occupations")
    print(c.fetchall())
    f = False
else:
    c.execute("DROP TABLE peeps;") # Gets rid of peeps table if it already exists
    c.execute("DROP TABLE courses;")
    c.execute("DROP TABLE occupations;") # Gets rid of courses table if it already exists
    makeTable("peeps.csv")
    makeTable("courses.csv")
    makeTable("occupations.csv") #run for both csv files
    c.execute("SELECT * FROM courses")
    print(c.fetchall())
    c.execute("SELECT * FROM peeps")
    print(c.fetchall()) #print data from each table
    c.execute("SELECT * FROM occupations")
    print(c.fetchall()) #print data from each table


db.commit() #save changes
db.close()  #close database

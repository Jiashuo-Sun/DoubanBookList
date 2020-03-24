import pymysql
import os
from datetime import datetime



filepath = os.path.dirname(os.getcwd())
datapath_in = filepath + '/data/CleanBookInfo.csv'

# Need to set up your own mysql user info and database.
config = {'user':'','password':'','host':'localhost','db':'doubanbook','local_infile':1}

con = pymysql.connect(**config)

with con.cursor() as cur:
    cur.execute('CREATE TABLE CleanBookInfo (bookname VARCHAR(255), author VARCHAR(255), Avg float, Num int);')
    sql_in = "load data local infile \'" + datapath_in + "\' into table CleanBookInfo fields terminated by ',' lines terminated by '\n';"
    cur.execute(sql_in)
    while True:
        minavg = input('Input the minimum average review score: ')
        if minavg.lower() == 'exit' or minavg.lower() == 'quit': break
        minnum = input('Input the minimum review number: ')
        if minnum.lower() == 'exit' or minnum.lower() == 'quit': break    

        
        datapath_out = filepath +'/BookList/BookList_' + str(minavg) + '_' + str(minnum) + '_' + ''.join(str(datetime.today().date()).split('-')) + '.csv'

        ## if the permission denied, one option is to save tables under /tmp and move them to the BookList file
        # datapath_out = '/tmp/BookList_' + str(minavg) + '_' + str(minnum) + '_' + ''.join(str(datetime.today().date()).split('-')) + '.csv'

        sql_out = "select * from CleanBookInfo where Avg >= "+ minavg +" and Num >= " + minnum + " order by Avg desc, Num desc into outfile \'" + datapath_out + "\' fields terminated by ',' lines terminated by '\n';" 
        cur.execute(sql_out)
    cur.execute('Drop table CleanBookInfo;')
    cur.close()
con.close()

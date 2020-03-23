``` SQL
CREATE TABLE tablename (id INT, num float, last_name VARCHAR(255), email VARCHAR(255), transactions INT NOT NULL, account_creation DATE, PRIMARY KEY (id));
```

``` SQL
LOAD DATA LOCAL INFILE '/home/user/Desktop/WebCrawler/cleanBookList.csv' 
INTO TABLE cleanBookList_0320 
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```


``` SQL
create table BookList_9_500 
select * from cleanBookList_0320 
where viewavg >= 9 and viewnum >= 500;
```

``` SQL
select * from BookList_9_500 
order by Avg desc,Num desc 
into outfile '/tmp/BookList_9_500.csv' 
fields terminated by ',' 
lines terminated by '\n';
```

``` CMD
sudo mv /tmp/BookList_9_500.csv ~/Desktop/WebCrawler/
```


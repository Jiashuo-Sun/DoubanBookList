# Douban Book List

[Douban Book](https://book.douban.com) is the largest book review website in China. 
In the website of particular book, it has the book name, auther, internatianal standard book number (ISBN), average review score, and review number.

![webpage](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/demo_image/page.png)

In this project, I use web crawler to grab book infomation from Douban Book and clean & merge books from different versions. Rank the top 500 high-score booklist. 


## Project Structure

![Structure](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/demo_image/Structure.png)

You can check some book list results in [BookList](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/BookList).

## Main datasets

You can find these datasets in [data](https://github.com/Jiashuo-Sun/DoubanBookList/tree/master/data).

1. [Book Link Set](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/data/BookLinkSet.txt)

Only record book links.

2. [Book Info Set (Main)](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/data/BookInfoSet.csv)

The main dataset for this project. It contains Book Name, Author, ISBN, Average Review Score, Review Number, URL, and Update Date.


3. [Clean Book Info](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/data/CleanBookInfo.csv)

Drop books without enough review number and clean the book infomation from BookInfoSet.csv and merger the books from different versions.

4. [Book Lists](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/BookList) 

All the filtered book lists are stored in the format of "BookList-MinAvg-MinNum-Date.csv". The books are sorted by the average review score and the number of review. 
By inputing the minimum average review score and minimun review number, [booklist.py](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/code/booklist.py) can generate the specific book list by using MySQL database.

5. [History data of Clean Book Info](https://github.com/Jiashuo-Sun/DoubanBookList/tree/master/history_data)

Since I'm still scraping data from website daily, I will update the CleanBookInfo dataset every day and save it in the history_data for future filtering. 

**I export one data list as a PDF file, you can find a completed one  [here](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/BookList/BookList_9_500_20200323.pdf)**


Happy Reading!

(I'm still working on this! Keep Updating~~)



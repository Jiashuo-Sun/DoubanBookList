# Douban Book List

[Douban Book](https://book.douban.com) is the largest book review website in China. 
In the website of particular book, it has the book name, auther, internatianal standard book number (ISBN), average review score, and review number.

![webpage](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/demo_image/page.png)

In this project, I use web crawler to grab book infomation from Douban Book and clean & merge books from different versions. Rank the top 500 high-score booklist. 


## Project Structure

![Structure](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/demo_image/Structure.png)

## Main datasets

You can find these datasets in [data](https://github.com/Jiashuo-Sun/DoubanBookList/tree/master/data).

1. [Book Link Set](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/data/BookLinkSet.txt)

Only record book links.

2. [Book Info Set (Main)](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/data/BookInfoSet.csv)

The main dataset for this project. It contains Book Name, Author, ISBN, Average Review Score, Review Number, URL, and Update Date.


3. [Clean Book Info](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/data/CleanBookInfo.csv)

Drop books without enough review number and clean the book infomation from BookInfoSet.csv and merger the books from different versions.

4. Book Lists ( Option)

5. [History data of Clean Book Info](https://github.com/Jiashuo-Sun/DoubanBookList/tree/master/history_data)

Since I'm still scraping data from website daily, I will update the cleaned book infomation set every day and save it in the history for future filtering. 

(I'm still working on this! Keep Updating~~)

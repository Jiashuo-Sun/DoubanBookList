# Douban Book List

[Douban Book](https://book.douban.com) is the largest book review website in China. 
In the website of particular book, it has the book name, auther, isbn, average review score, and review number.

![webpage](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/demo_image/page.png)

In this project, I use web crawler to grab book infomation from Douban Book and clean & merge books from different versions. Rank the top 500 high-score booklist. 


## Project Structure

![Structure](https://github.com/Jiashuo-Sun/DoubanBookList/blob/master/demo_image/Structure.png)

## Main datasets
1. Book Link Set

Only record book links.

2. Book Info Set (Main)

The main dataset for this project. It contains Book Name, Author, ISBN, Average Review Score, Review Number, URL, and Update Date.


3. Clean Book Info

Drop books without enough review number and clean the book infomation from BookInfoSet.csv and merger the books from different versions.

4. Book Lists ( Option)

(I'm still working on this! Keep Updating~~)

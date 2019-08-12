
# LogAnalysis Project 

 This project is the first project of the Full Stack Web Developer Nanodegree of Udacity, this project aims to do some statistic to extract information from our databases.
# Questions that this project can answer to it 

  - What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.

    Example:

            "Princess Shellfish Marries Prince Handsome" — 1201 views
            "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
            "Political Scandal Ends In Political Scandal" — 553 views

  - Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.

    Example:

            Ursula La Multa — 2304 views
            Rudolf von Treppenwitz — 1985 views
            Markoff Chaney — 1723 views
            Anonymous Contributor — 1023 views

  -  On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

        Example:

            July 29, 2016 — 2.5% errors

# requirements

  - Python version 3
  - PostgresSql Database

# Usage
- Import the data: [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Use this commande to load data into postgreSql database `psql -d news -f newsdata.sql`
- Run the script by using this commande `python3 project_1.py`
- you will see menu apear like this : 

        1 : the most popular three articles of all time
        2 : the most popular article authors of all time
        3 : the days that more than 1% of requests lead to errors

        to exit enter q
        
        enter the number of the request that you want :
- you have to enter the number of the question that you want and you will see the result
        
        

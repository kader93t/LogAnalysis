#!/usr/bin/env python

import psycopg2
DBNAME = "news"


def print_output(dic, out):
    """ print the output of dic """

    print("\n")
    for value1, value2 in dic:
        print('\t # {} __ {} {}'.format(value1, value2, out))


def query_database(query):

    """ execute the query on the database and return the result"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()

    return result


# 1. What are the most popular three articles of all time?
def top3_article():

    """ get three top aritcles """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = """select articles.title, count(*) as views from articles,
    log where log.path = concat('/article/', articles.slug)
    group by log.path, articles.title order by views desc limit 3;"""
    articles = query_database(query)
    print_output(articles, "views")


# 2. Who are the most popular article authors of all time?
def top_authors():
    """get the top authors """

    query = """select authors.name ,sum(v.views) as views
                from authors,articles,(select substring(path,
                length('/article/')+1,length(path)) as s, count(path) as views
                from log where path like '/article/%' group by path) as v
                where articles.author=authors.id and articles.slug = v.s
                group by authors.name
                order by views desc;
                """
    authors = query_database(query)
    print_output(authors, 'views')


# 3. On which days did more than 1% of requests lead to errors?
def get_day():
    """ get the days that has more than 1% of request lead error"""

    query = '''select er.* from (select to_char(date :: DATE, 'mon dd,yyyy'),
               round(cast((cast(err as float) * 100.0 ) / cast(total as float)
               as decimal ),2) as percentage
               from (select errTable.date, total, err
                    from (select date(time) as date, count(*) as err
                        from log
                        where log.status like '%404%' group by date)
                        as errTable ,
                    (select date(time) as date, count(*) as total
                    from log group by date) as totalTable
                    where totalTable.date=errTable.date) as tab) as
                    er where percentage >1.0; '''
    day = query_database(query)
    print_output(day, "%")


def menu():
    """ show the menu on the screen and get the input from the user
    to execute a specific query
    """

    inp = ''
    while inp != 'q':
        print("\n\n\t\t####### menu ####### \n")
        print("1 : the most popular three articles of all time")
        print("2 : the most popular article authors of all time")
        print("3 : the days that more than 1% of requests lead to errors ")
        print("\nto exit enter q\n")
        inp = input('enter the number of the request that you want : ')
        if inp in ['1', '2', '3']:
            if inp == '1':
                top3_article()
            elif inp == '2':
                top_authors()
            elif inp == '3':
                get_day()
        elif inp != 'q':
            print("please enter one of the choice apear in the menu !")


def main():
    menu()


if __name__ == '__main__':
    main()

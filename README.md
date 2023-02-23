# Interactive Photo Session page for my web-site
#### Video Demo:  <https://youtu.be/pnn0vRlyPwY>
#### Description:

Let me introduce myself: my name is Dima Sobolev, I'm 61 years old (maybe oldest Harvard CS-50 courses
student).

In my final project I used flask and python to modify Photo Session page of my web-site.
Before it was one loooooong page with the list of links various cities, that I visited in my life,
and that was very uncomfortabe for users to scroll down that list to find certain country and city.

In my project I created CS-50 SQL database (which was converted to PostgreSQL database) and then
published all my code in Heroku.

Now it looks much more friendly for visitors of my web-page and they can easily find desired city
just in two steps:

- choosing part of the world
- choosing country

The project contains following files:

- application.py - main program file
- Procfile - configuration files for Heroku
- requirements.txt - configuration files for Heroku
- readme.md - file you are reading now
- fotki.db - database file
- /static subfolder - some page pictures ans styles fiole styles.css
- /templates subfolder:
   - layout.html, layoute.html, layoutec.html - flask html-pages layouts

    English language city looking pages chain:
   - phe_rez.html - main page, form to choose part of the world
   - phe_filtered.html - next page, to choose country
   - phe_final.html - final page - shows the city list from chosen country

    Russian language pages chain:
   - ph_rez.html - main page, form to choose part of the world
   - ph_filtered.html - next page, to choose country
   - ph_final.html - final page - shows the city list from chosen country

   - izm.html - special page to add/delete cities to/from database
   
# Issues I had to publish my project on Heroku.

I got difficulties to publish my final project on Heroku, I tried to use Linux, Windows,
but without success.

Finally I look again to CS50 docs page and found there detailed instruction how to do that using
CS-50 IDE. The manual was very detailed and all project files were successfully submitted to Heroku.
But when I tried to run my application, I have error again. The reason was that my CS-50 SQL database 
calls using different syntax comparing to PostgreSQL database, which is supported by Heroku. 
Luckily I could have control my PostgreSQL database and was able to play with it.

It worth to me one almost sleepless night,but I found the reason:
When calling PostgreSQL database in python, all column names should be double quotes, 
and string values - single quotes. After I made appropriate changes in my application.py file,
the page started to work as it should be !

Seems that should be added to Heroku CS-50 docs.

#Additional possibilities
Also using such a database allows me very easy add new city to database and delete city from database.
Please enjoy my project and welcome to my updated site!

Dima-
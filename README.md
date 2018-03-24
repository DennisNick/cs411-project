# cs411-project

This is the github repository for CS411. 

The goal of our project will be to provide any user with the experience of quick access to big news all across the United States. 

* A user will be presented with a large, user-friendly map of the United States that will have pins located upon it with information from prominent news articles

* A user will a personal page where they can store their own collections of favorited articles, along with a 5-star tier system for these articles. 

* A user may also be able to share their collected articles with other users

[1. Running the Server](#1-run-server)<br/>
[2. Migrating](#2-migrating)<br/>

# 1. Running the Server
Running the server is extremely easy, just locate the directory where the manage.py is located and type in the command: `python3 manage.py runserver`

The server has a default port (for the time being) set at 127.0.0.1:3000

# 2. Migrating
Wherever the need may arise to migrate, the manage.py will also take care of this. The simplest way is simply to write `python3 manage.py makemigrations` and then `python3 manage.py migrate`.

Migrations for the applications are located in their migrations folder. 



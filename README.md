# CSCL API

Restful API for the cscl client application

## Stacks

- <b>Python(v3)</b>: Programming Language
- <b>Flask</b>: Micro Web Framework
- <b>MongoDB</b>: Database
- <b>MongoEngine</b>: Object Document Mapper

# Installation

A virtual environemnet has been configure with vagrant

1. Download <a href="https://git-scm.com/downloads" target="_blank">Git</a>, <a href="https://www.virtualbox.org/wiki/Downloads" target="_blank">VirtualBox</a> and <a href="https://www.vagrantup.com/downloads.html" target="_blank">Vagrant</a>
2. Launch terminal and run the following commands

```
- git clone https://github.com/2020HackDiversity-Team12/cscl-api.git
- cd cscl-api
```

# How to use

1- Bring up the vagrant environment then login via ssh

```
- vagrant up
- vagrant ssh
```

2- Navigate to the hackdiv-team12 directory which is located at the root

```
- cd /hackdiv-team12
```

3- Execute the main.py file

```
python3 main.py
```

## Endpoints

| Route         | Method | Params                | Body                                            | Description          | Payload            |
| ------------- | ------ | --------------------- | ----------------------------------------------- | -------------------- | ------------------ |
| /books        | GET    | none                  | none                                            | retreive all books   | books, next, total |
| /books        | POST   | none                  | {title, author, isbn, copies, publication_year} | add new book         | bookID             |
| /books/bookID | GET    | act(borrow\|handback) | none                                            | retreive target book | book, action       |
| /books/bookID | PUT    | none                  | {title, author, isbn, copies, publication_year} | update target book   | bookID             |
| /books/bookID | DELETE | none                  | {title, author, isbn, copies, publication_year} | delete target book   | bookID             |
| /search       | GET    | q                     | none                                            | search in database   | books, next, total |

## Data Object Model

```
Book
{
  isbn:str
  title:str
  author:str
  publisher:str
  image_url_s:url
  image_url_m:url
  image_url_l:url
  copies:int
  available:int
  publication_year:str
}
```

## Todo

- [ ] setup base project structure
- [ ] setup MongoDB server in cloud
- [ ] create book endpoints
- [ ] create search endpoint
- [ ] CRUD book
- [ ] deploy application

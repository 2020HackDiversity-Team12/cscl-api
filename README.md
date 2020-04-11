# CSCL API

Restful API for the cscl client application

# Stacks

- <b>VirtualBox</b>: Virtualization Platform
- <b>Vagrant</b>: Virtual Machine Management
- <b>Python(v3)</b>: Programming Language
- <b>Pipenv</b>: Dependency managers
- <b>Flask</b>: Micro Web Framework
- <b>MongoDB</b>: Nosql Database
- <b>MongoEngine</b>: Object Document Mapper

# Installation

A virtual development environment has been configured with vagrant

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

3- Create active environemnt

```
pipenv shell
```

4- Install packages dependencies

```
pipenv install
```

5- Run server

```
flask run -h 0.0.0.0
```

# Endpoints

| Route       | Method | Params                | Body                                            | Description                          | Payload     |
| ----------- | ------ | --------------------- | ----------------------------------------------- | ------------------------------------ | ----------- |
| /search     | GET    | q                     | none                                            | Search in database                   | books, next |
| /books      | GET    | none                  | none                                            | Retrieve lisiting of available books | books, next |
| /books      | POST   | none                  | {title, author, isbn, copies, publication_year} | Create a new book                    | bookID      |
| /books/isbn | GET    | act(borrow\|handback) | none                                            | Retrieve a single book by it's ISBN  | book        |
| /books/isbn | PUT    | none                  | {title, author, isbn, copies, publication_year} | Update book by it's ISBN             | bookID      |
| /books/isbn | DELETE | none                  | {title, author, isbn, copies, publication_year} | Delete a book                        | bookID      |

## Resource

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

- [x] add readme file
- [x] setup project skeleton
- [x] setup app configuration
- [x] setup MongoDB server in cloud
- [ ] create endpoints
- [x] create model
- [ ] deploy application

#### Useful Links

- [Restful API](https://mlsdev.com/blog/81-a-beginner-s-tutorial-for-understanding-restful-api)
- [Git](https://rogerdudler.github.io/git-guide/)

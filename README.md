# ItemCatalogApplication
This Application Provides the Catalog of Movies. You Can select a Particular genre of the Movie and It will show you all relevant Movies available. Plus , The application have login functionality. A particalur user can create, delete or update a movie. For Authorization we have used Google account.

### Prerequisites
* [Git Bash terminal](https://git-scm.com/downloads))
* [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)


### Running Project
Download the VM configuration from below link
* [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

* Unzip the **VM configuration** and you will find a **vagrant** folder
* Use the **Terminal** to get into the **vagrant** folder from **VM configuration**
* run the following command
```sh
$ vagrant up
```
* This will cause Vagrant to download the Linux operating system and install it.
* After it finished and after the shell prompt comes back, you can run this command
```sh
$ vagrant ssh
```
* And this will let you login to the Linux VM. (Please do not shut down the terminal after the login)

### Setting up the enviroment
* Clone the git repo from https://github.com/mohitsharma1750/ItemCatalogApplication.git
and place it inside the vagrant folder. So that it can be accessed inside VM.
* use the following line to get into the vagrant VM folder
```sh
$ cd /vagrant
```
* Use the command line to get in to the folder you just downloaded
* Then you can run this command
```sh
$ python reference_data.py
```
* After it added items succesfully, you can run the following command
```sh
$ python application.py
```
* After finish running project.py you can use your favorite browser to visit [this link](http://localhost:8000/)

### How to use
* You can browse through the website to find out the different categories of movies.
* A user can Log in and add a movie item.
* A user can edit/delete movies added by him



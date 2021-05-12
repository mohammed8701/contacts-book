# contacts-book

## Getting Started

1. Clone the repo<br/>

Under the repo name click *clone or download*<br/>
Click on *use HTTPs*, copy the clone URL of the repo<br/>
In the terminal go on the working directory where you want to clone the project<br/>
Use the `git clone` command and paste the clone URL then press enter :

```shell
$ git clone https://github.com/your-username/your-repositary.git
```

2. On your local machine go inside of the *Contacts-Book* directory :

```shell
$ cd contacts-book
```

### Create Docker Container for MySQL DB

1. Ensure you have Docker Desktop installed and running (you can check with `docker -v`).
2. Run the following command **inside** the directory in a terminal. This will create both the client and server for us which is running on localhost.

```
$ docker-compose up -d
```

​	You should get the following output:

```sh
Creating mysql_container   ... done
Creating adminer_container ... done
```

3. Navigate to the following URL to ensure that you can see the `Adminer` interface:

http://localhost:8080/

4. Fill in the username (`root`) and password field (`password`), leave the database field blank.



### Creating And Activating The Virtual Environment
Creating the virtual environment

On macOS and Linux:

```shell
python3 -m venv .venv
```
On Windows:
```shell
py -m venv .venv
```
Activate the virtual environment
Windows: 
```shell
$ source venv/Scripts/activate
```
MacOS/Unix: 
```shell
$ source venv/bin/activate
```

## Prerequisites

The requirements to run the project are:<br/>
cffi==1.14.4<br/>
cryptography==3.2.1<br/>
pycparser==2.20<br/>
PyMySQL==0.10.1<br/>
python-dotenv==0.15.0<br/>
six==1.15.0<br/>
cffi==1.14.4<br/>
pytest==6.2.4<br/>

To install these requirements, run in the terminal:

```shell
$ pip install -r requirements.txt
```

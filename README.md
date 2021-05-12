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

2. On your local machine go inside of the *pop-up-cafe* directory :

```shell
$ cd generation-mini-project
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

5. Select `SQL Command` on the left.
6. We'll create our own database with:

```
CREATE DATABASE popupcafe;
```

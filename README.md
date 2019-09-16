# QA_APP

## Steps:
0) Clone the repo
1) Run `docker build . -t qa_app:latest`
2) Run `docker volume create db`
3) Run `docker run --name=qa_db -d -v db:/var/lib/postgresql/data postgres:11.5-alpine`
4) `apt get` or `brew install` a postgres client, `psql` is needed
5) Run `cd db && ./init.sh` to setup the database (only needed to run once)
6) Run `docker run --name=qa_api -d --link=pgdb:database -p 8080:8080 qa_app:latest`

#### note:
* the admin user and pass are found in the `db/admin_user.sql` file, needed to login (can be changed as necessary) as this is the only user that can create other users.

### Finally:
Run through the endpoints in the `Python Developer Exercise` using curl or Insomnia or httpie or ...

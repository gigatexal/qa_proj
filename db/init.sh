#!/bin/bash

export ADMIN_EMAIL="admin@qa_user.com" # change me
export ADMIN_PHASH="mysuperdupersecretpassword1234" # change me

psql -U postgres -d postgres -f init.sql
psql -U postgres -d qa_db -f base.sql
psql -U postgres -d qa_db -f admin_user.sql
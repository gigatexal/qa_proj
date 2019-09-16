#!/bin/bash

psql -U postgres -d postgres -h localhost -f init.sql
psql -U postgres -d qa_db -h localhost -f base.sql
psql -U postgres -d qa_db -h localhost < admin_user.sql 
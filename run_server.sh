#!/bin/sh
export JWT_SECRET_KEY="!my@#$SUPERROUGHTOUGH!!!KEY" # change me obviously
export ADMIN_DEFAULT_EMAIL="admin@admin.com" # change me obviously
export ADMIN_DEFAULT_PHASH="root1234" # change me obviously
export JWT_EXPIRY=3
export DB_URI="postgresql://postgres@localhost:5432/postgres"

python3 server.py

INSERT INTO "users" (email, phash, role_id)
SELECT '$ADMIN_EMAIL', '$ADMIN_PHASH', r.id
FROM "role" r
WHERE r.name = 'admin';

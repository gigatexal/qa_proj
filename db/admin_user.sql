INSERT INTO "users" (email, phash, role_id)
SELECT 'admin', 'a.ridiculous.PASSWORD', r.id
FROM "roles" r
WHERE r.name = 'admin';

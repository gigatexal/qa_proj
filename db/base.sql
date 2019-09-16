/****** BEGIN USER TABLES ****/
CREATE TABLE "roles" (
    id SERIAL PRIMARY KEY, 
    name VARCHAR(10) NOT NULL,
    abilities JSON NOT NULL
);

INSERT INTO "roles" (
    name,
    abilities
)
VALUES 
(
    'admin',
       '{
           "create_project": "True", 
           "create_test": "True",
           "view_test_results": "True", 
           "run_test": "True",
           "can_create_users":"True"
        }'
),
(
    'manager',
       '{
           "create_project": "True", 
           "create_test": "False", 
           "view_test_results": "False", 
           "run_test": "False",
           "can_create_users":"False"
        }'
),
(
    'qa_manager', 
       '{
           "create_project": "False", 
           "create_test": "True", 
           "view_test_results": "True", 
           "run_test": "False",
           "can_create_users": "False"
        }'
),
(
    'user', 
       '{
           "create_project": "False", 
           "create_test": "False", 
           "view_test_results": "False", 
           "run_test": "True",
           "can_create_users": "False"
        }'
);
-- There can only be one admin role and one manager role and one ....
CREATE UNIQUE INDEX uq_name_roles ON "roles" (name);

CREATE TABLE "users" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    phash VARCHAR(128) NOT NULL, -- 128 should be long enough for a hash -- ex. hashlib.SHA512 only returns a 128 char long hash
    role_id INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP 
);

CREATE UNIQUE INDEX uq_email_users ON "users" (email);
CREATE INDEX ix_email_phash_role_id_users ON "users" (email, phash, role_id);

ALTER TABLE "users" ADD CONSTRAINT fk_users_role_id_id_roles FOREIGN KEY (role_id) REFERENCES "roles" (id); -- NO ON DELETE CASCADE HERE -- Handle deletes on the "roles" table carefully
/****** END USER TABLES ****/

/****** BEGIN PROJECT TABLES ****/
CREATE TABLE "projects" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX uq_name_projects ON "projects" (name);
CREATE INDEX ix_created_at_name_projects ON "projects" (created_at, name);
/****** END PROJECT TABLES ****/

/****** BEGIN TEST TABLES ****/
CREATE TABLE "tests" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    project_id INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE uq_tests_name ON "tests" (name);
CREATE INDEX ix_tests_name_project_id ON "tests" (name, project_id);
CREATE INDEX ix_tests_project_id_id ON "tests" (project_id, id);

ALTER TABLE "tests" ADD CONSTRAINT fk_tests_project_id_id_projects FOREIGN KEY (project_id) REFERENCES "projects" (id) ON DELETE CASCADE;

CREATE TABLE "test_results" (
    id SERIAL PRIMARY KEY,
    test_id INTEGER NOT NULL,
    executed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    result VARCHAR(9) NOT NULL DEFAULT 'Runnable'
);

CREATE INDEX ix_test_results_test_id_result ON "test_results" (test_id, result);

-- Keep the test results even if a test might get deleted -- keep it a manual process
ALTER TABLE "test_results" ADD CONSTRAINT fk_test_results_test_id_id_tests FOREIGN KEY (test_id) REFERENCES "tests" (id);
/****** END TEST TABLES ****/

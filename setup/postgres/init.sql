-- Create DB Schemas
CREATE SCHEMA redditor;
CREATE SCHEMA airflow;
CREATE SCHEMA superset;

-- Create Users
CREATE USER airflow_user WITH PASSWORD 'airflow_password';
CREATE USER superset_user WITH PASSWORD 'superset_password';

-- Grant users all privileges
GRANT ALL PRIVILEGES ON SCHEMA airflow TO airflow_user;
GRANT ALL PRIVILEGES ON SCHEMA superset TO superset_user;

-- Point roles to correct schemas
ALTER ROLE airflow_user SET search_path TO airflow;
ALTER ROLE superset_user SET search_path TO superset;

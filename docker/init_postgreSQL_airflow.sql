DO $$
BEGIN
   IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'airflow_db') THEN
      CREATE DATABASE airflow_db;
        CREATE USER airflow WITH PASSWORD 'airflow';
        GRANT ALL PRIVILEGES ON DATABASE airflow_db TO airflow;
   END IF;
END $$;




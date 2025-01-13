-- Create data warehouse schema (dw_schema)

DROP SCHEMA IF EXISTS dw_schema;

CREATE SCHEMA IF NOT EXISTS dw_schema
    AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA dw_schema
    IS 'chinook data warehouse schema (snowflake schema)';

GRANT ALL ON SCHEMA dw_schema TO pg_database_owner;


CREATE TABLE IF NOT EXISTS dw_schema.album_details
(
    album_id INT NOT NULL,
    title VARCHAR(160) NOT NULL,
    artist_name VARCHAR(120),
    CONSTRAINT album_details_pkey PRIMARY KEY  (album_id)
);

CREATE TABLE IF NOT EXISTS dw_schema.employee
(
    employee_id INT NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    title VARCHAR(30),
    reports_to INT,
    birth_date TIMESTAMP,
    hire_date TIMESTAMP,
    address VARCHAR(70),
    city VARCHAR(40),
    state VARCHAR(40),
    country VARCHAR(40),
    postal_code VARCHAR(10),
    phone VARCHAR(24),
    fax VARCHAR(24),
    email VARCHAR(60),
    CONSTRAINT employee_pkey PRIMARY KEY  (employee_id)
);

CREATE TABLE IF NOT EXISTS dw_schema.customer
(
    customer_id INT NOT NULL,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    state VARCHAR(40),
    country VARCHAR(40),
    phone VARCHAR(24),
    fax VARCHAR(24),
    email VARCHAR(60) NOT NULL,
    support_rep_id INT,
    CONSTRAINT customer_pkey PRIMARY KEY  (customer_id)
);

CREATE TABLE IF NOT EXISTS dw_schema.track
(
    track_id INT NOT NULL,
    name VARCHAR(200) NOT NULL,
    album_id INT,
    media_type_name VARCHAR(120),
    genre_name VARCHAR(120),
    composer VARCHAR(220),
    milliseconds INT NOT NULL,
    bytes INT,
    unit_price NUMERIC(10,2) NOT NULL,
    CONSTRAINT track_pkey PRIMARY KEY  (track_id)
);

CREATE TABLE IF NOT EXISTS dw_schema.playlist_track
(
    playlist_id INT NOT NULL,
    playlist_name VARCHAR(120),
    track_id INT NOT NULL,
    CONSTRAINT playlist_track_pkey PRIMARY KEY  (playlist_id, track_id)
);

CREATE TABLE IF NOT EXISTS dw_schema.invoice_details
(
    invoice_line_id INT NOT NULL,
    track_id INT NOT NULL,
    invoice_date TIMESTAMP NOT NULL,
    customer_id INT NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    quantity INT NOT NULL,
    billing_address VARCHAR(70),
    billing_city VARCHAR(40),
    billing_state VARCHAR(40),
    billing_country VARCHAR(40),
    billing_postal_code VARCHAR(10),
    total NUMERIC(10,2) NOT NULL,
    CONSTRAINT invoice_details_pkey PRIMARY KEY  (invoice_line_id)
);



-- Create Foreign Keys
ALTER TABLE IF EXISTS dw_schema.employee ADD CONSTRAINT employee_reports_to_fkey
    FOREIGN KEY (reports_to) REFERENCES dw_schema.employee (employee_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IF NOT EXISTS employee_reports_to_idx ON dw_schema.employee (reports_to);

ALTER TABLE IF EXISTS dw_schema.customer ADD CONSTRAINT customer_support_rep_id_fkey
    FOREIGN KEY (support_rep_id) REFERENCES dw_schema.employee (employee_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IF NOT EXISTS customer_support_rep_id_idx ON dw_schema.customer (support_rep_id);

ALTER TABLE IF EXISTS dw_schema.invoice_details ADD CONSTRAINT invoice_customer_id_fkey
    FOREIGN KEY (customer_id) REFERENCES dw_schema.customer (customer_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IF NOT EXISTS invoice_customer_id_idx ON dw_schema.invoice_details (customer_id);

ALTER TABLE IF EXISTS dw_schema.invoice_details ADD CONSTRAINT invoice_details_track_id_fkey
    FOREIGN KEY (track_id) REFERENCES dw_schema.track (track_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IF NOT EXISTS invoice_details_track_id_idx ON dw_schema.invoice_details (track_id);

ALTER TABLE IF EXISTS dw_schema.playlist_track ADD CONSTRAINT playlist_track_track_id_fkey
    FOREIGN KEY (track_id) REFERENCES dw_schema.track (track_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IF NOT EXISTS playlist_track_track_id_idx ON dw_schema.playlist_track (track_id);

ALTER TABLE IF EXISTS dw_schema.track ADD CONSTRAINT track_album_id_fkey
    FOREIGN KEY (album_id) REFERENCES dw_schema.album_details (album_id) ON DELETE NO ACTION ON UPDATE NO ACTION;

CREATE INDEX IF NOT EXISTS track_album_id_idx ON dw_schema.track (album_id);

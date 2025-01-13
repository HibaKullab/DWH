from ingestion import PostgreSQLConnection


if __name__ == "__main__":
    # Database configuration
    db_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '123', # User postgres password
        'host': 'localhost',
        'port': 5432
    }

    db_connection = PostgreSQLConnection(**db_config)
    db_connection.connect()

    # Path to the SQL file
    sql_schema_file = '../sql/dw_schema.sql'

    # Execute the SQL file that creates data warehouse schema
    db_connection.create_a_new_db("digital_store_DWH")
    db_connection.execute_sql_file(sql_schema_file)

    # Populate tables in dw_schema
    db_connection.connect()
    db_connection.execute_load_query("""
        INSERT INTO dw_schema.album_details (album_id, title, artist_name)
        SELECT a.album_id, a.title, ar.name
        FROM public.album a
        JOIN public.artist ar ON a.artist_id = ar.artist_id;
    """)

    db_connection.execute_load_query("""
        INSERT INTO dw_schema.employee (employee_id, last_name, first_name,
        title, reports_to, birth_date, hire_date, address, city, state,
        country, postal_code, phone, fax, email)
        SELECT e.employee_id, e.last_name, e.first_name,
        e.title, e.reports_to, e.birth_date, e.hire_date, e.address, e.city, e.state,
        e.country, e.postal_code, e.phone, e.fax, e.email
        FROM public.employee e;
    """)

    db_connection.execute_load_query("""
        INSERT INTO dw_schema.customer (customer_id, first_name, last_name, state,
        country, phone, fax, email, support_rep_id)
        SELECT c.customer_id, c.first_name, c.last_name, c.state,
        c.country, c.phone, c.fax, c.email, c.support_rep_id
        FROM public.customer c;
    """)

    db_connection.execute_load_query("""
        INSERT INTO dw_schema.track (track_id, name, album_id, media_type_name,
        genre_name, composer, milliseconds, bytes, unit_price)
        SELECT t.track_id, t.name, a.album_id, mt.name,
        g.name, t.composer, t.milliseconds, t.bytes, t.unit_price
        FROM public.track t
        JOIN public.album a ON t.album_id = a.album_id
        JOIN public.media_type mt ON t.media_type_id = mt.media_type_id
        JOIN public.genre g ON t.genre_id = g.genre_id;
    """)

    db_connection.execute_load_query("""
        INSERT INTO dw_schema.playlist_track (playlist_id, playlist_name, track_id)
        SELECT p.playlist_id, p.name, t.track_id
        FROM public.playlist_track pt
        JOIN public.track t ON pt.track_id = t.track_id
        JOIN public.playlist p ON pt.playlist_id = p.playlist_id;
    """)

    db_connection.execute_load_query("""
        INSERT INTO dw_schema.invoice_details (invoice_line_id, track_id, invoice_date,
        customer_id, unit_price, quantity, billing_address, billing_city,
        billing_state, billing_country, billing_postal_code, total)
        SELECT il.invoice_line_id, t.track_id, i.invoice_date,
        c.customer_id, il.unit_price, il.quantity, i.billing_address, i.billing_city,
        i.billing_state, i.billing_country, i.billing_postal_code, il.unit_price * il.quantity AS total
        FROM public.invoice_line il
        JOIN public.invoice i ON il.invoice_id = i.invoice_id
        JOIN public.track t ON il.track_id = t.track_id
        JOIN public.customer c ON i.customer_id = c.customer_id;
    """)

import psycopg2

def isTableExists(tableSchema, tableName):

    conn_string = "host='localhost' port='5432' dbname='postgres' user='postgres' password='admin2'"

    print ("Connecting to database\n    ->%s" % (conn_string))

    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    print ("Connected!\n")

    cursor.execute("SELECT EXISTS (SELECT 1   FROM   information_schema.tables   WHERE  table_schema = '%s'   AND    table_name = '%s');"%(tableSchema, tableName))

    result = cursor.fetchone()

    return result[0]
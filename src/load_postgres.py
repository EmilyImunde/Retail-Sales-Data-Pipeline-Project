import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="retail_project",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )
def load_sales_report(records):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM sales_report;")

    insert_query = """
        INSERT INTO sales_report (
            order_id,
            order_date,
            customer_id,
            customer_name,
            city,
            product_id,
            product_name,
            category,
            quantity,
            price,
            total_amount
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    for record in records:
        cursor.execute(
            insert_query,
            (
                record["order_id"],
                record["order_date"],
                record["customer_id"],
                record["customer_name"],
                record["city"],
                record["product_id"],
                record["product_name"],
                record["category"],
                record["quantity"],
                record["price"],
                record["total_amount"]
            )
        )

    connection.commit()
    cursor.close()
    connection.close()
from db.db_config import config
from datetime import datetime
import mysql.connector
import uuid

def insert_disasters(report):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    query = """
    INSERT INTO DisasterReports
    (id, source, raw_text, disaster_type, severity, location_text, lat, lon, summary, timestamp)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    data = (
        str(uuid.uuid4()),
        report["source"],
        report["raw_text"],
        report["disaster_type"],
        report["severity"],
        report["location_text"],
        report["lat"],
        report["lon"],
        report["summary"],
        datetime.now()
    )
    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()

def get_recent_disasters():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM DisasterReports ORDER BY timestamp DESC LIMIT 10")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
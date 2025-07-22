from db.db_utils import insert_disasters, get_recent_disasters

mock = {
    "source": "Twitter",
    "raw_text": "Massive flooding reported in Hobart suburbs.",
    "disaster_type": "Flood",
    "severity": "High",
    "location_text": "Hobart",
    "lat": -42.8821,
    "lon": 147.3272,
    "summary": "Major flooding in Hobart suburbs."
}

insert_disasters(mock)
print(get_recent_disasters())
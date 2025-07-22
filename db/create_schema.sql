CREATE TABLE DisasterReports (
    id CHAR(36) PRIMARY KEY,
    source VARCHAR(50),
    raw_text TEXT,
    disaster_type VARCHAR(50),
    severity VARCHAR(10),
    location_text VARCHAR(255),
    lat FLOAT,
    lon FLOAT,
    summary TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
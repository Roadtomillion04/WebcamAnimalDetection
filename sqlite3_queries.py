import sqlite3 # sqlite with db browser ide

def create_table(): # get code from db browser creating table visually
    connection = sqlite3.connect(database= "database.db")
    connection.execute(
        """
    CREATE TABLE "AnimalData" (
        "sid"	INTEGER,
        "animal_name"	TEXT,
        "time_of_incident"	TEXT,
        "confidence"	REAL,
        "image"	TEXT,
        PRIMARY KEY("sid" AUTOINCREMENT)
);
        """
)
    connection.commit()
    connection.close()

def insert_record_values(animal_name: str, time_of_incident: str, confidence: float, image):
    connection = sqlite3.connect(database= "database.db")
    connection.execute(
        f"""
        INSERT INTO "AnimalData" ("animal_name", "time_of_incident", "confidence", "image")
        VALUES ("{animal_name}", "{time_of_incident}", "{confidence}", "{image}" )
        """
    )
    connection.commit()
    connection.close()
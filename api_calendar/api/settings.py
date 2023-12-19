from sqlalchemy import URL
import os

db_url = URL.create(
    "postgresql",
    username=os.environ["DB_USERNAME"],
    password=os.environ["DB_PASSWORD"],
    host=os.environ["DB_HOST"],
    database=os.environ["DB_NAME"]
)
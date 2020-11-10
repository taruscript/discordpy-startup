import dataset
import os

db_url = os.environ.get('DATABASE_URL')

db = dataset.connect(db_url)
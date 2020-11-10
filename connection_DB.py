import dataset
import os

# DBのURLを設定した環境変数を取得
db_url = os.environ.get('DATABASE_URL')

#O/RマッパーがDBに設定する
db = dataset.connect(db_url)

table = db["mtg"]
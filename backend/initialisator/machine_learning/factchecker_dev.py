from pathlib import Path
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from initialisator.models import Claims
from ..database import get_db, SessionLocal



BASE_DIR = Path(__file__).resolve().parent
test_data = BASE_DIR / "1" / "test.tsv"


# Data collection
#import kagglehub
#path = kagglehub.dataset_download("doanquanvietnamca/liar-dataset")

fact_dict = {}

# Create columns
cols = [
    "id", "label", "statement", "subjects", "speaker", "job", "state_info", "party",
    "barely_true", "half_true", "mostly_true", "pants_on_fire", "context"
        ]

# Load data
data = pd.read_csv(test_data, sep="\t", names=cols)



def clean_upload_data(data):
    
    data = data.drop_duplicates()

    db = SessionLocal()


    try:
        for row in data.itertuples(index=False):

            # Skip row if any field fails validation
            if not all(check_empty(value, i) for i, value in enumerate(row)):
                continue


            claim = Claims(
                fact_string=row[1],
                fact_status=row[2],
                subjects=row[3],
                speaker=row[4],
                job=row[5],
                context=row[12]
            )

            db.add(claim)

        db.commit()

    except Exception as e:
        db.rollback()
        print(e)

    finally:
        db.close()



def check_empty(element, index):
    if element == '' or pd.isna(element):
        return False

    if index < 0 or index > 13:
        return False

    return element



clean_upload_data(data)
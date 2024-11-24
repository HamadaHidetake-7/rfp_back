from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# FastAPI アプリケーション
app = FastAPI()

# データベース接続情報
DATABASE_URL = "mysql+pymysql://root:F4XyhpicGw6P@localhost/rfp_test"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# テーブルモデル
class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(Text, nullable=False)
    option1 = Column(String(255))
    option2 = Column(String(255))
    option3 = Column(String(255))
    option4 = Column(String(255))
    correct_option = Column(Integer)
    explanation = Column(Text)
    category = Column(String(50))

# データベース接続関数
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ルートエンドポイント
@app.get("/")
def root():
    return {"message": "FastAPI is running!"}

# 質問データ取得エンドポイント
@app.get("/questions_db")
def read_questions(db=Depends(get_db)):
    questions = db.query(Question).all()
    return [
        {
            "id": q.id,
            "question_text": q.question_text,
            "options": [q.option1, q.option2, q.option3, q.option4],
            "correct_option": q.correct_option,
            "explanation": q.explanation,
            "category": q.category,
        }
        for q in questions
    ]

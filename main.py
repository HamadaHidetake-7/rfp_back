from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FastAPI アプリケーションのインスタンスを作成
app = FastAPI()

# CORS 設定を追加
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのオリジンを許可（必要に応じて制限可能）
    allow_credentials=True,
    allow_methods=["*"],  # すべてのHTTPメソッドを許可
    allow_headers=["*"],  # すべてのHTTPヘッダーを許可
)

# ルートエンドポイント ("/")
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

# 質問データを返すエンドポイント ("/questions_db")
@app.get("/questions_db")
def get_questions():
    return [
        {
            "id": 1,
            "question_text": "What is 2 + 2?",
            "options": ["3", "4", "5", "6"],
            "correct_option": 1,
            "explanation": "The correct answer is 4.",
            "category": "Tech",
        },
        {
            "id": 2,
            "question_text": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_option": 2,
            "explanation": "The correct answer is Paris.",
            "category": "Biz",
        },
    ]

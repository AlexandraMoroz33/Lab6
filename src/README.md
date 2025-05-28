## Requirements

- Python 3.8+
- MySQL (5.7+ or 8+)
- pip (Python package manager)

## Installation

1. Clone the repository:
   git clone https://github.com/AlexandraMoroz33/Lab6.git
   cd Lab6

2. Install dependencies
   pip install -r requirements.txt
   pip install fastapi uvicorn sqlalchemy pymysql

3. Configure the database
   Open database.py and update your MySQL connection string:
   DATABASE_URL = "mysql+pymysql://root@localhost:3306/ji9star"

   Make sure the database ji9star exists. If not, create it using MySQL:
   CREATE DATABASE ji9star;

4. Run the API server
   uvicorn main:app --reload
   Once the server is running, you can access:
   http://127.0.0.1:8000/docs
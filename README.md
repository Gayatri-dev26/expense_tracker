#  Expense Tracker API

A RESTful API built with **FastAPI** and **PostgreSQL** for managing personal income and expenses. Supports full CRUD operations, transaction filtering, and a financial summary endpoint.

---

##  Features

- Manage **income & expense categories**
- Track **transactions** with title, amount, date, and notes
- Filter transactions by **type, category, and date range**
- Get a **financial summary** (total income, expenses, and balance)
- Input **validation** with proper error responses (HTTP 422)
- API tested using **Postman**

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| FastAPI | Web framework |
| PostgreSQL | Database |
| SQLAlchemy | ORM |
| Pydantic | Data validation |
| Uvicorn | ASGI server |
| python-dotenv | Environment variables |
| Postman | API Testing |

---

##  Project Structure

```
expense_tracker/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── routers/
│   ├── categories.py
│   ├── transactions.py
│   └── summary.py
└── requirements.txt
```

---

##  Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Gayatri-dev26/expense_tracker.git
cd expense_tracker
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        
venv\Scripts\activate         
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory:
```
DATABASE_URL=postgresql://username:password@localhost/expense_tracker
```

### 5. Create PostgreSQL Database
Open your PostgreSQL shell (psql) and run:
```sql
CREATE DATABASE expense_tracker;
```

### 6. Run the server
```bash
uvicorn main:app --reload
```

### 7. Test APIs using Postman
- Open **Postman**
- Set base URL to: `http://localhost:8000`
- Start hitting the endpoints listed below!

---

##  API Endpoints

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/categories/` | Create a new category |
| GET | `/categories/` | List all categories |
| GET | `/categories/{id}` | Get a single category |
| PUT | `/categories/{id}` | Update a category |
| DELETE | `/categories/{id}` | Delete a category |

### Transactions
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/transactions/` | Add a new transaction |
| GET | `/transactions/` | List all (with filters) |
| GET | `/transactions/{id}` | Get a single transaction |
| PUT | `/transactions/{id}` | Update a transaction |
| DELETE | `/transactions/{id}` | Delete a transaction |

### Summary
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/summary/` | Get income, expense & balance totals |

---

##  Filtering Transactions

```
GET /transactions/?type=expense&start_date=2024-01-01&end_date=2024-01-31
```

Supported query parameters:
- `type` – `income` or `expense`
- `category_id` – filter by category
- `start_date` – from date (YYYY-MM-DD)
- `end_date` – to date (YYYY-MM-DD)

---

##  API Testing with Postman

All endpoints were tested using **Postman**. Example request to create a category:

- **Method:** POST
- **URL:** `http://localhost:8000/categories/`
- **Body (JSON):**
```json
{
  "name": "Food",
  "type": "expense"
}
```

Example request to add a transaction:

- **Method:** POST
- **URL:** `http://localhost:8000/transactions/`
- **Body (JSON):**
```json
{
  "title": "Grocery shopping",
  "amount": 500.00,
  "type": "expense",
  "category_id": 1,
  "date": "2024-01-15",
  "note": "Monthly groceries"
}
```

---

##  Validation Rules

- `amount` must be greater than 0
- `type` must be `income` or `expense`
- `category_id` must refer to an existing category
- `date` cannot be in the future
- `title` must not be empty

---

##  License

This project is open source and available under the [MIT License](LICENSE).

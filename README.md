🚀 Getting Started – Banking App
🐳 Prerequisites
Docker installed on your machine

⚙️ Setup Instructions
Create Docker volume for PostgreSQL:

docker volume create postgres_db

Build the Docker containers:
docker compose build

Start the services in detached mode:
docker compose up -d

💻 Running the Frontend
The frontend is hosted at:
http://localhost:5000

To run the app manually:

python app.py runserver

🛠️ Database Migrations
Downgrade database by a specific number of revisions:

alembic downgrade -x <number_of_revisions>

Upgrade database to the latest (head) revision:
alembic upgrade head

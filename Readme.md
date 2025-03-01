Backend API for Spreadsheet Integration
This repository contains the backend API for integrating with Google Spreadsheets. The API is built using Python and requires Google OAuth credentials to authenticate and interact with Google Sheets.

📌 Prerequisites
Ensure you have the following installed:

Python (>=3.8 recommended)
pip (Python package manager)
Google OAuth Credentials (JSON file for API authentication)
🚀 Setup Instructions
Follow these steps to set up and run the project:

1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Kamaleshkulal/backend-api-spreadsheet.git
cd backend-api-spreadsheet
2️⃣ Create and Activate a Virtual Environment
bash
Copy
Edit
python -m venv venv
# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3️⃣ Install Required Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Setup Google OAuth Credentials
Place your Google OAuth JSON file inside the api/ folder.
Rename it to credentials.json.
5️⃣ Run the Server
bash
Copy
Edit
python manage.py runserver
🎯 Usage
Once the server is running, you can access the API endpoints. Ensure that you have properly configured your Google Sheets API to allow read/write access.

🛠 Environment Variables
Create a .env file in the project root and add necessary environment variables if required.


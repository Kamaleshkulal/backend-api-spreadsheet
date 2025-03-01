Backend API for Spreadsheet Integration
This repository contains the backend API for integrating with Google Spreadsheets. The API is built using Python and requires Google OAuth credentials to authenticate and interact with Google Sheets.

📌 Prerequisites
Ensure you have the following installed:

Python (>=3.8 recommended)
pip (Python package manager)
Google OAuth Credentials (JSON file for API authentication)
🚀 Setup Instructions
Follow these steps to set up and run the project:

# 1 Clone the Repository
```sh
git clone https://github.com/Kamaleshkulal/backend-api-spreadsheet.git
cd backend-api-spreadsheet
```

# 2 Create and Activate a Virtual Environment

python -m venv venv
# Activate virtual environment
# On Windows:
```sh
venv\Scripts\activate
```
# On macOS/Linux:
```sh
source venv/bin/activate
```
# 3 Install Required Dependencies

```sh
pip install -r requirements.txt
```
#  Setup Google OAuth Credentials
Place your Google OAuth JSON file inside the api/ folder.
Rename it to credentials.json.

# 6 Run the Server
bash
```sh
python manage.py runserver
```
# 🎯 Usage
Once the server is running, you can access the API endpoints. Ensure that you have properly configured your Google Sheets API to allow read/write access.

# 🛠 Environment Variables
Create a .env file in the project root and add necessary environment variables if required.


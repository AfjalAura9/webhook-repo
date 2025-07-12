# Webhook Repository

This project is a Flask-based web application that collects and stores GitHub webhook events in a MongoDB database. It listens for POST requests from GitHub, processes the event payload, and stores the resulting event data in a collection.

## Features

- Receive and process webhook events via HTTP POST requests.
- Store incoming events in a MongoDB collection.
- View stored events through a web interface.

## Project Structure

```bash
webhook-repo/
├── app.py
├── config.py
├── requirements.txt
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── utils/
│   └── formatter.py
└── .env
```

## Requirements

- Python 3.x
- Flask
- PyMongo
- dateutil
- python-dotenv


## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/AfjalAura9/webhook-repo.git
   cd webhook-repo
   ```
2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows
   # or
   source .venv/bin/activate      # On Unix or MacOS
   ```
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   
   *Create a .env file in the root directory and add your configuration settings, such as:*
   ```bash
   MONGODB_URI=your_mongodb_connection_string
   ```

5. **Run the Application**

   ```bash
   python app.py
   ```
*The application will start on http://localhost:5000.*

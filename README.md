# URL Shortener
A simple Django-based web application to generate short URLs from long URLs. It provides quick redirection and a user-friendly interface.

## Features
- Input long URLs to generate unique short URLs.
- Redirect using the short URLs.
- Responsive and visually appealing interface using Bootstrap.

## Getting Started
Follow these instructions to set up and run the project locally.

### Prerequisites
- Python 3.x installed
- pip (Python package installer)

### Installation
1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd url_shortener

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3. Install dependencies:
pip install -r requirements.txt


4. Run the server:
python manage.py runserver


Usage
1. Open http://127.0.0.1:8000 in your browser.
2. Enter a long URL in the form and click "Shorten URL."
3. Copy and use the generated short URL for redirection.


Built With
Django - Backend framework

Bootstrap - Frontend framework

Future Improvements
Add expiration dates for URLs.

Track the number of visits per short URL.

License

This project is licensed under the MIT License - see the LICENSE file for details.

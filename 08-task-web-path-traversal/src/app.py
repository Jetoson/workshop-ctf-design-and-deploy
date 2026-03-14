#!/usr/bin/env python3
"""
Leaky Library - A digital book library with a path traversal vulnerability.

The /read endpoint takes a 'book' parameter and reads files from the /app/books/
directory, but doesn't sanitize the input — allowing ../../ traversal to read
arbitrary files on the system (including /flag).
"""

from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

BOOKS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'books')

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Leaky Library</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            background: #1a1a2e;
            color: #e0e0e0;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }
        h1 {
            color: #e6b800;
            text-align: center;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        .subtitle {
            text-align: center;
            color: #888;
            margin-bottom: 30px;
        }
        .book-list {
            background: #16213e;
            border-radius: 10px;
            padding: 20px 30px;
            margin: 20px 0;
            border: 1px solid #0f3460;
        }
        .book-list a {
            color: #5dade2;
            text-decoration: none;
            display: block;
            padding: 10px 0;
            border-bottom: 1px solid #0f3460;
            font-size: 1.1em;
        }
        .book-list a:last-child { border-bottom: none; }
        .book-list a:hover { color: #e6b800; }
        .content-box {
            background: #16213e;
            border-radius: 10px;
            padding: 25px;
            margin: 20px 0;
            border: 1px solid #0f3460;
            white-space: pre-wrap;
            line-height: 1.6;
        }
        .back-link {
            color: #e6b800;
            text-decoration: none;
        }
        .error { color: #e74c3c; }
        .footer {
            text-align: center;
            color: #555;
            margin-top: 40px;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>📚 Leaky Library</h1>
    <p class="subtitle">Your Digital Book Collection</p>
    {% if content is not none %}
        <p><a class="back-link" href="/">&larr; Back to Library</a></p>
        <h2>{{ book_name }}</h2>
        <div class="content-box">{{ content }}</div>
    {% elif error %}
        <p><a class="back-link" href="/">&larr; Back to Library</a></p>
        <p class="error">{{ error }}</p>
    {% else %}
        <div class="book-list">
            <h3>Available Books:</h3>
            {% for book in books %}
                <a href="/read?book={{ book }}">📖 {{ book }}</a>
            {% endfor %}
        </div>
    {% endif %}
    <p class="footer">Leaky Library v1.0 &mdash; "Every book has a secret passage"</p>
</body>
</html>
"""

@app.route('/')
def index():
    """List available books."""
    try:
        books = [f for f in os.listdir(BOOKS_DIR) if f.endswith('.txt')]
        books.sort()
    except FileNotFoundError:
        books = []
    return render_template_string(TEMPLATE, books=books, content=None, error=None, book_name=None)

@app.route('/read')
def read_book():
    """Read a book file. VULNERABLE: no path sanitization!"""
    book = request.args.get('book', '')
    if not book:
        return render_template_string(TEMPLATE, books=[], content=None,
                                       error="No book specified.", book_name=None)

    # VULNERABILITY: The filename is used directly without sanitization.
    # An attacker can use path traversal (e.g., ../../flag) to read
    # arbitrary files on the system.
    filepath = os.path.join(BOOKS_DIR, book)

    try:
        with open(filepath, 'r') as f:
            content = f.read()
        return render_template_string(TEMPLATE, books=[], content=content,
                                       error=None, book_name=book)
    except FileNotFoundError:
        return render_template_string(TEMPLATE, books=[], content=None,
                                       error=f"Book '{book}' not found.", book_name=None)
    except Exception as e:
        return render_template_string(TEMPLATE, books=[], content=None,
                                       error=f"Error reading book: {str(e)}", book_name=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

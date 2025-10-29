#!/usr/bin/env python3
"""
Duke Wiki - A lightweight wiki for MMORPG R&D team
"""

import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash
import markdown

app = Flask(__name__)
app.secret_key = 'duke_wiki_secret_key_change_in_production'

WIKI_DIR = os.path.join(os.path.dirname(__file__), 'wiki_data')

if not os.path.exists(WIKI_DIR):
    os.makedirs(WIKI_DIR)


def sanitize_filename(title):
    """Convert page title to safe filename"""
    return re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')


def get_page_path(title):
    """Get full path for a wiki page"""
    filename = sanitize_filename(title) + '.md'
    return os.path.join(WIKI_DIR, filename)


def load_page(title):
    """Load page content from file"""
    path = get_page_path(title)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    return None


def save_page(title, content):
    """Save page content to file"""
    path = get_page_path(title)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def list_pages():
    """List all wiki pages"""
    if not os.path.exists(WIKI_DIR):
        return []
    pages = []
    for filename in os.listdir(WIKI_DIR):
        if filename.endswith('.md'):
            title = filename[:-3].replace('_', ' ')
            pages.append(title)
    return sorted(pages)


def search_pages(query):
    """Search for pages containing query"""
    results = []
    query_lower = query.lower()
    for page_title in list_pages():
        content = load_page(page_title)
        if content and (query_lower in page_title.lower() or query_lower in content.lower()):
            results.append(page_title)
    return results


@app.route('/')
def index():
    """Redirect to home page"""
    return redirect(url_for('view_page', title='Home'))


@app.route('/page/<path:title>')
def view_page(title):
    """View a wiki page"""
    content = load_page(title)
    if content is None:
        return render_template('create.html', title=title)
    
    html_content = markdown.markdown(content, extensions=['fenced_code', 'tables', 'nl2br'])
    return render_template('view.html', title=title, content=html_content, raw_content=content)


@app.route('/edit/<path:title>', methods=['GET', 'POST'])
def edit_page(title):
    """Edit a wiki page"""
    if request.method == 'POST':
        content = request.form.get('content', '')
        save_page(title, content)
        flash(f'Page "{title}" saved successfully!', 'success')
        return redirect(url_for('view_page', title=title))
    
    content = load_page(title) or ''
    return render_template('edit.html', title=title, content=content)


@app.route('/create', methods=['GET', 'POST'])
def create_page():
    """Create a new wiki page"""
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('Please provide a page title', 'error')
            return render_template('create.html')
        
        if load_page(title) is not None:
            flash(f'Page "{title}" already exists', 'error')
            return redirect(url_for('view_page', title=title))
        
        return redirect(url_for('edit_page', title=title))
    
    return render_template('create.html')


@app.route('/all')
def all_pages():
    """List all pages"""
    pages = list_pages()
    return render_template('all.html', pages=pages)


@app.route('/search')
def search():
    """Search pages"""
    query = request.args.get('q', '')
    if query:
        results = search_pages(query)
    else:
        results = []
    return render_template('search.html', query=query, results=results)


@app.template_filter('wikilink')
def wikilink_filter(text):
    """Convert [[Page Title]] to links"""
    def replace_link(match):
        title = match.group(1)
        return f'<a href="{url_for("view_page", title=title)}">{title}</a>'
    
    return re.sub(r'\[\[(.*?)\]\]', replace_link, text)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

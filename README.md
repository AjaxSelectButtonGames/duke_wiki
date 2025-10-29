# Duke Wiki

A lightweight wiki system for the Duke County MMORPG Research & Development team.

## Features

- 📝 **Markdown Support**: Write pages using simple Markdown syntax
- 🔍 **Search Functionality**: Quickly find information across all wiki pages
- 🔗 **Wiki Links**: Easy page linking with `[[Page Name]]` syntax
- 📚 **Page Management**: Create, edit, and organize pages
- 🎮 **MMORPG Focused**: Pre-loaded with sample pages for game development
- 🚀 **Lightweight**: No database required - uses file-based storage
- 🎨 **Clean UI**: Modern, responsive interface

## Quick Start

### Installation

1. Clone the repository:
```bash
git clone https://github.com/AjaxSelectButtonGames/duke_wiki.git
cd duke_wiki
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Wiki

Start the Flask application:
```bash
python app.py
```

The wiki will be available at: `http://localhost:5000`

## Usage

### Creating Pages

1. Click "➕ New Page" in the navigation bar
2. Enter a page title
3. Write your content using Markdown
4. Click "💾 Save Page"

### Editing Pages

1. Navigate to any page
2. Click "✏️ Edit Page"
3. Modify the content
4. Click "💾 Save Page"

### Linking Pages

Use the wiki link syntax to link to other pages:
```markdown
[[Character Classes]]
[[Game Design Document]]
```

### Markdown Support

The wiki supports standard Markdown features:
- Headers (`#`, `##`, `###`)
- **Bold** and *italic* text
- Lists (ordered and unordered)
- Code blocks with syntax highlighting
- Tables
- Links and images

### Searching

Use the search bar in the top navigation to find pages containing specific terms.

## Project Structure

```
duke_wiki/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template with styling
│   ├── view.html        # Page view template
│   ├── edit.html        # Page editor template
│   ├── create.html      # New page template
│   ├── all.html         # All pages list
│   └── search.html      # Search results
├── wiki_data/           # Wiki page storage (Markdown files)
│   ├── Home.md
│   ├── Character_Classes.md
│   └── ...
└── README.md            # This file
```

## Sample Content

The wiki comes pre-loaded with sample pages for MMORPG development:
- **Home**: Main landing page
- **Game Design Document**: Core game design overview
- **Character Classes**: Player class descriptions
- **Combat Mechanics**: Combat system documentation
- **Technical Architecture**: System architecture details

Feel free to edit or delete these pages and create your own!

## Configuration

### Changing the Port

Edit `app.py` and modify the last line:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change port here
```

### Secret Key

For production use, change the secret key in `app.py`:
```python
app.secret_key = 'your-secure-secret-key-here'
```

## Development

### Requirements

- Python 3.8 or higher
- Flask 3.0.0
- markdown 3.5.1

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

Licensed under the Apache License 2.0. See LICENSE file for details.

## Support

For issues, questions, or contributions, please use the GitHub issue tracker.

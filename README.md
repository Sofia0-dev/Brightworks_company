# BrightWorks – Django + Bootstrap Project

A Django website with Home, About, Services and Employees pages. The Employees page is
filled with 30 randomly generated sample employees (name, email, age, department, job title,
salary, hire date). The sample data is created automatically by `python manage.py migrate`.

## Project Structure

```
testing/
├── manage.py
├── myproject/        # Project settings, urls, wsgi/asgi
├── myapp/            # Models, views, urls, admin, migrations (0002 seeds the data)
├── templates/        # master.html, home.html, about.html, services.html, employees.html
└── static/
    ├── css/custom.css
    └── images/
```

## Getting Started

```bash
git clone <your-repo-url>
cd <repo-folder>
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser # optional, for /admin
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Tests

```bash
python manage.py test
```

## Notes

- `db.sqlite3` and `.venv/` are not tracked in git; `migrate` creates the database and loads the sample data.

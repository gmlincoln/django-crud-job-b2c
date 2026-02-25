# Job Portal

A simple Django-based job portal application built as part of a training class. It allows users to
browse job listings, view details, and add new job postings. The project is structured as a single
`Job` app within a Django project and uses SQLite for development.

---

## 🔧 Features

- Add new job postings with title, company information, vacancy count, category, description,
  required skills, and optional company logo.
- Browse all jobs and view detailed information on individual job entries.
- Basic home page with links to browse or post jobs.
- Media handling for company logos and static assets via standard Django settings.

---

## 📁 Project Structure

```
Job_Portal/           # Django project folder
  ├── Job/             # Django app containing models, views, templates
  │   ├── models.py    # `Job` model definition
  │   ├── views.py     # request handlers for home, add, list, detail
  │   ├── urls.py      # URL routes for the app
  │   └── admin.py     # Admin 
  ├── Job_Portal/      # project configuration (settings, urls, wsgi, etc.)
  ├── db.sqlite3       # SQLite database used in development
  ├── manage.py        # CLI entry point for Django commands
  ├── media/           # uploaded company logos
  └── templates/       # shared templates (base, includes)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 (or compatible)
- virtualenv / venv (recommended)
- pip

### Installation & Setup

1. **Clone the repository** (if not already):
   ```bash
   mkdir Job_Portal
   git clone https://github.com/gmlincoln/django-crud-job-b2c
   cd Job_Portal
   ```
2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source ".venv/Scripts/activate"   # Windows PowerShell: .\.venv\Scripts\Activate.ps1
   ```
3. **Install dependencies**:
   ```bash
   pip install django
   pip install pillow
   ```
4. **Apply migrations** to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **(Optional)** Create a superuser to access the admin site:
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
7. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📄 Usage

- **Home page** (`/`) – links to browse or add jobs.
- **Add Job** (`/add_job/`) – submit a form to create a new listing.
- **All Jobs** (`/all_jobs/`) – view every job in the database.
- **Browse Jobs** (`/browse_jobs/`) – similar to all jobs but used for public listings.
- **Job Detail** (`/single_job_view/<id>`) – view detailed information on a single job.

Media files uploaded for company logos are stored under `media/company_logo/` and served via the
`MEDIA_URL` during development. Static assets should be placed in a `static/` directory if needed.

---

## 🛠 Model

```python
class Job(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(null=True)
    company_logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)
    vacancy = models.IntegerField()
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    skills = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.job_title
```

---

## 📦 Dependencies

- [Django](https://www.djangoproject.com/) 6.0.2 (as specified in `settings.py`)

You may add additional packages as needed and update `requirements.txt` accordingly.

---

## 📝 Notes

- This project is intended for learning and prototyping and is not production-ready.
- Ensure `DEBUG` is set to `False` and proper host(s) configured before deploying.
- Add proper authentication/authorization if expanding the app.

---

## 📚 Further Improvements

- Pagination for job listings
- Search/filter by category, skills, or company
- User accounts for posting/editing jobs
- REST API endpoints via Django REST Framework
- Styling with a CSS framework or custom design

---

Feel free to explore the code, tweak the models, and build on top of this simple
job portal! Happy coding. 👩‍💻👨‍💻

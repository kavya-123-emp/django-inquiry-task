# django-inquiry-task
# Django Inquiry Form Tasks

This Django project demonstrates the use of Django Forms and Models to handle customer inquiries.

## ✅ Task Breakdown

### 🔹 Task 1: Creating and Validating Forms
- Created `CustomerInquiry` model with fields: name, email, and message.
- Built `CustomerForm` in `forms.py` with:
  - Required fields
  - Custom validation for name (only alphabets)
  - Email uniqueness
  - Textarea for message field

---

### 🔹 Task 2: Handling Form Submissions
- Used `inquiry_view` to handle GET and POST
- On GET: display the empty form
- On POST: validate and save, show success or error messages
- Template: `inquiry_form.html` renders the form

---

### 🔹 Task 3: Admin Panel
- Registered `CustomerInquiry` in `admin.py`
- Displayed name, email, and submitted date in list
- Enabled search and filtering

---

## 🚀 How to Run

1. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate

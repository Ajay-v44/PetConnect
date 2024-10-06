# PetConnect

## Abstract

PetConnect is a comprehensive platform designed for pet owners, veterinary professionals, and animal enthusiasts. It serves as a community-driven hub where users can:

- **Post about lost pets** to seek help from the community in finding them.
- **Rehome pets** by posting available pets for adoption, making it easier for those who need to relocate or can't keep their pets anymore.
- **Access expert resources** related to pet nutrition, care, and health.
- **Book veterinary consultations**, offering advice and treatment options for pets with health concerns.

PetConnect fosters a supportive and informed community, helping ensure the well-being of pets by leveraging the power of collective care.

## Features

- Post about lost pets.
- Offer pets for adoption.
- Access pet care resources (nutrition, medical care, etc.).
- Consult with veterinarians through the platform.
- A supportive community for pet owners and animal lovers.

## Tech Stack

- **Backend**: Django (Python)
- **Database**:  SQLite
- **Frontend**: HTML, CSS, JavaScript (with Tailwind CSS for styling)
- **Deployment**: Deployed using Gunicorn, Nginx.

---

## Project Setup and Running Instructions

### 1. Prerequisites
Ensure you have the following installed:
- Python (3.8+)
- Django (latest version)
- PostgreSQL (if using PostgreSQL as the database)
- Virtualenv (for creating a virtual environment)

### 2. Run The Project By

```bash
cd PetCare
env/Scripts/activate
python manage.py runserver





# npx tailwindcss -i ./static/src/input.css -o ./static/src/output.css --watch
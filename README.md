# BIDYATek Backend API

Django REST Framework backend for BIDYATek branding website.

## Features

- Full REST API for all frontend data
- Admin panel with CRM features (demo request tracking, export)
- Multi-language support (English/Bangla)
- reCAPTCHA protection for forms
- Rate limiting on public POST endpoints
- Email confirmations for demo and contact forms
- SEO management per page

## Setup

1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate it: `source venv/bin/activate` (Linux) or `venv\Scripts\activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env` to `.env` and fill in your values
6. Run migrations: `python manage.py migrate`
7. Create superuser: `python manage.py createsuperuser`
8. Load initial data (optional): `python manage.py loaddata initial_data.json`
9. Run server: `python manage.py runserver`

## API Endpoints

All endpoints are under `/api/`:

- `GET /api/site-settings/` - Global site settings
- `GET /api/page-seo/{page}/` - SEO for specific page (page: home, about, etc.)
- `GET /api/how-it-works/` - Steps for "How It Works" section
- `GET /api/live-counters/` - Statistics counters
- `POST /api/newsletter/subscribe/` - Subscribe to newsletter (requires recaptcha_token)
- `GET /api/schools/` - Client schools
- `GET /api/modules/` - Product modules/features
- `GET /api/pricing-plans/` - Pricing plans with included modules
- `POST /api/demo-requests/` - Submit demo request (recaptcha_token required)
- `POST /api/contact/` - Submit contact form (recaptcha_token required)
- `GET /api/blog/posts/` - Blog posts
- `GET /api/blog/posts/{slug}/` - Single blog post by slug
- `GET /api/gallery/images/` - Gallery images
- `GET /api/testimonials/` - Testimonials
- `GET /api/faqs/` - FAQs

## Deployment

For production:
- Use PostgreSQL
- Set DEBUG=False
- Configure proper email backend
- Set up Nginx + Gunicorn
- Enable SSL
- Change ADMIN_URL in .env
- Set up CDN (Cloudflare) for static/media files

## Security Notes

- Admin panel is not at default `/admin` – change `ADMIN_URL` in `.env`
- Rate limiting on POST forms (5 per hour per IP)
- reCAPTCHA v3 on all public forms
- Django ORM prevents SQL injection
- CORS only allows frontend domain
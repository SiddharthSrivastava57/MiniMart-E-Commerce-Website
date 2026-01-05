# MiniMart - E-Commerce Website

A simple e-commerce website built with Django, featuring product listings, user authentication, and wishlist functionality.

## Features

- **Product Catalog**: Browse products organized by categories (Electronics, Books, Clothing, Home & Kitchen)
- **User Authentication**: Sign up, login, and logout functionality
- **Wishlist**: Add/remove products to/from personal wishlist
- **Dynamic Updates**: Uses HTMX for seamless AJAX interactions without page refreshes
- **Responsive Design**: Clean, modern UI with CSS styling
- **Image Support**: Product images with Django's media handling

## Technologies Used

- **Backend**: Django 6.0
- **Database**: SQLite3
- **Frontend**: HTML, CSS, HTMX
- **Authentication**: Django's built-in auth system
- **Image Handling**: Pillow for image processing

## Installation

1. **Clone the repository** (if applicable) or navigate to the project directory

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to the Django project directory**:
   ```bash
   cd MiniMart
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Populate the database with sample data**:
   ```bash
   python manage.py populate_db
   ```

7. **Create a superuser** (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Open your browser** and go to `http://127.0.0.1:8000/`

## Usage

### For Users:
- **Browse Products**: View all products on the homepage with sorting options (name, price low to high, price high to low)
- **Sign Up/Login**: Create an account or log in to access wishlist features
- **Add to Wishlist**: Click the heart icon on any product to add it to your wishlist
- **View Wishlist**: Access your wishlist from the navigation
- **Remove from Wishlist**: Remove items from your wishlist on the wishlist page or product list

### For Administrators:
- Access the Django admin at `http://127.0.0.1:8000/admin/` (requires superuser credentials)
- Manage categories, products, and users through the admin interface

## Project Structure

```
MiniMart/
├── MiniMart/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/              # User authentication app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── shop/                  # Main shop functionality
│   ├── models.py          # Product, Category, Wishlist models
│   ├── views.py           # Product listing, wishlist views
│   ├── urls.py
│   ├── management/commands/populate_db.py  # Database seeding
│   └── templates/
├── static/                # CSS, images
├── templates/             # Base templates
├── db.sqlite3             # SQLite database
├── manage.py
└── requirements.txt
```

## Models

### Category
- Represents product categories (Electronics, Books, etc.)

### Product
- Contains product information: name, description, price, category, image
- Ordered by name by default

### Wishlist
- Many-to-many relationship between users and products
- Tracks when items were added
- Unique constraint prevents duplicate wishlist entries

## API Endpoints

- `/` - Product list (GET)
- `/wishlist/` - User's wishlist (GET, requires login)
- `/wishlist/add/<product_id>/` - Add product to wishlist (POST, requires login)
- `/wishlist/remove/<product_id>/` - Remove product from wishlist (POST, requires login)
- `/accounts/signup/` - User registration (GET/POST)
- `/accounts/login/` - User login (GET/POST, Django built-in)
- `/accounts/logout/` - User logout (POST)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- Shopping cart functionality
- Payment integration
- Order management
- Product reviews and ratings
- Search functionality
- User profiles
- Email notifications

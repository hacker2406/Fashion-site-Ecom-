# ChazeFashion

ChazeFashion is a modern, stylish e-commerce web application for fashion products, inspired by platforms like Myntra. It features a clean, premium UI using TailwindCSS and daisyUI, and is built with Django.

---

## Features

- 🛍️ **Product Catalog**: Browse products by category, season, brand, and more.
- 🔍 **Advanced Filters**: Filter products by category, season, price range, fabric, and brand.
- ❤️ **Wishlist**: Save your favorite products for later.
- 🛒 **Cart & Checkout**: Add products to your cart and place orders securely.
- 👤 **User Profiles**: Manage your profile, address, and avatar.
- ⭐ **Product Reviews**: View and leave reviews for products.
- 🔐 **Authentication**: Secure signup, login, and logout.
- 📱 **Responsive Design**: Looks great on desktop and mobile.
- ⚡ **Modern UI**: Emerald + Slate + Sky color palette for a fresh, classy look.

---

## Tech Stack

- **Backend:** Django (Python)
- **Frontend:** TailwindCSS, daisyUI, FontAwesome
- **Database:** SQLite (default, can be changed)
- **Other:** AJAX for Add to Cart (no redirect), Django messages framework

---

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/ChazeFashion.git
    cd ChazeFashion
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On Mac/Linux
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser (admin)**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server**
    ```bash
    python manage.py runserver
    ```

7. **Access the app**
    - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Folder Structure

```
ChazeFashion/
├── catalog/                # Django app for products, cart, wishlist, etc.
│   ├── templates/
│   │   └── catalog/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── wishlist.html
│   │       ├── profile.html
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── checkout.html
│   └── ...
├── ChazeFashion/           # Django project settings
├── manage.py
└── requirements.txt
```

---

## Customization

- **Colors & Branding:** Easily change the color palette in the templates for your own brand.
- **Product Images:** Add your own images in the admin panel or via fixtures.
- **Extend Functionality:** Add payment gateways, order history, or more filters as needed.

---

## Credits

- [Django](https://www.djangoproject.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [daisyUI](https://daisyui.com/)
- [FontAwesome](https://fontawesome.com/)

---

## License

This project is for educational/demo purposes. For production use, please review and update security, privacy, and licensing as needed.

---

**Enjoy your stylish shopping experience with
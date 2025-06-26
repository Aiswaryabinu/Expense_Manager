# Expense Manager

Expense Manager is a user-friendly Django web application designed to help you track your expenses, manage your budget, and gain insights into your spending habits. With a clean interface and powerful features, you can take control of your personal finances.

## Features

- **Add, Edit, and Delete Expenses:** Easily record your daily expenses with details like amount, category, and date.
- **Expense Categories:** Organize your spending into customizable categories for better tracking.
- **Monthly & Yearly Reports:** Visualize your spending patterns with reports and charts.
- **Budget Management:** Set budgets for categories and receive alerts when you approach your limits.
- **Search & Filter:** Quickly find specific expenses using search and filter options.
- **Data Backup & Restore:** Keep your data safe with backup and restore functionality.
- **User Authentication:** Secure your data with user accounts and authentication.

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/) (recommended)
- (Optional) [PostgreSQL](https://www.postgresql.org/) or another production-ready database

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Aiswaryabinu/Expense_Manager.git
    cd Expense_Manager
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Copy `.env.example` to `.env` (or create a `.env` file in the root directory).
    - Add your configuration (example below):
        ```
        SECRET_KEY=your_django_secret_key
        DEBUG=True
        DB_NAME=your_db_name
        DB_USER=your_db_user
        DB_PASSWORD=your_db_password
        DB_HOST=localhost
        DB_PORT=5432
        ```

5. **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser (admin account):**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8. **Open in browser:**
    Visit [http://localhost:8000](http://localhost:8000)

## Usage

1. Register or log in to your account.
2. Add your expenses with relevant details.
3. Review reports and charts on the dashboard.
4. Set budgets and monitor your spending.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request to contribute.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or support, please contact [Aiswaryabinu](https://github.com/Aiswaryabinu).

---

*Happy Expense Tracking!*

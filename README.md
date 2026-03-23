# QA Automation Project (E-commerce Testing)

## 📌 Overview

This project contains automated test scripts for an e-commerce application, focusing on core user flows such as login, product interaction, cart management, and checkout.

The project is built using **Playwright with Python**, following the **Page Object Model (POM)** design pattern for better maintainability and scalability.

---

## 🛠️ Tech Stack

* Python
* Playwright
* Pytest
* Allure Reports

---

## 📂 Project Structure

```
qa-automation-project/
│
├── tests/                # Test cases
│   ├── test_login.py
│   ├── test_cart.py
│
├── pages/                # Page Object Model (POM)
│   ├── login_page.py
│   ├── product_page.py
│
├── screenshots/          # Test execution screenshots
├── allure-results/       # Allure report data
│
├── conftest.py           # Pytest fixtures (browser setup)
├── requirements.txt      # Dependencies
├── README.md             # Project documentation
```

---

## 🚀 Features Covered

### 🔐 Authentication

* Login with valid credentials
* Login with invalid email
* Login with invalid password
* Validation for empty fields

### 🛒 Cart Functionality

* Add product to cart
* Remove product from cart
* Update product quantity
* Handle multiple products

### 📦 Navigation & Checkout

* Product page navigation
* Pagination handling
* Checkout flow validation

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/qa-automation-ecommerce.git
cd qa-automation-ecommerce
```

### 2. Install Dependencies

```
pip install -r requirements.txt
playwright install
```

### 3. Run Tests

```
pytest --alluredir=allure-results
```

### 4. Generate Allure Report

```
allure serve allure-results
```

---

## 📊 Reporting

* Allure reports are used for test reporting
* Reports include:

  * Test execution status
  * Steps and logs
  * Screenshots on failure

---

## 🧠 Design Pattern Used

### Page Object Model (POM)

* Separates test logic from UI locators
* Improves code reusability
* Makes tests easier to maintain

---

## 📸 Screenshots

Screenshots are captured during execution and stored in the `screenshots/` folder.

(Add your report screenshots here if available)

---

## ✅ Key Highlights

* End-to-end automation using Playwright
* Structured using Pytest framework
* Clean POM implementation
* Assertions for validation
* Allure reporting integration

---

## 📄 Documentation

This project also includes:

* Functional Requirement Document (FRD)
* Test Plan
* Test Cases
* POMS
* Allure reports 
---

## 👤 Author

ROHAN SHARMA 

---

## 📌 Note

This project is created for learning and demonstration purposes to showcase QA automation skills.

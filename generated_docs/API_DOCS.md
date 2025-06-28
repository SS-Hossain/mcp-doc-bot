# API Documentation

## Function: `calculate_discount`
**File:** `uploaded_project\sample2.py`

**Arguments:** price, discount

**Docstring:**

Calculate discounted price given a percentage.

**Code Example:**

```python
def calculate_discount(price, discount):
    """
    Calculate discounted price given a percentage.
    """
    return price * (1 - discount / 100)
```

---

## Class: `Product`
**File:** `uploaded_project\sample2.py`

**Methods:** __init__, is_available

**Docstring:**

Represents a product with pricing and stock.

**Code Example:**

```python
class Product:
    """
    Represents a product with pricing and stock.
    """

    def __init__(self, name, price, stock):
        """
        Initialize a Product instance.
        """
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        """
        Check if the product is in stock.
        """
        return self.stock > 0
```

---

## Function: `__init__`
**File:** `uploaded_project\sample2.py`

**Arguments:** self, name, price, stock

**Docstring:**

Initialize a Product instance.

**Code Example:**

```python
def __init__(self, name, price, stock):
        """
        Initialize a Product instance.
        """
        self.name = name
        self.price = price
        self.stock = stock
```

---

## Function: `is_available`
**File:** `uploaded_project\sample2.py`

**Arguments:** self

**Docstring:**

Check if the product is in stock.

**Code Example:**

```python
def is_available(self):
        """
        Check if the product is in stock.
        """
        return self.stock > 0
```

---


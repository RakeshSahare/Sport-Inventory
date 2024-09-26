# Sports Equipment Inventory API

This project provides a RESTful API for managing sports equipment inventory.

## Features
- Create equipment entries
- Update equipment quantity
- Retrieve unavailable equipment (items having zero quantity)

## Endpoints
- POST `/api/equipment/` - Create a new equipment item
- PATCH `/api/equipment/{id}/update_quantity/` - Update quantity of a specific item
- GET `/api/equipment/unavailable/` - Retrieve items with zero quantity

## Script
- `check_unavailable_items.py` - Fetches unavailable items every minute and saves to a JSON file.

## Setup
1. Clone the repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run migrations:
    ```bash
    python manage.py migrate
    ```
4. Run the server:
    ```bash
    python manage.py runserver
    ```

## Tests
To run tests:
```bash
python manage.py test
```
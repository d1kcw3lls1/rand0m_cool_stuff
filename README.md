# Discount Codes Generator

To run the application:

```
python -m venv venv
venv\Scripts\activate.bat # for Linux: ./venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
> (enter email)
> (enter password)
python manage.py runserver
```

You can find the API in:

```
http://localhost:8000/api/v1/brands/1/generate-discount-codes/
http://localhost:8000/api/v1/brands/1/obtain-discount-code/
```

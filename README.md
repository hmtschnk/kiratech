# kiratech

Kiratech project is developed to complete Kiratech's assignment

## Project installation
1. Clone this repository to your local device

2. In your local device, create a new Python environment and activate. In this example, we will name our environment as "kiratech_env"

`$ python -m venv kiratech`

`$ kiratech_env/Scripts/activate.bat`

3. Go into the root of this project you just cloned, and install the dependencies

`$ pip install requirements.txt`

4. Run the project and visit http://127.0.0.1:8000/inventory

`$ python manage.py runserver`

## Project breakdown

This document will breakdown the units of this project according to the assignment PDF provided by Kiratech

## Question A
Django app called inventory is created containing two models; inventory and supplier

<p align="center">
<img src="https://github.com/hmtschnk/kiratech/blob/main/staticfiles/readme_md/database_structure.png" width="450">
</p>

## Question B
A list from model inventories at http://127.0.0.1:8000/inventory

<p align="center">
<img src="https://github.com/hmtschnk/kiratech/blob/main/staticfiles/readme_md/inventory.png" width="450">
</p>

The result of the above page is retrieved from Django Rest Framework at http://127.0.0.1:8000/api/inventory

<p align="center">
<img src="https://github.com/hmtschnk/kiratech/blob/main/staticfiles/readme_md/api_inventory.png" width="450">
</p>

User may filter the list by name using the top right corner of the page

<p align="center">
<img src="https://github.com/hmtschnk/kiratech/blob/main/staticfiles/readme_md/inventory.png" width="450">
</p>

## Question C
User view the details of a specific inventory by adding inventory ID at the URL. For example; http://127.0.0.1:8000/inventory/1

<p align="center">
<img src="https://github.com/hmtschnk/kiratech/blob/main/staticfiles/readme_md/inventory_1.png" width="450">
</p>
## Question D
Django admin can be accessed using the 'Admin' button at navigation bar or by using this link; http://127.0.0.1:8000/admin

```
Username: demo
Password: demo
```

Admin may add new inventory records at invetorys

## Question C
All the routings of this project has been tested and they are working fine.
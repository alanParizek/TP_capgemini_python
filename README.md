# Chango
Chango is a cart system for stores that allows users to add products to their purchases just by taking pictures. While the buyer adds items to their cart, the prices are displayed on the screen as well as the purchase price.

## Installation

To deploy Chango in your server, first clone the project.

Then install the project dependencies, by running from your terminal:
```bash
pip install -r dependencies.txt
```

You will also have to download this file:
>https://drive.google.com/file/d/1XG-xM6yvI-798wd2Akqv51luEG9WRlGw/view?usp=share_link

And save it in the visualizacionDeImagenes/yolov4 folder.

You will need to create a mysql database for storing the data. Once you have created yours, enter your database name and credentials in the DATABASES section on /listaDeCompras/listaDeCompras/settings.py.

Create the database tables with:
```bash
py manage.py makemigrations && py manage.py migrate
```
From the /listaDeCompras folder.

Finally, run the web server by executing:
```bash
py manage.py runserver
```

## Setup
For buyers to be able to add products to their Changos, you will need to load your catalog in the database. You can do that in the Django admin page.

To use the admin page you will need a super user account. Create your super user account by running:
```bash
py manage.py createsuperuser
```

Once you have an account, go to <yourdomain>/admin. In this page you can create, upload, modify and delete products. Products have two categories: countable and uncountable. For countable products, enter the price in terms of units, and for uncountable products, enter the price for 100 grams. The “count products” feature is only available for countable products.

## Usage
### As a client
First, you will need to log in. If you do not have an account yet, you can create one by clicking on the “Don't have an account” button.

Once you have logged in, you’ll be redirected to the cart page, where you’ll find some buttons, and, if you have already added some items, a list of items.

On top of the page there is an input type file where you can upload images of the products, and then click on the “Cargar Imagen” button so that the system can recognize it and count it. After that, the product, quantity and price will appear on the form below. If the options on the forms are not correct, or you want to change them for any reason, you can. The system allows you to fill the form fields manually without the need of uploading an image, too. Once the form fields are filled, you can click on the “Agregar Producto” button to add it to the cart.
The items will be displayed on the items list beneath the forms. A button named “Eliminar Producto” will appear next to the items on the list. This button will delete the item.

Click the button named “Cerrar Compra” to inform the cashier the purchase price.

Once you have finished shopping you can log out by clicking on the “Log Out” button placed on the top-right corner on the screen.

#### Demo video:
https://user-images.githubusercontent.com/82058481/207932021-7f79fa28-53af-4181-86ed-17dd5c1605d0.mp4
  
### As a cashier
First, you will need to log in. If you do not have an account yet, ask your manager to create an account for you.

Once you have logged in, you’ll be redirected to the cart page, where you’ll see all the purchases that haven’t been paid. It will show you the purchase id, the customer name and the total purchase price. Once you’ve charged the customer, click on the “Cobrar Chango” button next to that purchase to register the payment.
  
#### Demo video:
https://user-images.githubusercontent.com/82058481/207932163-828d9752-a71f-42de-a922-d30951e7c462.mp4



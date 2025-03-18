from django.db import models
import datetime  # Correct import for datetime

# Model for Menu Categories
class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model for Menu Items (Updated class name to MenuItem)
class MenuItem(models.Model):
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        MenuCategory, 
        on_delete=models.PROTECT, 
        default=None,
        related_name='category_name'  # Optional: Makes querying more intuitive
    )

    def __str__(self):
        return self.menu_item

# Model for Customers
class Customer(models.Model):
    name = models.CharField(max_length=100)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def __str__(self):
        return self.name

# Logger model
class Logger(models.Model):
    name = models.CharField(max_length=100)  # Renamed field
    last_name = models.CharField(max_length=100)
    time_log = models.TimeField(help_text="Enter the exact time")

    def __str__(self):
        return f"{self.name} {self.last_name}"

# Model for Reservations


    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name

# Model for Menu Items
class Menu(models.Model):
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField()
    category_id = models.ForeignKey(
        MenuCategory, 
        on_delete=models.PROTECT, 
        default=None,
        related_name='category_name'  # Optional: Makes querying more intuitive
    )

    def _str_(self):
        return self.menu_item

class Customer(models.Model):
    name = models.CharField(max_length=100)
    reservation_day = models.CharField(max_length=20)
    seats = models.IntegerField()

    def _str_(self):
        return self.name

class Logger(models.Model):
    name = models.CharField(max_length=100)  # Renamed field
    last_name = models.CharField(max_length=100)
    time_log = models.TimeField(help_text="Enter the exact time")

    def __str__(self):
        return f"{self.name} {self.last_name}"


    

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
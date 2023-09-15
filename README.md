# microcenter_inventory_checker

You need to configure the user settings in the config.toml file first.


The email sender and receiver can be the same email but it will look like an email to yourself.
I like to keep an extra email address for sending notifications from various scripts that I use.
If you dont want to use the email function then delete or comment out the last 2 lines of micro.py.

![micro6](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/575db81e-548b-4136-8557-d2406f702918)



If you are using gmail for the sender email you need to create an app password and use that instead of the actual email password.
Directions for creating an app password with gmail here https://support.google.com/mail/answer/185833?hl=en

---------------------------------------------------------------------------------------------------------------------------------

To get your local store id you need to first go to https://www.microcenter.com/
Navigate to the "your store" dropdown and select your stores location.

![micro](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/ac892f8c-8e22-408d-bbc0-422ea038e205)



When you select your local store the store id will be added to the end of the url.
Copy the store id and paste it into the config.toml file, in between the "" on the store_id= line.

![micro2](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/d69c7ecc-fdd5-4f1c-9dbb-a9d54f5ed227)

---------------------------------------------------------------------------------------------------------------------------------

To add an item you need to find it on the site and copy the whole url.
Paste it into the quotes "" on the url= line.
Give the item a proper name in between the "" on the name= line.

![micro5](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/ed36cfe4-44be-4f91-ae80-9c514d6fb6b0)



You may add as many items as you like.
Dont leave any blank. if theyre not being used delete or comment the item out. lines 23, 24, and 25 in the pic as an example.

![micro4](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/323bc260-161a-472e-b8d3-782a9dd78d3a)

---------------------------------------------------------------------------------------------------------------------------------

When everything is set make sure you have installed the required modules from requirements.txt then you can run micro.py

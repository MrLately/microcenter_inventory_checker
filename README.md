# microcenter_inventory_checker

you need to configure the user settings in the config.toml file first.

the email sender and receiver can be the same email but it will look like an email to yourself.
I like to keep an extra email address for sending notifications from various scripts that I use.

if you are using gmail for the sender email you need to create an app password and use that instead of the actual email password.
directions for creating an app password with gmail here https://support.google.com/mail/answer/185833?hl=en

to get your local store id you need to first go to https://www.microcenter.com/
navigate to the "your store" dropdown and select your stores location.

![micro](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/ac892f8c-8e22-408d-bbc0-422ea038e205)

when you select your local store the store id will be added to the end of the url.
copy the store id and paste it into the config.toml file.

![micro2](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/58047084-058d-4317-9503-69751fafe867)



to add an item you need to find it on the site and copy the whole url.
paste it into the quotes "" on the url= line.
give the item a proper name in between the "" on the name= line.

![micro5](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/ed36cfe4-44be-4f91-ae80-9c514d6fb6b0)


you may add as many items as you like.
dont leave any blank. if theyre not being used delete or comment the item out. lines 23, 24, and 25 in the pic as an example.

![micro4](https://github.com/MrLately/microcenter_inventory_checker/assets/94589563/323bc260-161a-472e-b8d3-782a9dd78d3a)

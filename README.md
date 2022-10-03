# upload_image
It Simple upload image file app.

here Rest Api has created using django rest framework. 

For user authentication JWT tokent system were used.

To Create new user go to admin panel and create new user manually. check bellow url link
http://127.0.0.1:8000/admin/

After creating new user we need to create JWT token , for that hit below url link and using post method by passing username and password data we successfully obtained the JWT token. It return refresh and access tokent.
http://127.0.0.1:8000/getjwt/

Now its time to access upload image url, and upload the image having size below than 500kb, need to hit the below url links and for authentication we need to enter access JWT tokent and we ready to access.
http://127.0.0.1:8000/upload/

Also this above is the web API for performing the CRUD operations.


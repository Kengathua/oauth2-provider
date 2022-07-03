
    git clone https://github.com/Kengathua/oauth2-provider.git

Then

    cd oauth2-provider

Setup a virtualenv and run

    pip install -r requirements/all.txt

    ./manage.py makemigrations

    ./manage.py migrate

To set up a new user run:

    ./manage.py shell

or

    python manage.py shell

Then copy and paste this block of code.

    from trial_oauth2_provider.users.models import User

    User.objects.create(
        email='oauth2trialuser@email.com', first_name='Trial',
        last_name='User', other_names='Oauth2', phone_no='+254718488252',
        password='oauth2trialuser')

To exit shell run:

    exit()

Now start the development server:

    ./manage.py runserver 9000

or

    python manage.py runserver 9000

**NOTE** the port for the authentication server is **9000**

http://127.0.0.1:9000/o/applications/

You will be redirected to the default django admin login page:

Enter email:

    oauth2trialuser@email.com

and password:

    oauth2trialuser

![Login Page](./screenshots/Screenshot%20from%202022-07-03%2023-25-59.png)

You will be redirected to the apps registration page

Select **NEW APPLICATION** and a form will appear.

![New Application](./screenshots/Screenshot%20from%202022-07-03%2023-26-32.png)

Enter the details of the application as follows:

    Name: <Enter a name your app>

    Client id: <Leave it as it is>

    Client secret: <Leave it as it is>

    Client type: <Select CONFIDENTIAL>

    Authorization grant type: <Select AUTHORIZATION CODE>

    Redirect Uris: 'http://127.0.0.1:8000/accounts/provider/login/callback/'

    Algorithm: <Select any>

    **SAVE**

![New Application](./screenshots/Screenshot%20from%202022-07-03%2012-16-12.png)

Now you have an app registered.

Now to set up access for the [Client Server / Consumer](https://github.com/Kengathua/oauth2-consumer) go to:
 https://github.com/Kengathua/oauth2-consumer

Copy the Client id and the Client secret codes from the created app.

Go to your client server environment file and paste these values in their respective fields

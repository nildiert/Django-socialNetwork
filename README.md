[![Django](https://www.djangoproject.com/m/img/logos/django-logo-positive.png)](https://www.djangoproject.com/)

# Django-socialNetwork

Django provides some useful tools that can allow you develop a social application, which means that users are able to join an online platform and interact with each other by sharing content. I focused on building an image sharing platform. Users can be able to bookmark any image on the Internet and share it with others. They also be able to see activity on the platform from the users they follow and like/unlike the images shared by them.

### Django tools used

- - -

> In construction ...

| Tool | Description |
| ---- | ----------- |
| [Data models](https://docs.djangoproject.com/en/3.1/topics/db/models/) | A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing. Generally, each model maps to a single database table. |
| [Migrations](https://docs.djangoproject.com/en/3.1/topics/migrations/) | Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into. |
| [Views](https://docs.djangoproject.com/en/3.1/topics/http/views/) | A view function, or view for short, is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image . . . or anything, really. The view itself contains whatever arbitrary logic is necessary to return that response. |
| [Templates](https://docs.djangoproject.com/en/3.1/ref/templates/) | Django’s template engine provides a powerful mini-language for defining the user-facing layer of your application, encouraging a clean separation of application and presentation logic. Templates can be maintained by anyone with an understanding of HTML; no knowledge of Python is required. For introductory material, see Templates topic guide. |
| [URL dispatcher](https://docs.djangoproject.com/en/3.1/topics/http/urls/) | A clean, elegant URL scheme is an important detail in a high-quality Web application. Django lets you design URLs however you want, with no framework limitations. |
| [Django Forms](https://docs.djangoproject.com/en/3.1/topics/forms/) | Django provides a range of tools and libraries to help you build forms to accept input from site visitors, and then process and respond to the input. |
| [Model Forms](https://docs.djangoproject.com/en/3.1/topics/forms/modelforms/) | If you’re building a database-driven app, chances are you’ll have forms that map closely to Django models. For instance, you might have a BlogComment model, and you want to create a form that lets people submit comments. In this case, it would be redundant to define the field types in your form, because you’ve already defined the fields in your model. |
| [Django authentication](https://docs.djangoproject.com/en/3.1/topics/auth/) | The Django authentication system handles both authentication and authorization. Briefly, authentication verifies a user is who they claim to be, and authorization determines what an authenticated user is allowed to do. Here the term authentication is used to refer to both tasks. |
| [Django authentication views](https://docs.djangoproject.com/en/3.0/topics/auth/default/#all-authentication-views) | Django includes several forms and views in the authentication framework that you can use right away. The login view you have created is a good exercise to understand the process of user authentication in Django. However, you can use the default Django authentication views in most cases. |
| [Email System](https://docs.djangoproject.com/en/3.1/topics/email/) | Although Python provides a mail sending interface via the smtplib module, Django provides a couple of light wrappers over it. These wrappers are provided to make sending email extra quick, to help test email sending during development, and to provide support for platforms that can’t use SMTP. |
| [Authentication URL patterns](https://github.com/django/django/blob/stable/3.0.x/django/contrib/auth/urls.py) | Django also provides the authentication URL patterns that are included in ```django.contrib.auth.urls``` |
| [Referencing the User model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#django.contrib.auth.get_user_model) | When you have to deal with user accounts, you will find that the user model of the Django authentication framework is suitable for common cases. However, the user model comes with very basic fields. You may wish to extend it to include additional data. The best way to do this is by creating a profile model that contains all additional fields and a one-to-one relationship with the Django ```User``` model. |
| [Pillow](https://pillow.readthedocs.io/en/stable/) | You need to install the Pillow library to handle images. Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors. |
| [Custom User Model](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#substituting-a-custom-user-model) | Django also offers a way to substitute the whole user model with your own custom model. Your user class should inherit from Django's ```AbstractUser``` class, which provides the full implementation of the default user as an abstract model. |
| [Messages framework](https://docs.djangoproject.com/en/3.1/ref/contrib/messages/#module-django.contrib.messages) | Quite commonly in web applications, you need to display a one-time notification message (also known as “flash message”) to the user after processing a form or some other types of user input. For this, Django provides full support for cookie- and session-based messaging, for both anonymous and authenticated users. The messages framework allows you to temporarily store messages in one request and retrieve them for display in a subsequent request (usually the next one). Every message is tagged with a specific **level** that determines its priority (e.g., **info**, **warning**, or **error**). |
| [Custom authentication backend](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#other-authentication-sources) | Django allows you to authenticate against different sources. The AUTHENTICATION\_BACKENDS setting includes the list of authentication backends for your project. By default, this setting is set as follows: ```['django.contrib.auth.backends.ModelBackend']```. The default ModelBackend authenticates users against the database using the user model of django.contrib.auth. This will suit most of your projects. However, you can create custom backends to authenticate your user against other sources, such as a **Lightweight Directory Access Protocol** (**LDAP**) directory or any other system. |
| [ALLOWED\_HOSTS](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts) | A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent [HTTP Host header attacks](https://docs.djangoproject.com/en/3.0/topics/security/#host-headers-virtual-hosting), which are possible even under many seemingly-safe web server configurations. |
| [Social Authentication](https://python-social-auth.readthedocs.io/en/latest/backends/index.html#supported-backends) | You can add social authentication to your site using services such as **Facebook**, **Twitter**, or **Google**. Python Social Auth is a Python module that simplifies the process of adding social authentication to your website. Using this module, you can let your users log in to your website using their accounts from other services. |
| [Relationships (Many to many)](https://docs.djangoproject.com/en/3.0/topics/db/examples/many_to_many/) | **ManyToManyField** accepts an extra set of arguments – all optional – that control how the relationship functions. |
| [Bookmarklet with jQuery](https://jquery.com/) | A bookmarklet is a bookmark stored in a web browser that contains JavaScript code to extend the browser's functionality. When you click on the bookmark, the JavaScript code is executed on the website being displayed in the browser. This is very useful for building tools that interact with other websites. |
| [Created image thumbnails using easy-thumbnails](https://pypi.org/project/easy-thumbnails/) | A powerful, yet easy to implement thumbnailing application for Django |
| [AJAX actions with jQuery](https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax) | On each XMLHttpRequest, set a custom X-CSRFToken header (as specified by the CSRF\_HEADER\_NAME setting) to the value of the CSRF token. This is often easier because many JavaScript frameworks provide hooks that allow headers to be set on every request. |
| [Cross-site request forgery in AJAX requests](https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax) | The CSRF middleware and template tag provides easy-to-use protection against Cross Site Request Forgeries. This type of attack occurs when a malicious website contains a link, a form button or some JavaScript that is intended to perform some action on your website, using the credentials of a logged-in user who visits the malicious site in their browser. |
| [custom decorators for your views](https://www.python.org/dev/peps/pep-0318/) | Decorators are a way to restrict access to views based on the request method or control caching behaviour. This is particularly useful when you want to separate logged-in users from unauthenticated users or create an admin page that only privileged users can access. |
| [AJAX pagination to the list views](https://stackoverflow.com/questions/4608323/django-core-paginator-ajax-pagination-with-jquery) | Used AJAX pagination to build an infinite scroll functionality. Infinite scroll is achieved by loading the next results automatically when the user scrolls to the bottom of the page. |

### Installation

```
git clone https://github.com/nildiert/Django-socialNetwork.git && cd Django-socialNetwork/
chmod u+x install.sh && ./install.sh
python3 manage.py runserver
```

### Changelog

- - -

* 15-Sep-2020

### Fixes, bugs and suggestions (DM)

- - -

[![Twitter](https://img.icons8.com/clouds/2x/twitter.png)](https://twitter.com/nildiert)
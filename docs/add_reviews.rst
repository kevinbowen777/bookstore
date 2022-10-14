Create new reviews
==================

Create batch reviews for testing bookstore application

Instructions
------------

In the application directory, run the following command:

.. code-block:: console

    $ python manage.py shell_plus

Sample user list
----------------

.. code-block:: console

    User = get_user_model()
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a my favorite book that has ever been written. I mean this is just wonderful",
        author = User.objects.get(username="susan"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a manual test review. Blah Blah Blah",
        author = User.objects.get(username="susan"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "Dictum non consectetur a erat nam at lectus urna duis. Purus viverra accumsan in nisl nisi. Arcu dictum varius duis at consectetur lorem donec massa sapien.",
        author = User.objects.get(username="john"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a manual test review 3. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt praesent semper feugiat nibh sed pulvinar. Ultrices vitae auctor eu augue. Neque vitae tempus quam pellentesque nec nam aliquam sem. Posuere lorem ipsum dolor sit amet consectetur.",
        author = User.objects.get(username="mary"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "Elementum eu facilisis sed odio morbi. Purus viverra accumsan in nisl nisi scelerisque eu. Hendrerit gravida rutrum quisque non tellus. Mollis nunc sed id semper.",
        author = User.objects.get(username="david"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a my favorite book that has ever been written. I mean this is just wonderful",
        author = User.objects.get(username="testuser"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a manual test review. Blah Blah Blah",
        author = User.objects.get(username="david"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "Tortor at auctor urna nunc. Sed libero enim sed faucibus turpis in eu mi bibendum. Dictum non consectetur a erat nam at lectus urna duis. Purus viverra accumsan in nisl nisi.",
        author = User.objects.get(username="john"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a manual test review 3. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt praesent semper feugiat nibh sed pulvinar. Ultrices vitae auctor eu augue. Neque vitae tempus quam pellentesque nec nam aliquam sem. Posuere lorem ipsum dolor sit amet consectetur.",
        author = User.objects.get(username="susan"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "Aliquam vestibulum morbi blandit cursus risus at ultrices. Sapien pellentesque habitant morbi tristique senectus et netus et. Dui accumsan sit amet nulla facilisi morbi tempus iaculis. ",
        author = User.objects.get(username="alice"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a my favorite book that has ever been written. I mean this is just wonderful",
        author = User.objects.get(username="david"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "This is a manual test review. Blah Blah Blah",
        author = User.objects.get(username="susan"),
    )
    Review.objects.create(
        book = Book.objects.get(title="Brave New World"),
        review = "Nulla facilisi etiam dignissim diam quis enim lobortis. Aliquam malesuada bibendum arcu vitae elementum curabitur vitae nunc sed. Eu ultrices vitae auctor eu augue ut lectus. Malesuada bibendum arcu vitae elementum curabitur vitae nunc. Eros donec ac odio tempor orci. ",
        author = User.objects.get(username="john"),
    )

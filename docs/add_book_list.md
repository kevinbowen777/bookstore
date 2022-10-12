##Template for adding a list of books to bookstore Django application

```
book = Book.objects.create(
    title="",
    author="",
    price="",
    cover="covers/.jpg")
```

`python manage.py shell_plus`

```
book = Book.objects.create(
    title="Brave New World",
    author="Aldous Huxley",
    price="19.95",
    cover="covers/brave/huxley.jpg"
)

Book.objects.create(
    title="Django for Beginners: Learn web development with Django",
    author="William S. Vincent",
    price="39.95",
    cover="covers/dfb_cover_40.jpg"
)

Book.objects.create(
    title="Django for APIs: Build web APIs with Python & Django",
    author="William S. Vincent",
    price="49.95",
    cover="covers/dfa_cover_40.jpg"
)
---------------
Book.objects.create(
    title="Django for Professionals: Production websites with Python & Django",
    author="William S. Vincent",
    price="39.95",
    cover="covers/dfp_cover_31.png"
)

Book.objects.create(
    title="Atoms, Metaphors and Paradoxes: Niels Bohr and the Construction of a New Physics",
    author="Sandro Petruccioli",
    price="59.95",
    cover="covers/atoms_metaphors.jpg"
)

Book.objects.create(
    title="Luce elettricità magnetismo",
    author="Sandro Petruccioli",
    price="79.95",
    cover="covers/luce_petro.jpg"
)

Book.objects.create(
    title="The Structure of Scientific Revolutions",
    author="Thomas Kuhn",
    price="29.95",
    cover="covers/struct_sci_rev_kuhn.jpg"
)

Book.objects.create(
    title="Black-Body Theory and the Quantum Discontinuity, 1894-1912",
    author="Thomas Kuhn",
    price="49.95",
    cover="covers/black_body_kuhn.jpg"
)

Book.objects.create(
    title="Capitalist Realism: Is There No Alternative?",
    author="Mark Fisher",
    price="12.95",
    cover="covers/cap_fisher.jpg"
)

Book.objects.create(
    title="Ghosts of My Life: Writings on Depression, Hauntology and Lost Futures",
    author="Mark Fisher",
    price="26.95",
    cover="covers/ghosts_fisher.jpg"
)

Book.objects.create(
    title="The Conquest of Bread",
    author="Pyotr Kropotkin",
    price="9.95",
    cover="covers/bread_kropot.jpg"
)

Book.objects.create(
    title="Anarchism: A Collection of Revolutionary Writings",
    author="Pyotr Kropotkin",
    price="8.95",
    cover="covers/anarcho_kropot.jpg"
)

Book.objects.create(
    title="My Mother: Demonology",
    author="Kathy Acker",
    price="27.95",
    cover="covers/mymother_acker.jpg"
)

Book.objects.create(
    title="Blood and Guts in High School",
    author="Kathy Acker",
    price="23.95",
    cover="covers/blood_guts_acker.jpg"
)

Book.objects.create(
    title="Dubliners",
    author="James Joyce",
    price="9.95",
    cover="covers/dubliners_joyce.jpg"
)

Book.objects.create(
    title="Ulysses",
    author="James Joyce",
    price="16.95",
    cover="covers/uly_joyce.jpg"
)

Book.objects.create(
    title="Eyeless in Gaza",
    author="Aldous Huxley",
    price="9.95",
    cover="covers/eyeless_huxley.jpg"
)

Book.objects.create(
    title="Programming Python",
    author="Mark Lutz",
    price="69.95",
    cover="covers/programming_python.jpg"
)

Book.objects.create(
    title="Test-Driven Development with Python",
    author="Harry J.W. Percival",
    price="59.99",
    cover="covers/tdd_with_python.jpg"
)

Book.objects.create(
    title="Two Scoops of Django 3.x",
    author="Daniel Feldroy",
    price="27.99",
    cover="covers/two_scoops.jpg"
)
```

In [37]: creator = CustomUser.objects.get(username="kbowen")

In [38]: for book in Book.objects.all():
    ...:     book.creator = creator
    ...:     book.save()
    ...:

In [39]: for book in Book.objects.all():
    ...:     print(book, book.creator)
    ...:


Sandro Petruccioli
James Joyce
Thomas Kuhn
William S. Vincent
Aldous Huxley
Mark Fisher
Kathy Acker
Pyotr Kropotkin

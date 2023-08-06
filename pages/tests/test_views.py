from django.core.mail import BadHeaderError
from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import (
    AboutPageView,
    ContactView,
    HomePageView,
    SuccessView,
)


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "pages/home.html")

    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, "Welcome to the Bookstore")

    def test_homepage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the Homepage")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__,
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, "pages/about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "About Page")

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the About page")

    def test_about_page_url_resolves_about_pageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__,
        )


class ContactViewTests(SimpleTestCase):
    def setUp(self):
        url = reverse("contact")
        self.response = self.client.get(url)

    def test_contact_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contact_page_url_resolves_contactpageview(self):
        view = resolve("/contact/")
        self.assertEqual(
            view.func.__name__,
            ContactView.__name__,
        )

    def test_contact_page_template(self):
        self.assertTemplateUsed(self.response, "pages/contact.html")

    def test_contact_page_contains_correct_html(self):
        self.assertContains(self.response, "Contact Us")

    def test_contact_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Home Page")

    def test_post_success(self):
        self.client.post(
            "/contact/",
            data={
                "from_email": "john@example.com",
                "subject": "Test Email",
                "messages": "This is a test",
            },
        )
        self.assertEqual(self.response.status_code, 200)

    def test_header_injection(self):
        error_occured = True
        try:
            self.client.post(
                "/contact/",
                data={
                    "from_email": "joe@example.com",
                    "subject": "Subject\nInjectionTest",
                    "message": "This is a test of a BadHeaderError",
                },
            )
            error_occured = False
        except BadHeaderError:
            error_occured = True
        self.assertFalse(error_occured)


class SuccessViewTests(SimpleTestCase):
    def setUp(self):
        url = reverse("success")
        self.response = self.client.get(url)

    def test_success_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_success_page_template(self):
        self.assertTemplateUsed(self.response, "pages/success.html")

    def test_success_page_contains_correct_html(self):
        self.assertContains(
            self.response,
            "Success! Thank you for your message.",
        )

    def test_success_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Please Go Away")

    def test_success_page_url_resolves_success_page_view(self):
        view = resolve("/success/")
        self.assertEqual(
            view.func.__name__,
            SuccessView.__name__,
        )

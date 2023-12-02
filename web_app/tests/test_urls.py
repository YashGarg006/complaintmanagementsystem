
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from GRsystem.views import register, change_password, change_password_g, counter, list, pdf_view, pdf_viewer, aboutus, login_redirect, slist, dashboard, complaints, allcomplaints
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


class TestUrls(SimpleTestCase):

    def test_register_is_reversed(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)

    def test_signin_is_reversed(self):
        url = reverse('signin')
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, LoginView)

    def test_logout_is_reversed(self):
        url = reverse('logout')
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, LogoutView)

    def test_change_password_is_reversed(self):
        url = reverse('change_password')
        self.assertEqual(resolve(url).func, change_password)

    def test_change_password_g_is_reversed(self):
        url = reverse('change_password_g')
        self.assertEqual(resolve(url).func,change_password_g)
    
    def test_counter_is_reversed(self):
        url = reverse('counter')
        self.assertEqual(resolve(url).func,counter)
    
    def test_list_is_reversed(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func,list)
    

    def test_pdf_viewer_is_reversed(self):
        url = reverse('view')
        self.assertEqual(resolve(url).func,pdf_viewer) 

    def test_aboutus_is_reversed(self):
        url = reverse('aboutus')
        self.assertEqual(resolve(url).func,aboutus)    

    def test_login_redirect_is_reversed(self):
        url = reverse('login_redirect')
        self.assertEqual(resolve(url).func,login_redirect)

    def test_dashboard_is_reversed(self):
        url = reverse('dashboard')
        self.assertEqual(resolve(url).func,dashboard)

    def test_complaints_is_reversed(self):
        url = reverse('complaints')
        self.assertEqual(resolve(url).func,complaints)

    def test_allcomplaints_is_reversed(self):
        url = reverse('allcomplaints')
        self.assertEqual(resolve(url).func,allcomplaints)
    

    def test_password_reset_view_is_reversed(self):
        url = reverse('password_reset')
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetView)

    def test_password_reset_done_view_is_reversed(self):
        url = reverse('password_reset_done')
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetDoneView)

    def test_password_reset_confirm_view_is_reversed(self):
        url = reverse('password_reset_confirm', args=['uidb64', 'token'])
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetConfirmView)

    def test_password_reset_complete_view_is_reversed(self):
        url = reverse('password_reset_complete')
        resolved_view = resolve(url).func.view_class
        self.assertEqual(resolved_view, PasswordResetCompleteView)
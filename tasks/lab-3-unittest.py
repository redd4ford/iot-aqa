import copy
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.selenium_academy.auth import (
    RegisterPage,
    AccountDashboardPage,
    LoginPage,
)
from pages.selenium_academy.main import HomePage
from tasks.utils import generate_random_email


class TestAuthenticationFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.used_email = 'bamij44058@invodua.com'
        cls.used_password = '123456'
        cls.user_data = {
            'first_name': 'Viktoriia',
            'last_name': 'Yehorova',
            'email': generate_random_email(char_num=20),
            'password': '123456',
            'confirm_password': '123456',
        }

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def testUserCanRegister(self):
        # arrange
        register_page = RegisterPage(browser=self.driver)

        # act
        dashboard_page = register_page.register(input_data=self.user_data)
        dashboard_page.wait_for_presence_of_all_elements_located(
            locator=AccountDashboardPage.REGISTRATION_MESSAGE_BOX
        )

        # assert
        self.assertTrue(
            dashboard_page.registration_message_box.text ==
            RegisterPage.StaticData.REGISTER_SUCCESS
        )

    def testCannotRegisterWithUsedEmail(self):
        # arrange
        user_data_with_used_email = copy.deepcopy(self.user_data)
        user_data_with_used_email['email'] = self.used_email

        register_page = RegisterPage(browser=self.driver)

        # act
        register_page.register(input_data=user_data_with_used_email)

        # assert
        self.assertTrue(register_page.is_error())

        self.assertTrue(
            register_page.register_error_message_box.text ==
            RegisterPage.StaticData.REGISTER_ERROR_WITH_EMAIL
        )

    def testUserCanLogin(self):
        # arrange
        login_page = LoginPage(browser=self.driver)

        # act
        dashboard_page = login_page.login(self.used_email, self.used_password)

        # assert
        self.assertTrue(
            self.user_data["first_name"] in dashboard_page.hello_text
            and
            self.user_data["last_name"] in dashboard_page.hello_text
        )


class TestSearchFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def testCanSearchItemInWomenTopsAndBlouses(self):
        # arrange
        home_page = HomePage(browser=self.driver)

        # act
        women_tops_and_blouses_page = home_page.navigate_to_women_tops_and_blouses()
        women_tops_and_blouses_page.choose_pink_color()

        # assert
        self.assertTrue(women_tops_and_blouses_page.is_results())

    def testCanSearchMenShirtWithSearchBar(self):
        # arrange
        home_page = HomePage(browser=self.driver)

        # act
        search_results_page = home_page.search('red shirt')
        search_results_page.choose_men_category()

        # assert
        self.assertTrue(search_results_page.is_red_shirt_present())

    def testCannotSearchEyewear(self):
        # arrange
        home_page = HomePage(browser=self.driver)

        # act
        eyewear_page = home_page.navigate_to_accessories_eyewear()

        # assert
        self.assertFalse(eyewear_page.is_items())


class TestAccountSettingsFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = {
            'email': 'bamij44058@invodua.com',
            'password': '123456'
        }
        cls.address_data = {
            'telephone': '+380123456789',
            'street_address': 'Stepana Bandery St, 12',
            'city': 'Lviv',
            'country': 'Ukraine',
            'zip': '79000'
        }

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def testCanEditAddressBook(self):
        # arrange
        login_page = LoginPage(browser=self.driver)
        dashboard_page = login_page.login(*self.user.values())

        # act
        dashboard_page.edit_address_book(input_data=self.address_data)

        # assert
        self.assertTrue(self.address_data.get('telephone') in dashboard_page.get_default_address())


if __name__ == '__main__':
    unittest.main()

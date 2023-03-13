import pytest
import config
from selenium import webdriver
from TestEnter.pom.enterFixture import EnterVFixture
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    # options.add_argument('--auto-open-devtools-for-tabs')
    options.add_argument('--ash-host-window-bounds=1920x1080')
    options.add_argument('--ignore-certificate-errors')  # игнорировать ошибку сертификата
    options.add_argument('--ignore-ssl-errors')  # игнорировать ошибку ssl
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    PATH = Service(r"C:\chromedriver.exe")
    driver = webdriver.Chrome(service=PATH, options=options)
    return driver


@pytest.fixture(params=config.urls)
def url(request):
    return request.param


@pytest.fixture(scope='function')
def setup(request, get_webdriver, url):
    driver = get_webdriver
    url = url
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield
    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture(scope='function')
def enterFixture():
    return EnterVFixture

from pytest import fixture
from selenium import webdriver
from resources.constants import *
from config import Config


# @fixture(scope='session')
@fixture()
def chrome_browser():
    """
    # By default Scope is Function:
    :return:
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(DRIVER.CHROME_PATH, chrome_options=options)
    yield driver

    # Teardown code:
    driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Environment to run tests"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


@fixture(scope='session')
def main_url(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    if port:
        url = f'{base_url}:{port}{URL.PATH}'
    else:
        url = f'{base_url}'
    return url


@fixture(scope='function')  # Default scope
def some_func():
    pass


@fixture(scope='class')
def some_func():
    pass


# To run all tests in a session
@fixture(scope='session')
def some_other_func():
    pass

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Choose browser: chrome or firefox",
    )
    parser.addoption(
        "--language",
        action="store",
        default=None,
        help="Choose language: es or fr",
    )


@pytest.fixture(scope="function")
def browser(request):
    language_names = [
        "ar",
        "ca",
        "cs",
        "da",
        "de",
        "en",
        "en-gb",
        "el",
        "es",
        "fi",
        "fr",
        "it",
        "ko",
        "nl",
        "pl",
        "pt",
        "pt-br",
        "ro",
        "ru",
        "sk",
        "uk",
        "zh-hans",
    ]
    browser_name = request.config.getoption("browser_name")
    language_name = request.config.getoption("language")
    browser = None
    if language_name in language_names:
        if browser_name == "chrome":
            from selenium.webdriver.chrome.options import Options

            options = Options()
            options.add_experimental_option(
                "prefs", {"intl.accept_languages": language_name}
            )
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            from selenium.webdriver.firefox.options import Options

            options = Options()
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language_name)
            options.profile = fp
            print("\nstart chrome browser for test..")
            browser = webdriver.Firefox(options=options)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        yield browser
        print("\nquit browser..")
        browser.quit()
    else:
        raise pytest.UsageError("--language should be es or fr")

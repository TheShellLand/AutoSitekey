from automon.log import logger

from autositekey.client import AutoSiteKeyClient
from autositekey.hotkey import WellfoundHK
from autositekey.hotkey import ZipRecruiterHK

log = logger.logging.getLogger(__name__)
log.setLevel(logger.DEBUG)


def main():
    client = AutoSiteKeyClient()
    client.run(headless=False)

    client.get('https://google.com')

    finished = False
    while not finished:

        if finished:
            break

        client.browser.add_cookie_from_current_url()
        client.browser.save_cookies_for_current_url()
        client.browser.refresh()

    client.browser.quit()


if __name__ == "__main__":
    main()

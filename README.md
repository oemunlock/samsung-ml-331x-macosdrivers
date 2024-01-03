# CleanBrowserForPentesting

A minimalist script for using an interactive browser instance to perform pentesting.

## Requirements
Needs selenium and webdriver-manager

On Linux and Mac machines the following lines worked:
```
python3 -m pip install selenium
python3 -m pip install webdriver-manager


```

This code used to use geckdriver-autoinstaller and chromedriver-autoinstaller. Selenium finally has APIs to get the latest webdrivers. I've also updated the scripts to use the proper APIs for the proxy server

## Description
Often times during a pentest, you'd like to use your favorite browser for researching things, but want to have another browser session open that is proxied through Burp. This project solves that issue. First launch your browser of choice (Chrome/Firefox), then run one of the scripts here. This will create an selenium controlled browser session that is "clean" without extensions or cookie values that might influence your pentesting session. In MacOS, it should appear as another browser icon in the dock. 

If you use Firefox, the address bar will appear orange.

<img src="https://github.com/oemunlock/CleanBrowserForPentesting/raw/master/images/firefox_on_windows.png" />

If you use Chrome, a small dialog box appears at the bottom of the address bar.

<img src="https://github.com/oemunlock/CleanBrowserForPentesting/raw/master/images/chrome_on_windows.png" />

The script remains in a python code repl shell in case you want to use other features like Selenium's screenshot capabilties or some other automation (such as login or recreating a usecase).

## Limitations
There are some websites and services that will detect usage of Selenium through the Javascript variables. I've found pentests are generally performed on development enviornments, but YMMV.

## Troubleshooting
Sometimes the autoinstaller fails, so you may need to manually download the binaries and add them to your path.

Geckodriver: https://github.com/mozilla/geckodriver/releases 
Chromedriver: https://sites.google.com/chromium.org/driver/

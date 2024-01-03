#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager
import traceback

# Documented in the Selenium documentation 
# https://www.selenium.dev/documentation/webdriver/drivers/options/#proxy

PROXY="127.0.0.1:8080"
caps = webdriver.DesiredCapabilities.CHROME
caps['proxy'] = {
         'proxyType': "manual",
         'httpProxy': PROXY,
         'sslProxy': PROXY,
}

try:
        ChromeDriverManager().install()
except Exception as e:
        traceback.print_exc()
        print("[-] Error updating chromedriver. Consider manual installation.")
        print (e)

driver = webdriver.Chrome()

def interact(driver):
	try:
                import os
                import code
                vars = globals()
                vars.update(locals())
                if os.name != 'nt':
                        import readline
                        import rlcompleter
                        readline.set_completer(rlcompleter.Completer(vars).complete)
                        readline.parse_and_bind("tab: complete")
                shell = code.InteractiveConsole(vars)
                shell.interact()
	except:
                traceback.print_exc()
                print("[-] Error with python repl!")
	finally:
                print("[+] Done with python repl")
                driver.quit()
	

print("[.] Any final debugging?")
interact(driver)

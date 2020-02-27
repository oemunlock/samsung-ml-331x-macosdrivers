#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui

def interact(driver):
	try:
		import code
		import readline
		import rlcompleter
		vars = globals()
		vars.update(locals())
		readline.set_completer(rlcompleter.Completer(vars).complete)
		readline.parse_and_bind("tab: complete")
		shell = code.InteractiveConsole(vars)
		shell.interact()
	except:
		print "[-] Error with python repl!"
	finally:
		print "[+] Done with python repl"
		driver.quit()


PROXY="127.0.0.1:8080"
caps = webdriver.DesiredCapabilities.FIREFOX
caps['proxy'] = {
         'proxyType': "manual",
         'httpProxy': PROXY,
         'ftpProxy': PROXY,
         'sslProxy': PROXY,
         }
driver = webdriver.Firefox(capabilities=caps)


print "[.] Any final debugging?"
interact(driver)

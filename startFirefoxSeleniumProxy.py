#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy
import os 
import geckodriver_autoinstaller

def interact(driver):
	try:
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
		print("[-] Error with python repl!")
	finally:
		print("[+] Done with python repl")
		driver.quit()
try:
	geckodriver_autoinstaller.install()
except Exception as e:
	print("[-] Error updating geckodriver. Consider manual installation.")
	print (e)
	
PROXY="127.0.0.1:8080"
caps = webdriver.DesiredCapabilities.FIREFOX
caps['proxy'] = {
         'proxyType': "manual",
         'httpProxy': PROXY,
         'ftpProxy': PROXY,
         'sslProxy': PROXY,
         }
driver = webdriver.Firefox(capabilities=caps)


print("[.] Any final debugging?")
interact(driver)

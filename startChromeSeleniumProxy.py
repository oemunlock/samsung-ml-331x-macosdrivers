#!/usr/bin/python

from selenium import webdriver

def give_me_a_shell(driver):
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
		print "[-] No shell for you!"
	finally:
		print "[+] Peace out"
		driver.quit()

PROXY = "127.0.0.1:8080" # IP:PORT or HOST:PORT
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(chrome_options=chrome_options)

print "[.] Any final debugging?"
give_me_a_shell(driver)

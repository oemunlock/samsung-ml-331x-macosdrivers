#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.proxy import Proxy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
import getpass, os, time, sys
import datetime, getopt


def debug_repl(driver):
	try:
		import code
		vars = globals()
		vars.update(locals())
		if os.name == 'posix':
			import readline
			import rlcompleter
			readline.set_completer(rlcompleter.Completer(vars).complete)
			readline.parse_and_bind("tab: complete")
		else:
			print("[-] Windows Hack to remove readline")
		shell = code.InteractiveConsole(vars)
		shell.interact()
	except:
		print("[-] Error with python repl!")
	finally:
		print("[+] Done with python repl")
		driver.quit()

def wait_for_xpath_then_click(driver, xpath):
	try:
		element = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.XPATH, xpath))
		)
	except:
		print("[-] wait_for_text time out: element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '" + xpath + "'))")
		debug_repl(driver)
	try:
		driver.find_element_by_xpath(xpath).click()
	except:
		print("[-] Time out: driver.find_element_by_xpath(" + xpath + ").click()")
		debug_repl(driver)


def wait_for_id_then_click(driver, id):
	try:
		element = WebDriverWait(driver, 30).until(
			EC.presence_of_element_located((By.ID, id))
		)
	except:
		print("[-] wait_for_text time out: element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, '" + id + "'))")
		debug_repl(driver)
	try:
		driver.find_element_by_id(id).click()
	except:
		print("[-] Time out: driver.find_element_by_id(" + id + ").click()")
		debug_repl(driver)

def save_screenshot(driver):
	filename = datetime.datetime.now().strftime("%m%d%Y%H.%M.%S")+".png"
	print("[+] Saving file: %s" % filename)
	driver.save_screenshot(filename)


def main():
	try:
		argv = sys.argv[1:]
		caps = None
		chrome_options = None
		random_password = "RandomPasswordGoesHere"
		browser = "firefox"
		opts, remainder = getopt.getopt(argv, ":pcf", ['proxy', 'chrome', 'firefox']) 

		for opt, arg in opts:
			if opt in ('-p', '--proxy'):
				print("[+] Proxy Being Used")
				PROXY = "127.0.0.1:8080" # IP:PORT or HOST:PORT		

			caps = webdriver.DesiredCapabilities.FIREFOX
			caps['proxy'] = {
				'proxyType': "manual",
				'httpProxy': PROXY,
				'ftpProxy': PROXY,
				'sslProxy': PROXY,
			}
			chrome_options = webdriver.ChromeOptions()
			chrome_options.add_argument('--proxy-server=%s' % PROXY)
			if opt in ('-c', '--chrome'):
				browser = "chrome"
	except:
		print("Usage: %s [-p | --proxy] [-f | --firefox ] [ -c | --chrome ]\n" % sys.argv[0])
		sys.exit()

	if (browser == "chrome"):
		print("[+] Launching Chrome")
		driver = webdriver.Chrome(options=chrome_options)
	else:
		print("[+] Launching Firefox")
		driver = webdriver.Firefox(capabilities=caps)


	try:
		driver.get("https://www.sharklasers.com/")
		wait_for_xpath_then_click(driver, "/html/body/div[3]/div/div[2]/div/span[1]/select/option[4]")
		email = driver.find_element_by_id("inbox-id").text + "@guerrillamail.com"
		print("[+] Email: %s "	 % email )
	except:
		print("[-] Error Getting Shark Lasers email")
		debug_repl(driver)

	try:
		driver.execute_script("window.open('about:blank', '_blank');")
		driver.switch_to.window(driver.window_handles[1])
		print("[+] Switching to new tab: %s" % driver.title)
		driver.get("https://profile.oracle.com/myprofile/account/create-account.jspx")
	except:
		print("[-] Error trying to create account")
		debug_repl(driver)


	try:
		print("[+] Waiting for email entry field: %s" % driver.title)	
		wait_for_id_then_click(driver, "email::content")
		print("[+] Entering User Data:")
		driver.find_element_by_id("email::content").send_keys(email)
		driver.find_element_by_id("password::content").send_keys(random_password)
		driver.find_element_by_id("retypePassword::content").send_keys(random_password)
		driver.find_element_by_id("firstName::content").send_keys("Darren")
		driver.find_element_by_id("lastName::content").send_keys("Shu")
		driver.find_element_by_id("jobTitle::content").send_keys("Pentest Hacker")
		driver.find_element_by_id("workPhone::content").send_keys("877-825-8522")

		driver.find_element_by_id("companyName::content").send_keys("Cisco Systems")

		driver.find_element_by_id("address1::content").send_keys("433 W Van Buren St")
		driver.find_element_by_id("city::content").send_keys("Chicago")
		driver.find_element_by_xpath("//select[@id='state::content']/option[text()='Illinois']").click()
		driver.find_element_by_id("postalCode::content").send_keys("60607")

		print("[-] TODO: This is where the click submit button would happen")
		
		driver.switch_to.window(driver.window_handles[0])
		time.sleep(1)

	except:
		print("[-] Error Getting Shark Lasers email")
		debug_repl(driver)

	print("[+] Done with script!")
	debug_repl(driver)

if __name__ == "__main__":
	main()


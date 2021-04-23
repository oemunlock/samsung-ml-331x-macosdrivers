Often times during a pentest, you'd like to use your favorite browser for researching things, but want to have another browser session open that is proxied through Burp. This project solves that issue. First launch your browser of choice (Chrome/Firefox), then run one of the scripts here. This will create an selenium controlled browser session that is "clean" without extensions or cookie values that might influence your pentesting session. In MacOS, it should appear as another browser icon in the dock. 

If you use Firefox, the address bar will appear orange.

The script remains in a code repl shell in case you want to use other features like Selenium's screenshot capabilties or some other automation (such as login or recreating a usecase).

Requires selenium (pip install selenium) and python3. 

Geckodriver (https://github.com/mozilla/geckodriver/releases) and Chromedriver (https://sites.google.com/chromium.org/driver/) will also need to be installed. This would need to be added to your path.


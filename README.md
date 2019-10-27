Often times during a pentest, you'd like to use your favorite browser for researching things, but want to have another browser session open that is proxied through Burp. This project solves that issue. First launch your browser of choice (Chrome/Firefox), then run one of the scripts here. This will create an selenium controlled browser session that is "clean" without extensions or cookie values that might influence your pentesting session. In MacOS, it appears as another browser icon in the dock. In Windows, the script will create another grouping in the taskbar. 

The script remains in a code repl shell in case you want to use other features like Selenium's screenshot capabilties.

Requires selenium and python

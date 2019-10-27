Often times during a pentest, you'd like to use your favorite browser for researching things, but want to have another browser session open that is proxied through Burp. This project solves that issue. First launch your browser of choice (Chrome/Firefox), then run one of the scripts here. This will create an selenium controlled browser session that is "clean" without extensions or cookie values that might influence your pentesting session. In MacOS, it should appear as another browser icon in the dock. 

The script remains in a code repl shell in case you want to use other features like Selenium's screenshot capabilties or some other automation (such as login or recreating a usecase).

Requires selenium and python. You may need to remove the python lines for readline if you are using this on Windows.

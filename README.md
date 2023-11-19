# samsung-ml-331x-macosdrivers
These drivers are confirmed to work on MacOS Sonoma 14.1.1 (23B81) for the ML-331x using a Macbook Pro 16" 2019 (Intel based machine). I wasn't able to find these on the (now) HP website.
At the time of this writing (Nov 2023), the support website only listed this: https://support.hp.com/us-en/drivers/samsung-ml-3310-laser-printer-series/17156823 which no longer distributes the driver files.

To install:
1) Ensure the Printer & Scanners window is closed. 

2) Move the Samsung directory into /Library/Printers
and the PPDs files need to be put in /Library/Printers/PPDs/Contents/Resources

In this repo, these directories are in the respective directories intended to be on your mac.

3) After placing the files in those directories, Click Add Printer. I was able to add my printer using Bonjour and by IP using IPP. The driver was automatically selected to be the Samsung ML-331x Series. 

Use at your own risk!

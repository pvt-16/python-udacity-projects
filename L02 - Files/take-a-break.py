import time
import webbrowser
import smtplib

total_breaks=3
count_breaks=0

while count_breaks< total_breaks:
    time.sleep(10)
    webbrowser.open("https://youtube.com")
    count_breaks= count_breaks+1
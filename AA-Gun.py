import pyautogui
import time
import webbrowser
import os
import subprocess


def firstServerKill():
   time.sleep(3)
   url = "https://www.roblox.com/games/286090429/Arsenal?refPageId=d8e19964-0d2b-46ef-9478-1fcef82e13c9"
   webbrowser.open_new_tab(url)
   time.sleep(5)
   pyautogui.moveTo(904, 490, 2)
   time.sleep(3); pyautogui.click()
   time.sleep(50)
   subprocess.call(["taskkill","/F","/IM","RobloxPlayerBeta.exe"])
   time.sleep(5)
   print("First Server Killed!")

firstServerKill()

count = 0

while True:
   time.sleep(10)
   pyautogui.moveTo(904, 490, 2)
   time.sleep(3); pyautogui.click()
   time.sleep(50)
   try:
      subprocess.check_output(["taskkill","/F","/IM","RobloxPlayerBeta.exe"])

   except subprocess.CalledProcessError as e:
      if e.returncode == 128:
         subprocess.call(["taskkill","/F","/IM","msedge.exe"])
         time.sleep(3)
         url = "https://www.roblox.com/games/286090429/Arsenal?refPageId=d8e19964-0d2b-46ef-9478-1fcef82e13c9"
         webbrowser.open_new_tab(url)
         time.sleep(10)
         pyautogui.moveTo(904, 490, 2)
         time.sleep(3); pyautogui.click()
         time.sleep(60)
         subprocess.call(["taskkill","/F","/IM","RobloxPlayerBeta.exe"])
         time.sleep(5)
         print("Server has been killed!")
         print("With An Error That Was Also Handled")
         count +=1
         print(count)

   count +=1
   print(count)



# Desktop Screenshot Cleaner
This code will scan the desktop from screenshots and then move them into a folder that will sort the screenshots based off the year and month they were taken.
<!-- screenshot of ss directory -->
<p align="center">
  <img width="916" alt="Screen Shot 2024-03-29 at 8 37 14 PM" src="https://github.com/jplip/Desktop_Screenshot_Cleaner/assets/142539012/01da2341-c948-40a8-a590-2fb0a79b2574">
</p>
<br>
This process however will not happen if the screenshot was renamed. This code was also made with mac os in mind and not tested with window or any other operating system. 

## Folders
This code runs without any need to make folders yourself. You can simply run the code and the folders will be made if there isn't already a folder to place the screenshots.
<br>
<!-- code running with no files in vscode terminal -->
<p align="center">
  <img width="492" alt="Screen Shot 2024-03-29 at 8 59 34 PM" src="https://github.com/jplip/Desktop_Screenshot_Cleaner/assets/142539012/3eabb892-7c08-4f30-bb2d-cc0b90248f0e">
</p>

## Run from terminal
This code can run from the terminal as well if you only want to download the cleaner.py file instead of the whole repository. Here are some examples of how to run the code in certain locations.
<p align="center">
  <img width="388" alt="Screen Shot 2024-03-30 at 12 35 01 AM" src="https://github.com/jplip/Desktop_Screenshot_Cleaner/assets/142539012/68922cbb-6c1f-4917-8a8c-ec6c111b65e2">
</p>

Home
```bash
python cleaner.py
```
<br>

Desktop
```bash
cd desktop
python cleaner.py
```

Repository
```bash
# replace 'justin' with your user
cd /Users/justin/vscode/Desktop_Screenshot_Cleaner
python cleaner.py
```

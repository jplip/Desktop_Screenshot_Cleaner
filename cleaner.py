import shutil
import os

#change 'justin' to desired user on computer
screenshot_dir = '/Users/justin/Desktop/ss' #'ss' for screenshots folder
desktop_dir = '/Users/justin/Desktop'

months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', 
          '06': 'June', '07': 'July', '08': 'August', '09': 'September','10': 'October', 
          '11': 'November', '12': 'December'}

# creates folder if it doesn't exist already
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)
    print('Created folder ...')

# checks for screenshots specifically
files_ond_desktop = os.listdir(desktop_dir)
for file in files_ond_desktop:
    if file.startswith('Screen Shot') and file.endswith('.png'):
        file_path = desktop_dir + '/' + file
        file_year = file[12:16]
        # Create year directory if it doesn't exist
        year_dir = screenshot_dir + '/' + file_year
        if not os.path.exists(year_dir):
            os.makedirs(year_dir)
            print(f'Created folder: {year_dir}')
        
        # Extract month from the filename
        file_month = file[17:19]
        # Create month directory within the year directory
        month_dir = year_dir + '/' + months[file_month]
        if not os.path.exists(month_dir):
            os.makedirs(month_dir)
            print(f'Created folder: {month_dir}')
        
        shutil.move(file_path, month_dir)
        print(f'Moved {file} to \n{month_dir}...')

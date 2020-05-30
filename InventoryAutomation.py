import pandas as pd
import seaborn as sns
import pyautogui
import time
#%matplotlib inline

employee_df = pd.read_csv('Beacon Test Two Take Two.csv')
transposed_employee_df = employee_df.transpose()

list_of_forms = []

for x in transposed_employee_df:
    list_of_forms.append(transposed_employee_df[x])


asset_type = ['Computer','Monitor1','Monitor2']

'''
for x in list_of_forms:
    for y in asset_type:
        newest_name = x['Name']
        first,last = newest_name.split()
        #will go through each asset type while maintaing first,last for each employee
        if x[y] in checked_out_list and != 'nan': #this list has to be pre-made
            pass
            #pyautogui commands to check out the item with gpu commands created already
        else:
            pass
            #pyautogui commands to check in, then check out item
'''

for x in list_of_forms:
    for y in asset_type:
        newest_name = x['Name']
        first,last = newest_name.split()
        print(first,last)
        print(x[y])
    # this shows above will work

checked_out_df = pd.read_csv('new checked out inv.csv')
checked_out_list = checked_out_df['Asset Tag'].tolist()


#THIS WORKS PERFECTLY
for x in list_of_forms:
    for y in asset_type:
        newest_name = x['Name']
        first,last = newest_name.split()
        #will go through each asset type while maintaing first,last for each employee
        if x[y] in checked_out_list: 
            pyautogui.moveTo(896,404, duration=1.0)
            pyautogui.click()
            time.sleep(15)
            pyautogui.moveTo(196,214, duration=1.0)
            pyautogui.click()
            time.sleep(3)
            pyautogui.typewrite(x[y], interval = .2)
            pyautogui.press('return')
            time.sleep(3)
            pyautogui.moveTo(381,397, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(958,408, duration=1.0)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(1825,997, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1818,1060, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1746,1094, duration=1.0)
            pyautogui.click()
            time.sleep(3)
            pyautogui.moveTo(1665,98, duration=1.0)
            pyautogui.click()
            #pyautogui commands to check out the item with gpu commands created already
            pyautogui.moveTo(945,1170, duration=1.0)
            time.sleep(1)
             #THIS LINE WILL CHANGE WITH HOW MANY APPS ARE OPEN(CHANGES LOCATION OF ICONS BY MAKING THEM SMALLER)
            pyautogui.moveTo(900,353, duration=1.0) #THIS LINE WILL CHANGE WITH HOW MANY APPS ARE OPEN(CHANGES LOCATION OF ICONS BY MAKING THEM SMALLER)
            pyautogui.click()
            time.sleep(15)
            pyautogui.moveTo(203,204, duration=1.0)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite(x[y], interval=.2)
            pyautogui.press('return')
            time.sleep(3)
            pyautogui.moveTo(1017,218, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1824,202, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1829,405, duration=1.0)
            pyautogui.click()
            pyautogui.click()
            pyautogui.moveTo(1398,401, duration=1.0)
            pyautogui.click()
            time.sleep(10)
            pyautogui.moveTo(543,391, duration=1.0)
            pyautogui.click()

        #for x in employee_df['Name']:  #MAKE THE LOOP AT THE BEGINNING

            pyautogui.moveTo(1046,535, duration=1.0)
            pyautogui.click()
            pyautogui.typewrite(last, interval=.5)
            time.sleep(2)
            pyautogui.moveTo(1045,565, duration=1.0)
            pyautogui.click()
            pyautogui.typewrite(first, interval=.5)
            time.sleep(2)
            pyautogui.moveTo(1050,745, duration=1.0)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(570,475, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1274,844, duration=1.0)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo(1826,243, duration=.5)
            pyautogui.click()
            if x['Location'] == 'Home':
                pyautogui.moveTo(1816,285, duration=.5)
                pyautogui.click()
            else:
                pyautogui.moveTo(1817,265, duration=.5)
                pyautogui.click()
            #sets due date to none
            pyautogui.moveTo(1027,328, duration=1.0)
            pyautogui.click()
            time.sleep(5)
            #checks out item
            pyautogui.moveTo(1752,1092, duration=1.0)
            pyautogui.click()
            time.sleep(5)
            #returns to home(check in check out)
            pyautogui.moveTo(1665,98, duration=1.0)
            pyautogui.click()
            
        else:
            pyautogui.moveTo(945,1170, duration=1.0)
            time.sleep(1)
            pyautogui.moveTo(900,353, duration=1.0) #THIS LINE WILL CHANGE WITH HOW MANY APPS ARE OPEN(CHANGES LOCATION OF ICONS BY MAKING THEM SMALLER)
            pyautogui.click()
            time.sleep(15)
            pyautogui.moveTo(203,204, duration=1.0)
            pyautogui.click()
            time.sleep(1)
            pyautogui.typewrite(x[y], interval=.2)
            pyautogui.press('return')
            time.sleep(3)
            pyautogui.moveTo(1017,218, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1824,202, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1829,405, duration=1.0)
            pyautogui.click()
            pyautogui.click()
            pyautogui.moveTo(1398,401, duration=1.0)
            pyautogui.click()
            time.sleep(10)
            pyautogui.moveTo(543,391, duration=1.0)
            pyautogui.click()

        #for x in employee_df['Name']:  #MAKE THE LOOP AT THE BEGINNING

            pyautogui.moveTo(1046,535, duration=1.0)
            pyautogui.click()
            pyautogui.typewrite(last, interval=.5)
            time.sleep(2)
            pyautogui.moveTo(1045,565, duration=1.0)
            pyautogui.click()
            pyautogui.typewrite(first, interval=.5)
            time.sleep(2)
            pyautogui.moveTo(1050,745, duration=1.0)
            pyautogui.click()
            time.sleep(2)
            pyautogui.moveTo(570,475, duration=1.0)
            pyautogui.click()
            pyautogui.moveTo(1274,844, duration=1.0)
            pyautogui.click()
            time.sleep(5)
            pyautogui.moveTo(1826,243, duration=.5)
            pyautogui.click()
            if x['Location'] == 'Home':
                pyautogui.moveTo(1816,285, duration=.5)
                pyautogui.click()
            else:
                pyautogui.moveTo(1817,265, duration=.5)
                pyautogui.click()
            #sets due date to none
            pyautogui.moveTo(1027,328, duration=1.0)
            pyautogui.click()
            time.sleep(5)
            #checks out item
            pyautogui.moveTo(1752,1092, duration=1.0)
            pyautogui.click()
            time.sleep(5)
            #returns to home(check in check out)
            pyautogui.moveTo(1665,98, duration=1.0)
            pyautogui.click()
            #pyautogui commands to check in, then check out item
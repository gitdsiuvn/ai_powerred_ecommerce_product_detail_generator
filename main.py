
import os
import time
import pyautogui
import pyperclip
import json
import random

time.sleep(5)

#prompt to generate the content
promptt = "write a product description for the uploaded image for ecommerce platforms. Make it seo friendly and selling. Also suggest a good price to sell it in india. make it in json. Properties to mention in json: name, sku, length in cm, breadth in cm, height in cm, weight in grams, description, short description, price in INR. do not write units for length, breath, height, weight and price. Exact attribute names to use: name, sku, length, breadth, height, weight, description, short_description, price"

#replace this file name and directory with local directory, this ensures there is no repeated implementation for the same products
file_name_done = "C:/Users/dr275/OneDrive/Desktop/wwg_ap/files/doneproduct.txt"
f = open(file_name_done, "r", encoding='utf8')
strcontent = f.read()


done_file_array = strcontent.split("; ")
print("done_file_array : ", done_file_array)
f.close()

# replace with the folder containing images of all products.
directoryy = "C:/Users/dr275/OneDrive/Desktop/designs and videos/bestservicependrive/co2 desgins/co2 desgin/"
foldernamelist = os.listdir(directoryy)

for foldername in foldernamelist:
    # incase there are subfolders then os.listdir needs to be called heirerchially
    filenamelist = os.listdir(directoryy + foldername + "/jpg/")
    print("FOLDER : ", foldername)
    for file_name_text in filenamelist:
        print("FILE NAME : ", file_name_text)
        try:
            fname = directoryy + foldername + "/jpg/" + file_name_text
            #checks if the file is not already done. 
            if fname not in done_file_array:
                print("doing this file")
                try:
                    location = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/clip.png', confidence=0.9)
                    clip_center_location_x = location.left + location.width / 2
                    clip_center_location_y = location.top + location.height / 2
                    pyautogui.moveTo(clip_center_location_x, clip_center_location_y)
                    pyautogui.click()
                    time.sleep(1)
                except:
                    print("clip not found")

                try:
                    location = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/upload.png', confidence=0.9)
                    clip_center_location_x = location.left + location.width / 2
                    clip_center_location_y = location.top + location.height / 2
                    pyautogui.moveTo(clip_center_location_x, clip_center_location_y)
                    pyautogui.click()
                    time.sleep(1)
                except:
                    print("upload not found")

                try:
                    location3 = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/navdialogicon.png', confidence=0.8)
                    navdialog_center_location_x = location3.left + location3.width / 2
                    navdialog_center_location_y = location3.top + location3.height / 2
                    pyautogui.moveTo(navdialog_center_location_x + 1200, navdialog_center_location_y)
                    pyautogui.click()
                    time.sleep(0.2)
                    file_dir_text = directoryy + foldername +"/jpg/"
                    pyautogui.write(file_dir_text, interval=0.01)
                    time.sleep(0.2)
                    pyautogui.press('enter')
                    time.sleep(1)
                except:
                    print("unable to find nav dialog")


                try:
                    location3 = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/filenametext.png', confidence=0.9)
                    filename_center_location_x = location3.left + location3.width / 2
                    filename_center_location_y = location3.top + location3.height / 2
                    pyautogui.moveTo(filename_center_location_x + 800, filename_center_location_y)
                    pyautogui.click()
                    time.sleep(0.2)
                    print(file_name_text)
                    pyautogui.write(file_name_text, interval=0.02)
                    time.sleep(1)
                except:
                    print("unable to find filename!")

                try:
                    location3 = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/openindialog.png', confidence=0.9)
                    open_center_location_x = location3.left + location3.width / 2
                    open_center_location_y = location3.top + location3.height / 2
                    pyautogui.moveTo(open_center_location_x , open_center_location_y)
                    pyautogui.click()
                except:
                    print("unable to find open in dialog!")

                try:
                    time.sleep(4)
                    pyautogui.moveTo(clip_center_location_x + 200, clip_center_location_y)
                    pyautogui.click()
                    time.sleep(0.5)
                    pyautogui.write(promptt, interval=0.09)
                    time.sleep(2)
                except:
                    print("ss")
                try:
                    location3 = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/go.png', confidence=0.9)
                    go_center_location_x = location3.left + location3.width / 2
                    go_center_location_y = location3.top + location3.height / 2
                    pyautogui.moveTo(go_center_location_x, go_center_location_y)
                    pyautogui.click()
                except:
                    print("unable to go!")
                time.sleep(70)

                try:
                    location3 = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/godown.png', confidence=0.9)
                    copyjson_center_location_x = location3.left + location3.width / 2
                    copyjson_center_location_y = location3.top + location3.height / 2
                    pyautogui.moveTo(copyjson_center_location_x, copyjson_center_location_y)
                    pyautogui.click()
                    time.sleep(4)
                except:
                    print("no button for go down!")

                try:
                    location3 = pyautogui.locateOnScreen('C:/Users/dr275/automation_files/chatgpt/copyjson.png', confidence=0.8)
                    copyjson_center_location_x = location3.left + location3.width / 2
                    copyjson_center_location_y = location3.top + location3.height / 2
                    pyautogui.moveTo(copyjson_center_location_x, copyjson_center_location_y)
                    pyautogui.click()
                except:
                    print("unable to copy json!")

                try:
                    prod_json = json.loads(pyperclip.paste())
                    prod_json["__IMAGE_FILE_LOCATION__"] = directoryy + foldername + "/jpg/" + file_name_text
                    prod_json["__TO__PUBLISH__"] = True
                    prod_json["sku"] = str(prod_json["sku"]) + str(random.randrange(100, 200))
                    prod_json["__NAME__"] =  prod_json["title"]
                    prod_json = str(prod_json)
                    prod_json.replace("'","\'")
                    print("prod_json : ", prod_json)
                except Exception as e:
                    print("prod_json exception", e)

                time.sleep(random.randrange(35, 62))
                try:
                    file_name_chatgpt = "C:/Users/dr275/OneDrive/Desktop/wwg_ap/files/chatgpt_product_scraper.txt"
                    f = open(file_name_chatgpt, "a", encoding='utf8')
                    stroutput = str(prod_json) + ', '
                    f.write(stroutput)
                    f.close()
                    time.sleep(random.randrange(8, 22))
                    file_name_done = "C:/Users/dr275/OneDrive/Desktop/wwg_ap/files/doneproduct.txt"
                    f = open(file_name_done, "a", encoding='utf8')
                    stroutput = directoryy + foldername  + "/jpg/" + file_name_text+ "; "
                    f.write(stroutput)
                    f.close()

                except Exception as e:
                    print("file write exception ", e)

        except Exception as ee:

            print("Exception", ee)

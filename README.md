# Univ. of Macau - Computer Network Project
I prefer nodeJS

## Environment
Python 3.7

## Server (How To) 
in Terminal  
1. ``` cd py-chat && cd server ```
2. ``` python server.py``` 
(For closing just kill the process directly)

## Client (How To)
in Terminal  
1. ``` cd py-chat && cd client ```
2. ``` python client.py```
2. Enter your user name (example : eddy)  
 Change Host and Port number if you have to
3. Press continue  
( To leave, just close the GUI or type `{quit}` )
4. Type and press enter or the Send button to send message
5. Press File to select a file to send (10 MB is the max size)

## Reference
(2021/1/6) https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/  
(2021/1/8) https://stackoverflow.com/questions/43107577/python-os-check-if-file-exists-if-so-rename-check-again-then-save  


## TODOS
- [x] Handles client receiving file contents
- [x] Make clients stores the previous file name shared by others until finish transaction
- [ ] ISSUE : collision of file name on client side when share at the same time
- [x] ISSUE : self.recv_file_name not set (by sleeping server for 0.1 s)
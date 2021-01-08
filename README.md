# Univ. of Macau - Computer Network Project
I prefer nodeJS

## Environment
Python 3.7

## Server (How To) 
1. Go to server folder run ```chat_sample.py```

## Client (How To)
1. Go to client folder run ```chat_client.py```
2. Enter your user name (example : eddy)  
 Change Host and Port number if you have to
3. Press continue

## Reference
(2021/1/6) https://www.geeksforgeeks.org/gui-chat-application-using-tkinter-in-python/
(2021/1/8) https://stackoverflow.com/questions/43107577/python-os-check-if-file-exists-if-so-rename-check-again-then-save


## TODOS
[-] Handles client receiving file contents
[-] Make clients stores the previous file name shared by others until finish transaction
[] ISSUE : collision of file name on client side when share at the same time
[-] ISSUE : self.recv_file_name not set (by sleeping server for 0.5 s)
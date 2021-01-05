#!/usr/bin/env python3
"""Script for Tkinter GUI chat client."""
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from tkinter import font
from tkinter import ttk

BUFSIZ = 1024

class GUI:
	def receive(self):
		"""Handles receiving of messages."""
		while True:
			try:
				msg = self.client_socket.recv(BUFSIZ).decode("utf8")
				self.textCons.config(state='normal')
				self.textCons.insert('end',
                                    msg+"\n\n")
				self.textCons.config(state='disabled')
				self.textCons.see('end')
			except OSError:  # Possibly client has left the chat.
				break

	def send(self, event=None):  # event is passed by binders.
		"""Handles sending of messages."""
		msg = self.my_msg.get()
		self.my_msg.set("")  # Clears input field.
		self.client_socket.send(bytes(msg, "utf8"))
		if msg == "{quit}":
			self.client_socket.close()
			self.Window.quit()

	def on_closing(self, event=None):
		"""This function is to be called when the window is closed."""
		if not self.HOST:
			exit()
		self.my_msg.set("{quit}")
		self.send()

	def __init__(self):
		self.Window = tkinter.Tk()
		self.Window.resizable(width=False,
								height=False)
		self.Window.configure(width=470,
								height=550,
								bg="#17202A")
		# login window
		self.login = tkinter.Toplevel()
		self.login.title("Login")
		# set the title
		# create a Label
		self.pls = tkinter.Label(self.login,
							text="Please login to continue",
							justify='center',
							font="Consolas 14 bold")

		self.pls.place(relheight=0.15,
						relx=0.2,
						rely=0.07)
		# create a Label
		self.labelName = tkinter.Label(self.login,
										text="Name: ",
										font="Consolas 12")

		self.labelName.place(relheight=0.2,
								relx=0.1,
								rely=0.2)

		# create a entry box for
		# tyoing the message
		self.entryName = tkinter.Entry(self.login,
										font="Consolas 14")

		self.entryName.place(relwidth=0.4,
								relheight=0.12,
								relx=0.35,
								rely=0.2)

		# set the focus of the curser
		self.entryName.focus()

		self.hostLabel = tkinter.Label(self.login,
										text="Host: ",
										font="Consolas 12")

		self.hostLabel.place(relheight=0.2,
								relx=0.1,
								rely=0.4)

		self.host = tkinter.Entry(self.login,
									font="Consolas 14")

		self.host.place(relwidth=0.4,
						relheight=0.12,
						relx=0.35,
						rely=0.4)

		self.portLabel = tkinter.Label(self.login,
										text="Port: ",
										font="Consolas 12")

		self.portLabel.place(relheight=0.2,
								relx=0.1,
								rely=0.6)

		self.port = tkinter.Entry(self.login,
									font="Consolas 14")

		self.port.place(relwidth=0.4,
						relheight=0.12,
						relx=0.35,
						rely=0.6)

		# create a Continue Button
		# along with action
		self.go = tkinter.Button(self.login,
							text="CONTINUE",
							font="Consolas 14 bold",
							command=lambda: self.goAhead(self.entryName.get(), self.host.get(), self.port.get()))
		self.entryName.bind("<Return>", lambda : self.goAhead(
			self.entryName.get(), self.host.get(), self.port.get()))
		self.go.place(relx=0.4,
						rely=0.8)
		self.Window.mainloop()

		

	def goAhead(self, name, host, port):
		self.login.destroy()

		self.HOST = host; self.PORT = port

		if not self.PORT:
			self.PORT = 33000
		else:
			self.PORT = int(self.PORT)

		if not self.HOST:
			self.HOST = 'localhost'


		ADDR = (self.HOST, self.PORT)

		self.client_socket = socket(AF_INET, SOCK_STREAM)
		self.client_socket.connect(ADDR)
		self.layout(name)	

		rcv = Thread(target=self.receive)
		rcv.start()
		

	def layout(self, name):
		self.Window.title("py-chat")
		self.messages_frame = tkinter.Frame(self.Window)
		self.my_msg = tkinter.StringVar()  # For the messages to be sent.
		self.my_msg.set(name)
		self.send()

		self.my_msg.set("Type your messages here.")
		# To navigate through past messages.
		self.scrollbar = tkinter.Scrollbar(self.messages_frame)
		# Following will contain the messages.

		self.labelHead = tkinter.Label(self.Window, bg="#17202A", fg="#EAECEE",
									text='Speaking as %s' % name, font="Consolas 13 bold", pady=5)
		self.labelHead.place(relwidth=1)
		self.line = tkinter.Label(self.Window, width=450, bg="#44474a")
		self.line.place(relwidth=1, rely=0.07, relheight=0.012)
		self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

		self.textCons = tkinter.Text(self.Window,
								width=20,
								height=2,
								bg="#17202A",
								fg="#EAECEE",
								font="Consolas 12",
								yscrollcommand=self.scrollbar.set,
								padx=5,
								pady=5)

		self.textCons.place(relheight=0.745,
						relwidth=1,
						rely=0.08)

		# entry_field.pack()
		self.labelBottom = tkinter.Label(self.Window, bg="#44474a", height=80)
		self.labelBottom.place(relwidth=1, rely=0.825)
		self.entry_field = tkinter.Entry(
			self.labelBottom, textvariable=self.my_msg, bg="#2C3E50", fg="#EAECEE", font="Consolas 13")
		self.entry_field.bind("<Return>", self.send)
		self.entry_field.place(relwidth=0.74,
							relheight=0.06,
							rely=0.008,
							relx=0.011)
		# send_button = tkinter.Button(self.Window, text="Send", command=send)
		self.send_button = tkinter.Button(
			self.labelBottom, text="Send", font="Consolas 12 bold", width=20, bg="#abb2b9", command=self.send)

		self.send_button.place(relx=0.77, rely=0.008,
							relheight=0.06,  relwidth=0.22)

		self.Window.protocol("WM_DELETE_WINDOW", self.on_closing)

# ----Now comes the sockets part----
# HOST = input('Enter host: ')
# PORT = input('Enter port: ')


if __name__ == "__main__":
    g = GUI()

    
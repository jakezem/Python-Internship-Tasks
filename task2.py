import customtkinter as ctk
import sys

def chat(): #chatbot logic
    user = entry.get().lower()
    if not user.strip(): #to ignore empty messages and whitespaces
      return  
    if "hi" in user or "hello" in user:
      bot.configure(text="BOT: Welcome to our restaurant! How can I assist you today?")
    elif "menu" in user:
     bot.configure(text="BOT: We serve biryani, pizza, pasta, noodles, and desserts.")
    elif "timing" in user:
      bot.configure(text="BOT: We're open from 12 PM to 11 PM, all days of the week.")
    elif "delivery" in user:
      bot.configure(text="BOT: Yes, we deliver through Zomato and Swiggy.")
    elif "thank" in user:
      bot.configure(text="BOT: You're welcome! Let me know if you have any more questions.")
    elif "bye" in user or "exit" in user: 
      bot.configure(text="BOT: Thank you for visiting! Have a great day!")
      sys.exit() #program stops 
    else:
      bot.configure(text="BOT: I'm sorry, I didn't understand that. Can you ask something else?")

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("500x300")
app.title("ChatBOT")

label = ctk.CTkLabel(app,text="Welcome to Jacob's Restaurant !",font=("Arial",19))
label.pack(pady=30)

user_msg = ctk.CTkLabel(app,text="",font=("Arial",14))
bot = ctk.CTkLabel(app,text="",font=("Arial",16),text_color="green")
user_msg.pack()
bot.pack(pady=10)

# I grouped entry and button into a frame,to bring it to the bottom together.
bottom_frame = ctk.CTkFrame(app)
bottom_frame.pack(side="bottom", pady=30)

entry = ctk.CTkEntry(bottom_frame, placeholder_text="Enter message..", width=350)
entry.pack(side="left", padx=5)

button = ctk.CTkButton(bottom_frame, text="Send", command=chat)
button.pack(side="right")
app.mainloop()


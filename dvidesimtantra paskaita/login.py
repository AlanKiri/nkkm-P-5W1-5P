import tkinter as tk
from tkinter import messagebox

accounts = [
    {'email':'test@gmail.com', 'password':'test', 'logins':0},
    {'email':'volodyagaming@gmail.com', 'password':'123', 'logins':10},
    {'email':'raelme@gmail.com', 'password':'.ru', 'logins':1000}
]


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Prisijunk prie musu')
    window.geometry('170x150')
    
    def handle_show_password_toggle():
        if show_password_state.get():
            password_entry.config(show='')
        else:
            password_entry.config(show='*')
            
    def handle_login():
        email = email_entry.get()
        password = password_entry.get()
        
        found_account = None
        
        for account in accounts:
            if account['email'] ==email:
                found_account = account
                
        if found_account is None:
            messagebox.showerror('Login failed!', 'No user found')
            return
        
        if found_account['password'] == password:
            found_account['logins'] +=1
            messagebox.showinfo('Login successful!', f"Welcome, this is your {found_account['logins']} login")    
        else:
            messagebox.showerror('Login failed!', 'Wrong password')
        
    

    def handle_disabled_submit(_=None):
        email = email_entry.get()
        password = password_entry.get()
        
        if not email or not password:
            submit_button.config(state='disabled')
        else:
            submit_button.config(state='normal')

    
    show_password_state = tk.IntVar()
    
    email_label = tk.Label(window, text='email')
    email_entry = tk.Entry(window)
    email_entry.bind('<KeyRelease>', handle_disabled_submit)
    # Row -> vertikaliai, column -> horizontaliai
    email_label.grid(column=0, row=1)
    email_entry.grid(column=0, row=2)
    
    password_label=tk.Label(window, text='password')
    password_entry=tk.Entry(window, show='*')
    password_entry.bind('<KeyRelease>', handle_disabled_submit)
    password_label.grid(column=0, row=3)
    password_entry.grid(column=0, row=4)
    
    show_password_checkbutton = tk.Checkbutton(window, text='Show password', variable=show_password_state, command=handle_show_password_toggle)
    show_password_checkbutton.grid(column=0, row=5)
    
    submit_button = tk.Button(text='Submit', state='disabled', command=handle_login)
    submit_button.grid(column=0, row=6)

    window.mainloop()
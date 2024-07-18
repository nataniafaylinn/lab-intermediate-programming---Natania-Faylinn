import sqlite3

# Membuat dan menghubungkan ke database
conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# Membuat tabel contacts tanpa AUTOINCREMENT
c.execute('''CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                nama TEXT NOT NULL,
                alamat TEXT NOT NULL,
                no_telp TEXT NOT NULL,
                email TEXT NOT NULL)''')

conn.commit()
conn.close()

def get_available_id():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT id FROM contacts ORDER BY id")
    ids = c.fetchall()
    conn.close()

    # Cari ID yang tersedia
    current_id = 1
    for i in ids:
        if i[0] != current_id:
            break
        current_id += 1
    return current_id

def insert_contact(nama, alamat, no_telp, email):
    new_id = get_available_id()
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (id, nama, alamat, no_telp, email) VALUES (?, ?, ?, ?, ?)",
              (new_id, nama, alamat, no_telp, email))
    conn.commit()
    conn.close()

def get_contacts():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    conn.close()
    return contacts

def update_contact(contact_id, nama, alamat, no_telp, email):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute('''UPDATE contacts 
                 SET nama = ?, alamat = ?, no_telp = ?, email = ? 
                 WHERE id = ?''', (nama, alamat, no_telp, email, contact_id))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def refresh_contacts():
    for i in tree.get_children():
        tree.delete(i)
    contacts = get_contacts()
    for contact in contacts:
        tree.insert('', 'end', values=contact)

def add_contact():
    insert_contact(entry_name.get(), entry_address.get(), entry_phone.get(), entry_email.get())
    refresh_contacts()
    clear_entries()

def select_contact(event):
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        entry_name.delete(0, tk.END)
        entry_name.insert(0, values[1])
        entry_address.delete(0, tk.END)
        entry_address.insert(0, values[2])
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, values[3])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, values[4])

def update_contact_gui():
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        update_contact(values[0], entry_name.get(), entry_address.get(), entry_phone.get(), entry_email.get())
        refresh_contacts()
        clear_entries()
    else:
        messagebox.showerror("Error", "Select a contact to update")

def delete_contact_gui():
    selected = tree.focus()
    if selected:
        values = tree.item(selected, 'values')
        delete_contact(values[0])
        refresh_contacts()
    else:
        messagebox.showerror("Error", "Select a contact to delete")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Setup GUI window
root = tk.Tk()
root.title("Address Book")

# Labels and entries
tk.Label(root, text="Name").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
tk.Label(root, text="Address").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
tk.Label(root, text="Phone").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
tk.Label(root, text="Email").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W)

entry_address = tk.Entry(root, width=30)
entry_address.grid(row=1, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W)

entry_phone = tk.Entry(root, width=30)
entry_phone.grid(row=2, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W)

entry_email = tk.Entry(root, width=30)
entry_email.grid(row=3, column=1, padx=10, pady=5, columnspan=2, sticky=tk.W)

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)
tk.Button(root, text="Update Contact", command=update_contact_gui).grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)
tk.Button(root, text="Delete Contact", command=delete_contact_gui).grid(row=4, column=2, padx=10, pady=10, sticky=tk.W)

# Treeview for displaying contacts
columns = ('id', 'nama', 'alamat', 'no_telp', 'email')
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading('id', text='ID')
tree.heading('nama', text='Name')
tree.heading('alamat', text='Address')
tree.heading('no_telp', text='Phone')
tree.heading('email', text='Email')

tree.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky=tk.EW)

# Bind the select event
tree.bind('<<TreeviewSelect>>', select_contact)

# Adjust the column widths
for col in columns:
    tree.column(col, width=100)

# Stretch the last column
tree.column('email', width=150)

refresh_contacts()

root.mainloop()


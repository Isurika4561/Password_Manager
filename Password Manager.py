from tkinter import Tk, Label, Button, Entry, Frame, END
from tkinter import ttk  # Import ttk for Treeview
from Db_Operations import DbOperations


class RootWindow:

    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("900x500+40+40")

        head_title = Label(self.root, text="Password Manager", width=40,
                           bg="#7a4e9b", font=("Times New Roman", 20), padx=10, pady=10,
                           anchor="center").grid(columnspan=4, padx=130, pady=20)

        self.crud_frame = Frame(self.root, highlightbackground="black", highlightthickness=1, padx=25, pady=20)
        self.crud_frame.grid()
        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_crud_buttons()

        self.search_entry = Entry(self.crud_frame, width=30, font=("Times New Roman", 12))
        self.search_entry.grid(row=self.row_no, column=self.col_no)
        self.col_no += 1
        Button(self.crud_frame, text="Search", width=20, bg="#ffc107", font=("Times New Roman", 12),
               command=self.search_record).grid(row=self.row_no, column=self.col_no, padx=10, pady=5)

        self.create_records_tree()

    def create_entry_labels(self):
        self.col_no = self.row_no = 0
        labels_info = ("ID", "Website", "Username", "Password")
        for label_info in labels_info:
            Label(self.crud_frame, text=label_info, bg="#2f4f4f", fg="white",
                  font=("Times New Roman", 12), padx=5, pady=2).grid(row=self.row_no, column=self.col_no, padx=5, pady=2)
            self.col_no += 1

    def create_crud_buttons(self):
        buttons_info = (('Save', "#4caf50", self.save_record), 
                        ('Update', "#4682B4", self.update_record), 
                        ('Delete', "#dc143c", self.delete_record),
                        ('Copy Password', "#b57edc", self.copy_password), 
                        ('Show All Records', '#4b0082', self.show_records))
        self.row_no += 1  # Move to the next row for buttons
        self.col_no = 0  # Reset column index for buttons
        for btn_info in buttons_info:
            if btn_info[0] == 'Show All Records':
                self.row_no += 1  # Move "Show All Records" to a new row
                self.col_no = 0
            Button(self.crud_frame, text=btn_info[0], bg=btn_info[1], fg="white",
                   font=("Times New Roman", 12), padx=5, pady=2, command=btn_info[2]).grid(row=self.row_no, column=self.col_no, padx=5, pady=5)
            self.col_no += 1

    def create_entry_boxes(self):
        self.entry_boxes = []
        self.row_no += 1  # Move to the next row for entry boxes
        self.col_no = 0  # Reset column index for entry boxes
        for i in range(4):
            show = ""
            if i == 3:
                show = "*"
            entry_box = Entry(self.crud_frame, width=25, font=("Times New Roman", 12),
                              background="#f5f5f5", show=show)
            entry_box.grid(row=self.row_no, column=self.col_no, padx=5, pady=2)
            self.col_no += 1
            self.entry_boxes.append(entry_box)

    # CRUD Functions

    def save_record(self):
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()

        data = {'website': website, 'username': username, 'password': password}
        self.db.create_record(data)
        self.show_records()

    def delete_record(self):
        record_id = self.entry_boxes[0].get()
        self.db.delete_record(record_id)
        self.show_records()

    def update_record(self):
        ID = self.entry_boxes[0].get()
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()

        data = {'website': website, 'username': username, 'password': password}
        self.db.update_record(data, ID)
        self.show_records()

    def show_records(self):
        # Clear the treeview before inserting new data
        for row in self.records_tree.get_children():
            self.records_tree.delete(row)

        record_list = self.db.show_record()
        for record in record_list:
            self.records_tree.insert('', END, values=(record[0], record[3], record[4], record[5]))  # Correct data indexing

    def create_records_tree(self):
        columns = ('ID', 'Website', 'Username', 'Password')
        self.records_tree = ttk.Treeview(self.root, columns=columns, show='headings')
        self.records_tree.grid(row=self.row_no + 1, column=0, columnspan=4, padx=10, pady=10)

        for col in columns:
            self.records_tree.heading(col, text=col)
            self.records_tree.column(col, width=150)

    def search_record(self):
        search_query = self.search_entry.get()
        # Placeholder for search function - you need to implement this in DbOperations
        pass

    def copy_password(self):
        pass  # This functionality needs implementation.


if __name__ == "__main__":
    db_class = DbOperations()
    db_class.create_table()

    root = Tk()
    root_class = RootWindow(root, db_class)
    root.mainloop()

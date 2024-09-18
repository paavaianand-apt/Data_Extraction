'''
This module is used to provide the user interface for the code
'''
import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

OUTPUT_DIRECTORY = ""
FOLDER_TO_DELETE = ""

# global value declaration
selected_folder_path = ""
folder_path = ""
table = ""

def user_interface(process_file, debug_print):
    '''
    This function is used to set up the User Interface
    '''
    def upload_folder():
        '''
        This is a function to get the folder from the user
        This function uses the UI to accept and upload the folder
        '''
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            folder_path.set(folder_selected)
            selected_folder_path = folder_selected
            process_files(folder_selected)

    def process_files(selected_folder):
        '''
        This function is used to process the files in the folder
        It creates an output directory in the parent folder
        It iterates through the folder
        It checks if the file is an RTF file
        If the file is an RTF file, the schema of the file is checked
        If the file adheres to the schema, the file is converted to JSON
        '''
        global OUTPUT_DIRECTORY, FOLDER_TO_DELETE  # Declare as global variables
        for row in table.get_children():
            table.delete(row)

        if not selected_folder:
            return

        files = os.listdir(selected_folder)
        OUTPUT_DIRECTORY = os.path.join(selected_folder, 'Output')
        FOLDER_TO_DELETE = OUTPUT_DIRECTORY  # Assign the output directory to FOLDER_TO_DELETE
        os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
        print(f'{OUTPUT_DIRECTORY} successfully created')
        file_no = 0
        for file in files:
            status, remarks, color, if_inc = process_file(file, file_no, selected_folder, OUTPUT_DIRECTORY)
            if if_inc:
                file_no += 1
            table.insert("", "end", values=(file, status, remarks), tags=(color,))

    def on_continue():
        '''
        This function serves as a placeholder for the functionality of the 'continue' button
        '''
        messagebox.showinfo("Info", "Continue button clicked!")

    def on_delete():
        '''
        This function is used to delete the output folder
        '''
        for row in table.get_children():
            table.delete(row)
        folder_path.set("")

    app = tk.Tk()
    app.title("RTF to JSON Converter")
    app.geometry("800x600")
    global folder_path
    folder_path = tk.StringVar()
    title_label = tk.Label(app, text="RTF to JSON Converter", font=("Times New Roman", 20, "bold"))
    title_label.place(relx=0.5, rely=0.05, anchor=tk.CENTER)
    subtitle1_label = tk.Label(
    app,
    text="Convert Your RTF Document to JSON Format",
    font=("Times New Roman", 8)
    )

    subtitle1_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
    subtitle2_label = tk.Label(
    app,
    text="Select the RTF Folder to be Uploaded",
    font=("Times New Roman", 14)
    )

    subtitle2_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

    upload_button = tk.Button(app, text="UPLOAD RTF FOLDER", command=upload_folder)
    upload_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
    global table
    columns = ("File Name", "Status", "Remarks")
    table = ttk.Treeview(app, columns=columns, show="headings")
    table.heading("File Name", text="File Name")
    table.heading("Status", text="Status")
    table.heading("Remarks", text="Remarks")
    table.place(relx=0.5, rely=0.57, anchor=tk.CENTER, relwidth=0.8, relheight=0.55)

    table.tag_configure('green', background='lightgreen')
    table.tag_configure('red', background='lightcoral')

    style = ttk.Style()
    style.configure("TButton", padding=6, relief="flat", background="#ccc")
    style.map("TButton",
            background=[('active', '#0052cc'), ('!disabled', '#004080')],
            foreground=[('active', 'white'), ('!disabled', 'Black')],
            relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

    continue_button = ttk.Button(app, text="CONTINUE", command=on_continue, style="TButton")
    continue_button.place(relx=0.3, rely=0.9, anchor=tk.CENTER)

    delete_button = ttk.Button(app, text="DELETE", command=on_delete, style="TButton")
    delete_button.place(relx=0.7, rely=0.9, anchor=tk.CENTER)

    app.mainloop()
    debug_print("UI loaded")

# Main function to call the user_interface() function
# if __name__ == "__main__" :
#     try: #pragma nocover
#         user_interface() #pragma nocover
#     except Exception: #pragma nocover
#         debug_print("UI unsuccessful") #pragma nocover

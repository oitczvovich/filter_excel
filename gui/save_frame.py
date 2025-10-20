import tkinter as tk
import tkinter.filedialog as fd


class Save_Frame(tk.LabelFrame):
    def __init__(self, parent, request):
        super().__init__(parent, text='3. Сохранение отчета')
        self.request = request
        self._build_ui()
        
    def _build_ui(self):
        tk.Button(self, text='Сохранить как', command=self._save_file).grid(row=0, column=0, padx=10, pady=5)
        self.label_path = tk.Label(self, text='')
        self.label_path.grid(row=0, column=1, padx=10, pady=5)
        
    def _save_file(self):
        file_name = fd.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel 2007-365", "*.xlsx")]
        )
        if file_name: 
            self.request.target_path = file_name
            self.label_path.config(text=file_name)
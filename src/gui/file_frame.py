import tkinter as tk
import tkinter.filedialog as fd


class File_Frame(tk.LabelFrame):
    def __init__(self, parent, request):
        super().__init__(parent, text='1. Выбор файла')
        self.request = request
        self._build_ui()

    def _build_ui(self):
        tk.Label(self, text='Указать путь Excel файла для фильтрации.').grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self, text='Открыть', command=self._select_file).grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
        self.label_path = tk.Label(self, text='')
        self.label_path.grid(row=1, column=0)

    def _select_file(self):
        file_name = fd.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
        if file_name:
            self.request.source_path = file_name
            self.label_path.config(text=file_name)

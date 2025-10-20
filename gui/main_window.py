from datetime import datetime
import tkinter as tk
import tkinter.messagebox as box
import tkinter.filedialog as fd

from gui.tooltip import Tooltip
from gui import File_Frame, Filter_Frame, Save_Frame, Execute_Frame
from adapter.processor_adapter import ProcessorAdapter
from core.models import ProcessingRequest


class MainWindow():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Обработчик Excel файлов')
        self.root.geometry('450x550')
        self.adapter = ProcessorAdapter()
        self.request = ProcessingRequest(
            source_path='',
            target_path='',
            filter_column='',
            filter_item='',
            # requered_columns=None
        )

        self._setup_ui()
    
    def _setup_ui(self):
        icon = tk.PhotoImage(file='/home/oitc/Dev/filter_excel/gui/icon.png')
        self.root.iconphoto(True, icon)

        ## 1.  Указываем адрем файла
        self.file_frame = File_Frame(self.root, self.request)
        self.file_frame.pack(padx=10, pady=10, fill='x')
        
        ## 2. Настройки фильтрации
        self.filter_frame = Filter_Frame(self.root, self.request)
        self.filter_frame.pack(padx=10, pady=10, fill='x')
                
        ##3. Указываем куда сохранять 
        self.save_frame = Save_Frame(self.root, self.request)
        self.save_frame.pack(padx=10, pady=10, fill='x')

        ##4. Выполнение
        self.execute_frame = Execute_Frame(self.root, self.request)
        self.execute_frame.pack(padx=10,pady=10, fill='x')

    # def _select_column(self):
    #     column = self.listbox.get(self.listbox.curselection())
    #     self.request.filter_column = column
    #     box.showinfo('Выберите столбец для фильтрации', f'Фильтрация по столбцу {column}')



import tkinter as tk

from src.gui import File_Frame, Filter_Frame, Save_Frame, Execute_Frame
from src.adapter.processor_adapter import ProcessorAdapter
from src.core.models import ProcessingRequest


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
        )

        self._setup_ui()

    def _setup_ui(self):
        icon = tk.PhotoImage(file='/home/oitc/Dev/filter_excel/src/gui/icon.png')
        self.root.iconphoto(True, icon)

        # # 1.  Указываем адрем файла
        self.file_frame = File_Frame(self.root, self.request)
        self.file_frame.pack(padx=10, pady=10, fill='x')

        # # 2. Настройки фильтрации
        self.filter_frame = Filter_Frame(self.root, self.request)
        self.filter_frame.pack(padx=10, pady=10, fill='x')

        # # 3. Указываем куда сохранять
        self.save_frame = Save_Frame(self.root, self.request)
        self.save_frame.pack(padx=10, pady=10, fill='x')

        # #4. Выполнение
        self.execute_frame = Execute_Frame(self.root, self.request, self.adapter)
        self.execute_frame.pack(padx=10, pady=10, fill='x')

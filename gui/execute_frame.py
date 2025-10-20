import tkinter as tk
import tkinter.messagebox as box
from  adapter.processor_adapter import ProcessorAdapter

class Execute_Frame(tk.Label):
    def __init__(self, parent, request):
        super().__init__(parent)
        self.request = request
        self._build_ui()
        
    def _build_ui(self):
        tk.Button(self, text='Выполнить', command=self._execute).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self, text='Exit', command=self.quit).grid(row=0, column=1, padx=10, pady=5, sticky='es')
        
    
    def _execute(self):
        required_fields = {
            'source_path': 'Необходимо указать файл для чтения!',
            'target_path': 'Необходимо указать файл для сохранения!',
            'filter_column': 'Необходимо указать столбец для фильтрации',
            'filter_item': 'Необходимо указать значение',
        }
        for field, error_message in required_fields.items():
            value = getattr(self.request, field, None)
            if not value:
                box.showwarning('Ошибка', message=error_message)
                return None
        print(self.request)
        
        
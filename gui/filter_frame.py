import tkinter as tk
import tkinter.messagebox as box
from datetime import datetime
from gui.tooltip import Tooltip
from core.models import Columns


class Filter_Frame(tk.LabelFrame):
    def __init__(self, parent, request):
        super().__init__(parent, text="2. Настройка фильтрации")
        self.request = request
        self.requered_columns = [col.value for col in Columns]
        self._build_ui()
        
    def _build_ui(self):
        tk.Label(self, text="Выберите столбец для фильтрации").grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky='w')
        
        self.listbox  = tk.Listbox(self, height=len(self.requered_columns))
        for column in self.requered_columns:
            self.listbox.insert(tk.END, column)
        self.listbox.grid(row=1, column=0, padx=10, pady=5)
        
        tk.Button(self, text='Колонка', command=self._select_column).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text='Значение фильтрации:').grid(row=2, column=0, sticky='w')
        self.entry_filter = tk.Entry(self)
        self.entry_filter.grid(row=3, column=0, padx=10, pady=5)
        Tooltip(self.entry_filter, "Формат даты: ДД.ММ.ГГГГ (например, 19.10.2025)\n Зарплата должна быть больше 0")
        
        tk.Button(self, text='Ok', command=self._get_filter_value).grid(row=3, column=1, padx=10, pady=5, sticky='w')
        
        
    def _select_column(self):
        try:
            column = self.listbox.get(self.listbox.curselection())
        except tk.TclError:
            box.showwarning("Ошибкаб", "Выберите колонку из списка!")
            return
        
        self.request.filter_column = column
        box.showinfo('Фильтрация', f'Выбрана колонка:{column}')
        
    def _get_filter_value(self):
        """ Сохраняем значения из поля ввода"""
        value = self.entry_filter.get().strip()
        
        if not getattr(self.request, 'filter_column', None):
            box.showwarning("Ошибка", "Сначала выберите колонку для фильтрации!")
            return None
        
        column  = self.request.filter_column
        
        validators = {
            Columns.HIRE_DATE.value: self._validate_date,
            Columns.SALARY.value: self._validate_cost,
        }
        validate_func = validators.get(column)
        
        if validate_func and not validate_func(value):
            error_messages = {
                Columns.HIRE_DATE.value: 'Неверный формат даты! Используйте ДД.ММ.ГГГГ',
                Columns.SALARY.value: 'Зарплата должна быть положительным числом!',
            }
            box.showerror('Ошибка', error_messages[column])
            return None
        self.request.filter_item = value.lower()
        return value


    @staticmethod
    def _validate_date(date):
        try:
            datetime.strptime(date, "%d.%m%.%Y")
            return True
        except ValueError:
            return False

    @staticmethod
    def _validate_cost(cost):
        try:
            if isinstance(cost, str):
                cost = cost.replace(',', '.')
            if float(cost) > 0:
                return True
        except ValueError:
            return False
    

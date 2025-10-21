from core.excel_processor import ExcelProcessor
from core.models import ProcessingRequest, ProcessingResult

#TODO перенести в env
# REQUERED_COLUMNS = ['ФИО', 'Должность', 'Отдел', 'Дата найма', 'Зарплата']

class ProcessorAdapter:
    def __init__(self):
        self.processor = ExcelProcessor()
        
    def execute_processing(
        self,
        proces:ProcessingRequest
    ) -> ProcessingResult:
        
        request = ProcessingRequest(
            source_path=proces.source_path,
            target_path=proces.target_path,
            filter_column=proces.filter_column,
            filter_item=proces.filter_item,
        )
        return self.processor.process(request)
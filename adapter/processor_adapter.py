from core.excel_processor import ExcelProcessor
from core.models import ProcessingRequest, ProcessingResult

#TODO перенести в env
REQUERED_COLUMNS = ['ФИО', 'Должность', 'Отдел', 'Дата найма', 'Зарплата']

class ProcessorAdapter:
    def __init__(self):
        self.processor = ExcelProcessor()
        
    def execute_processing(
        self,
        source_path: str,
        target_path: str,
        filter_column: str,
        filter_item: str
    ) -> ProcessingResult:
        
        request = ProcessingRequest(
            source_path=source_path,
            target_path=target_path,
            filter_column=filter_column,
            filter_item=filter_item,
        )
        return self.processor.process(request)
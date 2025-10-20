import openpyxl
import os

from .models import ProcessingRequest, ProcessingResult

class ExcelProcessor:
    def process(self, request: ProcessingRequest) -> ProcessingResult:
        try:
            wb = openpyxl.load_workbook(request.source_path, read_only=True)
            sheet = wb.active

            filtered_data = self._filter_data(sheet, request)
            
            self._create_output_file(
                filtered_data,
                target_path=request.target_path
            )
            
            return ProcessingResult(
                success=True,
                message=f"Документ обработан",
                output_path=request.target_path
            )

        except Exception as e:
            return ProcessingResult(success=False, message=str(e), output_path=None)

    def _filter_data(self, sheet, request):
        pass
    
    def _create_output_file(self, data, target_path):
        pass
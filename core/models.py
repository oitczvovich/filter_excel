from pydantic import BaseModel, field_validator
from typing import Optional, List
from enum import Enum

class Columns(Enum):
    FIO = 'ФИО'
    POSITION = 'Должность'
    DEPARTMENT = "Отдел"
    HIRE_DATE = "Дата найма"
    SALARY = "Зарплата"

class ProcessingRequest(BaseModel):
    source_path: str
    target_path: str
    filter_column: str
    filter_item: str | float
    
class ProcessingResult(BaseModel):
    success: bool
    message: str
    output_path: Optional[str]
    

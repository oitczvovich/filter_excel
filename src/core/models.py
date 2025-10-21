from enum import Enum
from pydantic import BaseModel
from typing import Optional


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

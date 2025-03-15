#entity: defining return type of function
from dataclasses import dataclass
from pathlib import Path

#data class decorator
@dataclass(frozen = True)
class DataIngestionConfig:
    #return type of a function entity
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list


from ..formatting import Formatter as Formatter
from typing import Any, Optional

class FormattableMixin:
    def format(self, fmt: Any, locale: Optional[Any] = ...): ...
    def for_json(self): ...
    def __format__(self, format_spec: Any): ...

from .exceptions import AmbiguousTime as AmbiguousTime, NonExistingTime as NonExistingTime
from .zoneinfo import read as read, read_file as read_file
from .zoneinfo.transition import Transition as Transition
from datetime import timedelta, tzinfo
from pendulum.helpers import local_time as local_time, timestamp as timestamp
from typing import Any, Optional

POST_TRANSITION: str
PRE_TRANSITION: str
TRANSITION_ERROR: str

class Timezone(tzinfo):
    def __init__(self, name: str, extended: bool=...) -> None: ...
    @property
    def name(self) -> str: ...
    def convert(self, dt: _D, dst_rule: Optional[str]=...) -> _D: ...
    def datetime(self, year: int, month: int, day: int, hour: int=..., minute: int=..., second: int=..., microsecond: int=...) -> _datetime: ...
    def utcoffset(self, dt: None) -> None: ...
    def utcoffset(self, dt: _datetime) -> timedelta: ...
    def utcoffset(self, dt: Any): ...
    def dst(self, dt: Optional[_datetime]) -> Optional[timedelta]: ...
    def tzname(self, dt: Optional[_datetime]) -> Optional[str]: ...
    def fromutc(self, dt: _D) -> _D: ...
    def __getinitargs__(self) -> tuple: ...

class FixedTimezone(Timezone):
    def __init__(self, offset: Any, name: Optional[Any] = ...) -> None: ...
    @property
    def offset(self) -> int: ...
    def utcoffset(self, dt: Optional[_datetime]) -> timedelta: ...
    def dst(self, dt: Optional[_datetime]) -> timedelta: ...
    def fromutc(self, dt: _D) -> _D: ...
    def tzname(self, dt: Optional[_datetime]) -> Optional[str]: ...
    def __getinitargs__(self) -> tuple: ...

class TimezoneFile(Timezone):
    def __init__(self, path: Any) -> None: ...

UTC: Any

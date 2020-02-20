from pydantic import BaseModel
from typing import List, Optional

class MovieIn(BaseModel):
    name: str
    plot: str
    genres: List[str]
    casts: List[str]


class MovieOut(MovieIn):
    id: int


class MovieUpdate(MovieIn):
    name: Optional[str] = None
    plot: Optional[str] = None
    genres: Optional[List[str]] = None
    casts: Optional[List[str]] = None

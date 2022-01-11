from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Movie:
    """Class for keeping track of an item in inventory."""
    id: int
    name: any
    path: str

    @classmethod
    def from_movie_api(cls, object_dict: dict[str, any]) -> Movie:
        return cls(
            id=object_dict['id'],
            name=object_dict['title'],
            path=object_dict['full_path']
        )

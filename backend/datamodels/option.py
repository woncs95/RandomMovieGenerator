from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class Option:
    """Class for keeping track of an item in inventory."""
    providers: List[str] = field(default_factory=lambda: ['amz', 'ply'])
    release_year_from: int = 1990
    content_types: List[str] = field(default_factory=lambda: ["movie"])
    page_size: int = 100
    page: int = 1


"""
"scoring_filter_types": -- null or
    {
    "imdb:score":
        {
        "min_scoring_value":0.0,"max_scoring_value":10.0
        },
    "tomato:meter":
        {
        "min_scoring_value":0,"max_scoring_value":100
        }
    }"
"""

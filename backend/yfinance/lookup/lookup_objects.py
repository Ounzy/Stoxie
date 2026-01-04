from dataclasses import dataclass
from typing import Optional
from datetime import datetime   
from pydantic import BaseModel, Field, ConfigDict, AliasGenerator
from pydantic.alias_generators import to_camel

class Lookup(BaseModel):
    model_config = ConfigDict(extra='ignore')

    exchange: str
    industryLink: Optional[str] = None
    industryName: Optional[str] = None
    quoteType: Optional[str] = None
    rank: int
    regularMarketChange: float
    regularMarketPercentChange: float
    regularMarketPrice: float
    shortName: str

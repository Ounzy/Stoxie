from dataclasses import dataclass
from typing import Optional
from datetime import datetime   
from pydantic import BaseModel, Field, ConfigDict, AliasGenerator
from pydantic.alias_generators import to_camel


class TimezoneModel(BaseModel):
    model_config = ConfigDict(extra='ignore')

    dst: str
    gmtoffset: str
    short: str
    # Das Feld im JSON heißt '$text', in Python nutzen wir Alias, 
    # da Variablennamen kein '$' enthalten dürfen.
    text: str = Field(alias='$text')

@dataclass
class Market(BaseModel):
    model_config = ConfigDict(extra='ignore')

    id: str
    name: str
    status: str
    open: datetime
    close: datetime
    timezone: TimezoneModel




class Exchange(BaseModel):

    model_config = ConfigDict(
        alias_generator=AliasGenerator(
            validation_alias=to_camel,  # Liest camelCase von der API
        ),
        extra='ignore',
        populate_by_name=True
    )

    language: str
    region: str
    quote_type: str
    type_disp: str
    quote_source_name: str
    triggerable: bool
    custom_price_alert_confidence: str
    currency: Optional[str] = None
    short_name: str
    regular_market_change: float
    regular_market_change_percent: float
    regular_market_price: float
    regular_market_previous_close: float
    has_pre_post_market_data: bool
    first_trade_date_milliseconds: int
    price_hint: int
    regular_market_time: int
    exchange: str
    market: str
    full_exchange_name: str
    market_state: str
    source_interval: int
    exchange_data_delayed_by: int
    exchange_timezone_name: str
    exchange_timezone_short_name: str
    gmt_off_set_milliseconds: int
    esg_populated: bool
    tradeable: bool
    crypto_tradeable: bool
    symbol: str
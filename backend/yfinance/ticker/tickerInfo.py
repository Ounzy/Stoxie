from typing import Optional, List, Any
from pydantic import ConfigDict
from pydantic import BaseModel, Field, ConfigDict, AliasGenerator
from pydantic.alias_generators import to_camel

""" class CompanyOfficer:
        model_config = ConfigDict(extra='ignore')
        
        max_age: int
        name: str
        age: Optional[int]
        title: str
        year_born: Optional[int]
        fiscal_year: int
        total_pay: Optional[int]
        exercised_value: int
        unexercised_value: int"""

  


class TickerInfo(BaseModel):
    model_config = ConfigDict(extra='ignore')
    
    address1: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    website: Optional[str] = None
    industry: Optional[str] = None
    sector: Optional[str] = None
    longBusinessSummary: Optional[str] = None
    fullTimeEmployees: Optional[int] = None
    """  company_officers: List[CompanyOfficer]
    executive_team: List[Any]
    price_hint: int
    previous_close: float
    open: float
    day_low: float
    day_high: float
    dividend_rate: float
    dividend_yield: float
    ex_dividend_date: int
    payout_ratio: float
    five_year_avg_dividend_yield: float
    beta: float
    trailing_pe: float
    forward_pe: float
    volume: int
    regular_market_volume: int
    average_volume: int
    average_volume10_days: int
    average_daily_volume10_day: int"""
    marketCap: Optional[int] = None
    allTimeHigh: Optional[float] = None
    allTimeLow: Optional[float] = None
    trailingAnnualDividendRate: Optional[float] = None
    trailingAnnualDividendYield: Optional[float] = None
    currency: Optional[str] = None
    tradeable: bool
    enterpriseValue: Optional[int] = None
    profitMargins: Optional[float] = None
    floatShares: Optional[int] = None
    sharesOutstanding: Optional[int] = None
    bookValue: Optional[float] = None
    priceToBook: Optional[float] = None
    """last_fiscal_year_end: int
    next_fiscal_year_end: int
    most_recent_quarter: int
    earnings_quarterly_growth: float
    net_income_to_common: int
    trailing_eps: float
    forward_eps: float
    last_split_factor: str
    last_split_date: int
    enterprise_to_revenue: float
    last_dividend_value: float
    last_dividend_date: int
    quote_type: str"""
    current_price: Optional[float] = None
    totalCash: Optional[int] = None
    totalCashPerShare: Optional[float] = None
    totalDebt: Optional[int] = None
    totalRevenue: Optional[int] = None
    revenuePerShare: Optional[float] = None
    returnOnAssets: Optional[float] = None
    returnOnEquity: Optional[float] = None
    grossProfits: Optional[int] = None
    """earnings_growth: float
    revenue_growth: float
    gross_margins: float
    ebitda_margins: float
    operating_margins: float
    financial_currency: str
    symbol: str"""
    language: Optional[str] = None
    region: Optional[str] = None
    """type_disp: str
    custom_price_alert_confidence: str
    market_state: str
    regular_market_change_percent: float
    regular_market_price: float
    regular_market_change: float
    regular_market_day_range: str
    full_exchange_name: str
    average_daily_volume3_month: int"""
    shortName: Optional[str] = None
    longName: Optional[str] = None
    """corporate_actions: List[Any]
    regular_market_time: int
    exchange: str
    message_board_id: str
    exchange_timezone_name: str
    exchange_timezone_short_name: str"""
    market: Optional[str] = None
    """source_interval: int
    exchange_data_delayed_by: int
    crypto_tradeable: str
    has_pre_post_market_data: str
    first_trade_date_milliseconds: int
    trailing_peg_ratio: float"""

   
TickerInfo.model_rebuild()







"""
{
  "address1": "25 Gresham Street",
  "city": "London",
  "zip": "EC2V 7HN",
  "country": "United Kingdom",
  "phone": "44 20 7626 1500",
  "website": "https://www.lloydsbankinggroup.com",
  "industry": "Banks - Regional",
  "industryKey": "banks-regional",
  "industryDisp": "Banks - Regional",
  "sector": "Financial Services",
  "sectorKey": "financial-services",
  "sectorDisp": "Financial Services",
  "longBusinessSummary": "Lloyds Banking Group plc, together with its subsidiaries, provides a range of banking and financial products and services in the United Kingdom and internationally. The company operates through three segments: Retail; Commercial Banking; and Insurance, Pensions and Investments. The Retail segment offers a range of financial service products, including current accounts, savings, mortgages, motor finance, unsecured loans, and leasing solutions, as well as credit cards to personal customers. The Commercial Banking segment provides lending, transactional banking, working capital management, risk management, and debt financing services to small and medium businesses, corporates, and institutions. The Insurance, Pensions and Investments segment offers insurance, investment, and pension management products and services. It also provides digital banking services. The company offers its products and services under the Lloyds Bank, Halifax, Bank of Scotland, Scottish Widows, MBNA, Schroders Personal Wealth, Black Horse, Lex Autolease, Birmingham Midshires, LDC, AMC, Embark Group, Lloyds Living, IWeb, Cavendish Online, HGP, and Tusker brand names. Lloyds Banking Group plc was founded in 1695 and is based in London, the United Kingdom.",
  "fullTimeEmployees": 61228,
  "companyOfficers": [
    {
      "maxAge": 1,
      "name": "Mr. Charles Alan Nunn",
      "age": 54,
      "title": "Group Chief Executive & Executive Director",
      "yearBorn": 1971,
      "fiscalYear": 2024,
      "totalPay": 2525000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. William Leon David Chalmers",
      "age": 57,
      "title": "Group CFO & Executive Director",
      "yearBorn": 1968,
      "fiscalYear": 2024,
      "totalPay": 1846000,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Ron van Kemenade",
      "title": "Group Chief Operating Officer",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Peter  Fitzgerald CFA",
      "title": "Chief Investment Officer",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Ms. Carla A. S. Antunes Da Silva",
      "age": 51,
      "title": "Director of Group Strategy, Corporate Development & Investor Relations",
      "yearBorn": 1974,
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Ms. Catherine Lucy Cheetham",
      "age": 62,
      "title": "Chief Legal Officer & Company Secretary",
      "yearBorn": 1963,
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Matt  Smith",
      "title": "Head of Media Relations",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Suresh  Balaji",
      "title": "Chief Marketing Officer",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Ms. Sharon  Doherty",
      "age": 56,
      "title": "Chief People & Places Officer",
      "yearBorn": 1969,
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    },
    {
      "maxAge": 1,
      "name": "Mr. Chris  Sood-Nicholls",
      "title": "Head of Global Services & MD",
      "fiscalYear": 2024,
      "exercisedValue": 0,
      "unexercisedValue": 0
    }
  ],
  "auditRisk": 1,
  "boardRisk": 1,
  "compensationRisk": 2,
  "shareHolderRightsRisk": 1,
  "overallRisk": 1,
  "governanceEpochDate": 1767225600,
  "compensationAsOfEpochDate": 1735603200,
  "executiveTeam": [],
  "maxAge": 86400,
  "priceHint": 2,
  "previousClose": 98.24,
  "open": 98.24,
  "dayLow": 98.2,
  "dayHigh": 100.2254,
  "regularMarketPreviousClose": 98.24,
  "regularMarketOpen": 98.24,
  "regularMarketDayLow": 98.2,
  "regularMarketDayHigh": 100.2254,
  "dividendRate": 0.03,
  "dividendYield": 3.36,
  "exDividendDate": 1753920000,
  "payoutRatio": 0.58419997,
  "fiveYearAvgDividendYield": 4.49,
  "beta": 0.988,
  "trailingPE": 16.54,
  "forwardPE": 10.081267,
  "volume": 132174537,
  "regularMarketVolume": 132174537,
  "averageVolume": 144120309,
  "averageVolume10days": 98320639,
  "averageDailyVolume10Day": 98320639,
  "bid": 99.36,
  "ask": 99.4,
  "bidSize": 0,
  "askSize": 0,
  "marketCap": 58313216000,
  "fiftyTwoWeekLow": 52.435,
  "fiftyTwoWeekHigh": 100.2254,
  "allTimeHigh": 698.3536,
  "allTimeLow": 19.3102,
  "priceToSalesTrailing12Months": 3.2517266,
  "fiftyDayAverage": 93.3264,
  "twoHundredDayAverage": 81.631,
  "trailingAnnualDividendRate": 0.033,
  "trailingAnnualDividendYield": 0.00033591205,
  "currency": "GBp",
  "tradeable": "False",
  "enterpriseValue": -113024729088,
  "profitMargins": 0.2201,
  "floatShares": 56332370500,
  "sharesOutstanding": 58759791299,
  "heldPercentInsiders": 0.00068000006,
  "heldPercentInstitutions": 0.55889,
  "impliedSharesOutstanding": 58759791299,
  "bookValue": 0.771,
  "priceToBook": 128.71594,
  "lastFiscalYearEnd": 1735603200,
  "nextFiscalYearEnd": 1767139200,
  "mostRecentQuarter": 1759190400,
  "earningsQuarterlyGrowth": -0.44,
  "netIncomeToCommon": 3460000000,
  "trailingEps": 0.06,
  "forwardEps": 0.09844,
  "lastSplitFactor": "41:40",
  "lastSplitDate": 1242000000,
  "enterpriseToRevenue": -6.303,
  "52WeekChange": 0.7797705,
  "SandP52WeekChange": 0.14778805,
  "lastDividendValue": 0.0122,
  "lastDividendDate": 1753920000,
  "quoteType": "EQUITY",
  "currentPrice": 99.24,
  "targetHighPrice": 110.0,
  "targetLowPrice": 52.999996,
  "targetMeanPrice": 96.222,
  "targetMedianPrice": 1e+2,
  "recommendationKey": "none",
  "numberOfAnalystOpinions": 18,
  "totalCash": 313158991872,
  "totalCashPerShare": 5.257,
  "totalDebt": 141017006080,
  "totalRevenue": 17933000704,
  "revenuePerShare": 0.298,
  "returnOnAssets": 0.00438,
  "returnOnEquity": 0.08738,
  "grossProfits": 17933000704,
  "earningsGrowth": -0.469,
  "revenueGrowth": 0.059,
  "grossMargins": 0.0,
  "ebitdaMargins": 0.0,
  "operatingMargins": 0.24845,
  "financialCurrency": "GBP",
  "symbol": "LLOY.L",
  "language": "en-US",
  "region": "US",
  "typeDisp": "Equity",
  "quoteSourceName": "Delayed Quote",
  "triggerable": "False",
  "customPriceAlertConfidence": "LOW",
  "marketState": "PREPRE",
  "regularMarketChangePercent": 1.0179154,
  "regularMarketPrice": 99.24,
  "regularMarketChange": 1.0,
  "regularMarketDayRange": "98.2 - 100.2254",
  "fullExchangeName": "LSE",
  "averageDailyVolume3Month": 144120309,
  "fiftyTwoWeekLowChange": 46.804996,
  "fiftyTwoWeekLowChangePercent": 0.8926289,
  "fiftyTwoWeekRange": "52.435 - 100.2254",
  "fiftyTwoWeekHighChange": -0.98540497,
  "fiftyTwoWeekHighChangePercent": -0.009831889,
  "fiftyTwoWeekChangePercent": 77.97705,
  "earningsTimestamp": 1771432200,
  "earningsTimestampStart": 1771432200,
  "earningsTimestampEnd": 1771432200,
  "earningsCallTimestampStart": 1761208200,
  "earningsCallTimestampEnd": 1761208200,
  "isEarningsDateEstimate": "False",
  "epsTrailingTwelveMonths": 0.06,
  "epsForward": 0.09844,
  "epsCurrentYear": 0.07616,
  "priceEpsCurrentYear": 1303.0463,
  "shortName": "LLOYDS BANKING GROUP PLC ORD 10",
  "longName": "Lloyds Banking Group plc",
  "corporateActions": [],
  "regularMarketTime": 1767381021,
  "exchange": "LSE",
  "messageBoardId": "finmb_670064",
  "exchangeTimezoneName": "Europe/London",
  "exchangeTimezoneShortName": "GMT",
  "gmtOffSetMilliseconds": 0,
  "market": "gb_market",
  "esgPopulated": "False",
  "fiftyDayAverageChange": 5.913597,
  "fiftyDayAverageChangePercent": 0.06336468,
  "twoHundredDayAverageChange": 17.609001,
  "twoHundredDayAverageChangePercent": 0.21571465,
  "sourceInterval": 15,
  "exchangeDataDelayedBy": 15,
  "cryptoTradeable": "False",
  "hasPrePostMarketData": "False",
  "firstTradeDateMilliseconds": 820137600000,
  "trailingPegRatio": 1.7455
}
"""
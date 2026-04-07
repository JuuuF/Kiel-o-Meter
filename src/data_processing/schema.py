import polars as pl
from polars import Schema, Struct, List, String, Null, Int64, Int16

alerts_struct = Struct(
    {
        "title": String,
    }
)

arrival_struct = Struct(
    {
        "actualRelativeTime": Int16,
        "actualTime": String,
        "direction": String,
        "mixedTime": String,
        "passageid": Int64,
        "patternText": String,
        "plannedTime": String,
        "routeId": Int64,
        "status": String,
        "tripId": Int64,
        "vehicleId": Int64,
    }
)

routes_struct = Struct(
    {
        "alerts": List(alerts_struct),
        "authority": String,
        "directions": List(String),
        "id": Int64,
        "name": String,
        "routeType": String,
        "shortName": String,
    }
)

fetched_data_dtypes = {
    "actual": List(arrival_struct),
    "directions": List(String),
    "firstPassageTime": Int64,
    "generalAlerts": List(alerts_struct),
    "lastPassageTime": Int64,
    "old": List(arrival_struct),
    "routes": List(routes_struct),
    "stopName": String,
    "stopShortName": String,
    "fetchTime": String,
}

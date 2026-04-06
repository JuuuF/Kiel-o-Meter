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
        "passageid": String,  # "Int64"
        "patternText": String,
        "plannedTime": String,
        "routeId": String,  # "Int64"
        "status": String,
        "tripId": String,  # "Int64"
        "vehicleId": String,  # "Int64"
    }
)

routes_struct = Struct(
    {
        "alerts": List(alerts_struct),
        "authority": String,
        "directions": List(String),
        "id": String,  # "Int64"
        "name": String,
        "routeName": String,
        "shortName": String,
    }
)

stops_struct = Struct(
    {
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
)

fetched_data_schema = Schema(
    {
        "fetched_data": List(stops_struct),
    }
)

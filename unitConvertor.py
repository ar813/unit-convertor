import streamlit as st

# Unit conversion data
unit_categories = {
    "Area": {
        "square_meters": 1, "square_kilometers": 1e-6, "square_miles": 3.861e-7,
        "square_yards": 1.19599, "square_foot": 10.7639, "square_inch": 1550,
        "hectares": 1e-4, "acres": 0.000247105
    },
    "Energy": {
        "joules": 1, "kilojoules": 0.001, "kilocalories": 0.000239006,
        "watt_hours": 0.000277778, "kilowatt_hours": 2.7778e-7
    },
    "Frequency": {
        "hertz": 1, "kilohertz": 0.001, "megahertz": 1e-6, "gigahertz": 1e-9
    },
    "Length": {
        "meters": 1, "kilometers": 0.001, "centimeters": 100, "millimeters": 1000,
        "micrometer": 1e+6, "nanometer": 1e+9, "miles": 0.000621371, "yards": 1.09361,
        "foot": 3.28084, "inch": 39.3701, "nautical_mile": 0.000539957
    },
    "Mass": {
        "kilograms": 1, "Tonne": 0.001, "grams": 1000, "milligrams": 1e+6,
        "microgram": 1e+9, "imperial_ton": 0.000984207, "US_ton": 0.00110231,
        "stone": 0.157473, "pounds": 2.20462, "ounces": 35.274
    },
    "Data Transfer Rate": {
        "bps": 1, "Kbps": 1e3, "Mbps": 1e6, "Gbps": 1e9, "Tbps": 1e12
    },
    "Digital Storage": {
        "bits": 1, "bytes": 8, "kilobytes": 8e3, "megabytes": 8e6,
        "gigabytes": 8e9, "terabytes": 8e12, "petabytes": 8e15
    },
    "Fuel Economy": {
        "mpg_us": 1, "mpg_uk": 1.20095, "km_per_liter": 0.425144,
        "liters_per_100km": 235.214
    },
    "Plane Angle": {
        "degrees": 1, "radians": 0.0174533, "gradians": 1.11111
    },
    "Pressure": {
        "pascals": 1, "kilopascals": 1e-3, "megapascals": 1e-6,
        "bar": 1e-5, "psi": 0.000145038, "atmosphere": 9.86923e-6
    },
    "Speed": {
        "mps": 1, "kph": 3.6, "mph": 2.23694, "knots": 1.94384
    },
    "Time": {
        "seconds": 1, "minutes": 1/60, "hours": 1/3600,
        "days": 1/86400, "weeks": 1/604800, "years": 1/3.154e+7
    },
    "Volume": {
        "liters": 1, "milliliters": 1e3, "cubic_meters": 1e-3,
        "cubic_inches": 61.0237, "cubic_feet": 0.0353147,
        "gallons_us": 0.264172, "gallons_uk": 0.219969
    }
}

def convert_units(value, from_unit, to_unit, category):
    units = unit_categories[category]
    return value * units[to_unit] / units[from_unit]

# Streamlit UI
st.title("Unit Convertor")

st.sidebar.header("Unit Categories")
conversion_type = st.sidebar.selectbox("Select a category", list(unit_categories.keys()))

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", list(unit_categories[conversion_type].keys()))
with col2:
    to_unit = st.selectbox("To", list(unit_categories[conversion_type].keys()))
    
input_value = st.number_input("Enter value", value=0.0)

if st.button("Convert"):
    result = convert_units(input_value, from_unit, to_unit, conversion_type)
    st.success(f"{input_value} {from_unit} = {result} {to_unit}")

import requests

def get_current_location(api_key):
    # Get the device's IP address
    ip_request = requests.get('https://api.ipify.org')
    ip_address = ip_request.text

    # Make a request to Google Maps Geocoding API
    url = f'https://maps.googleapis.com/maps/api/geocode/json?key={api_key}&sensor=false&language=en&address={ip_address}'
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if data['status'] == 'OK':
            # Extract latitude and longitude from the response
            location = data['results'][0]['geometry']['location']
            return location
        else:
            return f"Error: {data['status']}"
    else:
        return "Error: Unable to fetch location"

# Set your Google Maps Geocoding API key
api_key = 'Aggsggasgd34g43g55b 3434'

# Get the current location
current_location = get_current_location(api_key)
print("Current Location:", current_location)
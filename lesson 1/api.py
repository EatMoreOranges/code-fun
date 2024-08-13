# Import the requests library
import requests

# Make a GET request to the GitHub API
response = requests.get('https://api.github.com')

# Print the status code of the response
print(response.status_code)  # Output: 200

# Print the JSON response from the API
print(response.json())
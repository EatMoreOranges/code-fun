# Import the requests library
import requests

# Define a class named GitHubUser
class GitHubUser:
    # The __init__ method initializes the object's attributes
    def __init__(self, username):
        self.username = username  # Instance variable for the GitHub username
        self.api_url = f"https://api.github.com/users/{username}"  # API URL for the user

    # Method to get user information from the GitHub API
    def get_user_info(self):
        response = requests.get(self.api_url)  # Make a GET request to the API
        return response.json()  # Return the JSON response

# Create an instance of the GitHubUser class
user = GitHubUser("octocat")

# Get user information and print it
user_info = user.get_user_info()
print(user_info)
# README.md

## Google Maps Location Sharing API

This API allows you to retrieve the real-time location of people who are sharing their location with you on Google Maps.

### Prerequisites

- Docker installed on your machine.
- A valid `cookies.txt` file from your Google account.

### Setup Instructions

#### 1. Obtain `cookies.txt`

- Use a browser extension like [Get cookies.txt LOCALLY](https://chrome.google.com/webstore/detail/get-cookiestxt-locally/khmbgihllnapdngfnfmhkofmbcmeamkh) to export your Google account cookies.
- Save the `cookies.txt` file in the root directory of this project.

#### 2. Build the Docker Container

Open a terminal in the project directory and run:

```bash
docker build -t location-api .

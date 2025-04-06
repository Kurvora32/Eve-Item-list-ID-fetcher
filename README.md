# Item TypeID Fetcher

This script reads item names and quantities from a tab-separated text file (`input.txt`) (only tested format copied out of [Janice.com](https://janice.e-351.com)), retrieves their corresponding `typeID` from an external API, and exports the results to a CSV file (`output.csv`) with the following columns:

- **Name**: The name of the item.
- **Amount**: The quantity of the item.
- **TypeID**: The unique identifier for the item fetched from the API.

## Prerequisites

- Python 3.x
- The `requests` library (used for making HTTP requests to the API).

UK Companies House viewer - use the UK companies house to get details on multiple companeis into an Excel file

The script allows the user to provide an Excel with UK company number and add the current registration details
of these companies into the same Excel file through the Companies House API

In order to use this tool, the user must obtain an API key from https://developer-specs.company-information.service.gov.uk/guides/authorisation
the API key should be saved in a text file named api_key.txt.
In addition, an Excel file containing the numbers of the relevant companies in the first column must be provided.

The script imports the ch_api.py module, that include calls to the Companies House API.

(c) Shai Shulman, 2021, under the GNU General Public License v3
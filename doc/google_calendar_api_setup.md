## Enable the Google Calendar API

Before using Google Calendar APIs for this project, you need to enable the Google Calendar API in your Google Cloud project. Follow these steps to enable the API:

1. In the Google Cloud console, navigate to **Menu > APIs & Services**.
2. Click on **Enable APIs and Services**.
3. Search for "Google Calendar API" and select it.
4. Click the **Enable** button to enable the API for your project.

## Configure the OAuth Consent Screen

To configure the OAuth consent screen and set up necessary credentials for accessing the Google Calendar API, follow these steps:

1. In the Google Cloud console, go to **Menu > APIs & Services > OAuth consent screen**.
2. Select the appropriate user type for your app and click **Create**.
3. Complete the app registration form and click **Save and Continue**.
4. Review your app registration summary. Click **Back to Dashboard** if everything looks correct.

## Authorize Credentials for a Desktop Application

To authenticate as an end user and access user data through your desktop application, you need to create OAuth 2.0 Client IDs. Follow these steps:

1. In the Google Cloud console, go to **Menu > APIs & Services > Credentials**.
2. Click **Create Credentials > OAuth client ID**.
3. Choose **Desktop app** as the application type.
4. Type a name for the credential in the **Name** field.
5. Click **Create**; the OAuth client created screen appears, displaying your new Client ID and Client secret.
6. Click **OK**, and the newly created credential appears under **OAuth 2.0 Client IDs**.
7. Save the downloaded JSON file as `credentials.json` and move it to your working directory.

These configurations and credentials are essential for connecting your project to the Google Calendar API securely.

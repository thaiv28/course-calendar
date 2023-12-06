# Google Calendar to UCSC Courses Converter

## Overview

This project is a Python designed to simplify the process of importing your into the UCSC (University of California, Santa Cruz) courses into Google Calendar. 

## Features

- **Choose Calendar**: Select the specific Google Calendar you want to export events into.
- **Metadata Preserving**: Preserves correct time, start/end date, location, and more.
- **Timezone Handling**: Ensure accurate conversion by handling timezones appropriately.

## How to Use

1. **Installation**:
    - Clone this repository to your local machine.
    ```bash
    git clone https://github.com/thaiv28/course-calendar.git
    ```

2. **Dependencies**:
    - Install the required dependencies using the provided `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

3. **Google Calendar API Setup**:
    - Obtain your Google Calendar API credentials and save them in the project directory.
    - Follow the instructions in the `doc/google_calendar_api_setup.md` file.

4. **Upload Course Schedule**:
    - Download pdf of course schedule and save to project directory.
    - Follow the instructions in the `doc/upload_schedule.md` file.

5. **Run the Converter**:
    - Execute the main script to start the conversion process.
    ```bash
    python main.py
    ```

6. **Follow On-screen Instructions**:
    - The CLI tool will guide you through the process of connecting to your Google Calendar and mapping events to UCSC courses.

## To-do
- Package as python package using pip
- Store credentials using Google Secret Manager (or alternative)

## Contributing

If you find any bugs, have suggestions, or want to contribute new features, please submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Acknowledgments

- Special thanks to the UCSC community for inspiration and feedback.
- This project utilizes the Google Calendar API; credit to the Google API team.

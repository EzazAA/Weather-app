
---
![Command Prompt - powershell 01-10-2024 3 20 03 PM](https://github.com/user-attachments/assets/c3dd8f6c-3f61-49a6-b629-fbe4281c28e4)

# Weather App ☀️🌧️

## Overview

Welcome to the Weather App! This Python application allows users to get current weather information for any city around the world. It utilizes the OpenWeatherMap API to fetch real-time weather data and provides a simple command-line interface for interaction.

## Features

- **Current Weather**: Fetches and displays the current weather conditions for a specified city.
- **Temperature Information**: Provides temperature in Celsius (or Fahrenheit if you prefer).
- **Weather Description**: Displays a brief description of the weather conditions (e.g., clear sky, light rain).

## Installation 📩

### Prerequisites

- Python 3.x installed on your system.
- An API key from OpenWeatherMap.

### Setup 

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/weather-app.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd weather-app
   ```

3. **Install Dependencies**:

   The application requires the `requests` library. You can install it using pip:

   ```cmd
   pip install requests
   ```

4. **Obtain Your API Key**:

   - Sign up at [OpenWeatherMap](https://openweathermap.org/).
   - Navigate to your API keys section and generate a new API key.

5. **Update the API Key**:

   Open the `weather_app.py` file and replace `'YOUR_API_KEY'` with your actual OpenWeatherMap API key:

   ```python
   api_key = 'YOUR_API_KEY'
   ```

## Usage ✍

1. **Run the Script**:

   Execute the script using Python:

   ```bash
   python weather_app.py
   ```

2. **Input the City Name**:

   When prompted, enter the name of the city for which you want to retrieve the weather information.

3. **View the Results**:

   The script will display the current temperature and weather description for the specified city.

## Example

```bash
Enter city name: Delhi
Weather in Delhi:
Temperature: 30°C
Description: Clear sky
```

## Troubleshooting ❗

- **Invalid API Key**: Ensure you have correctly replaced `'YOUR_API_KEY'` with a valid key from OpenWeatherMap.
- **City Not Found**: Verify the city name is correct and spelled properly. 

## Contributing 🤝

We welcome contributions from the community! If you have ideas for new features or improvements, please follow these steps:

1. **Fork the Repository**: Click the "Fork" button at the top right of this page.
2. **Clone Your Fork**: 

   ```bash
   git clone https://github.com/yourusername/weather-app.git
   ```

3. **Create a New Branch**:

   ```bash
   git checkout -b feature-branch
   ```

4. **Make Your Changes**: Implement your improvements or new features.
5. **Commit Your Changes**:

   ```bash
   git add .
   git commit -m "Add new feature"
   ```

6. **Push to Your Fork**:

   ```bash
   git push origin feature-branch
   ```

7. **Create a Pull Request**: Go to the original repository and click "New Pull Request" to submit your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
@EzazAA
---

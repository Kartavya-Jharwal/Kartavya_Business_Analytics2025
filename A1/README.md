# Basic Streamlit App

This is a basic Streamlit application created using `uv` for dependency management.

## Features

- **Home Page**: Welcome message with user input and metrics
- **Data Analysis**: Sample dataset with filtering capabilities
- **Interactive Charts**: Various chart types with customizable parameters

## Setup and Installation

1. Make sure you have `uv` installed. If not, install it from [https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)

2. Clone or navigate to this directory

3. Install dependencies:
   ```bash
   uv sync
   ```

## Running the Application

To run the Streamlit app:

```bash
uv run streamlit run app.py
```

This will start the Streamlit server and you can view the app in your browser at `http://localhost:8501`

## Project Structure

```
├── app.py              # Main Streamlit application
├── pyproject.toml      # Project configuration and dependencies
├── uv.lock            # Lock file for reproducible builds
└── README.md          # This file
```

## Dependencies

- **Streamlit**: Web app framework
- **Pandas**: Data manipulation and analysis
- **Numpy**: Numerical computing

## Features Demonstrated

- Page navigation with sidebar
- Interactive widgets (text input, sliders, selectbox, etc.)
- Data display with DataFrames
- Various chart types (line, bar, scatter, area)
- Metrics and statistics display
- Color picker and settings
- Responsive layout with columns

## Customization

You can easily extend this app by:
- Adding new pages to the navigation
- Incorporating your own datasets
- Adding more chart types
- Implementing user authentication
- Adding database connectivity

Enjoy building with Streamlit and uv! 🚀

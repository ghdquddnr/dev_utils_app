# Developer Utilities App (Dev Utils App)

A Python GUI application that provides various utility features for developers. With a modern UI and convenient functions, it makes development work more efficient.

![Application Screenshot](screenshot.png)

## Main Features

### Text Comparison (Text Diff)
- Visually display differences between two texts
- Accurate difference highlighting through line-by-line comparison
- Intuitive UI for easy use
- Reset button for quickly starting new work

### JSON Viewer
- Visualize JSON strings as a tree structure
- Collapse/expand node functionality for easy navigation of complex structures
- Sample data provided for quick testing
- Automatic theme changes according to light/dark mode

## Technology Stack

- **Frontend**: CustomTkinter (Python GUI library)
- **Comparison Algorithm**: diff-match-patch library
- **JSON Parsing**: Python built-in json module
- **Theme System**: Light/dark mode support

## System Requirements

- Python 3.8 or higher
- The following Python packages:
  - customtkinter
  - pillow
  - diff-match-patch

## Installation

### 1. Clone Repository
```bash
git clone https://github.com/ghdquddnr/dev_utils_app.git
cd dev_utils_app
```

### 2. Set up Virtual Environment and Install Packages
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install packages
pip install customtkinter pillow diff-match-patch
```

### 3. Run Application
```bash
python main.py
```

## How to Use

### Text Comparison Feature
1. Enter the original text in the left text area.
2. Enter the text to compare in the right text area.
3. Click the "Compare" button to see differences between the two texts highlighted with colors.
   - Deleted parts: Red background
   - Added parts: Green background
4. Click the "Reset" button to clear all text and start a new comparison.

### JSON Viewer Feature
1. Enter a JSON string in the left text area.
2. Click the "Convert" button to visualize the JSON as a tree structure on the right.
3. Click the + or - buttons on tree nodes to expand or collapse them.
4. Use the "Expand All"/"Collapse All" button to control the entire tree at once.
5. Click the "Example Data" button to automatically input sample JSON data.
6. Click the "Reset" button to clear all data.

### Theme Change
- Click the "Change Theme" button at the bottom of the sidebar to switch between light and dark modes.

## Development Environment Setup

```bash
# Install development packages
pip install -e ".[dev]"
```

## Future Plans

- Additional utility features in development
- Performance optimization
- User settings save functionality

## License

This project is distributed under the MIT license. For more details, please refer to the [LICENSE](LICENSE) file.

## Contributing

Contributions are always welcome! You can help improve this project through bug reports, feature requests, or code contributions. 
# Microplastic Analytics Platform

A full-stack web application for analyzing and visualizing microplastic pollution data, specifically focusing on the San Francisco Bay Microplastics Project. This platform provides scientific intelligence for tracking microplastic distribution by type, size, color, and location.

## Live Demo
**[Launch Microplastic Analytics Platform on Render](#)** <!-- Replace # with your Render.com live link -->

## Features
- **Data Analytics:** Cleans and processes raw microplastic datasets to generate reliable summary statistics.
- **Dynamic Visualizations:** Interactive charts to explore pollution distribution by particle type, size, and color.
- **Geographic Interpolation:** Explore pollution levels across various sample locations with advanced data mapping.
- **Risk Indicators:** Automatically calculates environmental pollution risk scores based on particle concentrations.
- **Modern Dashboard UI:** A deeply stylized, responsive, user-friendly interface powered by advanced HTML, CSS, JS and a dark theme for optimal data reading.

## Tech Stack
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, Chart.js (or similar charing librarires)
- **Backend:** Python (Standard HTTP Server), Pandas for data processing

## Getting Started

### Prerequisites
- Python 3.8+
- Pandas

### Local Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Swatii-Sharma/Cyber_Attack_Dashboard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Cyber_Attack_Dashboard
   ```
3. Install dependencies:
   ```bash
   pip install pandas
   ```
4. Run the backend server:
   ```bash
   cd backend
   python app.py
   ```
5. Note: The server serves the `frontend` static files. You can visit `http://localhost:8000/` in your browser.

## Deployment
This app can be deployed to [Render.com](https://render.com) using a Web Service. Just connect your GitHub repository and point the build command and start command as needed for the Python backend.

## License
MIT License

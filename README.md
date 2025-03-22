# FLex: Financial Literacy Expert for Students

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30.0%2B-red)
![Status](https://img.shields.io/badge/Status-Development-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## 📚 Overview

**FLex** (Financial Literacy Expert) is an AI-powered assistant designed specifically for students and beginners in the world of finance. Our mission is to simplify financial concepts, help users understand their own financial situation, and keep them informed about relevant market trends - all in language that's easy to understand.

The application leverages the Palmyra-Fin-70B language model along with data from multiple financial APIs to provide personalized guidance and education.

## ✨ Features

### 📖 Financial Information
- Search for financial terms and concepts
- Get simplified explanations with real-world examples
- Explore related financial concepts

### 💼 Know Your Finances
- Create a personal financial profile
- Receive a financial health score
- Get personalized savings strategies and investment recommendations
- Visualize recommended budget allocations

### 📈 Current Market
- Compare bank interest rates
- Track market performance of major indices
- Stay updated on student loan interest rates
- Get student-focused financial news and insights

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/GeetChoudhari/Flex_App.git
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```
flex_app/
│
├── app.py                   # Main application entry point
├── config.py                # Configuration variables
├── utils.py                 # Shared utility functions
│
├── pages/                   # Directory containing individual page files
│   ├── 01_Financial_Information.py
│   ├── 02_Know_Your_Finances.py
│   └── 03_Current_Market.py
│
├── assets/                  # Static assets (images, css, etc.)
│   └── custom.css           # Custom CSS styling
│
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🚀 Usage

### Running Locally

After installation, access FLex through your web browser:

```
http://localhost:8501
```

### Navigation

- Use the sidebar to navigate between different sections
- Complete your financial profile in the "Know Your Finances" section
- Search for financial terms in the "Financial Information" section
- Check current market data in the "Current Market" section

## 🔧 Technology Stack

- **Frontend**: Streamlit
- **Data Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **AI Integration**: Palmyra-Fin-70B (NVIDIA)
- **External Data Sources**: 
  - Polygon API
  - Yahoo Finance
  - DuckDuckGo

## 🔮 Future Development Plans

### Phase 1: Core Implementation
- Complete Streamlit interface with all pages
- Implement user profile functionality
- Build out financial terms database

### Phase 2: AI Integration
- Integrate LangFlow for visual workflow design
- Connect Palmyra-Fin-70B model for personalized responses
- Implement user query analysis system

### Phase 3: Data Integration
- Connect to Polygon API for real-time market data
- Implement Yahoo Finance integration for stock information
- Add DuckDuckGo for supplementary research

### Phase 4: Advanced Features
- Personalized learning paths based on financial knowledge level
- Interactive financial planning tools
- Notification system for important financial updates

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- NVIDIA for the Palmyra-Fin-70B model
- Streamlit for the interactive web framework
- Financial education resources that inspired this project

---

<p align="center">
  Made with ❤️ for financial literacy
</p>
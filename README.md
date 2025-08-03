# 🎬 Movie Recommender System

A Streamlit-based movie recommendation system that suggests similar movies based on your selection using machine learning similarity algorithms.

![Movie Recommender](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## ✨ Features
- 🎯 Interactive movie selection from a curated database
- 🖼️ Visual movie posters fetched from TMDB API
- 🤖 ML-powered recommendations based on similarity analysis
- 📱 Clean and responsive UI built with Streamlit
- ⚡ Fast and efficient recommendation engine

## 🚀 Live Demo

You can try the live application here: [Movie Recommender System](https://movie-recommender-system-abdulrehman028.streamlit.app/)

<img width="1920" height="1424" alt="image" src="https://github.com/user-attachments/assets/ef3b6651-fc30-483e-8f2e-9811841a9393" />


## 📋 Prerequisites
- Python 3.7 or higher
- Internet connection (for fetching movie posters)

## 🔧 Installation & Setup

1. **Clone the repository:**
```bash
git clone https://github.com/AbdulRehman028/movie-recommender-system.git
cd movie-recommender-system
```

2. **Install the required dependencies:**
```bash
pip install -r requirements.txt
```

3. **Make sure you have the required data files:**
   - `movie_dict.pkl` - Contains movie data
   - `similarity.pkl` - Contains similarity matrix

## 🏃‍♂️ Running the Application

To start the application, run the following command in your terminal:

```bash
streamlit run app.py
```

The application will start and open in your default web browser, typically at `http://localhost:8501`.

## 📱 How to Use

1. 🎬 Select a movie from the dropdown menu
2. 🔍 Click the "Recommend" button  
3. 📋 View the 5 recommended movies with their posters

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. **Push your code to GitHub**
2. **Go to [Streamlit Cloud](https://streamlit.io/cloud)**
3. **Connect your GitHub account**
4. **Select your repository**
5. **Your app will be live at:** `https://your-app-name.streamlit.app`

### Deploy to Heroku

1. Create a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

2. Deploy using Heroku CLI or GitHub integration

## 🛠️ Technologies Used

- **Python 3.7+** - Programming language
- **Streamlit** - Web framework for the UI
- **Pandas** - Data manipulation and analysis
- **Requests** - HTTP library for API calls
- **Pickle** - Data serialization
- **TMDB API** - Movie posters and metadata

## 📊 Project Structure

```
movies-recommender-system/
├── app.py                 # Main Streamlit application
├── movie_dict.pkl         # Serialized movie data
├── similarity.pkl         # Precomputed similarity matrix
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .gitignore           # Git ignore file
└── run_app.bat          # Windows batch script to run app
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer
Developed by **M.Abdulrehman Baig** ❤️ using Streamlit

## 🌟 Acknowledgments

- [The Movie Database (TMDB)](https://www.themoviedb.org/) for providing the movie poster API
- [Streamlit](https://streamlit.io/) for the amazing web framework
- The open-source community for the incredible tools and libraries

---

⭐ **If you found this project helpful, please give it a star!** ⭐

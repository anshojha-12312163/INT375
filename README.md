# Malware Classification System

A Django-based web application for malware classification using machine learning techniques.

## Features

- Upload and analyze malware samples
- Static and dynamic feature extraction
- Machine learning-based classification
- Interactive dashboard with visualizations
- REST API for programmatic access

## Project Structure

```
malware_classifier/
├── __init__.py
├── config.py
├── data/
│   ├── __init__.py
│   ├── loader.py
│   └── preprocessor.py
├── features/
│   ├── __init__.py
│   ├── static_extractor.py
│   ├── dynamic_extractor.py
│   └── feature_selector.py
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── traditional_models.py
│   └── deep_learning_models.py
├── evaluation/
│   ├── __init__.py
│   ├── metrics.py
│   └── visualizer.py
└── utils/
    ├── __init__.py
    ├── file_ops.py
    └── logger.py
```

## Installation

1. Clone the repository:
```
git clone https://github.com/yourusername/malware-classifier.git
cd malware-classifier
```

2. Create a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Set up the database:
```
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```
python manage.py createsuperuser
```

## Usage

1. Start the development server:
```
python manage.py runserver
```

2. Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

3. Log in with your superuser credentials

4. Use the dashboard to:
   - Upload malware samples
   - View analysis results
   - Monitor classification statistics

## API Usage

The system provides a REST API for programmatic access:

- `POST /api/analyze/`: Submit a file for analysis
- `GET /api/analysis-results/`: Retrieve analysis results

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django web framework
- scikit-learn for machine learning
- YARA for pattern matching
- PEfile for PE file analysis 
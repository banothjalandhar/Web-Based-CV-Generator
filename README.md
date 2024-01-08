# Web-Based CV Generator

## Overview

The Web-Based CV Generator is a Django project designed to help users create professional and visually appealing CVs (Curriculum Vitae) online. This project simplifies the process of CV creation by providing a user-friendly web interface.

## Features

- **CV Creation:**
  - Provide a form-based interface for users to input personal information, education, work experience, skills, and other relevant details.

- **Download CV:**
  - Allow users to download their completed CV in various formats (e.g., PDF, DOCX) for offline use.

- **Responsive Design:**
  - Ensure a seamless experience on various devices, including desktops, tablets, and mobile phones.

## Installation

Follow these steps to set up the project locally:

### 1. Clone the Repository
```bash
git clone https://github.com/banothjalandhar/Web-Based-CV-Generator.git
cd your-cv-generator

### 2. Create a Virtual Environment
python -m venv venv


### 3. Activate the Virtual Environment
.\venv\Scripts\activate

### 4. Install Dependencies
pip install pdfkit

### 5. Run Migrations
python manage.py makemigrations
python manage.py migrate


### 6.Start the Development Server
python manage.py runserver


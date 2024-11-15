# Project Name
> A simple application to process text articles using OpenAI's API and generate HTML output.

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Setup](#setup)

## General Information
- This project aims to create a simple Python application that connects to the OpenAI API, processes a text article, and generates structured HTML code.
- The main purpose of this project is to transform raw article text into a well-structured HTML format, including suggestions for images.
- The application is useful for automating the creation of HTML content from text articles, making it easier to visualize and format the content.

## Technologies Used
- Python - version 3.10
- HTML/CSS (for HTML templates and preview)
- OpenAI API (GPT-4o)
- openai==0.28.0
- dotenv - version 1.0.1

## Setup
1. Clone the repository to your local machine.
2. Install the required dependencies by running:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory and add your OpenAI API key:
   ```
   API_KEY=your_openai_api_key_here
   ```
4. Run the script to generate the HTML content:
   ```sh
   python main.py
   ```
5. Generated files:
   - `artykul.html`: The HTML content generated from the article.
   - `szablon.html`: A template file to preview the article.
   - `podglad.html`: A complete preview file that combines the template and the generated article content.

# Langchain_flask
This repository contains a Flask web application that leverages the Langchain library to build a conversational AI system. The AI system is powered by the GPT-3.5 Turbo model from OpenAI and utilizes the Langchain library for managing conversational chains, document retrieval, and more.

## Getting Started
Follow these steps to set up and run the conversational AI web application:

1. **Clone the Repository:** Begin by cloning this repository to your local machine:
  ```bash
  git clone https://github.com/KANGRUIMING/Langchain_flask.git
  cd Langchain_flask
  ```
2. **Install Dependencies:** Install the required dependencies using `pip` by executing the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Your OpenAI API Key:** Start by copying the `.env.example` file in the repository and renaming it to `.env`. Then, open the `.env` file in a text editor and enter your OpenAI API key:

   ```bash
   cp .env.example .env
   ```

4. **Run the Flask Application:** Launch the Flask application to start the conversational AI system. In your terminal, execute the following command:

   ```bash
   python app.py
   ```

## Adding Custom Data

You can enhance the capabilities of the conversational AI by providing your own data in the `/data` directory. This data can include text files, PDF documents, or other relevant information that you want the AI to reference during conversations.

To add your custom data:

1. Navigate to the `/data` directory within the repository.
2. Place your desired files in the directory. Supported file formats include `.txt` for plain text files and `.pdf` for PDF documents.

For example, if you have a text file named `my_custom_data.txt` that you want the AI to access, you would place it in the `/data` directory.

Keep in mind that the conversational AI utilizes Langchain's document retrieval and indexing features, so adding relevant documents can help improve the AI's responses and information retrieval capabilities.



   

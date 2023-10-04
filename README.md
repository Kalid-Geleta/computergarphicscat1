Python3 Development Environment for Assessment 1
To set up a new Python3 development environment for this assessment, follow these steps:

Install Python 3. You can do this using your operating system's package manager, or by downloading and installing the Python 3 installer from the Python website.
Install a Python virtual environment tool. This is optional, but it is recommended to use a virtual environment to isolate your project's dependencies from the rest of your system. You can install a virtual environment tool such as virtualenv or venv.
Create a new virtual environment for your project. To do this, run the following command:
python3 -m venv my_project_env
Activate the virtual environment. To do this, run the following command:
source my_project_env/bin/activate
Install the required dependencies for your project. To do this, run the following command:
pip install -r requirements.txt
Building a Python3 Project
To build a Python3 project with the structure of projects in PyCharm, follow these steps:

Create a new directory for your project.
Inside the project directory, create a new file called __init__.py. This file is empty, but it is required to make the directory a Python package.
Create a new directory for your project's code.
Inside the code directory, create a new file called main.py. This is where you will write your main code.
In main.py, import the necessary libraries and modules.
Write your main code.
To run your project, run the following command:
python main.py
Generating an en-xx.xlxs File for All Languages
To generate an en-xx.xlxs file for all languages in the MASSIVE dataset, follow these steps:

Write a Python script that iterates over the dataset and generates an Excel spreadsheet for each language.
The spreadsheet should contain the following columns:
id
utt
annot_utt
Save the spreadsheet as en-xx.xlxs, where xx is the language code.
Repeat steps 1-3 for all languages in the dataset.
Generating JSONL Files for English, Swahili, and German
To generate separate JSONL files with test, train, and dev for English (en), Swahili (sw), and German (de), follow these steps:

Write a Python script that iterates over the MASSIVE dataset and extracts the test, train, and dev data for each language.
Save the data to JSONL files, with the following naming convention:
{language_code}-{split}.jsonl
For example, the JSONL file for the English test data would be named en-test.jsonl.

Generating a Large JSON File with All Translations from en to xx with id and utt for All Train Sets
To generate a large JSON file showing all the translations from en to xx with id and utt for all train sets, follow these steps:

Write a Python script that iterates over the train data for all languages and extracts the translations from en to xx.
Save the translations to a JSON file, with the following naming convention:
en-to-xx-train.json
Pretty Printing the JSON File Structure
To pretty print the JSON file structure, you can use the following command:

python -m json.tool json_file.json
This will print the JSON file to the console with a formatted structure.

Uploading the Files to Google Drive
To upload the files to your Google Drive Backup Folder, you can use the following command:

gdrive upload -r my_project_files
This will upload the my_project_files directory to your Google Drive Backup Folder.

Uploading the Changes to GitHub
To upload the changes to GitHub, you can use the following command:

git push origin main
This will push the changes on your local branch to the main branch on GitHub.


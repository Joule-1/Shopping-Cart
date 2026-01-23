After reopening your terminal, reactivate virtual environment by navigating to project directory and running the activation command.

cd Shopping-Cart
venv\Scripts\activate

Installing Dependencies

pip install <package-name>
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add <package-name> dependency"
git push
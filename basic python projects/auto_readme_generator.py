import os

# Folder where script is run
FOLDER = os.path.dirname(os.path.abspath(__file__))
README_FILE = os.path.join(FOLDER, 'README.md')

# Header content
header = """# 🐍 Basic Python Projects

This folder contains a collection of beginner-friendly Python mini projects designed to reinforce your core programming skills.

---

## 📁 Projects Included

| File Name               | Description                            |
|-------------------------|----------------------------------------|
"""

# Descriptions dictionary
descriptions = {
    "compound_interest_calculator.py": "Calculates compound interest with user input.",
    "madlibs_game.py": "A fun Mad Libs word game.",
    "temperature_conversion_program.py": "Converts between Celsius and Fahrenheit.",
    "weight converter.py": "Converts weight between kg and lbs.",
    "mini calculator.py": "Performs basic arithmetic operations.",
    "shopping cart.py": "takes input of name and prices from user and give's a shooping list and total price.",
    "concession_stand_program.py": "shows menu of the concession stand and adds food to your cart and prints the total price of the food.",
    "number_guessing_game.py": " user can play by guessing numbers between numbers 1 to 100 until he guess the correct number."
}

def generate_readme():
    # Start content
    content = header

    # List and sort .py files (ignore this generator script)
    py_files = [f for f in os.listdir(FOLDER) if f.endswith('.py') and f != os.path.basename(__file__)]
    py_files.sort()

    if not py_files:
        print("⚠️ No Python files found.")
        return

    for file in py_files:
        desc = descriptions.get(file, "🚧 Description pending...")
        content += f"| `{file}` | {desc} |\n"

    # Footer note
    content += "\n---\n\n✅ This README was auto-generated using `auto_readme_generator.py`.\n"

    # Write to README.md
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ README.md successfully updated with {len(py_files)} files.")

if __name__ == "__main__":
    generate_readme()

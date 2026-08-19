# 🚀 Run the Project

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Statistics-Playground.git
```

```bash
cd Statistics-Playground
```

---

## Step 2: Create a Virtual Environment

### Windows

```bash
python -m venv .venv
```

Activate it

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

---

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4: Run the Application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## Step 5: Open in Browser

After the server starts, open:

```
http://localhost:8501
```

Streamlit usually opens this URL automatically.

---

# 🛑 Stop the Application

Press:

```text
CTRL + C
```

inside the terminal.

---

# 🔄 Install New Dependencies

If you add a new library:

```bash
pip install package_name
```

Update the requirements file:

```bash
pip freeze > requirements.txt
```

---

# 🔄 Reinstall Dependencies

If you clone the project on another machine:

```bash
pip install -r requirements.txt
```

---

# 📂 Project Entry Point

The application starts from:

```text
app.py
```

Streamlit automatically detects all modules inside the **pages/** folder and displays them in the sidebar.

---

# 🧪 Verify Installation

Run:

```bash
streamlit hello
```

If the demo application opens successfully, Streamlit is installed correctly.

You can also verify the installed versions:

```bash
python --version
```

```bash
streamlit --version
```

```bash
pip list
```

---

# 📝 Example Terminal Session

```bash
git clone https://github.com/yourusername/Statistics-Playground.git

cd Statistics-Playground

python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt

streamlit run app.py
```
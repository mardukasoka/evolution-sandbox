# 🧠 Multi-Agent Evolution Sandbox

This project is a simple AI playground where two agents compete to evolve Python expressions that approximate a target number. The agents are influenced by simulated human emotions like "Calm", "Frustrated", or "Curious" to explore or exploit more aggressively.

Built with **Gradio** for the web UI and **Python** for the evolutionary logic.

---

## 🚀 Live Demo (Optional)

You can deploy this on [Hugging Face Spaces](https://huggingface.co/spaces) or run it locally.

---

## 🛠 How to Run Locally

### Prerequisites

- Python 3.9+
- `pip` installed

### Steps

```bash
git clone https://github.com/YOUR_USERNAME/evolution-sandbox.git
cd evolution-sandbox
pip install -r requirements.txt
python app.py
```

Then visit: http://127.0.0.1:7860/

---

## 🌍 How to Deploy on Hugging Face Spaces

1. Create a new Space at [Hugging Face Spaces](https://huggingface.co/spaces)
2. Choose:
   - SDK: **Gradio**
   - Visibility: **Public** or **Private**
3. Upload all files from this repo
4. Add a `requirements.txt` with:
   ```
   gradio
   ```
5. It will auto-launch!

---

## 📁 Project Structure

| File              | Purpose                                      |
|-------------------|----------------------------------------------|
| `app.py`          | Gradio web interface                         |
| `agents.py`       | Agent logic + evolution loop                 |
| `emotion.py`      | Maps emotion labels to evolution behavior    |
| `shared_memory.py`| Stores top results across agents             |
| `requirements.txt`| Gradio dependency                            |

---

## 🤖 How It Works

- Each agent evolves a small population of math expressions (e.g., `3 + 4`)
- They try to get as close as possible to a **user-specified target number**
- The user's selected **emotion** influences how much each agent explores new solutions
- The best result is shown live

---

## 📬 License

MIT License. Feel free to build on this!
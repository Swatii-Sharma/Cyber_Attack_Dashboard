# Cyber Intelligence Dashboard

**Project Link:** [https://github.com/Swatii-Sharma/Micro_Particle_Dashboard](https://github.com/Swatii-Sharma/Micro_Particle_Dashboard)

## 🛡️ What is this project?

This project is a powerful but easy-to-use **Cyber Intelligence Dashboard**. It connects to the official MITRE ATT&CK database (a global list of known hacker techniques and tactics) to create a visual and interactive web dashboard. 

In simple words, it reads raw data about how hackers attack systems, analyzes it, and then builds a beautiful, human-readable webpage (`dashboard.html`) to show you:
- **Analytics Hub:** Charts and stats about different hacker tactics.
- **Matrix Explorer:** A searchable table of over 800 hacking techniques, their risk levels, and targeted platforms (like Windows, Linux, Cloud).
- **Defense Strategies:** Ways to protect systems and stop these attacks.
- **Data Export:** You can even download a neat Excel/CSV report of the top threats!

All you have to do is run the Python script (`main.py`), and it automatically updates and creates the dashboard for you!

---

## 🚀 How to Run it on Your Own Computer

1. Make sure you have Python installed.
2. Install the required tools by typing this in your terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main file:
   ```bash
   python main.py
   ```
4. A file called `dashboard.html` will be created in your folder. Double-click it to open your new dashboard in your web browser!

---

## 🌐 How to Deploy to Render (Free)

Want to share your dashboard with the world using a public link? You can use Render to host it for free!

1. Go to [Render](https://render.com/) and sign up or log in.
2. Click the **"New"** button and select **"Static Site"**.
3. Connect your GitHub account and select this repository (`Micro_Particle_Dashboard`).
4. Fill in the deployment details like this:
   - **Name:** Choose a name (e.g., `cyber-dashboard`)
   - **Branch:** `main`
   - **Build Command:** `pip install -r requirements.txt && python main.py`
   - **Publish directory:** `.` (just a single dot)
5. Click **Create Static Site**.

Render will now run your Python code, generate the `dashboard.html`, and host it on a public link. Wait a minute for it to finish 

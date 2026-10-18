from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Muscab | Software Developer</title>
<style>
:root {
  --bg: #08111f;
  --panel: #101d30;
  --blue: #55a6ff;
  --text: #eef4ff;
  --muted: #a9b8cc;
}
* { box-sizing: border-box; scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
}
header {
  position: sticky;
  top: 0;
  background: rgba(8,17,31,.95);
  border-bottom: 1px solid #223149;
  z-index: 10;
}
nav {
  max-width: 1050px;
  margin: auto;
  padding: 16px 22px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}
.logo { font-size: 20px; font-weight: bold; }
.logo span, h1 span { color: var(--blue); }
nav a {
  color: var(--text);
  text-decoration: none;
  margin-left: 15px;
  font-size: 14px;
}
nav a:hover, .link:hover { color: var(--blue); }
section {
  max-width: 1050px;
  padding: 75px 22px;
  margin: auto;
}
.hero { min-height: 78vh; display: flex; align-items: center; }
.eyebrow { color: var(--blue); font-weight: bold; }
h1 { font-size: clamp(38px, 7vw, 68px); line-height: 1.12; margin: 12px 0; }
h2 { font-size: 32px; margin-top: 0; }
p { color: var(--muted); }
.buttons { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 24px; }
.btn {
  display: inline-block; padding: 11px 18px; border-radius: 8px;
  background: var(--blue); color: #06101e; text-decoration: none;
  font-weight: bold;
}
.btn.secondary { background: transparent; border: 1px solid #536780; color: var(--text); }
.grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(220px,1fr)); gap: 18px; }
.card {
  background: var(--panel); padding: 22px; border: 1px solid #223149;
  border-radius: 14px;
}
.card h3 { margin-top: 0; }
.tag {
  display: inline-block; background: #172c45; color: #b8d9ff;
  padding: 5px 10px; border-radius: 20px; margin: 4px; font-size: 13px;
}
.link { color: var(--blue); text-decoration: none; }
footer { text-align: center; padding: 28px; border-top: 1px solid #223149; color: var(--muted); }
@media (max-width: 600px) {
  nav { align-items: flex-start; flex-direction: column; }
  nav a { margin: 0 12px 0 0; }
  section { padding-top: 55px; padding-bottom: 55px; }
}
</style>
</head>
<body>

<header>
  <nav>
    <div class="logo">Muscab<span>.</span></div>
    <div>
      <a href="#home">Home</a>
      <a href="#about">About</a>
      <a href="#skills">Skills</a>
      <a href="#projects">Projects</a>
      <a href="#contact">Contact</a>
    </div>
  </nav>
</header>

<section class="hero" id="home">
  <div>
    <p class="eyebrow">SOFTWARE DEVELOPER</p>
    <h1>Hi, I'm <span>Muscab Maxamed Abdulahi</span></h1>
    <h2>Building useful things with code.</h2>
    <p>
      Welcome to my portfolio. I'm learning, building projects,
      and developing my skills in computer science and software development.
    </p>
    <div class="buttons">
      <a class="btn" href="#projects">Explore my work</a>
      <a class="btn secondary" href="#contact">Contact me</a>
    </div>
  </div>
</section>

<section id="about">
  <p class="eyebrow">GET TO KNOW ME</p>
  <h2>About Me</h2>
  <div class="card">
    <p>
      I'm Muscab Maxamed Abdulahi, also known as Dalooliye.
      I'm interested in software development, computer science,
      and solving real problems through technology.
    </p>
    <p>
      My goal is to keep learning, build practical applications,
      and work with people who value useful software.
    </p>
  </div>
</section>

<section id="skills">
  <p class="eyebrow">WHAT I'M LEARNING</p>
  <h2>Skills</h2>
  <div class="card">
    <span class="tag">Python</span>
    <span class="tag">HTML</span>
    <span class="tag">CSS</span>
    <span class="tag">JavaScript</span>
    <span class="tag">Flask</span>
    <span class="tag">Problem Solving</span>
  </div>
  <p>Only keep skills you can honestly describe or demonstrate.</p>
</section>

<section id="projects">
  <p class="eyebrow">MY WORK</p>
  <h2>Projects</h2>
  <div class="grid">
    <div class="card">
      <h3>Portfolio Website</h3>
      <p>A responsive personal website built with Python, Flask, HTML and CSS.</p>
      <span class="tag">Python</span><span class="tag">Flask</span>
    </div>
    <div class="card">
      <h3>Student Planner</h3>
      <p>A project idea for organizing study sessions, tasks and deadlines.</p>
      <span class="tag">Python</span>
    </div>
    <div class="card">
      <h3>Business Assistant Bot</h3>
      <p>A project idea for answering common customer questions automatically.</p>
      <span class="tag">Python</span>
    </div>
  </div>
  <p>These are examples and ideas, not claims that you've already built them.
     Replace them with your real work as you complete projects.</p>
</section>

<section id="contact">
  <p class="eyebrow">LET'S CONNECT</p>
  <h2>Contact Me</h2>
  <div class="card">
    <p>Have a project or an opportunity? Feel free to reach out.</p>
    <p>Email: <a class="link" href="mailto:YOUR_EMAIL@example.com">
      YOUR_EMAIL@example.com</a></p>
    <p>GitHub: <a class="link" href="https://github.com/" target="_blank">
      Add your GitHub profile</a></p>
    <p>LinkedIn: <a class="link" href="https://www.linkedin.com/" target="_blank">
      Add your LinkedIn profile</a></p>
  </div>
</section>

<footer>
  © 2026 Muscab Maxamed Abdulahi. Built with Python and Flask.
</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=False)
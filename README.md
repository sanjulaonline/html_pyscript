# AWS Particle Animation

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS" />
  <img src="https://img.shields.io/badge/PyScript-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="PyScript" />
</div>

<div align="center">
  <p>A beautiful interactive particle animation that creates a dynamic AWS logo effect using PyScript and HTML Canvas.</p>
  
  <a href="sample.mp4">
    <img src="https://img.shields.io/badge/View_Demo-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white" alt="View Demo" />
  </a>
</div>

## ✨ Features

- 🔄 Interactive particle animation with AWS logo design
- 🖱️ Responsive to mouse movement and touch interactions
- 📱 Mobile-friendly and fully responsive
- 🎨 Smooth color transitions and beautiful effects
- ⚡ Real-time particle physics simulation
- 🌈 Dynamic color effects based on interaction

## 🎬 Preview

<div align="center">
  <video width="600" controls>
    <source src="sample.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
</div>

## 🧩 Project Structure

```
.
├── index.html          # Main HTML file with PyScript integration
├── main.py             # Python code for particle animation
├── requirements.txt    # Python package dependencies
├── vercel.json         # Vercel deployment configuration
└── netlify.toml        # Netlify deployment 
```

## 🔧 Dependencies

- Python 3.x
- Required Python packages:
  - pyodide==0.21.0
  - pyscript==2024.1.1
  - js==1.0

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/sanjulaonline/aws-particle-animation.git
   cd aws-particle-animation
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

Simply open the `index.html` file in your web browser. PyScript will automatically:
- Load the Python runtime
- Execute the Python code
- Handle the particle animation

No server setup or build process is required!

## ⚙️ Animation Parameters

The main animation function includes several customizable parameters:

```python
def create_particle():
    return {
        "x": x,
        "y": y,
        "base_x": x,
        "base_y": y,
        "size": Math.random() * 1 + 0.5,  # Particle size
        "color": "white",                 # Default particle color
        "scatter": "#FF9900" or "#00DCFF", # Scatter effect color
        "life": Math.random() * 100 + 50   # Particle lifetime
    }
```

You can adjust these parameters to achieve different effects:
- **size**: Controls the size of particles (default: 0.5-1.5)
- **color**: Sets the default particle color
- **scatter**: Defines the color when particles scatter
- **life**: Determines how long particles live before regenerating

## 🔍 How It Works

1. The program creates a canvas element and initializes the AWS logo
2. Generates particles based on the logo's shape
3. Tracks mouse/touch position for interaction
4. Updates particle positions based on:
   - Mouse/touch proximity
   - Base position
   - Physics calculations
5. Renders particles with dynamic colors and effects
6. Continuously animates the scene using requestAnimationFrame

## 🚀 Deployment

### Deploy to Vercel

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy:
   ```bash
   vercel
   ```

### Deploy to Netlify

1. Install Netlify CLI:
   ```bash
   npm install -g netlify-cli
   ```

2. Deploy:
   ```bash
   netlify deploy
   ```

Or deploy through the Netlify website:
1. Push your code to GitHub
2. Go to [Netlify](https://app.netlify.com)
3. Click "New site from Git"
4. Choose your repository
5. Configure build settings:
   - Build command: `pip install -r requirements.txt`
   - Publish directory: `.`
6. Click "Deploy site"

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new particle effects
- Improving the animation performance
- Adding new interactive features
- Reporting issues

## 📞 Contact

For any questions, suggestions, or collaborations, you can reach me on:
- Telegram: [@SiXtySL](https://t.me/SiXtySL)
- GitHub: [@sanjulaonline](https://github.com/sanjulaonline)
- LinkedIn: [Sanjula](https://www.linkedin.com/in/sanjulaherath)
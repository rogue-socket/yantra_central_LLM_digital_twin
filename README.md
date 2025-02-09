# Water Management Digital Twin - AI Simulation & Analysis  

This project is a streamlined AI-powered application utilizing a **Large Language Model (LLM)** to facilitate **water management system simulations** for a digital twin. Built using the **Google API**, this system allows users to interact naturally with the model, request simulations, analyze past runs, and receive intelligent responses to general queries regarding water management systems.  

Deployed Link: https://yantradigitaltwin.streamlit.app/

# 📌 Important Notes  

1. The code is currently modified to suit the running of a **Streamlit application**.  
   - This can be changed by loading the API key into the environment and **uncommenting** the following line of code:  
     ```python
     load_dotenv()
     ```

2. The **simulation engine** is an external factor.  
   - The code for the simulation exists in the file **"test4_1_fin.py"**, but it needs to be **interfaced using a JSON file address**.  
   - Currently, the output is **hardcoded** to demonstrate the functionality of other components. 

## 🚀 Features  

### 1️⃣ Smart Simulation Execution  
- Simply prompt the LLM to **run a water management simulation**.  
- The LLM intelligently:  
  1. **Generates the necessary parameters**  
  2. **Calls the simulation function**  
  3. **Runs the simulation**  
  4. **Collects the output**  
  5. **Analyzes the results** and provides insights  

### 2️⃣ General Water Management & Digital Twin Q&A  
- Ask **any** question related to water management systems or digital twins.  
- The LLM provides accurate, **context-aware responses** based on its training data and external references.  

### 3️⃣ Reviewing & Analyzing Past Simulations  
- Retrieve **insights and analysis** from previous simulations.  
- The LLM reads and interprets past results, providing **key findings, patterns, and recommendations**.  

## 🛠️ Setup & Installation  

### Prerequisites  
- Python 3.11+  
- Google AI API Key  

### Installation Steps  
1. Clone the repository:  

```bash
git clone https://github.com/rogue-socket/yantra_central_LLM_digital_twin.git
cd yantra_central_LLM_digital_twin
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up your Google API Key:

```bash
export GOOGLE_API_KEY="your-api-key-here"
```

## 📌 Usage  

Start the application:

```bash
streamlit run chatbot.py
```

## 📝 Example Prompts

```
> Run a water simulation where the water speed is 5m/s
> What are common water management issues?  
> Analyze the last simulations
``` 

## 🔗 Future Enhancements  
- Integration with real-time digital twin water management data  
- Graphical interface for simulation results, dashboard integration
- Enhanced ML-driven insights based on multiple simulations  

## 🤝 Contributing  
Contributions are welcome! Please submit a pull request or open an issue to discuss improvements.  

## 📜 License  
This project is licensed under the MIT License. See LICENSE for details.  

---

Developed with ❤️ using Google LLM & Langgraph for digital twin water management.

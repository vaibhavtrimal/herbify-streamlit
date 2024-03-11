
# HERBIFY - MEDICINAL PLANT DETECTION 🌿
A simple ML and DL based website that detects medicinal plants.

## DISCLAIMER ⚠️
This project is a Proof of Concept (POC) and comes with no guarantees from the creator. It is not intended for real-world application. The creator bears no responsibility for any use of the project. However, this project showcases the potential of ML/DL in identifying medicinal plants if developed on a larger scale with clean and extensive data.

## MOTIVATION 💪
- Developing a tool for ensuring the authenticity and quality of raw materials used in Ayurvedic medicine.
- Creating an accurate and user-friendly system for identifying various medicinal plants to reduce the risk of misidentification.
- Making the software accessible to all stakeholders in the supply chain, from wholesalers to distributors.

## DATA SOURCE 📊
- [Medicinal Plant Dataset](https://data.mendeley.com/datasets/748f8jkphb/3)

## Notebooks 📓
*Note: The corresponding code will be uploaded to Kaggle Notebooks soon.*

# Built with 🛠️
- Python,Streamlit for the web interface.
- Tesnorflow, CNN for model development
- Numpy,OpenCV, Matplotlib, for data processing and analysis.
- Git for version control.
- Streamlit for deployment.



## DEPLOYMENT 🚀
The website is deployed and accessible [here](https://herbify.streamlit.app/). Note: The website may take a minute to load sometimes due to server hibernation.


## How to use 💻
**Medicinal Plant Detection**: Upload an image of a plant, and wait for the model to predict its classification.

## DEMO



![demo](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWZmNXQ2M3J0MXQwYmxxN3phY2F5aGV5aTBiaWh5OTB0ajhta210YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/V80FSMBPtxbJW26Fgr/giphy.gif)

## Supported plants
- **This model supports for 40 Medicinal plants:**
- Aloevera, Amla, Amruta_Balli, Arali, Ashoka, Ashwagandha, Avacado, Bamboo, Basale, Betel, Betel_Nut, Brahmi, Castor, Curry_Leaf, Doddapatre, Ekka, Ganike, Gauva, Geranium, Henna, Hibiscus, Honge, Insulin, Jasmine, Lemon, Lemon_grass, Mango, Mint, Nagadali, Neem, Nithyapushpa, Nooni, Papaya, Pepper, Pomegranate, Raktachandini, Rose, Sapota, Tulasi, Wood_sorel
**Medicinal Plant Detection**: Upload an image of a plant, and wait for the model to predict its classification.

## How to run locally 🛠️
1. Clone the complete project with git clone ```https://github.com/vaibhavtrimal/herbify-streamlit.git``` or you can just download the code and unzip it

2. Create a virtual environment:
```
python -m venv herbify-env
```

3. Activate the virtual environment:
- On Windows:
  ```
  herbify-env\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source herbify-env/bin/activate
  ```
3. Install the required packages:

```
pip install -r requirements.txt
```

4. Run the application:

```
streamlit run app.py
```

## Contribute 👨‍💻
Contributions are welcome! Please feel free to contribute to the improvement of the project.

## Usage ⚙️
This project can be used as a basis for further development in the field of medicinal plant identification. If you use this project, please credit the original source and link back to this repository.

## Further Improvements 📈
- The dataset can be expanded and refined to improve model accuracy. The current version utilizes a TensorFlow pre-trained MobileNet model for development.
- UI can be improved

## Contact 📞
If you have any questions or would like to contribute, feel free to contact me on [LinkedIn](https://in.linkedin.com/in/vaibhav-trimal-1a6096243).


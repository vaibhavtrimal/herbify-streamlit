import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Classes list
classes = ["Aloevera", "Amla", "Amruta_Balli", "Arali", "Ashoka", "Ashwagandha", "Avocado", "Bamboo", "Basale", "Betel", "Betel_Nut", "Brahmi", "Castor", "Curry_Leaf", "Doddapatre", "Ekka", "Ganike", "Guava", "Geranium", "Henna", "Hibiscus", "Honge", "Insulin", "Jasmine", "Lemon", "Lemon_grass", "Mango", "Mint", "Nagadali", "Neem", "Nithyapushpa", "Nooni", "Papaya", "Pepper", "Pomegranate", "Raktachandini", "Rose", "Sapota", "Tulasi", "Wood_sorrel"]

# Detailed information list
plants_info_list = [
    ["Aloevera", "Aloe barbadensis", "Xanthorrhoeaceae", "Succulent plant used for wound healing and skin soothing.", "Used in cosmetics, lotions, and gels."],
    ["Amla", "Phyllanthus emblica", "Phyllanthaceae", "Indian gooseberry rich in Vitamin C and antioxidants.", "Used in Ayurvedic medicine for various health benefits."],
    ["Amruta_Balli", "Tinospora cordifolia", "Menispermaceae", "Indian creeper known for its immune-boosting properties.", "Used in Ayurvedic medicine for treating fevers and respiratory problems."],
    ["Arali", "Ficus elastica", "Moraceae", "Rubber tree, popular ornamental plant with air-purifying properties.", "Grown indoors for decoration and air purification."],
    ["Ashoka", "Saraca asoca", "Caesalpiniaceae", "Indian flowering tree with religious significance.", "Used in Ayurvedic medicine for female health issues."],
    ["Ashwagandha", "Withania somnifera", "Solanaceae", "Adaptogenic herb known for reducing stress and anxiety.", "Used in Ayurvedic medicine for improving sleep and overall well-being."],
    ["Avocado", "Persea americana", "Lauraceae", "Fruit tree with creamy, nutrient-rich fruit.", "Eaten as a fruit, used in guacamole and various dishes."],
    ["Bamboo", "Bambusoideae", "Poaceae", "Fast-growing grass with diverse uses in construction and crafts.", "Used for making furniture, flooring, and other construction materials."],
    ["Basale", "Ocimum basilicum", "Lamiaceae", "Sweet basil, a culinary herb with a distinctive aroma.", "Used in various cuisines for adding flavor to dishes."],
    ["Betel", "Piper betle", "Piperaceae", "Climbing vine with leaves used in a cultural practice in Asia.", "Leaves are chewed with lime and betel nut, with potential health risks."],
    ["Betel_Nut", "Areca catechu", "Arecaceae", "Seed of a palm tree, chewed with betel leaf, addictive and potentially carcinogenic.", "Used in a cultural practice in Asia, but has health risks."],
    ["Brahmi", "Bacopa monnieri", "Scrophulariaceae", "Creeping herb used in Ayurvedic medicine for cognitive health.", "Used to improve memory, focus, and learning."],
    ["Castor", "Ricinus communis", "Euphorbiaceae", "Spiny plant with toxic seeds, but oil is used in laxatives.", "Castor oil is used for constipation relief, but the plant itself is poisonous."],
    ["Curry_Leaf", "Murraya koenigii", "Rutaceae", "Fragrant leaves used as a seasoning in South Asian cuisine.", "Adds a distinctive flavor to curries, dals, and other dishes."],
    ["Doddapatre", "Centella asiatica", "Apiaceae", "Gotu kola, a perennial herb used in wound healing and skin care.", "Used topically for wound healing and to improve skin health."],
    ["Ekka", "Aegle marmelos", "Rutaceae", "Bael fruit tree, with religious significance in India.", "Fruit is eaten ripe or used in Ayurvedic medicine for digestive issues."],
    ["Ganike", "Solanum angulata", "Solanaceae", "Prickly eggplant, a vegetable used in South Asian cuisine.", "Eaten as a cooked vegetable, similar to eggplant."],
    ["Gauva", "Psidium guajava", "Myrtaceae", "Tropical fruit tree with a sweet, tangy fruit.", "Eaten fresh, used in jams, juices, and desserts."],
    ["Geranium", "Pelargonium", "Geraniaceae", "Popular flowering plant with various species and colors.", "Grown as ornamental plants for balconies, gardens, and indoors."],
    ["Henna", "Lawsonia inermis", "Lythraceae", "Shrub with leaves used for making henna paste for temporary body art.", "Used for creating intricate henna designs on hands and feet."],
    ["Hibiscus", "Hibiscus rosa-sinensis", "Malvaceae", "Flowering shrub with large, showy flowers in various colors.", "Grown as ornamental plants and used in some cultures for beverages."],
    ["Honge", "Pongamia pinnata", "Fabaceae", "Karanji tree, with oil used for biofuel and soap production.", "Seed oil is a potential source of renewable biofuel."],
    ["Insulin", "Costus igneus", "Costaceae", "Spiral ginger, a medicinal plant used in diabetes management.", "Used in traditional medicine for its potential blood sugar-lowering effects."],
    ["Jasmine", "Jasminum officinale", "Oleaceae", "Fragrant flowering vine, with flowers used in"],
    ["Lemon", "Citrus limon", "Rutaceae", "Citrus fruit known for its acidic juice and vitamin C content.", "Used in beverages, cooking, and cleaning."],
    ["Lemon_grass", "Cymbopogon citratus", "Poaceae", "Grass with a lemony aroma, used as a flavoring agent in Asian cuisine.", "Used in curries, soups, and teas for its lemongrass flavor."],
    ["Mango", "Mangifera indica", "Anacardiaceae", "Tropical fruit tree with a sweet, juicy fruit.", "Eaten fresh, used in juices, jams, and chutneys."],
    ["Mint", "Mentha spp.", "Lamiaceae", "Herb with various aromatic species used in cooking and teas.", "Used in salads, desserts, and beverages for its refreshing flavor."],
    ["Nagadali", "Mesua ferrea", "Clusiaceae", "Indian ironwood tree with fragrant flowers used in perfumes.", "Used in traditional medicine and for making perfumes."],
    ["Neem", "Azadirachta indica", "Meliaceae", "Multipurpose tree with leaves used for medicinal and insecticidal purposes.", "Used in Ayurvedic medicine and as a natural pesticide."],
    ["Nithyapushpa", "Cestrum nocturnum", "Solanaceae", "Night-blooming jasmine, with fragrant flowers used for decoration.", "Grown for its beautiful, fragrant flowers that bloom at night."],
    ["Nooni", "Morinda citrifolia", "Rubiaceae", "Noni fruit tree with a strong-smelling fruit used in juices and supplements.", "Used in alternative medicine for various health claims, but scientific evidence is limited."],
    ["Pappaya", "Carica papaya", "Caricaceae", "Tropical fruit tree with a delicious, fleshy fruit.", "Eaten fresh, used in juices, and has digestive enzyme properties."],
    ["Pepper", "Piper nigrum", "Piperaceae", "Spice plant with black peppercorns used for adding heat and flavor.", "Used in savory dishes around the world."],
    ["Pomegranate", "Punica granatum", "Lythraceae", "Fruit tree with a jewel-toned, antioxidant-rich fruit.", "Eaten fresh, used in juices, and has potential health benefits."],
    ["Raktachandini", "Ixora coccinea", "Rubiaceae", "Jungle flame flower, a shrub with vibrant red flowers.", "Grown as an ornamental plant for its showy flowers."],
    ["Rose", "Rosa spp.", "Rosaceae", "Flowering shrub with beautiful blooms and fragrant varieties.", "Grown as ornamental plants, used in bouquets, and for fragrance products."],
    ["Sapota", "Manilkara zapota", "Sapotaceae", "Sapodilla fruit tree with a sweet, brown sugar-like flavor.", "Eaten fresh, used in ice cream, and other desserts."],
    ["Tulasi", "Ocimum tenuiflorum", "Lamiaceae", "Holy basil, a sacred plant in Hinduism with medicinal uses.", "Used in Ayurvedic medicine for respiratory problems and stress relief."],
    ["Wood_sorrel", "Oxalis spp.", "Oxalidaceae", "Delicate clover-like plant with edible leaves with a sour taste.", "Used in salads and as a garnish for its unique flavor."]
]


# Load your pre-trained model
model = load_model('mobilenet_model.h5')

# Prediction function
def predict_image_with_confidence(image, confidence_threshold=0.6):
    img = cv2.resize(image, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    predicted_confidence = np.max(predictions)

    if predicted_confidence > confidence_threshold:
        predicted_class = classes[np.argmax(predictions)]
        n=np.argmax(predictions)
        return f"**Predicted class: {predicted_class} with confidence: {predicted_confidence:.2f}** \n\n**Botanical Name**: {plants_info_list[n][1]}\n\n**Family**: {plants_info_list[n][2]}\n\n**About**: {plants_info_list[n][3]}\n\n**Uses**: {plants_info_list[n][4]}"
    
    else:
        return "Prediction confidence is too low. Unable to classify image."

# Streamlit UI
st.title('Medicinal Plant Detection')

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    # Convert the file to an opencv image.
    file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # Display the uploaded image
    st.image(opencv_image, channels="BGR", caption="Uploaded Image")

    # Predict and display the result
    result = predict_image_with_confidence(opencv_image)
    st.write(result)

import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model

BASE_DIR = "./"

MODEL_PATH = os.path.join(BASE_DIR, "model/bitki_secim_model.h5")
MODEL_COLUMNS = os.path.join(BASE_DIR, "model_columns.csv")

FRONT_DIR = os.path.join(BASE_DIR, "images/front_view")
TOP_DIR   = os.path.join(BASE_DIR, "images/top_view")

EXCEL_PATH = os.path.join(BASE_DIR, "morphology.xlsx")

# Load expected features
model_features = pd.read_csv(MODEL_COLUMNS, header=None)[0].tolist()

# Load morphology
df = pd.read_excel(EXCEL_PATH)
bitki_ids = df["Bitki_Adi"].astype(str)

df = df.drop(columns=["Bitki_Adi"], errors="ignore")

categorical_cols = df.select_dtypes(include=["object"]).columns
numerical_cols = df.select_dtypes(exclude=["object"]).columns

df[categorical_cols] = df[categorical_cols].fillna("Bilinmiyor")
df_encoded = pd.get_dummies(df, columns=categorical_cols)

df_encoded[numerical_cols] = df_encoded[numerical_cols].fillna(
    df_encoded[numerical_cols].mean()
)

scaler = StandardScaler()
df_encoded[numerical_cols] = scaler.fit_transform(df_encoded[numerical_cols])

X_aligned = pd.DataFrame(0.0, index=df_encoded.index, columns=model_features)
common_cols = list(set(df_encoded.columns) & set(model_features))
X_aligned[common_cols] = df_encoded[common_cols]

X_morph = X_aligned.values.astype(np.float32)

def load_image(path):
    img = load_img(path, target_size=(224,224))
    return img_to_array(img) / 255.0

front_imgs, top_imgs = [], []

for bid in bitki_ids:
    f = os.path.join(FRONT_DIR, f"{bid}.jpg")
    t = os.path.join(TOP_DIR, f"{bid}.jpg")
    if os.path.exists(f) and os.path.exists(t):
        front_imgs.append(load_image(f))
        top_imgs.append(load_image(t))

front_imgs = np.array(front_imgs)
top_imgs = np.array(top_imgs)

model = load_model(MODEL_PATH)
predictions = model.predict([front_imgs, top_imgs, X_morph[:len(front_imgs)]])

print("Inference completed.")

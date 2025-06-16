# 🚗 ADAS: Object Detection and Tracking for Low-Visibility Conditions

An Advanced Driver Assistance System (ADAS) prototype that improves on-road safety during adverse weather and lighting conditions using thermal camera input and real-time object detection and tracking. Developed with YOLOv4, DeepSORT, and OpenCV.

---

## 📌 Project Overview

Low visibility due to fog, rain, and nighttime driving contributes to a large percentage of road accidents. This system uses a thermal imaging camera to detect and track objects (pedestrians, vehicles, etc.) on the road, even in poor visibility conditions. The information is then projected onto a Heads-Up Display (HUD) for real-time driver assistance.

---

## 🎯 Features

* ✅ Real-time object detection using **YOLOv4**
* 🔄 Object tracking with **DeepSORT**
* 🌡️ Uses **thermal camera input** (IR) instead of traditional RGB
* 🧠 Audio interface with **speech recognition** and **text-to-speech**
* 🌦️ Displays **weather and time information**
* 🧩 Modular Python code for detection, tracking, HUD rendering
* 📍 Includes live geolocation capabilities (Google Maps API)

---

## 🧰 Tech Stack

| Category           | Tools/Technologies              |
| ------------------ | ------------------------------- |
| Language           | Python                          |
| Object Detection   | YOLOv4                          |
| Object Tracking    | DeepSORT                        |
| GUI & Display      | OpenCV, Custom HUD              |
| Location           | Google Maps API                 |
| Audio Interaction  | `pyttsx3`, `speech_recognition` |
| Development Tools  | Spyder IDE, Anaconda            |
| Dataset (optional) | MS COCO (for model training)    |

---

## 🧪 System Architecture

1. **Thermal camera** captures video in IR spectrum.
2. **YOLOv4** detects objects in real-time.
3. **DeepSORT** tracks detected objects with unique IDs.
4. **OpenCV** displays output on simulated HUD with overlaid object labels.
5. **Voice command** triggers system start; weather/time info provided.
6. **Live geolocation** is retrieved using Google Maps API.

---

## 📂 Project Structure

```
ADAS-Visibility-System/
│
├── main.py              # Entry point with voice command handling
├── dot.py               # Core detection logic (YOLOv4 + DeepSORT)
├── object_tracker.py    # Object tracking via DeepSORT
├── livelocation.py      # Location services using Google Maps API
├── addsymbol.py         # HUD symbol rendering
├── directions.py        # Find direction to a location using Google Maps API
├── text2speech.py       # Convert text to speech
├── dateweather.py       # Get the current date and time
├── speech2text.py       # Convert speech to text
├── /model/              # YOLOv4 weights and config files
├── /docs/               # Phase reports and dissertation
└── README.md            # This file
```

---

## ▶️ Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ADAS-Visibility-System.git
   cd ADAS-Visibility-System
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**

   * Replace your Google Maps API key in `livelocation.py`

4. **Run the system**

   ```bash
   python main.py
   ```

---

## 📈 Future Improvements

* Integrate with real-time vehicle HUDs
* Hardware prototype with IR camera module
* Road condition detection (wet, icy, etc.)
* More robust voice command handling

---

## 📜 License

This project is open-source under the [MIT License].

---

## 🙌 Acknowledgements

* Dr. Doddegowda B. J (Guide, AMCEC)
* David Corne (Supervisor, Heriot-Watt University)
* My project partners: Akshay, Harish, Devraj

---

Let me know if you’d like a zipped GitHub structure for this one too!


Extra Large Files that could not be uploaded due to size limits can be found in the link below.
https://drive.google.com/drive/folders/1F3CiQUp--0y89J7c_4JHThiV3NJPq5rF?usp=sharing
You can find the path of the files in the .gitignore file

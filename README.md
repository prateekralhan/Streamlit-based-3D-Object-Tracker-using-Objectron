# ☕📷 3D Object Tracker 👞🪑 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A simple 3D Object Tracking webapp for humans built using streamlit.

### Supports Images 📸✅
![image_demo](https://user-images.githubusercontent.com/29462447/155856376-464e6f70-ce7a-4c05-ab21-4ac52c072b18.gif)

### Supports Live Feed from Webcam 📽✅
![demo](https://user-images.githubusercontent.com/29462447/155856202-7e1e7896-1051-40bb-8b89-7b7293d0ca8c.gif)


## Installation:
Simply run ***pip install -r requirements.txt*** to install all the dependencies.

## Usage:
1. Clone this repository and install the dependencies as mentioned above.
2. Simply run the command: ***streamlit run app.py***
3. Navigate to http://localhost:8501 in your web-browser.

## Results:

#### Images 📸✅

![cup_live_feed](https://user-images.githubusercontent.com/29462447/155856334-f495f8db-01ba-499b-815a-31cc4374010c.png)
![shoe_live_feed](https://user-images.githubusercontent.com/29462447/155856338-83d0eab9-0817-4e38-a371-efe36f5fe88d.png)

| **Cups**  | **Shoes**  |
|-----------|------------|
| ![output_cup_3](https://user-images.githubusercontent.com/29462447/155856484-42663f2b-6d87-43c1-995e-8eb5adf44c58.jpg) | ![output_shoe_2](https://user-images.githubusercontent.com/29462447/155856514-351bac6b-05c1-47f7-a690-5dbd71a34220.jpg)  | 
| ![output_cup_1](https://user-images.githubusercontent.com/29462447/155856502-448226b7-2141-41d8-b41b-ed83bd14ff35.png) | ![output_shoe_1](https://user-images.githubusercontent.com/29462447/155856517-4d347493-2d7d-4bcd-813b-6b30b2b5c1dc.jpg)  | 

| **Chairs** | **Camera** |
|------------|------------|
| ![output_chair_1](https://user-images.githubusercontent.com/29462447/155856533-182c17ea-b078-4f30-8f9a-2843c78df136.jpg) | ![output_camera_1](https://user-images.githubusercontent.com/29462447/155856559-284b043b-afaa-4e39-a463-b1183e1a0b7a.jpg) |
| ![output_chair_2](https://user-images.githubusercontent.com/29462447/155856531-9a2436ea-a05e-4a34-be86-33178b79193a.jpg) | ![output_camera_3](https://user-images.githubusercontent.com/29462447/155856561-824c5bb4-2725-450f-bf2f-4dfa31a4c447.jpg) |

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```

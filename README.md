# gta-car-ai, fully autonomous driving model

Project is deeply inspired by a [video](https://www.youtube.com/watch?v=KSX2psajYrg&list=PLQVvvaa0QuDeETZEOy4VdocT7TOjfSA8a&index=14&ab_channel=sentdex) created by [Sentdex](https://www.youtube.com/c/sentdex) i found on YouTube long time ago. I was curious if i can achieve some decent result by myself.

## Instructions

```
drive.py
```
It's main script, run it to start collecting data and send predictions to virtual joystick. It takes screenshots of your game window and processes them like it is shown on the picture:


![Alt text](https://github.com/MrKubul/gta-car-ai/blob/main/Assets/car.png)

## Model v1.0
Data consists mainly highways, roads are empty and speed is stable value. Main goal for model is to keep car beetween lines, and turn when needed. Thats first implementation and dataset is fairly small.

https://user-images.githubusercontent.com/57231340/163730420-84b2a90a-5d3a-4f31-b44a-b932e946b478.mp4

Model performs ok. It clearly got some intuition about roadlines and can drive even curviest routes, but it's kinda wobbly and drives on the lines all the time.

## Model v2.0(work in progress..)
Much bigger model, trained on full images of road.
Full PDF file documenting process of development is comming soon.

import whisper

model = whisper.load_model("base")
result = model.transcribe("radical_cohere_hackathon/utils/Never Gonna Give You Up.mp4")
print(result["text"])
x=0 #using as a breakpoint
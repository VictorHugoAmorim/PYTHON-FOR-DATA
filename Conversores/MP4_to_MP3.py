import moviepy.editor

#Carregar video
local = input("Favor informar localização do arquivo\n")

video = moviepy.editor.VideoFileClip(local)

# Extrai o audio
audio_data = video.audio

#Salva o arquivo de áudio extraído do vídeo
audio_data.write_audiofile(local+".mp3")

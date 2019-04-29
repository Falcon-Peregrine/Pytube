from pytube import YouTube
from pytube import Playlist
import os


link = ''



link = input('Copy the link:')

try:
    yt = YouTube(link)

    stream = yt.streams.filter(
        progressive=True, subtype='mp4',
        ).order_by('resolution').desc().first()
    #print(stream)
    stream.download()
    print('File downloaded successfully')
    
    try:
    	name = stream.default_filename
    	caption = yt.captions.get_by_language_code('en').generate_srt_captions()
    	saveSrt = open(os.path.abspath('.')+'/'+str(name)+'.srt', 'w')
    	saveSrt.write(caption)
    	saveSrt.close()
    except Exception as e:
    	print(str(e))

except Exception as e:
    print(str(e))






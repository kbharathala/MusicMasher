from urllib.request import urlopen
import urllib.request
import wget

def get_contents(url):
    full_text = ""
    for line in urlopen(url):
        lineStr = str(line)
        full_text = (full_text + lineStr)
    return full_text

def get_download_link(song_name):
	contents = get_contents("http://www.midiworld.com/search/?q=" + song_name.replace(" ", "+"))
	if(contents.find("found nothing!") != -1):
		return False
	start = contents.find("http://www.midiworld.com/download/")
	end = contents[start:].find("\" target")
	return contents[start:start+end]

def download_file(song_name):
	wget.download(get_download_link(song_name))
	return(True)

print(download_file("Thinking out loud"))
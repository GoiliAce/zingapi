from zingapi import ZingMp3, getUrlTypeAndID

# getUrlTypeAndID("https://zingmp3.vn/liveradio/IWZ979CW.html")
zi = ZingMp3()
for song in zi.getDetailPlaylist("ZB08FIBW").songs:
    print(song.getStreaming())
# zi.getDetailArtist("Cammie")
# zi.getRadioInfo("IWZ979CW")
# zi.getSongInfo("ZWAF6UFD")
# zi.getSongStreaming("ZWAF6UFD")
# zi.getTop100()
# zi.search("rick roll")
# print(zi.getHub())
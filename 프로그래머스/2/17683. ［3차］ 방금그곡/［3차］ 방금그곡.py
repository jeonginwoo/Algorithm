import re

def solution(m, musicinfos):
    
    # def tab_to_s(tab:str)->str:
    #     d = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a"}
    #     s = ""
    #     for i in range(1, len(tab)):
    #         if tab[i] == "#":
    #             s += d[tab[i-1] + tab[i]]
    #         elif tab[i-1] != "#":
    #             s += tab[i-1]
    #     if tab[-1] != "#":
    #         s += tab[-1]
    #     return s
    
    def tab_to_s(tab: str) -> str:
        d = {"C#": "c", "D#": "d", "F#": "f", "G#": "g", "A#": "a", "B#": "b"}
        return re.sub(r"C#|D#|F#|G#|A#|B#", lambda x: d[x.group()], tab)

    def h_to_m(time: str) -> int:
        h, m = map(int, time.split(":"))
        return h * 60 + m

    m = tab_to_s(m)

    for i in range(len(musicinfos)):
        musicinfo = musicinfos[i].split(",")
        musicinfo[0] = h_to_m(musicinfo[0])
        musicinfo[1] = h_to_m(musicinfo[1])
        temp = tab_to_s(musicinfo[3])
        length = musicinfo[1] - musicinfo[0]
        musicinfo[3] = (temp * (length // len(temp) + 1))[:length]
        musicinfos[i] = musicinfo

    musicinfos.sort(key=lambda x: (x[0] - x[1], x[0]))

    for musicinfo in musicinfos:
        if m in musicinfo[3]:
            return musicinfo[2]

    return "(None)"
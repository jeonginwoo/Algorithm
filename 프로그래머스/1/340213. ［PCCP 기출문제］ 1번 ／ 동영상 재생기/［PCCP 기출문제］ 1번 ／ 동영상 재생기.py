def solution(video_len, pos, op_start, op_end, commands):
    def m_to_s(time:str):
        t = [int(x) for x in time.split(":")]
        return t[0]*60 + t[1]
    
    def s_to_m(time:int):
        return f"{time//60:02d}:{time%60:02d}"
    
    vl = m_to_s(video_len)
    p = m_to_s(pos)
    os = m_to_s(op_start)
    oe = m_to_s(op_end)
    
    for command in commands:
        if os <= p < oe:
            p = oe
        if command == "prev":
            p = max(0, p-10)
        elif command == "next":
            p = min(vl, p+10)
        else:
            print("error")
    if os <= p < oe:
        p = oe
    
    return s_to_m(p)
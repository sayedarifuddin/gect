       import language_tool_python
        tl = language_tool_python.LanguageTool('en-US')
    
        txt = "good mooorning sirr and medam my namee anderen i am from amerecia !"
        m = tl.check(txt)
        len(m)

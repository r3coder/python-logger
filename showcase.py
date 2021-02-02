from log import Log

Log.Print("Hello!")

Log.Print("I don't need timestamp",current=False)

Log.Print("I'm ALONE",current=False,elapsed=False)

Log.Print("I'm red",col="r")

Log.Print("not I'm blue",bg="b")

Log.Print("Don't go next line",end="\t")

Log.Print("Yes, you could...",current=False,elapsed=False)

Log.Print("I'm level 1", level=1)

Log.SetPrintLevel(2)

Log.Print("I'm level 1, again", level=1)

Log.SetPrintLevel(0)

Log.Print("I'll be flushed! Nooo",flush=True)

Log.Print("But my hope will never die")

Log.SetMessages(False)

Log.SetPrintLevel(1)

Log.SetPrintLevel(0)

Log.SetMessages(True)

Log.SetMSPrecision(5)

Log.Print("Five")

Log.SetMSPrecision(0)

Log.Print("ZERO")

Log.SetMSPrecision(3)

Log.Print("Three!")
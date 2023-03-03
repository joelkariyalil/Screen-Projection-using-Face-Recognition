'''import wx,time
app=wx.App()
dc=wx.ScreenDC()
dc.SetBrush(wx.Brush("black",wx.SOLID)) 
dc.SetPen(wx.Pen((0, 0, 0), width=3, style=wx.PENSTYLE_SOLID))
dc.DrawLine(100,100,500,500)
#time.sleep(10)
dc.Clear()

import wx
app=wx.App()
dc=wx.ScreenDC()
panel = wx.Panel()
dc.SetBrush(wx.Brush("black",wx.SOLID)) 
dc.SetPen(wx.Pen((0, 0, 0), width=3, style=wx.PENSTYLE_SOLID))
dc.DrawLine(100,100,500,500)
dc.Clear()

# and then
dc.Refresh()

app.MainLoop()


import wx

class DrawPanel(wx.Frame):

    """Draw a line to a panel."""

    def __init__(self):
        wx.Frame.__init__(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetBrush(wx.Brush("black",wx.SOLID)) 
	  #dc.SetPen(wx.Pen((0, 0, 0), width=3, style=wx.PENSTYLE_SOLID))
        dc.DrawLine(100, 100, 500, 500)

app = wx.App(False)
frame = DrawPanel()
frame.Show()
app.MainLoop()


import wx

app = wx.App(False)

frame = wx.Frame(None, title="Draw on Panel")
panel = wx.Panel(frame)

def on_paint(event):
    dc = wx.PaintDC(event.GetEventObject())
    dc.Clear()
    dc.SetPen(wx.Pen("BLACK", 4))
    dc.DrawLine(0, 0, 50, 50)

panel.Bind(wx.EVT_PAINT, on_paint)

frame.Show(True)
app.MainLoop()

'''

import wx

class DrawPanel(wx.Frame):

    """Draw a line to a panel."""

    def __init__(self):
        wx.Frame.__init__(self)
        self.Bind(wx.EVT_PAINT, self.OnPaint)

    def OnPaint(self, event=None):
        dc = wx.PaintDC(self)
        dc.Clear()
        dc.SetPen(wx.Pen(wx.BLACK, 4))
        dc.DrawLine(0, 0, 50, 50)

app = wx.App(False)
frame = DrawPanel()
frame.Show()
app.MainLoop()
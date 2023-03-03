import wx

# init
app=wx.App()
dc=wx.ScreenDC()

# set line and fill style
dc.SetBrush(wx.Brush("black",wx.SOLID)) 
dc.SetPen(wx.Pen((0, 0, 0), width=3, style=wx.PENSTYLE_SOLID))

# draw (x, y, width, height)

dc.DrawRectangle(100, 100, 200, 100)
""" import colorise

colorise.cprint("Hola, mundo", fg="#ff0080", bg="#99ffff") """

import wx

aplicacion = wx.App()
ventana = wx.Frame(parent = None, title="Hola Olimanteca!!")
ventana.Show()
aplicacion.MainLoop()

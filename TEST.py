import Tkinter as tk
from nredarwin.webservice import DarwinLdbSession
import time



def callback():
    darwin_session = DarwinLdbSession(wsdl='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2015-05-14', api_key = '6adcdf6a-2b06-40e0-8436-469c4468a679')
    crs_code = "HGY"
    board = darwin_session.get_station_board(crs_code)
    tex.delete(1.0, tk.END)
    s = "\nNext departures for %s" % (board.location_name)
    t = """
-------------------------------------------------------------------------------
|  PLAT  | DEST                                        |   SCHED   |    DUE   |
------------------------------------------------------------------------------- """
    tex.insert(tk.END, s + t)
    tex.see(tk.END)

    for service in board.train_services:
        u = ("| %6s | %43s | %9s | %8s |\n" %(service.platform or "", service.destination_text, service.std, service.etd))
                 # Scroll if necessary
        tex.insert(tk.END, u)
        tex.see(tk.END)
    v = "-------------------------------------------------------------------------------\n"
    tex.insert(tk.END, v)
    tex.see(tk.END)
    timey = time.asctime()
    tex.insert(tk.END, timey)
    
    top.after(1000, callback)


    
top = tk.Tk()
top.title("Departure Board for Harringay Station")
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
callback()
top.mainloop()

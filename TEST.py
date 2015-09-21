import Tkinter as tk
from nredarwin.webservice import DarwinLdbSession


darwin_session = DarwinLdbSession(wsdl='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2015-05-14', api_key = '6adcdf6a-2b06-40e0-8436-469c4468a679')

crs_code = "HGY"

board = darwin_session.get_station_board(crs_code)

def cbc(id, tex):
    return lambda : callback(id, tex)

def callback():
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
    v = "-------------------------------------------------------------------------------"
    tex.insert(tk.END, v)
    tex.see(tk.END)

    
top = tk.Tk()
tex = tk.Text(master=top)
tex.pack(side=tk.RIGHT)
bop = tk.Frame()
bop.pack(side=tk.LEFT)
tv = 'Refresh'
b = tk.Button(bop, text=tv, command=callback())
b.pack()

tk.Button(bop, text='Exit', command=top.destroy).pack()
top.mainloop()

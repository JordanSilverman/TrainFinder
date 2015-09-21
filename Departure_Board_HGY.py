from nredarwin.webservice import DarwinLdbSession

# initiate a session
# this depends on the DARWIN_WEBSERVICE_API_KEY environment variable
# The WSDL environment variable also allows for

def HGY_dep_board():
    darwin_session = DarwinLdbSession(wsdl='https://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2015-05-14', api_key = '6adcdf6a-2b06-40e0-8436-469c4468a679')

    crs_code = "HGY"

# retrieve departure board
    board = darwin_session.get_station_board(crs_code)

# print table header
    print("\nNext departures for %s" % (board.location_name))
    print("""
-------------------------------------------------------------------------------
|  PLAT  | DEST                                        |   SCHED   |    DUE   |
------------------------------------------------------------------------------- """)

# Loop through services
    for service in board.train_services:
        print("| %6s | %43s | %9s | %8s |" %(service.platform or "", service.destination_text, service.std, service.etd))

 #Print a footer 
    print("-------------------------------------------------------------------------------")


HGY_dep_board()




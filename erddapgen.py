import os
from subprocess import call

def main():
    print "Please select from one of the following options:"
    print "pub: public     |    pri: private" 
    pubOrPri = raw_input()

    while not (pubOrPri=="pub" or pubOrPri=="pri"):
        print("error: invalid input. Please enter \"pri\" or \"pub\"")
        answer=raw_input()
    if pubOrPri=="pub":
        printPublicDatasets()
        genPublic()        
    if pubOrPri=="pri":
        print "not yet implemented :("



        
  
def genPublic():
    selection = raw_input("Select from the above: ")
    print selection
    if int(selection) > 42 or int(selection) < 1:
        print("invalid input")
        exit()
    os.chdir("/usr/local/tomcat2/webapps/erddap/WEB-INF")

    command = "./GenerateDatasetsXML.sh"
    option1 = "EDDGridFromThreddsCatalog"
    option2 = "http://apdrc.soest.hawaii.edu/thredds/catalog/las/catalog.xml"
    option3 = "\"\""

    if selection=="1":
        regex=".*_Argo_Products_.*"
    elif selection=="2":
        regex=".*_CFSv2_.*"
    elif selection=="3":
        regex=".*_CMIP5_.*"
    elif selection=="4":
        regex=".*_CSIRO_Atlas_.*"
    elif selection=="5":
        regex=".*_CliPAS_.*"
    elif selection=="6":
        regex=".*_CDASK1.4_.*"
    elif selection=="7":
        regex=".*_ECCO2_.*"
    elif selection=="8":
        regex=".*_ERA-40_.*"
    elif selection=="9":
        regex=".*_ERA75deg_.*"
    elif selection=="10":
        regex=".*_FRA-JCOPE2_.*"
    elif selection=="11":
        regex=".*_GAME_.*"
    elif selection=="12":
        regex=".*_GFDL_.*"
    elif selection=="13":
        regex=".*_HadSST_.*"
    elif selection=="14":
        regex=".*_ISVHE_.*"
    elif selection=="15":
        regex=".*_Interpolated_precipitation_.*"
    elif selection=="16":
        regex=".*_J-OFURO2_.*"
    elif selection=="17":
        regex=".*_KYUSHU_.*"
    elif selection=="18":
        regex=".*_Model_output_.*"
    elif selection=="19":
        regex=".*_NCOM_.*"
    elif selection=="20":
        regex=".*_NLOM_.*"
    elif selection=="21":
        regex=".*_NLOM_32_.*"
    elif selection=="22":
        regex=".*_NOAA_SST_.*"
    elif selection=="23":
        regex=".*_Ocean_Climatology_.*"
    elif selection=="24":
        regex=".*_PODAAC_.*"
    elif selection=="25":
        regex=".*_PRIDE_.*"
    elif selection=="26":
        regex=".*_Paleoclimate_modeling_.*"
    elif selection=="27":
        regex=".*_Reanalysis_Data_.*"
    elif selection=="28":
        regex=".*_SCUD_.*"
    elif selection=="29":
        regex=".*_SOCAT_.*"
    elif selection=="30":
        regex=".*_SODA_.*"
    elif selection=="31":
        regex=".*_Tohoku_.*"
    elif selection=="32":
        regex=".*_Typhoon_Reanalysis_.*"
    elif selection=="33":
        regex=".*_WASWind_.*"
    elif selection=="34":
        regex=".*_WHOI_OAFlux_.*"
    elif selection=="35":
        regex=".*_WOA_.*"
    elif selection=="36":
        regex=".*_bimodal_ISO_index_.*"
    elif selection=="37":
        regex=".*_hydrobase_.*"
    elif selection=="38":
        regex=".*_hydrological_data_.*"
    elif selection=="39":
        regex=".*_iCOADS_.*"
    elif selection=="40":
        regex=".*_satellite_product_.*"
    elif selection=="41":
        regex=".*_topography_.*"
    elif selection=="42":
        regex=".*_LOCA_.*"


    call([command, option1, option2, regex, option3])

    print("finished call lol")

    #print(regex)


def printPublicDatasets():
    print("1: Argo Products\t\t2: CFSv2")
    print("3: CMIP5\t\t\t4: CSIRO Atlas")
    print("5: CliPAS\t\t\t6: CDASK1.4")
    print("7: ECCO2\t\t\t8: ERA-40")
    print("9: ERA75deg\t\t\t10:FRA-JCOPE2")
    print("11:GAME\t\t\t\t12:GFDL")
    print("13:HadSST\t\t\t14:ISVHE")
    print("15:Interpolated Precipitation\t16:J-OFURO")
    print("17:KYUSHU\t\t\t18:Model output")
    print("19:NCOM\t\t\t\t20:NLOM")
    print("21:NLOM32\t\t\t22:NOAA SST")
    print("23:Ocean climatology\t\t24:PODAAC")
    print("25:PRIDE\t\t\t26:Paleoclimate modeling")
    print("27:Reanalysis Data\t\t28:SCUD")
    print("29:SOCAT\t\t\t30:SODA")
    print("31:Tohoku\t\t\t32:Typhoon Reanalysis")
    print("33:WASWind\t\t\t34:WHOI OAFlux")
    print("35:WOA\t\t\t\t36:bimodal ISO index")
    print("37:hydrobase\t\t\t38:hydrological data")
    print("39:iCOADS\t\t\t40:Satellite Product")
    print("41:topography\t\t\t42:Loca")

if __name__ == "__main__":
    main()



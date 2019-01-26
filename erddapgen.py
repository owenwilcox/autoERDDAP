import os
import subprocess

def main():
    print "Please select from one of the following options:"
    print "pub: public     |    pri: private" 
    pubOrPri = raw_input()

    while not (pubOrPri=="pub" or pubOrPri=="pri"):
        print("error: invalid input. Please enter \"pri\" or \"pub\"")
        answer=raw_input()
    if pubOrPri=="pub":
        printPublicDatasets()
        filename = genPublic()
        fullFilename = "/usr/local/tomcat2/content/erddap/" + filename + ".xml"
        print fullFilename    
        subprocess.call(["mv", "./temp/EDDGridFromThreddsCatalog.xml", fullFilename])
        subprocess.call(["rm", "/usr/local/tomcat2/content/erddap/datasets.xml"])

    if pubOrPri=="pri":
        print "not yet implemented :("



        
  
def genPublic():
    selection = raw_input("Select from the above: ")
    #print selection
    if int(selection) > 43 or int(selection) < 1:
        print("invalid input")
        exit()
    os.chdir("/usr/local/tomcat2/webapps/erddap/WEB-INF")

    command = "/usr/local/tomcat2/webapps/erddap/WEB-INF/GenerateDatasetsXml.sh"
    option1 = "EDDGridFromThreddsCatalog"
    option2 = "http://apdrc.soest.hawaii.edu/thredds/catalog/las/catalog.xml"
    option3 = "\"\""

    if selection=="1":
        regex=".*_Argo_Products_.*"
        filename="datasets1_Argo_Products"

    elif selection=="2":
        regex=".*_CFSv2_.*"
        filename="datasets2_CFSv2"

    elif selection=="3":
        regex=".*_CMIP5_.*"
        filename="datasets3_CMIP5"

    elif selection=="4":
        regex=".*_CSIRO_Atlas_.*"
        filename="datasets4_CSIRO_Atlas"

    elif selection=="5":
        regex=".*_CliPAS_.*"
        filename="datasets5_CLiPAS"

    elif selection=="6":
        regex=".*_CDASK1.4_.*"
        filename="datasets6_dask14"

    elif selection=="7":
        regex=".*_ECCO2_.*"
        filename="datasets7_ECCO2"

    elif selection=="8":
        regex=".*_ERA-40_.*"
        filename="datasets8_ERA-40"

    elif selection=="9":
        regex=".*_ERA75deg_.*"
        filename="datasets9_ERA75"

    elif selection=="10":
        regex=".*_FRA-JCOPE2_.*"
        filename="datasets10_FRA-JCOPE2"

    elif selection=="11":
        regex=".*_GAME_.*"
        filename="datasets11_GAME"

    elif selection=="12":
        regex=".*_GFDL_.*"
        filename="datasets12_GFDL"

    elif selection=="13":
        regex=".*_HadSST_.*"
        filename="datasets13_HadSST"

    elif selection=="14":
        regex=".*_ISVHE_.*"
        filename="datasets14_ISVHE"

    elif selection=="15":
        regex=".*_Interpolated_precipitation_.*"
        filename="datasets15_Interpolated_precipitation"

    elif selection=="16":
        regex=".*_J-OFURO2_.*"
        filename="datasets16_J-OFURO"

    elif selection=="17":
        regex=".*_KYUSHU_.*"
        filename="datasets17_KYUSHU"

    elif selection=="18":
        regex=".*_Model_output_.*"
        filename="datasets18_Model_output"

    elif selection=="19":
        regex=".*_NCOM_.*"
        filename="datasets19_NCOM"

    elif selection=="20":
        regex=".*_NLOM_.*"
        filename="datasets20_NLOM"

    elif selection=="21":
        print "This appears to be no longer in use. If I'm wrong, please continue."
        regex=".*_NLOM_32_.*"
        filename="datasets21_NLOM_32"

    elif selection=="22":
        regex=".*_NOAA_SST_.*"
        filename="datasets22_NOAA_SST"

    elif selection=="23":
        regex=".*_Ocean_Climatology_.*"
        filename="datasets23_Ocean_Climatology"

    elif selection=="24":
        regex=".*_PODAAC_.*"
        filename="datasets24_PODAAC"

    elif selection=="25":
        regex=".*_PRIDE_.*"
        filename="datasets25_PRIDE"

    elif selection=="26":
        regex=".*_Paleoclimate_modeling_.*"
        filename="datasets26_Paleoclimate_modeling"

    elif selection=="27":
        regex=".*_Reanalysis_Data_.*"
        filename="datasets27_Reanalysis_Data"

    elif selection=="28":
        regex=".*_SCUD_.*"
        filename="datasets28_SCUD"

    elif selection=="29":
        regex=".*_SOCAT_.*"
        filename="datasets29_SOCAT"

    elif selection=="30":
        regex=".*_SODA_.*"
        filename="datasets30_SODA"

    elif selection=="31":
        regex=".*_Tohoku_.*"
        filename="datasets31_Tohoku"

    elif selection=="32":
        regex=".*_Typhoon_Reanalysis_.*"
        filename="datasets32_Typhoon_Reanalysis"

    elif selection=="33":
        regex=".*_WASWind_.*"
        filename="datasets33_WASWind"

    elif selection=="34":
        regex=".*_WHOI_OAFlux_.*"
        filename="datasets34_WHOI_OAFlux"

    elif selection=="35":
        regex=".*_WOA_.*"
        filename="datasets35_WOA"

    elif selection=="36":
        regex=".*_bimodal_ISO_index_.*"
        filename="datasets36_bimodal_ISO_index"

    elif selection=="37":
        regex=".*_hydrobase_.*"
        filename="datasets37_hydrobase"

    elif selection=="38":
        regex=".*_hydrological_data_.*"
        filename="datasets38_hydrological_data"

    elif selection=="39":
        regex=".*_iCOADS_.*"
        filename="datasets39_iCOADS"

    elif selection=="40":
        regex=".*_satellite_product_.*"
        filename="datasets40_satellite_product"

    elif selection=="41":
        regex=".*_topography_.*"
        filename="datasets41_topography"

    elif selection=="42":
        regex=".*_LOCA_.*"
        filename="datasets42_LOCA"

    elif selection=="43":
        regex=".*_SCSPOD14_.*"
        filename="datasets43_SCSPOD14"

	

    #print command
    #print option1
    #print option2
    #regex = "\"" + regex + "\""
    #print regex
    #print option3
    subprocess.call([command + " " + option1 + " " + option2 + "  " + regex + " " + option3], shell=True)
    #print regex
    #subprocess.call([command], shell=True)
    #print "finished call lol" 
    #print "do I work???"
    print "#########################" 
    print "# done with generation! #"
    print "#########################"
    subprocess.call(["sed","-i", "s/HAWAII SOEST/APDRC/g","./temp/EDDGridFromThreddsCatalog.xml"])
    subprocess.call(["sed","-i", "s/data apdrc.soest.hawaii.edu dods public data //g","./temp/EDDGridFromThreddsCatalog.xml"])
    subprocess.call(["sed","-i", "s/data apdrc.soest.hawaii.edu 80 dods public data //g","./temp/EDDGridFromThreddsCatalog.xml"]) 
    return filename


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
    print "43:SCSPOD14"
if __name__ == "__main__":
    main()



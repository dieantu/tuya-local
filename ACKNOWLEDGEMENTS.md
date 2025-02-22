## Acknowledgements

None of this would have been possible without some foundational discovery work to get me started:

- [nikrolls](https://github.com/nikrolls)'s [homeassistant-goldair-climate](https://github.com/nikrolls/homeassistant-goldair-climate) was the starting point for expanding to non-Goldair devices as well.
- [TarxBoy](https://github.com/TarxBoy)'s [investigation using codetheweb/tuyapi](https://github.com/codetheweb/tuyapi/issues/31) to figure out the correlation of the cryptic DPS states .
- [sean6541](https://github.com/sean6541)'s [tuya-homeassistant](https://github.com/sean6541/tuya-homeassistant) library giving an example of integrating Tuya devices with Home Assistant.
- [clach04](https://github.com/clach04)'s [python-tuya](https://github.com/clach04/python-tuya) library.
- [jasonacox](https://github.com/jasonacox)'s [tinytuya](https://github.com/jasonacox/tinytuya) library which improves on the original.

Further device support has been made with the assistance of users.  Please consider contributing if you find a device that is not supported by gathering some information about the device's DPS ids and their values.

- [etamtlosz](https://github.com/etamtlosz) and [KiLLeRRaT](https://github.com/KiLLeRRaT) for their support and dev work towards GECO and GPCV heaters.
- [botts7](https://github.com/botts7) for support towards widening Kogan SmartPlug support.
- [awaismun](https://github.com/awaismun) for assistance in supporting Andersson heaters.
- [FeikoJoosten](https://github.com/FeikoJoosten) for development of support for Eurom Mon Soleil 600 heaters.
- [Xeovar](https://github.com/Xeovar) for assistance in supporting Purline M100 heaters, Garden PAC pool heatpumps and Qoto sprinklers.
- [paulmfclark](https://github.com/paulmfclark) for assistance in supporting Remora Inverter pool heatpumps
- [cartman10](https://github.com/cartman10) for assistance with BWT FI 45 pool heater.
 - [superman110](https://github.com/superman110) for assistance in supporting Eanons/purenjoy humidifier.
 - [woolmonkey](https://github.com/woolmonkey) for assistance in supporting Inkbird ITC306A Thermostat.
 - [hazell20](https://github.com/hazell20) for assistance in supporting Anko fans.
 - [meremortals70](https://github.com/meremortals70) for assistance in supporting Deta fan controllers.
 - [mvnixon](https://github.com/mvnixon) for assistance in supporting Madimack pool heaters.
 - [Lapy](https://github.com/Lapy) for contributing support for Electriq CD25PRO dehumidifiers.
 - [thomas-fr](https://github.com/thomas-fr) for contributing support for Poolex Silverline heatpumps.
 - [lperez31](https://github.com/lperez31) for contributing support for Poolex Vertigo heatpumps.
 - [b3nnyk22](https://github.com/b3nnyk22) for assistance in supporting Kogan Dehumidifiers.
 - [rodrigoGA](https://github.com/rodrigoGA) for assistance in supporting Greenwind dehumidifiers.
 - [jorgenDK](https://github.com/jorgenDK) for assistance in supporting TroniTechnik Air Conditioner, and thanks for the coffee!
 - [Fannangir](https://github.com/Fannangir) for assistance in supporting Tadiran Wind Air Conditioner.
 - [marrold](https://github.com/marrold) for contributing support for ElectriQ CD20PRO dehumidifiers.
 - [Uaeguy](https://github.com/Uaeguy) for assistance in supporting Beca BHP-6000, Siswell T29UTK and Owon PCT513 thermostats, and thanks for the coffee!
 - [Johnnybyzhang](https://github.com/Johnnybyzhang) for assistance in supporting Lexy F501 fans.
 - [domgrimm](https://github.com/domgrimm) for assistance in supporting newer models of Kogan heater.
 - [EKCJ](https://github.com/EKCJ) for contributing support for ElectriQ DESD9LW dehumidifiers.
 - [ed-holland](https://github.com/ed-holland) for contributing support for Awow TH213 thermostats
 - [Vikedlol](https://github.com/Vikedlol) for assistance in supporting Wetair WCH-750 heaters.
 - [wwalczyszyn](https://github.com/wwalczyszyn) for contributing support for Fersk Vind 2 heatpumps.
 - [xbmcnut](https://github.com/xbmcnut) for assistance in supporting Kogan Smart Kettles and the new type of Kogan heater.
 - [ThomasADavis](https://github.com/ThomasADavis) for contributing support for Renpho RP-AP001S air purifiers.
 - [darek-margas](https://github.com/darek-margas) for contributing support for Arlec fans, Carson portable air conditioners, Grid Connect double outlets with and without USB and power monitoring, Mirabella Genio smartplugs.
 - [SamJongenelen](https://github.com/SamJongenelen) for assistance in supporting Siswell C16 Thermostats
 - [antoweb](https://github.com/antoweb) for assistance in supporting Beca BHT-6000 thermostats.
 - [klausahrenberg](https://github.com/klausahrenberg) for figuring out the BHT-6000 and other thermostats' internal MCU protocol for his alternate MQQT firmware, which helped with finding some of the details.
 - [Swiftnesses](https://github.com/Swiftnesses) for contributing support for Electriq CD12PW dehumidifiers
 - [MrDeon](https://github.com/MrDeon) for assistance in supporting Kogan KAWFPAC09YA air conditioners.
 - [SatarisGIT](https://github.com/SatarisGIT) for assistance in supporting Eberg Qubo Q40HD portable heatpump.
 - [lucaxxaa](https://github.com/lucaxxaa) for assistance in supporting Beca BHT-002 thermostat.
 - [nickdos](https://github.com/nickdos) for assistance in supporting Stirling FS1-40DC fan.
 - [Skro11-ru](https://github.com/Skro11-ru) for assistance in supporting Moes BHT-002 variant without external temperature sensor.
 - [novisys](https://github.com/novisys) for clarifications about BHT-6000 thermostat functionality.
 - [nzcodarnoc](https://github.com/nzcodarnoc) for contributing support for Kogan KASHMFP heaters.
 - [pascaltippelt](https://github.com/pascaltippelt) for assistance in supporting Minco MH-1823 thermostat.
 - [voed](https://github.com/voed) for assistance in supporting Advanced Energy monitoring smart switch, based on CBE smart switch but seeming to follow a Tuya Standard Template, so probably applicable to others.
 - [myevit](https://github.com/myevit) for assistance in supporting simple garage doors.
 - [maartendamen](https://github.com/maartendamen) for assistance in supporting Eurom Mon Soleil 601 heaters.
 - [TeddyLafrite](https://github.com/TeddyLafrite) for assistance in supporting Nedis HTPL20F heaters.
 - [mvroosmalen1970](https://github.com/mvroosmalen1970) for assistance in supporting Eurom SaniWall 2000 heaters.
 - [petrkotek](https://github.com/petrkotek) for contributing support for Madimack Elite V3 pool heatpumps.
 - [irakhlin](https://github.com/irakhlin) for contributing support for Aspen ASP200 fans.
 - [vampywiz17](https://github.com/vampywiz17) for contributing support for TMWF02 fan controllers, Digoo and Woox smartplugs and powerstrips and simple switches with timers.
 - [awaldram](https://github.com/awaldram) for confirming BHT-3000 support.
 - [bob-tm](https://github.com/bob-tm) for contributing support from Wetair WAW-H1210LW humidifiers.
 - [shakin89](https://github.com/shakin89) for assistance in supporting Beca BAC-002 thermostats.
 - [PaulJoosten](https://github.com/PaulJoosten) for assistance in figuring out the similarities and capabilities of different Eurom heaters.
 - [jdavidr17](https://github.com/jdavidr17) for assistance with discovering timer parameters for switches.
 - [miannelli516](https://github.com/miannelli516) for assistance with TR9B thermostats.
 - [edwinyoo44](https://github.com/edwinyoo44) for contributing support for JJPro JPD01 and JPD02 dehumidifiers and assistance with Poiema One purifiers.
 - [mpetcuRO](https://github.com/mpetcuRO) for assistance with Hysen HT08WE-2 thermometers.
 - [Paul-C-S](https://github.com/Paul-C-S) for assistance with Ecostrad Accent iQ heaters and contributing support for iQ Ceramic radiators.
 - [WildeRNS](https://github.com/WildeRNS) for assistance with Nashone MTS-700-WB thermostat smartplugs, SmartMCB Energy meter.
 - [ishioni](https://github.com/ishioni) for contributing support for Eberg Cooly C32HD air conditioner.
 - [Gekko47](https://github.com/Gekko47) for contributing support for ElectriQ CD12v2 dehumidifiers.
 - [andreq](https://github.com/andreq) for assistance with Inkbird ITC-308 thermostats.
 - [dlosito](https://github.com/dlosito) for assistance with a second variant of Awow TH213 thermostat.
 - [UrZdcw9](https://github.com/UrZdcw9) for assistance with Arlec ceiling fan with light.
 

#Reads in Brooklyn.csv and brooklyn_zip_codes.png from C:/ drive

#Package name: matplotlib-1.3.1
#Download link: https://pypi.python.org/pypi/matplotlib/1.3.1

#Package name: mpldatacursor-0.4.1
#Download link: https://pypi.python.org/pypi/mpldatacursor

import matplotlib.pyplot as plt
from mpldatacursor import datacursor


#sums up the following data fields for each zip code:

#-brooklyn_(zipcode) = number of properties

#-brooklyn_(zipcode)_ghg = amount of greenhouse gas produced
# by the properties in the zip code
# measured in pounds per year (lbs/yr)

#-brooklyn_(zipcode)_ghg_red = amount of greenhouse gas that
# could be reduced in the zipcode if the properties installed
# rooftop photovoltaic (PV) solar energy systems
# measured in pounds per year (lbs/yr)

#-brooklyn_(zipcode)_trees = the number of trees planted that
# would be the equivalent of the greenhouse gas reduction

#-brooklyn_(zipcode)_eprod = amount of electricity produced
# by the properties if rooftop photovoltaic (PV)
# solar energy systems were installed
# measured in kilowatt hours per year (kWh/yr) 

#-brooklyn_(zipcode)_esavings = amount of money saved by the
# properties if rooftop photovoltaic (PV) solar 
# energy systems were installed
# measured in dollars per year ($/yr)

class Brooklyn:
    count = 0
    
    brooklyn_11201 = 0
    brooklyn_11201_ghg = 0.0
    brooklyn_11201_ghg_red = 0
    brooklyn_11201_trees = 0
    brooklyn_11201_eprod = 0
    brooklyn_11201_esavings = 0
    brooklyn_11201_x_coor = 261
    brooklyn_11201_y_coor = 171    
    
    brooklyn_11203 = 0
    brooklyn_11203_ghg = 0.0
    brooklyn_11203_ghg_red = 0
    brooklyn_11203_trees = 0
    brooklyn_11203_eprod = 0
    brooklyn_11203_esavings = 0
    brooklyn_11203_x_coor = 428
    brooklyn_11203_y_coor = 350    
    
    brooklyn_11204 = 0
    brooklyn_11204_ghg = 0.0
    brooklyn_11204_ghg_red = 0
    brooklyn_11204_trees = 0
    brooklyn_11204_eprod = 0
    brooklyn_11204_esavings = 0
    brooklyn_11204_x_coor = 273
    brooklyn_11204_y_coor = 468
    
    brooklyn_11205 = 0
    brooklyn_11205_ghg = 0.0
    brooklyn_11205_ghg_red = 0
    brooklyn_11205_trees = 0
    brooklyn_11205_eprod = 0
    brooklyn_11205_esavings = 0
    brooklyn_11205_x_coor = 337
    brooklyn_11205_y_coor = 181
    
    brooklyn_11206 = 0
    brooklyn_11206_ghg = 0.0
    brooklyn_11206_ghg_red = 0
    brooklyn_11206_trees = 0
    brooklyn_11206_eprod = 0
    brooklyn_11206_esavings = 0
    brooklyn_11206_x_coor = 402
    brooklyn_11206_y_coor = 142
    
    brooklyn_11207 = 0
    brooklyn_11207_ghg = 0.0
    brooklyn_11207_ghg_red = 0
    brooklyn_11207_trees = 0
    brooklyn_11207_eprod = 0
    brooklyn_11207_esavings = 0
    brooklyn_11207_x_coor = 549
    brooklyn_11207_y_coor = 265

    brooklyn_11208 = 0
    brooklyn_11208_ghg = 0.0
    brooklyn_11208_ghg_red = 0
    brooklyn_11208_trees = 0
    brooklyn_11208_eprod = 0
    brooklyn_11208_esavings = 0
    brooklyn_11208_x_coor = 595
    brooklyn_11208_y_coor = 252
    
    brooklyn_11209 = 0
    brooklyn_11209_ghg = 0.0
    brooklyn_11209_ghg_red = 0
    brooklyn_11209_trees = 0
    brooklyn_11209_eprod = 0
    brooklyn_11209_esavings = 0
    brooklyn_11209_x_coor = 134
    brooklyn_11209_y_coor = 457
    
    brooklyn_11210 = 0
    brooklyn_11210_ghg = 0.0
    brooklyn_11210_ghg_red = 0
    brooklyn_11210_trees = 0
    brooklyn_11210_eprod = 0
    brooklyn_11210_esavings = 0
    brooklyn_11210_x_coor = 393
    brooklyn_11210_y_coor = 436
    
    brooklyn_11211 = 0
    brooklyn_11211_ghg = 0.0
    brooklyn_11211_ghg_red = 0
    brooklyn_11211_trees = 0
    brooklyn_11211_eprod = 0
    brooklyn_11211_esavings = 0
    brooklyn_11211_x_coor = 366
    brooklyn_11211_y_coor = 96
    
    brooklyn_11212 = 0
    brooklyn_11212_ghg = 0.0
    brooklyn_11212_ghg_red = 0
    brooklyn_11212_trees = 0
    brooklyn_11212_eprod = 0
    brooklyn_11212_esavings = 0
    brooklyn_11212_x_coor = 484
    brooklyn_11212_y_coor = 298
    
    brooklyn_11213 = 0
    brooklyn_11213_ghg = 0.0
    brooklyn_11213_ghg_red = 0
    brooklyn_11213_trees = 0
    brooklyn_11213_eprod = 0
    brooklyn_11213_esavings = 0
    brooklyn_11213_x_coor = 420
    brooklyn_11213_y_coor = 265
    
    brooklyn_11214 = 0
    brooklyn_11214_ghg = 0.0
    brooklyn_11214_ghg_red = 0
    brooklyn_11214_trees = 0
    brooklyn_11214_eprod = 0
    brooklyn_11214_esavings = 0
    brooklyn_11214_x_coor = 235
    brooklyn_11214_y_coor = 540
    
    brooklyn_11215 = 0
    brooklyn_11215_ghg = 0.0
    brooklyn_11215_ghg_red = 0
    brooklyn_11215_trees = 0
    brooklyn_11215_eprod = 0
    brooklyn_11215_esavings = 0
    brooklyn_11215_x_coor = 284
    brooklyn_11215_y_coor = 283

    brooklyn_11216 = 0
    brooklyn_11216_ghg = 0.0
    brooklyn_11216_ghg_red = 0
    brooklyn_11216_trees = 0
    brooklyn_11216_eprod = 0
    brooklyn_11216_esavings = 0
    brooklyn_11216_x_coor = 382
    brooklyn_11216_y_coor = 227

    brooklyn_11217 = 0
    brooklyn_11217_ghg = 0.0
    brooklyn_11217_ghg_red = 0
    brooklyn_11217_trees = 0
    brooklyn_11217_eprod = 0
    brooklyn_11217_esavings = 0
    brooklyn_11217_x_coor = 286
    brooklyn_11217_y_coor = 221
    
    brooklyn_11218 = 0
    brooklyn_11218_ghg = 0.0
    brooklyn_11218_ghg_red = 0
    brooklyn_11218_trees = 0
    brooklyn_11218_eprod = 0
    brooklyn_11218_esavings = 0
    brooklyn_11218_x_coor = 300
    brooklyn_11218_y_coor = 374
    
    brooklyn_11219 = 0
    brooklyn_11219_ghg = 0.0
    brooklyn_11219_ghg_red = 0
    brooklyn_11219_trees = 0
    brooklyn_11219_eprod = 0
    brooklyn_11219_esavings = 0
    brooklyn_11219_x_coor = 240
    brooklyn_11219_y_coor = 416
    
    brooklyn_11220 = 0
    brooklyn_11220_ghg = 0.0
    brooklyn_11220_ghg_red = 0
    brooklyn_11220_trees = 0
    brooklyn_11220_eprod = 0
    brooklyn_11220_esavings = 0
    brooklyn_11220_x_coor = 172
    brooklyn_11220_y_coor = 388
    
    brooklyn_11221 = 0
    brooklyn_11221_ghg = 0.0
    brooklyn_11221_ghg_red = 0
    brooklyn_11221_trees = 0
    brooklyn_11221_eprod = 0
    brooklyn_11221_esavings = 0
    brooklyn_11221_x_coor = 441
    brooklyn_11221_y_coor = 197
    
    brooklyn_11222 = 0
    brooklyn_11222_ghg = 0.0
    brooklyn_11222_ghg_red = 0
    brooklyn_11222_trees = 0
    brooklyn_11222_eprod = 0
    brooklyn_11222_esavings = 0
    brooklyn_11222_x_coor = 380
    brooklyn_11222_y_coor = 39
    
    brooklyn_11223 = 0
    brooklyn_11223_ghg = 0.0
    brooklyn_11223_ghg_red = 0
    brooklyn_11223_trees = 0
    brooklyn_11223_eprod = 0
    brooklyn_11223_esavings = 0
    brooklyn_11223_x_coor = 311
    brooklyn_11223_y_coor = 557
    
    brooklyn_11224 = 0
    brooklyn_11224_ghg = 0.0
    brooklyn_11224_ghg_red = 0
    brooklyn_11224_trees = 0
    brooklyn_11224_eprod = 0
    brooklyn_11224_esavings = 0
    brooklyn_11224_x_coor = 240
    brooklyn_11224_y_coor = 658
    
    brooklyn_11225 = 0
    brooklyn_11225_ghg = 0.0
    brooklyn_11225_ghg_red = 0
    brooklyn_11225_trees = 0
    brooklyn_11225_eprod = 0
    brooklyn_11225_esavings = 0
    brooklyn_11225_x_coor = 373
    brooklyn_11225_y_coor = 297
        
    brooklyn_11226 = 0
    brooklyn_11226_ghg = 0.0
    brooklyn_11226_ghg_red = 0
    brooklyn_11226_trees = 0
    brooklyn_11226_eprod = 0
    brooklyn_11226_esavings = 0
    brooklyn_11226_x_coor = 358
    brooklyn_11226_y_coor = 362
    
    brooklyn_11228 = 0
    brooklyn_11228_ghg = 0.0
    brooklyn_11228_ghg_red = 0
    brooklyn_11228_trees = 0
    brooklyn_11228_eprod = 0
    brooklyn_11228_esavings = 0
    brooklyn_11228_x_coor = 189
    brooklyn_11228_y_coor = 481
    
    brooklyn_11229 = 0
    brooklyn_11229_ghg = 0.0
    brooklyn_11229_ghg_red = 0
    brooklyn_11229_trees = 0
    brooklyn_11229_eprod = 0
    brooklyn_11229_esavings = 0
    brooklyn_11229_x_coor = 388
    brooklyn_11229_y_coor = 541
          
    brooklyn_11230 = 0
    brooklyn_11230_ghg = 0.0
    brooklyn_11230_ghg_red = 0
    brooklyn_11230_trees = 0
    brooklyn_11230_eprod = 0
    brooklyn_11230_esavings = 0
    brooklyn_11230_x_coor = 332
    brooklyn_11230_y_coor = 458     
          
    brooklyn_11231 = 0
    brooklyn_11231_ghg = 0.0
    brooklyn_11231_ghg_red = 0
    brooklyn_11231_trees = 0
    brooklyn_11231_eprod = 0
    brooklyn_11231_esavings = 0
    brooklyn_11231_x_coor = 216
    brooklyn_11231_y_coor = 237
    
    brooklyn_11232 = 0
    brooklyn_11232_ghg = 0.0
    brooklyn_11232_ghg_red = 0
    brooklyn_11232_trees = 0
    brooklyn_11232_eprod = 0
    brooklyn_11232_esavings = 0
    brooklyn_11232_x_coor = 229
    brooklyn_11232_y_coor = 332
    
    brooklyn_11233 = 0
    brooklyn_11233_ghg = 0.0
    brooklyn_11233_ghg_red = 0
    brooklyn_11233_trees = 0
    brooklyn_11233_eprod = 0
    brooklyn_11233_esavings = 0
    brooklyn_11233_x_coor = 478
    brooklyn_11233_y_coor = 237
    
    brooklyn_11234 = 0
    brooklyn_11234_ghg = 0.0
    brooklyn_11234_ghg_red = 0
    brooklyn_11234_trees = 0
    brooklyn_11234_eprod = 0
    brooklyn_11234_esavings = 0
    brooklyn_11234_x_coor = 441
    brooklyn_11234_y_coor = 483
    
    brooklyn_11235 = 0
    brooklyn_11235_ghg = 0.0
    brooklyn_11235_ghg_red = 0
    brooklyn_11235_trees = 0
    brooklyn_11235_eprod = 0
    brooklyn_11235_esavings = 0
    brooklyn_11235_x_coor = 355
    brooklyn_11235_y_coor = 620
    
    brooklyn_11236 = 0
    brooklyn_11236_ghg = 0.0
    brooklyn_11236_ghg_red = 0
    brooklyn_11236_trees = 0
    brooklyn_11236_eprod = 0
    brooklyn_11236_esavings = 0
    brooklyn_11236_x_coor = 526
    brooklyn_11236_y_coor = 387
    
    brooklyn_11237 = 0
    brooklyn_11237_ghg = 0.0
    brooklyn_11237_ghg_red = 0
    brooklyn_11237_trees = 0
    brooklyn_11237_eprod = 0
    brooklyn_11237_esavings = 0
    brooklyn_11237_x_coor = 457
    brooklyn_11237_y_coor = 134
    
    brooklyn_11238 = 0
    brooklyn_11238_ghg = 0.0
    brooklyn_11238_ghg_red = 0
    brooklyn_11238_trees = 0
    brooklyn_11238_eprod = 0
    brooklyn_11238_esavings = 0
    brooklyn_11238_x_coor = 338
    brooklyn_11238_y_coor = 233
    
    brooklyn_11239 = 0
    brooklyn_11239_ghg = 0.0
    brooklyn_11239_ghg_red = 0
    brooklyn_11239_trees = 0
    brooklyn_11239_eprod = 0
    brooklyn_11239_esavings = 0
    brooklyn_11239_x_coor = 595
    brooklyn_11239_y_coor = 367    
          
    def __init__(self, input_street_num, input_street_name, input_zip, \
                 input_emissions, input_property_type, input_system_size, \
                 input_cost, input_cost_reduced, input_break_even, \
                 input_energy_production, input_savings, \
                 input_emissions_reduction, input_trees):
        self.__class__.count += 1
        self.street_num = input_street_num
        self.street_name = input_street_name
        self.zip = input_zip
        self.emissions = input_emissions
        self.property_type = input_property_type
        self.system_size = input_system_size
        self.cost = input_cost
        self.cost_reduced = input_cost_reduced
        self.break_even = input_break_even
        self.energy_production = input_energy_production
        self.savings = input_savings
        self.emissions_reduction = input_emissions_reduction
        self.trees = input_trees
        
        if input_zip == "11201":
            self.__class__.brooklyn_11201 += 1            
            self.__class__.brooklyn_11201_ghg += float(input_emissions)
            self.__class__.brooklyn_11201_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11201_trees += int(input_trees)
            self.__class__.brooklyn_11201_eprod += int(input_energy_production)
            self.__class__.brooklyn_11201_esavings += int(input_savings)
        elif input_zip == "11203":
            self.__class__.brooklyn_11203 += 1            
            self.__class__.brooklyn_11203_ghg += float(input_emissions)
            self.__class__.brooklyn_11203_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11203_trees += int(input_trees)
            self.__class__.brooklyn_11203_eprod += int(input_energy_production)
            self.__class__.brooklyn_11203_esavings += int(input_savings)
        elif input_zip == "11204":
            self.__class__.brooklyn_11204 += 1            
            self.__class__.brooklyn_11204_ghg += float(input_emissions)
            self.__class__.brooklyn_11204_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11204_trees += int(input_trees)
            self.__class__.brooklyn_11204_eprod += int(input_energy_production)
            self.__class__.brooklyn_11204_esavings += int(input_savings)
        elif input_zip == "11205":
            self.__class__.brooklyn_11205 += 1            
            self.__class__.brooklyn_11205_ghg += float(input_emissions)
            self.__class__.brooklyn_11205_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11205_trees += int(input_trees)
            self.__class__.brooklyn_11205_eprod += int(input_energy_production)
            self.__class__.brooklyn_11205_esavings += int(input_savings)
        elif input_zip == "11206":
            self.__class__.brooklyn_11206 += 1            
            self.__class__.brooklyn_11206_ghg += float(input_emissions)
            self.__class__.brooklyn_11206_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11206_trees += int(input_trees)
            self.__class__.brooklyn_11206_eprod += int(input_energy_production)
            self.__class__.brooklyn_11206_esavings += int(input_savings)
        elif input_zip == "11207":
            self.__class__.brooklyn_11207 += 1            
            self.__class__.brooklyn_11207_ghg += float(input_emissions)
            self.__class__.brooklyn_11207_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11207_trees += int(input_trees)
            self.__class__.brooklyn_11207_eprod += int(input_energy_production)
            self.__class__.brooklyn_11207_esavings += int(input_savings)
        elif input_zip == "11208":
            self.__class__.brooklyn_11208 += 1            
            self.__class__.brooklyn_11208_ghg += float(input_emissions)
            self.__class__.brooklyn_11208_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11208_trees += int(input_trees)
            self.__class__.brooklyn_11208_eprod += int(input_energy_production)
            self.__class__.brooklyn_11208_esavings += int(input_savings)
        elif input_zip == "11209":
            self.__class__.brooklyn_11209 += 1            
            self.__class__.brooklyn_11209_ghg += float(input_emissions)
            self.__class__.brooklyn_11209_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11209_trees += int(input_trees)
            self.__class__.brooklyn_11209_eprod += int(input_energy_production)
            self.__class__.brooklyn_11209_esavings += int(input_savings)
        elif input_zip == "11210":
            self.__class__.brooklyn_11210 += 1            
            self.__class__.brooklyn_11210_ghg += float(input_emissions)
            self.__class__.brooklyn_11210_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11210_trees += int(input_trees)
            self.__class__.brooklyn_11210_eprod += int(input_energy_production)
            self.__class__.brooklyn_11210_esavings += int(input_savings)
        elif input_zip == "11211":
            self.__class__.brooklyn_11211 += 1            
            self.__class__.brooklyn_11211_ghg += float(input_emissions)
            self.__class__.brooklyn_11211_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11211_trees += int(input_trees)
            self.__class__.brooklyn_11211_eprod += int(input_energy_production)
            self.__class__.brooklyn_11211_esavings += int(input_savings)
        elif input_zip == "11212":
            self.__class__.brooklyn_11212 += 1            
            self.__class__.brooklyn_11212_ghg += float(input_emissions)
            self.__class__.brooklyn_11212_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11212_trees += int(input_trees)
            self.__class__.brooklyn_11212_eprod += int(input_energy_production)
            self.__class__.brooklyn_11212_esavings += int(input_savings)
        elif input_zip == "11213":
            self.__class__.brooklyn_11213 += 1            
            self.__class__.brooklyn_11213_ghg += float(input_emissions)
            self.__class__.brooklyn_11213_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11213_trees += int(input_trees)
            self.__class__.brooklyn_11213_eprod += int(input_energy_production)
            self.__class__.brooklyn_11213_esavings += int(input_savings)
        elif input_zip == "11214":
            self.__class__.brooklyn_11214 += 1            
            self.__class__.brooklyn_11214_ghg += float(input_emissions)
            self.__class__.brooklyn_11214_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11214_trees += int(input_trees)
            self.__class__.brooklyn_11214_eprod += int(input_energy_production)
            self.__class__.brooklyn_11214_esavings += int(input_savings)
        elif input_zip == "11215":
            self.__class__.brooklyn_11215 += 1            
            self.__class__.brooklyn_11215_ghg += float(input_emissions)
            self.__class__.brooklyn_11215_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11215_trees += int(input_trees)
            self.__class__.brooklyn_11215_eprod += int(input_energy_production)
            self.__class__.brooklyn_11215_esavings += int(input_savings)
        elif input_zip == "11216":
            self.__class__.brooklyn_11216 += 1            
            self.__class__.brooklyn_11216_ghg += float(input_emissions)
            self.__class__.brooklyn_11216_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11216_trees += int(input_trees)
            self.__class__.brooklyn_11216_eprod += int(input_energy_production)
            self.__class__.brooklyn_11216_esavings += int(input_savings)
        elif input_zip == "11217":
            self.__class__.brooklyn_11217 += 1            
            self.__class__.brooklyn_11217_ghg += float(input_emissions)
            self.__class__.brooklyn_11217_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11217_trees += int(input_trees)
            self.__class__.brooklyn_11217_eprod += int(input_energy_production)
            self.__class__.brooklyn_11217_esavings += int(input_savings)
        elif input_zip == "11218":
            self.__class__.brooklyn_11218 += 1            
            self.__class__.brooklyn_11218_ghg += float(input_emissions)
            self.__class__.brooklyn_11218_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11218_trees += int(input_trees)
            self.__class__.brooklyn_11218_eprod += int(input_energy_production)
            self.__class__.brooklyn_11218_esavings += int(input_savings)
        elif input_zip == "11219":
            self.__class__.brooklyn_11219 += 1            
            self.__class__.brooklyn_11219_ghg += float(input_emissions)
            self.__class__.brooklyn_11219_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11219_trees += int(input_trees)
            self.__class__.brooklyn_11219_eprod += int(input_energy_production)
            self.__class__.brooklyn_11219_esavings += int(input_savings)
        elif input_zip == "11220":
            self.__class__.brooklyn_11220 += 1            
            self.__class__.brooklyn_11220_ghg += float(input_emissions)
            self.__class__.brooklyn_11220_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11220_trees += int(input_trees)
            self.__class__.brooklyn_11220_eprod += int(input_energy_production)
            self.__class__.brooklyn_11220_esavings += int(input_savings)
        elif input_zip == "11221":
            self.__class__.brooklyn_11221 += 1            
            self.__class__.brooklyn_11221_ghg += float(input_emissions)
            self.__class__.brooklyn_11221_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11221_trees += int(input_trees)
            self.__class__.brooklyn_11221_eprod += int(input_energy_production)
            self.__class__.brooklyn_11221_esavings += int(input_savings)
        elif input_zip == "11222":
            self.__class__.brooklyn_11222 += 1            
            self.__class__.brooklyn_11222_ghg += float(input_emissions)
            self.__class__.brooklyn_11222_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11222_trees += int(input_trees)
            self.__class__.brooklyn_11222_eprod += int(input_energy_production)
            self.__class__.brooklyn_11222_esavings += int(input_savings)
        elif input_zip == "11223":
            self.__class__.brooklyn_11223 += 1            
            self.__class__.brooklyn_11223_ghg += float(input_emissions)
            self.__class__.brooklyn_11223_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11223_trees += int(input_trees)
            self.__class__.brooklyn_11223_eprod += int(input_energy_production)
            self.__class__.brooklyn_11223_esavings += int(input_savings)
        elif input_zip == "11224":
            self.__class__.brooklyn_11224 += 1            
            self.__class__.brooklyn_11224_ghg += float(input_emissions)
            self.__class__.brooklyn_11224_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11224_trees += int(input_trees)
            self.__class__.brooklyn_11224_eprod += int(input_energy_production)
            self.__class__.brooklyn_11224_esavings += int(input_savings)
        elif input_zip == "11225":
            self.__class__.brooklyn_11225 += 1            
            self.__class__.brooklyn_11225_ghg += float(input_emissions)
            self.__class__.brooklyn_11225_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11225_trees += int(input_trees)
            self.__class__.brooklyn_11225_eprod += int(input_energy_production)
            self.__class__.brooklyn_11225_esavings += int(input_savings)
        elif input_zip == "11226":
            self.__class__.brooklyn_11226 += 1            
            self.__class__.brooklyn_11226_ghg += float(input_emissions)
            self.__class__.brooklyn_11226_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11226_trees += int(input_trees)
            self.__class__.brooklyn_11226_eprod += int(input_energy_production)
            self.__class__.brooklyn_11226_esavings += int(input_savings)
        elif input_zip == "11228":
            self.__class__.brooklyn_11228 += 1            
            self.__class__.brooklyn_11228_ghg += float(input_emissions)
            self.__class__.brooklyn_11228_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11228_trees += int(input_trees)
            self.__class__.brooklyn_11228_eprod += int(input_energy_production)
            self.__class__.brooklyn_11228_esavings += int(input_savings)
        elif input_zip == "11229":
            self.__class__.brooklyn_11229 += 1            
            self.__class__.brooklyn_11229_ghg += float(input_emissions)
            self.__class__.brooklyn_11229_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11229_trees += int(input_trees)
            self.__class__.brooklyn_11229_eprod += int(input_energy_production)
            self.__class__.brooklyn_11229_esavings += int(input_savings)
        elif input_zip == "11230":
            self.__class__.brooklyn_11230 += 1            
            self.__class__.brooklyn_11230_ghg += float(input_emissions)
            self.__class__.brooklyn_11230_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11230_trees += int(input_trees)
            self.__class__.brooklyn_11230_eprod += int(input_energy_production)
            self.__class__.brooklyn_11230_esavings += int(input_savings)
        elif input_zip == "11231":
            self.__class__.brooklyn_11231 += 1            
            self.__class__.brooklyn_11231_ghg += float(input_emissions)
            self.__class__.brooklyn_11231_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11231_trees += int(input_trees)
            self.__class__.brooklyn_11231_eprod += int(input_energy_production)
            self.__class__.brooklyn_11231_esavings += int(input_savings)
        elif input_zip == "11232":
            self.__class__.brooklyn_11232 += 1            
            self.__class__.brooklyn_11232_ghg += float(input_emissions)
            self.__class__.brooklyn_11232_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11232_trees += int(input_trees)
            self.__class__.brooklyn_11232_eprod += int(input_energy_production)
            self.__class__.brooklyn_11232_esavings += int(input_savings)
        elif input_zip == "11233":
            self.__class__.brooklyn_11233 += 1            
            self.__class__.brooklyn_11233_ghg += float(input_emissions)
            self.__class__.brooklyn_11233_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11233_trees += int(input_trees)
            self.__class__.brooklyn_11233_eprod += int(input_energy_production)
            self.__class__.brooklyn_11233_esavings += int(input_savings)            
        elif input_zip == "11234":
            self.__class__.brooklyn_11234 += 1            
            self.__class__.brooklyn_11234_ghg += float(input_emissions)
            self.__class__.brooklyn_11234_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11234_trees += int(input_trees)
            self.__class__.brooklyn_11234_eprod += int(input_energy_production)
            self.__class__.brooklyn_11234_esavings += int(input_savings)
        elif input_zip == "11235":
            self.__class__.brooklyn_11235 += 1            
            self.__class__.brooklyn_11235_ghg += float(input_emissions)
            self.__class__.brooklyn_11235_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11235_trees += int(input_trees)
            self.__class__.brooklyn_11235_eprod += int(input_energy_production)
            self.__class__.brooklyn_11235_esavings += int(input_savings)
        elif input_zip == "11236":
            self.__class__.brooklyn_11236 += 1            
            self.__class__.brooklyn_11236_ghg += float(input_emissions)
            self.__class__.brooklyn_11236_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11236_trees += int(input_trees)
            self.__class__.brooklyn_11236_eprod += int(input_energy_production)
            self.__class__.brooklyn_11236_esavings += int(input_savings)
        elif input_zip == "11237":
            self.__class__.brooklyn_11237 += 1            
            self.__class__.brooklyn_11237_ghg += float(input_emissions)
            self.__class__.brooklyn_11237_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11237_trees += int(input_trees)
            self.__class__.brooklyn_11237_eprod += int(input_energy_production)
            self.__class__.brooklyn_11237_esavings += int(input_savings)
        elif input_zip == "11238":
            self.__class__.brooklyn_11238 += 1            
            self.__class__.brooklyn_11238_ghg += float(input_emissions)
            self.__class__.brooklyn_11238_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11238_trees += int(input_trees)
            self.__class__.brooklyn_11238_eprod += int(input_energy_production)
            self.__class__.brooklyn_11238_esavings += int(input_savings)
        elif input_zip == "11239":
            self.__class__.brooklyn_11239 += 1            
            self.__class__.brooklyn_11239_ghg += float(input_emissions)
            self.__class__.brooklyn_11239_ghg_red += int(input_emissions_reduction)
            self.__class__.brooklyn_11239_trees += int(input_trees)
            self.__class__.brooklyn_11239_eprod += int(input_energy_production)
            self.__class__.brooklyn_11239_esavings += int(input_savings)            
    
    
#takes zip code as parameter
#returns string containing total results for zip code
def labelMaker(input_zip):
    label_num_properties = "brooklyn_" + str(input_zip)
    label_ghg = "brooklyn_" + str(input_zip) + "_ghg"
    label_ghg_red = "brooklyn_" + str(input_zip) + "_ghg_red"
    label_trees = "brooklyn_" + str(input_zip) + "_trees"
    label_eprod = "brooklyn_" + str(input_zip) + "_eprod"
    label_esavings = "brooklyn_" + str(input_zip) + "_esavings"
    
    return ("Zip = " + str(input_zip) + "     " + "Properties = " + str(getattr(Brooklyn, label_num_properties)) + \
            "\nGHG Production = " + str("{:,}".format(getattr(Brooklyn, label_ghg))) + " lbs/yr" + \
            "\nGHG Reduction = " + str("{:,}".format(getattr(Brooklyn, label_ghg_red))) + " lbs/yr" + \
            "\nTrees Equivalent = " + str("{:,}".format(getattr(Brooklyn, label_trees))) + \
            "\nEnergy Production = " + str("{:,}".format(getattr(Brooklyn, label_eprod))) + " kWh/yr" + \
            "\nEnergy Savings = $" + str("{:,}".format(getattr(Brooklyn, label_esavings))) + "/yr")
    

if __name__ == "__main__":       
    f = open("C:/Brooklyn.csv", "r")
    brooklyn_data = []
    for line in f:
        line = line.strip()
        input_list = line.split(",")
        brooklyn_data.append(Brooklyn(input_list[0], input_list[1], input_list[2], \
                                      input_list[3], input_list[4], input_list[5], \
                                      input_list[6], input_list[7], input_list[8], \
                                      input_list[9], input_list[10], input_list[11], \
                                      input_list[12]))
        
    f.close()
    
    
    brooklyn_image = plt.imread('C:/brooklyn_zip_codes.png')
    brooklyn_map = plt.imshow(brooklyn_image)
    
    #creates data points for each zip code in Brooklyn
    #calls labelMaker function to create data label for each zip code
    
    zip_11201 = plt.scatter(Brooklyn.brooklyn_11201_x_coor, Brooklyn.brooklyn_11201_y_coor,
                            s = 50, c = 'black', label = labelMaker(11201))
    zip_11203 = plt.scatter(Brooklyn.brooklyn_11203_x_coor, Brooklyn.brooklyn_11203_y_coor,
                            s = 50, c = 'black', label = labelMaker(11203))
    zip_11204 = plt.scatter(Brooklyn.brooklyn_11204_x_coor, Brooklyn.brooklyn_11204_y_coor,
                            s = 50, c = 'black', label = labelMaker(11204))
    zip_11205 = plt.scatter(Brooklyn.brooklyn_11205_x_coor, Brooklyn.brooklyn_11205_y_coor,
                            s = 50, c = 'black', label = labelMaker(11205))
    zip_11206 = plt.scatter(Brooklyn.brooklyn_11206_x_coor, Brooklyn.brooklyn_11206_y_coor,
                            s = 50, c = 'black', label = labelMaker(11206))
    zip_11207 = plt.scatter(Brooklyn.brooklyn_11207_x_coor, Brooklyn.brooklyn_11207_y_coor,
                            s = 50, c = 'black', label = labelMaker(11207))
    zip_11208 = plt.scatter(Brooklyn.brooklyn_11208_x_coor, Brooklyn.brooklyn_11208_y_coor,
                            s = 50, c = 'black', label = labelMaker(11208))
    zip_11209 = plt.scatter(Brooklyn.brooklyn_11209_x_coor, Brooklyn.brooklyn_11209_y_coor,
                            s = 50, c = 'black', label = labelMaker(11209))
    zip_11210 = plt.scatter(Brooklyn.brooklyn_11210_x_coor, Brooklyn.brooklyn_11210_y_coor,
                            s = 50, c = 'black', label = labelMaker(11210))
    zip_11211 = plt.scatter(Brooklyn.brooklyn_11211_x_coor, Brooklyn.brooklyn_11211_y_coor,
                            s = 50, c = 'black', label = labelMaker(11211))
    zip_11212 = plt.scatter(Brooklyn.brooklyn_11212_x_coor, Brooklyn.brooklyn_11212_y_coor,
                            s = 50, c = 'black', label = labelMaker(11212))
    zip_11213 = plt.scatter(Brooklyn.brooklyn_11213_x_coor, Brooklyn.brooklyn_11213_y_coor,
                            s = 50, c = 'black', label = labelMaker(11213))
    zip_11214 = plt.scatter(Brooklyn.brooklyn_11214_x_coor, Brooklyn.brooklyn_11214_y_coor,
                            s = 50, c = 'black', label = labelMaker(11214))
    zip_11215 = plt.scatter(Brooklyn.brooklyn_11215_x_coor, Brooklyn.brooklyn_11215_y_coor,
                            s = 50, c = 'black', label = labelMaker(11215))
    zip_11216 = plt.scatter(Brooklyn.brooklyn_11216_x_coor, Brooklyn.brooklyn_11216_y_coor,
                            s = 50, c = 'black', label = labelMaker(11216))
    zip_11217 = plt.scatter(Brooklyn.brooklyn_11217_x_coor, Brooklyn.brooklyn_11217_y_coor,
                            s = 50, c = 'black', label = labelMaker(11217))
    zip_11218 = plt.scatter(Brooklyn.brooklyn_11218_x_coor, Brooklyn.brooklyn_11218_y_coor,
                            s = 50, c = 'black', label = labelMaker(11218))
    zip_11219 = plt.scatter(Brooklyn.brooklyn_11219_x_coor, Brooklyn.brooklyn_11219_y_coor,
                            s = 50, c = 'black', label = labelMaker(11219))
    zip_11220 = plt.scatter(Brooklyn.brooklyn_11220_x_coor, Brooklyn.brooklyn_11220_y_coor,
                            s = 50, c = 'black', label = labelMaker(11220))
    zip_11221 = plt.scatter(Brooklyn.brooklyn_11221_x_coor, Brooklyn.brooklyn_11221_y_coor,
                            s = 50, c = 'black', label = labelMaker(11221))
    zip_11222 = plt.scatter(Brooklyn.brooklyn_11222_x_coor, Brooklyn.brooklyn_11222_y_coor,
                            s = 50, c = 'black', label = labelMaker(11222))
    zip_11223 = plt.scatter(Brooklyn.brooklyn_11223_x_coor, Brooklyn.brooklyn_11223_y_coor,
                            s = 50, c = 'black', label = labelMaker(11223))
    zip_11224 = plt.scatter(Brooklyn.brooklyn_11224_x_coor, Brooklyn.brooklyn_11224_y_coor,
                            s = 50, c = 'black', label = labelMaker(11224))
    zip_11225 = plt.scatter(Brooklyn.brooklyn_11225_x_coor, Brooklyn.brooklyn_11225_y_coor,
                            s = 50, c = 'black', label = labelMaker(11225))
    zip_11226 = plt.scatter(Brooklyn.brooklyn_11226_x_coor, Brooklyn.brooklyn_11226_y_coor,
                            s = 50, c = 'black', label = labelMaker(11226))
    zip_11228 = plt.scatter(Brooklyn.brooklyn_11228_x_coor, Brooklyn.brooklyn_11228_y_coor,
                            s = 50, c = 'black', label = labelMaker(11228))
    zip_11229 = plt.scatter(Brooklyn.brooklyn_11229_x_coor, Brooklyn.brooklyn_11229_y_coor,
                            s = 50, c = 'black', label = labelMaker(11229))
    zip_11230 = plt.scatter(Brooklyn.brooklyn_11230_x_coor, Brooklyn.brooklyn_11230_y_coor,
                            s = 50, c = 'black', label = labelMaker(11230))
    zip_11231 = plt.scatter(Brooklyn.brooklyn_11231_x_coor, Brooklyn.brooklyn_11231_y_coor,
                            s = 50, c = 'black', label = labelMaker(11231))
    zip_11232 = plt.scatter(Brooklyn.brooklyn_11232_x_coor, Brooklyn.brooklyn_11232_y_coor,
                            s = 50, c = 'black', label = labelMaker(11232))
    zip_11233 = plt.scatter(Brooklyn.brooklyn_11233_x_coor, Brooklyn.brooklyn_11233_y_coor,
                            s = 50, c = 'black', label = labelMaker(11233))
    zip_11234 = plt.scatter(Brooklyn.brooklyn_11234_x_coor, Brooklyn.brooklyn_11234_y_coor,
                            s = 50, c = 'black', label = labelMaker(11234))
    zip_11235 = plt.scatter(Brooklyn.brooklyn_11235_x_coor, Brooklyn.brooklyn_11235_y_coor,
                            s = 50, c = 'black', label = labelMaker(11235))
    zip_11236 = plt.scatter(Brooklyn.brooklyn_11236_x_coor, Brooklyn.brooklyn_11236_y_coor,
                            s = 50, c = 'black', label = labelMaker(11236))
    zip_11237 = plt.scatter(Brooklyn.brooklyn_11237_x_coor, Brooklyn.brooklyn_11237_y_coor,
                            s = 50, c = 'black', label = labelMaker(11237))
    zip_11238 = plt.scatter(Brooklyn.brooklyn_11238_x_coor, Brooklyn.brooklyn_11238_y_coor,
                            s = 50, c = 'black', label = labelMaker(11238))
    zip_11239 = plt.scatter(Brooklyn.brooklyn_11239_x_coor, Brooklyn.brooklyn_11239_y_coor,
                            s = 50, c = 'black', label = labelMaker(11239))
    
    
    #finds zip code with highest concentration of greenhouse gas emissions (lbs/yr)
    #creates data point and data label
    
    brooklyn_ghg = {"11201": Brooklyn.brooklyn_11201_ghg, "11203": Brooklyn.brooklyn_11203_ghg,
                    "11204": Brooklyn.brooklyn_11204_ghg, "11205": Brooklyn.brooklyn_11205_ghg,
                    "11206": Brooklyn.brooklyn_11206_ghg, "11207": Brooklyn.brooklyn_11207_ghg,
                    "11208": Brooklyn.brooklyn_11208_ghg, "11209": Brooklyn.brooklyn_11209_ghg,
                    "11210": Brooklyn.brooklyn_11210_ghg, "11211": Brooklyn.brooklyn_11211_ghg,
                    "11212": Brooklyn.brooklyn_11212_ghg, "11213": Brooklyn.brooklyn_11213_ghg,
                    "11214": Brooklyn.brooklyn_11214_ghg, "11215": Brooklyn.brooklyn_11215_ghg,
                    "11216": Brooklyn.brooklyn_11216_ghg, "11217": Brooklyn.brooklyn_11217_ghg,
                    "11218": Brooklyn.brooklyn_11218_ghg, "11219": Brooklyn.brooklyn_11219_ghg,
                    "11220": Brooklyn.brooklyn_11220_ghg, "11221": Brooklyn.brooklyn_11221_ghg,
                    "11222": Brooklyn.brooklyn_11222_ghg, "11223": Brooklyn.brooklyn_11223_ghg,
                    "11224": Brooklyn.brooklyn_11224_ghg, "11225": Brooklyn.brooklyn_11225_ghg,
                    "11226": Brooklyn.brooklyn_11226_ghg, "11228": Brooklyn.brooklyn_11228_ghg,
                    "11229": Brooklyn.brooklyn_11229_ghg, "11230": Brooklyn.brooklyn_11230_ghg,
                    "11231": Brooklyn.brooklyn_11231_ghg, "11232": Brooklyn.brooklyn_11232_ghg,
                    "11233": Brooklyn.brooklyn_11233_ghg, "11234": Brooklyn.brooklyn_11234_ghg,
                    "11235": Brooklyn.brooklyn_11235_ghg, "11236": Brooklyn.brooklyn_11236_ghg,
                    "11237": Brooklyn.brooklyn_11237_ghg, "11238": Brooklyn.brooklyn_11238_ghg,
                    "11239": Brooklyn.brooklyn_11239_ghg}
    
    max_ghg_zip_code = max(brooklyn_ghg, key = brooklyn_ghg.get)
        
    max_ghg_zip_code_string = "brooklyn_" + str(max_ghg_zip_code) + "_ghg"
           
    max_ghg_zip_code_value = getattr(Brooklyn, max_ghg_zip_code_string)
        
    max_ghg_zip_code_x_coor_string = "brooklyn_" + str(max_ghg_zip_code) + "_x_coor"    
    
    max_ghg_zip_code_y_coor_string = "brooklyn_" + str(max_ghg_zip_code) + "_y_coor"
    
    max_ghg_zip_code_x_coor_value = getattr(Brooklyn, max_ghg_zip_code_x_coor_string)
    
    max_ghg_zip_code_y_coor_value = getattr(Brooklyn, max_ghg_zip_code_y_coor_string)
    
    max_ghg_zip_code_data_point = plt.scatter(max_ghg_zip_code_x_coor_value - 13, max_ghg_zip_code_y_coor_value,
                                              s = 50, c = 'red', label = "Highest concentration\nof GHG emissions\n" + \
                                              str("{:,}".format(max_ghg_zip_code_value)) + " lbs/yr")
    
    
    #finds zip code with highest potential for greenhouse gas emissions reduction by amount (lbs/yr)
    #creates data point and data label
    
    brooklyn_ghg_red = {"11201": Brooklyn.brooklyn_11201_ghg_red, "11203": Brooklyn.brooklyn_11203_ghg_red,
                        "11204": Brooklyn.brooklyn_11204_ghg_red, "11205": Brooklyn.brooklyn_11205_ghg_red,
                        "11206": Brooklyn.brooklyn_11206_ghg_red, "11207": Brooklyn.brooklyn_11207_ghg_red,
                        "11208": Brooklyn.brooklyn_11208_ghg_red, "11209": Brooklyn.brooklyn_11209_ghg_red,
                        "11210": Brooklyn.brooklyn_11210_ghg_red, "11211": Brooklyn.brooklyn_11211_ghg_red,
                        "11212": Brooklyn.brooklyn_11212_ghg_red, "11213": Brooklyn.brooklyn_11213_ghg_red,
                        "11214": Brooklyn.brooklyn_11214_ghg_red, "11215": Brooklyn.brooklyn_11215_ghg_red,
                        "11216": Brooklyn.brooklyn_11216_ghg_red, "11217": Brooklyn.brooklyn_11217_ghg_red,
                        "11218": Brooklyn.brooklyn_11218_ghg_red, "11219": Brooklyn.brooklyn_11219_ghg_red,
                        "11220": Brooklyn.brooklyn_11220_ghg_red, "11221": Brooklyn.brooklyn_11221_ghg_red,
                        "11222": Brooklyn.brooklyn_11222_ghg_red, "11223": Brooklyn.brooklyn_11223_ghg_red,
                        "11224": Brooklyn.brooklyn_11224_ghg_red, "11225": Brooklyn.brooklyn_11225_ghg_red,
                        "11226": Brooklyn.brooklyn_11226_ghg_red, "11228": Brooklyn.brooklyn_11228_ghg_red,
                        "11229": Brooklyn.brooklyn_11229_ghg_red, "11230": Brooklyn.brooklyn_11230_ghg_red,
                        "11231": Brooklyn.brooklyn_11231_ghg_red, "11232": Brooklyn.brooklyn_11232_ghg_red,
                        "11233": Brooklyn.brooklyn_11233_ghg_red, "11234": Brooklyn.brooklyn_11234_ghg_red,
                        "11235": Brooklyn.brooklyn_11235_ghg_red, "11236": Brooklyn.brooklyn_11236_ghg_red,
                        "11237": Brooklyn.brooklyn_11237_ghg_red, "11238": Brooklyn.brooklyn_11238_ghg_red,
                        "11239": Brooklyn.brooklyn_11239_ghg_red}
    
    max_ghg_red_zip_code = max(brooklyn_ghg_red, key = brooklyn_ghg_red.get)
        
    max_ghg_red_zip_code_string = "brooklyn_" + str(max_ghg_red_zip_code) + "_ghg_red"
        
    max_ghg_red_zip_code_value = getattr(Brooklyn, max_ghg_red_zip_code_string)
       
    max_ghg_red_zip_code_x_coor_string = "brooklyn_" + str(max_ghg_red_zip_code) + "_x_coor"    
    
    max_ghg_red_zip_code_y_coor_string = "brooklyn_" + str(max_ghg_red_zip_code) + "_y_coor"
    
    max_ghg_red_zip_code_x_coor_value = getattr(Brooklyn, max_ghg_red_zip_code_x_coor_string)
    
    max_ghg_red_zip_code_y_coor_value = getattr(Brooklyn, max_ghg_red_zip_code_y_coor_string)
    
    max_ghg_red_zip_code_data_point = plt.scatter(max_ghg_red_zip_code_x_coor_value + 10, max_ghg_red_zip_code_y_coor_value - 15,
                                              s = 50, c = 'blue', label = "Highest GHG emissions\nreduction potential (by number)\n" + \
                                              str("{:,}".format(max_ghg_red_zip_code_value)) + " lbs/yr")
    
    
    #finds zip code with highest potential for greenhouse gas emissions reduction by proportion
    #to the amount of greenhouse gas produced by the properties in the zip code
    #creates data point and data label
    
    brooklyn_ghg_red_proportion = {"11201": Brooklyn.brooklyn_11201_ghg_red/Brooklyn.brooklyn_11201_ghg,
                                   "11203": Brooklyn.brooklyn_11203_ghg_red/Brooklyn.brooklyn_11203_ghg,
                                   "11204": Brooklyn.brooklyn_11204_ghg_red/Brooklyn.brooklyn_11204_ghg,
                                   "11205": Brooklyn.brooklyn_11205_ghg_red/Brooklyn.brooklyn_11205_ghg,
                                   "11206": Brooklyn.brooklyn_11206_ghg_red/Brooklyn.brooklyn_11206_ghg,
                                   "11207": Brooklyn.brooklyn_11207_ghg_red/Brooklyn.brooklyn_11207_ghg,
                                   "11208": Brooklyn.brooklyn_11208_ghg_red/Brooklyn.brooklyn_11208_ghg,
                                   "11209": Brooklyn.brooklyn_11209_ghg_red/Brooklyn.brooklyn_11209_ghg,
                                   "11210": Brooklyn.brooklyn_11210_ghg_red/Brooklyn.brooklyn_11210_ghg,
                                   "11211": Brooklyn.brooklyn_11211_ghg_red/Brooklyn.brooklyn_11211_ghg,
                                   "11212": Brooklyn.brooklyn_11212_ghg_red/Brooklyn.brooklyn_11212_ghg,
                                   "11213": Brooklyn.brooklyn_11213_ghg_red/Brooklyn.brooklyn_11213_ghg,
                                   "11214": Brooklyn.brooklyn_11214_ghg_red/Brooklyn.brooklyn_11214_ghg,
                                   "11215": Brooklyn.brooklyn_11215_ghg_red/Brooklyn.brooklyn_11215_ghg,
                                   "11216": Brooklyn.brooklyn_11216_ghg_red/Brooklyn.brooklyn_11216_ghg,
                                   "11217": Brooklyn.brooklyn_11217_ghg_red/Brooklyn.brooklyn_11217_ghg,
                                   "11218": Brooklyn.brooklyn_11218_ghg_red/Brooklyn.brooklyn_11218_ghg,
                                   "11219": Brooklyn.brooklyn_11219_ghg_red/Brooklyn.brooklyn_11219_ghg,
                                   "11220": Brooklyn.brooklyn_11220_ghg_red/Brooklyn.brooklyn_11220_ghg,
                                   "11221": Brooklyn.brooklyn_11221_ghg_red/Brooklyn.brooklyn_11221_ghg,
                                   "11222": Brooklyn.brooklyn_11222_ghg_red/Brooklyn.brooklyn_11222_ghg,
                                   "11223": Brooklyn.brooklyn_11223_ghg_red/Brooklyn.brooklyn_11223_ghg,
                                   "11224": Brooklyn.brooklyn_11224_ghg_red/Brooklyn.brooklyn_11224_ghg,
                                   "11225": Brooklyn.brooklyn_11225_ghg_red/Brooklyn.brooklyn_11225_ghg,
                                   "11226": Brooklyn.brooklyn_11226_ghg_red/Brooklyn.brooklyn_11226_ghg,
                                   "11228": Brooklyn.brooklyn_11228_ghg_red/Brooklyn.brooklyn_11228_ghg,
                                   "11229": Brooklyn.brooklyn_11229_ghg_red/Brooklyn.brooklyn_11229_ghg,
                                   "11230": Brooklyn.brooklyn_11230_ghg_red/Brooklyn.brooklyn_11230_ghg,
                                   "11231": Brooklyn.brooklyn_11231_ghg_red/Brooklyn.brooklyn_11231_ghg,
                                   "11232": Brooklyn.brooklyn_11232_ghg_red/Brooklyn.brooklyn_11232_ghg,
                                   "11233": Brooklyn.brooklyn_11233_ghg_red/Brooklyn.brooklyn_11233_ghg,
                                   "11234": Brooklyn.brooklyn_11234_ghg_red/Brooklyn.brooklyn_11234_ghg,
                                   "11235": Brooklyn.brooklyn_11235_ghg_red/Brooklyn.brooklyn_11235_ghg,
                                   "11236": Brooklyn.brooklyn_11236_ghg_red/Brooklyn.brooklyn_11236_ghg,
                                   "11237": Brooklyn.brooklyn_11237_ghg_red/Brooklyn.brooklyn_11237_ghg,
                                   "11238": Brooklyn.brooklyn_11238_ghg_red/Brooklyn.brooklyn_11238_ghg,
                                   "11239": Brooklyn.brooklyn_11239_ghg_red/Brooklyn.brooklyn_11239_ghg}
    
    max_ghg_red_proportion_zip_code = max(brooklyn_ghg_red_proportion, key = brooklyn_ghg_red_proportion.get)
       
    max_ghg_red_proportion_zip_code_top = "brooklyn_" + str(max_ghg_red_proportion_zip_code) +  "_ghg_red"
    
    max_ghg_red_proportion_zip_code_top_value = getattr(Brooklyn, max_ghg_red_proportion_zip_code_top)
    
    max_ghg_red_proportion_zip_code_bottom = "brooklyn_" + str(max_ghg_red_proportion_zip_code) +  "_ghg"
    
    max_ghg_red_proportion_zip_code_bottom_value = getattr(Brooklyn, max_ghg_red_proportion_zip_code_bottom)
    
    max_ghg_red_proportion_zip_code_value = round((max_ghg_red_proportion_zip_code_top_value/
                                             max_ghg_red_proportion_zip_code_bottom_value)*100, 2)
           
    max_ghg_red_proportion_zip_code_x_coor_string = "brooklyn_" + str(max_ghg_red_proportion_zip_code) + "_x_coor"    
    
    max_ghg_red_proportion_zip_code_y_coor_string = "brooklyn_" + str(max_ghg_red_proportion_zip_code) + "_y_coor"
    
    max_ghg_red_proportion_zip_code_x_coor_value = getattr(Brooklyn, max_ghg_red_proportion_zip_code_x_coor_string)
    
    max_ghg_red_proportion_zip_code_y_coor_value = getattr(Brooklyn, max_ghg_red_proportion_zip_code_y_coor_string)
    
    max_ghg_red_proportion_zip_code_data_point = plt.scatter(max_ghg_red_proportion_zip_code_x_coor_value, \
                                                             max_ghg_red_proportion_zip_code_y_coor_value + 25,
                                                             s = 50, c = 'white', label = "Highest GHG emissions\nreduction potential" + \
                                                             " (by proportion)\n" + str("{:,}".format(max_ghg_red_proportion_zip_code_value)) + "%")
    
    
    #finds zip code with highest energy production from rooftop  
    #photovoltaic (PV) solar energy systems potential (kWh/yr)
    #creates data point and data label
    
    brooklyn_eprod = {"11201": Brooklyn.brooklyn_11201_eprod, "11203": Brooklyn.brooklyn_11203_eprod,
                      "11204": Brooklyn.brooklyn_11204_eprod, "11205": Brooklyn.brooklyn_11205_eprod,
                      "11206": Brooklyn.brooklyn_11206_eprod, "11207": Brooklyn.brooklyn_11207_eprod,
                      "11208": Brooklyn.brooklyn_11208_eprod, "11209": Brooklyn.brooklyn_11209_eprod,
                      "11210": Brooklyn.brooklyn_11210_eprod, "11211": Brooklyn.brooklyn_11211_eprod,
                      "11212": Brooklyn.brooklyn_11212_eprod, "11213": Brooklyn.brooklyn_11213_eprod,
                      "11214": Brooklyn.brooklyn_11214_eprod, "11215": Brooklyn.brooklyn_11215_eprod,
                      "11216": Brooklyn.brooklyn_11216_eprod, "11217": Brooklyn.brooklyn_11217_eprod,
                      "11218": Brooklyn.brooklyn_11218_eprod, "11219": Brooklyn.brooklyn_11219_eprod,
                      "11220": Brooklyn.brooklyn_11220_eprod, "11221": Brooklyn.brooklyn_11221_eprod,
                      "11222": Brooklyn.brooklyn_11222_eprod, "11223": Brooklyn.brooklyn_11223_eprod,
                      "11224": Brooklyn.brooklyn_11224_eprod, "11225": Brooklyn.brooklyn_11225_eprod,
                      "11226": Brooklyn.brooklyn_11226_eprod, "11228": Brooklyn.brooklyn_11228_eprod,
                      "11229": Brooklyn.brooklyn_11229_eprod, "11230": Brooklyn.brooklyn_11230_eprod,
                      "11231": Brooklyn.brooklyn_11231_eprod, "11232": Brooklyn.brooklyn_11232_eprod,
                      "11233": Brooklyn.brooklyn_11233_eprod, "11234": Brooklyn.brooklyn_11234_eprod,
                      "11235": Brooklyn.brooklyn_11235_eprod, "11236": Brooklyn.brooklyn_11236_eprod,
                      "11237": Brooklyn.brooklyn_11237_eprod, "11238": Brooklyn.brooklyn_11238_eprod,
                      "11239": Brooklyn.brooklyn_11239_eprod}
    
    max_eprod_zip_code = max(brooklyn_eprod, key = brooklyn_eprod.get)
        
    max_eprod_zip_code_string = "brooklyn_" + str(max_ghg_red_zip_code) + "_eprod"
        
    max_eprod_zip_code_value = getattr(Brooklyn, max_eprod_zip_code_string)
           
    max_eprod_zip_code_x_coor_string = "brooklyn_" + str(max_eprod_zip_code) + "_x_coor"    
    
    max_eprod_zip_code_y_coor_string = "brooklyn_" + str(max_eprod_zip_code) + "_y_coor"
    
    max_eprod_zip_code_x_coor_value = getattr(Brooklyn, max_eprod_zip_code_x_coor_string)
    
    max_eprod_zip_code_y_coor_value = getattr(Brooklyn, max_eprod_zip_code_y_coor_string)
    
    max_eprod_zip_code_data_point = plt.scatter(max_eprod_zip_code_x_coor_value + 55, max_eprod_zip_code_y_coor_value - 15,
                                                s = 50, c = 'yellow', label = "Highest energy production\n" + \
                                                "from rooftop photovoltaic (PV) solar\nenergy systems potential\n" + \
                                                str("{:,}".format(max_eprod_zip_code_value)) + " kWh/yr")
    
    
    #finds zip code with highest savings from energy production ($/yr)  
    #creates data point and data label
    
    brooklyn_esavings = {"11201": Brooklyn.brooklyn_11201_esavings, "11203": Brooklyn.brooklyn_11203_esavings,
                         "11204": Brooklyn.brooklyn_11204_esavings, "11205": Brooklyn.brooklyn_11205_esavings,
                         "11206": Brooklyn.brooklyn_11206_esavings, "11207": Brooklyn.brooklyn_11207_esavings,
                         "11208": Brooklyn.brooklyn_11208_esavings, "11209": Brooklyn.brooklyn_11209_esavings,
                         "11210": Brooklyn.brooklyn_11210_esavings, "11211": Brooklyn.brooklyn_11211_esavings,
                         "11212": Brooklyn.brooklyn_11212_esavings, "11213": Brooklyn.brooklyn_11213_esavings,
                         "11214": Brooklyn.brooklyn_11214_esavings, "11215": Brooklyn.brooklyn_11215_esavings,
                         "11216": Brooklyn.brooklyn_11216_esavings, "11217": Brooklyn.brooklyn_11217_esavings,
                         "11218": Brooklyn.brooklyn_11218_esavings, "11219": Brooklyn.brooklyn_11219_esavings,
                         "11220": Brooklyn.brooklyn_11220_esavings, "11221": Brooklyn.brooklyn_11221_esavings,
                         "11222": Brooklyn.brooklyn_11222_esavings, "11223": Brooklyn.brooklyn_11223_esavings,
                         "11224": Brooklyn.brooklyn_11224_esavings, "11225": Brooklyn.brooklyn_11225_esavings,
                         "11226": Brooklyn.brooklyn_11226_esavings, "11228": Brooklyn.brooklyn_11228_esavings,
                         "11229": Brooklyn.brooklyn_11229_esavings, "11230": Brooklyn.brooklyn_11230_esavings,
                         "11231": Brooklyn.brooklyn_11231_esavings, "11232": Brooklyn.brooklyn_11232_esavings,
                         "11233": Brooklyn.brooklyn_11233_esavings, "11234": Brooklyn.brooklyn_11234_esavings,
                         "11235": Brooklyn.brooklyn_11235_esavings, "11236": Brooklyn.brooklyn_11236_esavings,
                         "11237": Brooklyn.brooklyn_11237_esavings, "11238": Brooklyn.brooklyn_11238_esavings,
                         "11239": Brooklyn.brooklyn_11239_esavings}      
    
    max_esavings_zip_code = max(brooklyn_esavings, key = brooklyn_esavings.get)
       
    max_esavings_zip_code_string = "brooklyn_" + str(max_ghg_red_zip_code) + "_esavings"
        
    max_esavings_zip_code_value = getattr(Brooklyn, max_esavings_zip_code_string)
       
    max_esavings_zip_code_x_coor_string = "brooklyn_" + str(max_esavings_zip_code) + "_x_coor"    
    
    max_esavings_zip_code_y_coor_string = "brooklyn_" + str(max_esavings_zip_code) + "_y_coor"
    
    max_esavings_zip_code_x_coor_value = getattr(Brooklyn, max_esavings_zip_code_x_coor_string)
    
    max_esavings_zip_code_y_coor_value = getattr(Brooklyn, max_esavings_zip_code_y_coor_string)
    
    max_esavings_zip_code_data_point = plt.scatter(max_esavings_zip_code_x_coor_value + 70, max_esavings_zip_code_y_coor_value - 15,
                                                   s = 50, c = 'green', label = "Highest savings\nfrom energy production\n$" + \
                                                   str("{:,}".format(max_esavings_zip_code_value)) + "/yr")
    
    
    brooklyn_data_points = [zip_11201, zip_11203, zip_11204, zip_11205, zip_11206, zip_11207, \
                            zip_11208, zip_11209, zip_11210, zip_11211, zip_11212, zip_11213, \
                            zip_11214, zip_11215, zip_11216, zip_11217, zip_11218, zip_11219, \
                            zip_11220, zip_11221, zip_11222, zip_11223, zip_11224, zip_11225, \
                            zip_11226, zip_11228, zip_11229, zip_11230, zip_11231, zip_11232, \
                            zip_11233, zip_11234, zip_11235, zip_11236, zip_11237, zip_11238, \
                            zip_11239, max_ghg_zip_code_data_point, max_ghg_red_zip_code_data_point, \
                            max_ghg_red_proportion_zip_code_data_point, max_eprod_zip_code_data_point, \
                            max_esavings_zip_code_data_point]    
    
    #plots data points and data labels on map of Brooklyn
    
    datacursor(brooklyn_data_points, arrowprops = dict(arrowstyle= 'simple', fc = 'white', alpha = 1), \
               bbox = dict(boxstyle = 'round, pad = 0.5', fc = 'white', alpha = 0.8))   
                
    plt.show()
    
    

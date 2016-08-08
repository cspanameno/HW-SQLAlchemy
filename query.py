"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
q1 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
q2= Model.query.filter_by(name = 'Corvette', brand_name = 'Chevrolet').all()

# Get all models that are older than 1960.
q3 = Brands.query.filter_by(founded = 1960).all()

# Get all brands that were founded after 1920.
q4 = Brands.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
q5 = Model.query.filter(Model.name.like('Cor%')).all()
 
# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brands.query.filter_by(founded = 1903, discontinued == none)

# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

q7 = Brands.query.filter(Brands.founded < 1950 | Brands.discontinued.isnot(none)).all()

# Get any model whose brand_name is not Chevrolet.

q8=  Model.query.filter(brand_name != 'Chevrolet')

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # Model.query.filter_by(year=1950).all()

    # model_info = db.session.query(Model.name, Model.brand_name, Brand.headquarters)
    # filter(Model.year=year).all()

    # print model_info

    model_info = db.session.query(Model.name, Model.brand_name, 
                                    Brand.headquarters).filter(Model.year==1950).all()
   

    print model_info

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = db.session.query(Model.brand_name, Model.name)

    for brand in brands:
        print brand

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# An object

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An association table does not have meaningful data is supposed to connect two tables 
#using foreign keys. 
#It manages a many to many relationship. 

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands_info = Brand.query.filter((Brand.name.contains(mystr)) | (Brand.name == mystr)).all()
    
    print brands_info


def get_models_between(start_year, end_year):
    cars_chosen = Model.query.filter(Model.year > start_year, Model.year < end_year)
    
    print cars_chosen

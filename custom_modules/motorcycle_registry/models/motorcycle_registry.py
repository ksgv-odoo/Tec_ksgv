from odoo import fields, models

class motorcycle_registry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Motorcycle registry info'
    _rec_name = "registry_number"

    registry_number= fields.Char(string="registry number", required= True)
    vin = fields.Char(string="Vin", required= True)
    first_name = fields.Char(string="First Name", required= True)
    last_name = fields.Char(string="Last Name", required= True)
    picture = fields.Image(string="Image")
    current_mileage = fields.Float('Mileage',digits ='current mileage')
    license_plate = fields.Char(string="License Pate")
    certificate_title = fields.Binary(string="certificate")
    register_date = fields.Date(index=True)


'''
The VIN Number should follow the following Pattern:
Make - 2 Capital Letters
Model - 2 Capital Letters
Year - 2 Digits
Battery Capacity - 2 Capital Letters or Numbers
Serial Number - 6 Digits

XLAD96AC112233
DAER98DC445678
TYCX00RT324376


Create one record from the Motorcycle Registry Model. This Registry should have more than 1000 miles and no license plate.

registry2=env['motorcycle.registry'].create({'registry_number':'MRN0005','vin':'KSJN92BT921204','first_name':'Alex','last_name':'Fuentes','current_mileage':2000,'license_plate':''})
env['motorcycle.registry'].browse([1])


Search for all Motorcycles Registries with less than 1000 miles.

res2=env['motorcycle.registry'].browse([3])
res2.write({'current_mileage':750})
env['motorcycle.registry'].search_read([('current_mileage','<','1000')],['current_mileage'])


Search for all Motorcycle Registries with a VIN Number but no License Plate. Only show the fields: registry_number, vin, license_plate, and lastname
env['motorcycle.registry'].search_read([('vin','!=',False),('license_plate','=',False)],['registry_number','vin','license_plate','last_name'])

Search for all Motorcycle Registries with a VIN Number or a License Plate
env['motorcycle.registry'].search_read([('vin','!=',False),('license_plate','=',False)],['registry_number','vin'])

Update the Name and Lastname of the record you created to John Wick
Delete the Record.
'''
from odoo.upgrade import util

def migrate(cr, version):
    util.remove_module(cr, "aup_module")

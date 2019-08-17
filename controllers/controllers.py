# -*- coding: utf-8 -*-
from odoo import http

# class CreateApplicationAttachmentShortcut(http.Controller):
#     @http.route('/create_application_attachment_shortcut/create_application_attachment_shortcut/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/create_application_attachment_shortcut/create_application_attachment_shortcut/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('create_application_attachment_shortcut.listing', {
#             'root': '/create_application_attachment_shortcut/create_application_attachment_shortcut',
#             'objects': http.request.env['create_application_attachment_shortcut.create_application_attachment_shortcut'].search([]),
#         })

#     @http.route('/create_application_attachment_shortcut/create_application_attachment_shortcut/objects/<model("create_application_attachment_shortcut.create_application_attachment_shortcut"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('create_application_attachment_shortcut.object', {
#             'object': obj
#         })
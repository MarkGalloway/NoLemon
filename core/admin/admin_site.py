from django.contrib.admin.sites import AdminSite

__all__ = ['NoLemonAdminSite']

class NoLemonAdminSite(AdminSite):

    site_header = 'NoLemon Administration'
    site_title = 'NoLemon Administration'
    index_title = ''
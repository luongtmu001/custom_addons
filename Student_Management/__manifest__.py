{
    'name': 'Student managenment',
    'author': 'Luong Hoang Tuan',
    'version': '1.0',
    'summary': 'Quản lý sinh viên',
    'description': 'Quản lý sinh viên',
    'sequence': 10,
    'depends' : ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/sm_menu.xml',
        'views/sm_student_list_view.xml',
        'views/sm_schoolyear_view.xml',

    ],
    'application': True

}
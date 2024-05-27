{
    'name': 'student managenment',
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
        # 'views/sm_category_view.xml',
        'views/sm_student_dept.xml',
        'views/sm_student_ct_view.xml',
        'views/sm_category_majors.xml',
        'views/sm_category_class_view.xml',
        'views/sm_category_subject_view.xml',
        'views/sm_category_lecture_view.xml',

    ],
    'application': True

}
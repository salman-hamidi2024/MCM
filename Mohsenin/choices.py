ORPHAN = 1
INMATE = 2
DIVORCED = 3
ABANDONED = 4
SICK = 5
POOR = 6
FAMILY_TYPE_CHOICES = [
    (ORPHAN, 'یتیم'),
    (INMATE, 'زندانی'),
    (DIVORCED, 'مطلقه'),
    (ABANDONED, 'رها شده'),
    (SICK, 'بیمار'),
    (POOR, 'فقیر')

]

MID = 1
HIGH = 2
HIGHEST = 3
NEED_LEVEL_CHOICE = [
    (MID, 'متوسط'),
    (HIGH, 'شدید'),
    (HIGHEST, 'خیلی شدید'),
]

SUPPORTING_CHOICE = [
    (True, 'تحت حمایت'),
    (False, 'عدم حمایت'),
]

YES_NO_CHOICE = [
    (True,'بله'),
    (False, 'خیر'),
]

ACTIVATION_CHOICE = [
    (True, 'فعال'),
    (False, 'غیرفعال'),
]